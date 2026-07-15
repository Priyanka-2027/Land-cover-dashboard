import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from typing import List, Tuple, Optional

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from typing import List, Tuple, Optional

def apply_moving_average(data: List[float], window: int = 3) -> List[float]:
    """Apply moving average smoothing to reduce noise in historical data."""
    if len(data) < window:
        return data
    
    smoothed = []
    for i in range(len(data)):
        if i < window - 1:
            # For early points, use available data
            smoothed.append(np.mean(data[:i+1]))
        else:
            # Use moving window
            smoothed.append(np.mean(data[i-window+1:i+1]))
    
    return smoothed

def predict_future(years: List[int], green_percentages: List[float], target_year: int) -> Tuple[float, float, dict]:
    """
    Predict future greenery using robust linear regression with smoothing.
    Includes realistic constraints, trend analysis, and model justification.
    
    Returns:
        prediction: Predicted greenery percentage
        slope: Annual trend (% per year)
        model_info: Dictionary with equation and justification details
    """
    try:
        if len(years) < 2 or len(green_percentages) < 2:
            return (green_percentages[-1] if green_percentages else 50.0, 0.0, 
                   {"equation": "Insufficient data", "justification": "Need at least 2 data points"})
        
        # Apply moving average smoothing to reduce noise
        smoothed_green = apply_moving_average(green_percentages, window=min(3, len(green_percentages)))
        
        # Reshape data for scikit-learn
        X = np.array(years).reshape(-1, 1)
        y = np.array(smoothed_green)
        
        # Train Linear Regression model
        model = LinearRegression().fit(X, y)
        
        # Extract model parameters
        slope = model.coef_[0]
        intercept = model.intercept_
        
        # Predict for the target year
        raw_prediction = model.predict([[target_year]])[0]
        
        # Apply realistic constraints and trend dampening
        current_value = smoothed_green[-1]
        
        # Dampen extreme predictions (environmental systems change slowly)
        years_ahead = target_year - years[-1]
        max_change_per_year = 2.0  # Maximum 2% change per year is realistic
        max_total_change = max_change_per_year * years_ahead
        
        constraint_applied = False
        if abs(raw_prediction - current_value) > max_total_change:
            # Cap the prediction to realistic change rates
            constraint_applied = True
            if raw_prediction > current_value:
                prediction = current_value + max_total_change
            else:
                prediction = current_value - max_total_change
        else:
            prediction = raw_prediction
        
        # Final constraint: Keep within 0-100% bounds
        prediction = max(0.0, min(100.0, float(prediction)))
        
        # Create model information for display
        model_info = {
            "equation": f"y = {slope:.3f}x + {intercept:.1f}",
            "slope": slope,
            "intercept": intercept,
            "r_squared": model.score(X, y),
            "raw_prediction": raw_prediction,
            "constrained": constraint_applied,
            "max_change_per_year": max_change_per_year,
            "justification": _get_model_justification(len(years), slope, constraint_applied)
        }
        
        return prediction, float(slope), model_info
    except Exception:
        # Fallback: return current value with no change
        return (green_percentages[-1] if green_percentages else 50.0, 0.0,
               {"equation": "Error in calculation", "justification": "Using current value as fallback"})

def _get_model_justification(data_points: int, slope: float, constrained: bool) -> str:
    """Generate justification text for the prediction model."""
    justification = "Using linear regression for trend prediction. "
    
    # Data quality assessment
    if data_points >= 5:
        justification += "High confidence with 5+ data points. "
    elif data_points >= 3:
        justification += "Moderate confidence with 3+ data points. "
    else:
        justification += "Limited confidence with only 2 data points. "
    
    # Trend interpretation
    if abs(slope) < 0.5:
        justification += "Stable trend detected (minimal change). "
    elif slope > 0:
        justification += f"Positive trend: +{slope:.2f}% per year. "
    else:
        justification += f"Negative trend: {slope:.2f}% per year. "
    
    # Constraint explanation
    if constrained:
        justification += "Prediction constrained to realistic environmental change rates (max 2%/year)."
    else:
        justification += "Prediction within realistic environmental change bounds."
    
    return justification

def generate_prediction_plot(years: List[int], green_percentages: List[float], target_year: int, predicted_value: float, model_info: dict = None) -> plt.Figure:
    """Create a professional prediction plot with model equation and justification."""
    try:
        fig, ax = plt.subplots(figsize=(12, 7))
        
        # Apply smoothing for visualization
        smoothed_green = apply_moving_average(green_percentages, window=min(3, len(green_percentages)))
        
        # Create extended timeline for trend line
        extended_years = list(range(min(years), target_year + 1))
        
        # Fit model for trend line
        if len(years) >= 2:
            X = np.array(years).reshape(-1, 1)
            y = np.array(smoothed_green)
            model = LinearRegression().fit(X, y)
            
            # Generate trend line (with realistic constraints)
            trend_predictions = []
            for year in extended_years:
                raw_pred = model.predict([[year]])[0]
                # Apply the same constraints as in predict_future
                current_value = smoothed_green[-1]
                years_ahead = year - years[-1]
                max_change = 2.0 * years_ahead
                
                if abs(raw_pred - current_value) > max_change:
                    if raw_pred > current_value:
                        constrained_pred = current_value + max_change
                    else:
                        constrained_pred = current_value - max_change
                else:
                    constrained_pred = raw_pred
                
                trend_predictions.append(max(0, min(100, constrained_pred)))
        
        # Plot historical data points
        ax.scatter(years, green_percentages, color='#1976d2', label='Raw Historical Data', 
                  s=80, alpha=0.7, zorder=3)
        
        # Plot smoothed historical data
        ax.plot(years, smoothed_green, color='#2e7d32', linewidth=3, 
               label='Smoothed Trend', zorder=4)
        
        # Plot trend line
        if len(years) >= 2:
            ax.plot(extended_years, trend_predictions, '--', color='#ff9800', 
                   linewidth=2, alpha=0.8, label='Projected Trend', zorder=2)
        
        # Plot predicted point
        ax.scatter([target_year], [predicted_value], color='#d32f2f', marker='*', 
                  s=300, label=f'Prediction {target_year}', zorder=5, edgecolor='white', linewidth=2)
        
        # Styling
        ax.set_xlabel("Year", fontsize=12, fontweight='bold')
        ax.set_ylabel("Greenery Percentage (%)", fontsize=12, fontweight='bold')
        ax.set_title("Environmental Greenery Trend Analysis & Prediction", fontsize=14, fontweight='bold')
        ax.legend(loc='upper right', frameon=True, fancybox=True, shadow=True)
        ax.grid(True, linestyle='--', alpha=0.3)
        ax.set_ylim(0, 100)
        
        # --- METHOD LABEL: always shown, top-left ---
        r2_str = ""
        if model_info and "r_squared" in model_info:
            r2_str = f"  |  R\u00b2 = {model_info['r_squared']:.3f}"
        method_text = f"Method: Linear regression with smoothing applied{r2_str}"
        if model_info and "equation" in model_info:
            method_text += f"\nEquation: {model_info['equation']}"
        
        ax.text(0.02, 0.98, method_text, transform=ax.transAxes,
                fontsize=10, verticalalignment='top', fontfamily='monospace',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#fffde7',
                          edgecolor='#f9a825', alpha=0.92))
        
        # Add confidence band
        if len(years) >= 3:
            # Calculate prediction uncertainty
            residuals = np.array(smoothed_green) - model.predict(X)
            std_error = np.std(residuals)
            
            # Add confidence band around trend line
            upper_bound = [min(100, p + std_error) for p in trend_predictions]
            lower_bound = [max(0, p - std_error) for p in trend_predictions]
            
            ax.fill_between(extended_years, lower_bound, upper_bound, 
                           alpha=0.2, color='#ff9800', label='Confidence Band')
        
        # Add constraint information if model was constrained
        if model_info and model_info.get("constrained", False):
            ax.text(0.02, 0.02, "⚠️ Prediction constrained to realistic rates (max 2%/year)", 
                   transform=ax.transAxes, fontsize=9, 
                   bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))
        
        plt.tight_layout()
        return fig
    except Exception as e:
        # Fallback simple plot
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.scatter(years, green_percentages, color='#2e7d32', s=100)
        ax.scatter([target_year], [predicted_value], color='#d32f2f', marker='*', s=200)
        ax.set_xlabel("Year")
        ax.set_ylabel("Greenery %")
        ax.set_title("Greenery Prediction")
        ax.grid(True, alpha=0.3)
        return fig
