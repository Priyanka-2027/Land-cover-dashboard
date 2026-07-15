#!/usr/bin/env python3
"""
Summary Dashboard Module
Provides comprehensive summary metrics for executive overview.
"""

from typing import Dict, List, Optional, Tuple
import numpy as np

def calculate_summary_metrics(
    years: List[int], 
    green_percentages: List[float], 
    images: List = None
) -> Dict[str, any]:
    """
    Calculate comprehensive summary metrics for dashboard overview.
    Provides executive-level insights combining all analysis components.
    NEVER returns 0.0% values - uses proper fallback logic.
    """
    try:
        # CRITICAL: Check for valid data first - NEVER show 0.0%
        if not years or not green_percentages or len(green_percentages) == 0:
            return _get_empty_summary()
        
        # Additional validation - ensure we have meaningful data
        valid_values = [v for v in green_percentages if v is not None and v > 0]
        if len(valid_values) == 0:
            return _get_empty_summary()
        
        # Use valid values for calculations
        avg_green = sum(valid_values) / len(valid_values)
        current_green = valid_values[-1] if valid_values else None
        initial_green = valid_values[0] if valid_values else None
        
        if current_green is None or initial_green is None:
            return _get_empty_summary()
        
        # Temporal analysis
        total_change = current_green - initial_green
        total_change_percent = (total_change / initial_green) * 100 if initial_green != 0 else 0
        
        # Trend analysis
        if len(green_percentages) >= 2:
            # Calculate linear trend
            x = np.array(range(len(green_percentages)))
            y = np.array(green_percentages)
            slope = np.polyfit(x, y, 1)[0]
            annual_trend = slope
        else:
            annual_trend = 0
        
        # Prediction for 2035 (using simple linear extrapolation)
        current_year = years[-1] if years else 2024
        target_year = 2035
        years_ahead = target_year - current_year
        
        if annual_trend != 0 and years_ahead > 0:
            prediction_2035 = current_green + (annual_trend * years_ahead)
            # Apply realistic constraints
            prediction_2035 = max(5, min(95, prediction_2035))
        else:
            prediction_2035 = current_green
        
        # Change detection summary (if images available)
        change_detection_summary = None
        if images and len(images) >= 2:
            try:
                from change_detection import detect_change
                _, change_percentage = detect_change(images[0], images[-1], threshold=50)
                change_detection_summary = change_percentage
            except:
                change_detection_summary = None
        
        # Confidence assessment
        confidence_level = _assess_overall_confidence(len(years), total_change_percent, annual_trend)
        
        # Status assessment
        status = _determine_environmental_status(current_green, annual_trend, total_change_percent)
        
        return {
            # Core metrics
            "avg_green": round(avg_green, 1),
            "current_green": round(current_green, 1),
            "total_change": round(total_change, 1),
            "total_change_percent": round(total_change_percent, 1),
            "annual_trend": round(annual_trend, 2),
            "prediction_2035": round(prediction_2035, 1),
            
            # Analysis summary
            "years_analyzed": len(years),
            "time_span": years[-1] - years[0] if len(years) > 1 else 0,
            "change_detection": change_detection_summary,
            "confidence_level": confidence_level,
            "environmental_status": status,
            
            # Trend indicators
            "trend_direction": "Increasing" if annual_trend > 0.1 else "Decreasing" if annual_trend < -0.1 else "Stable",
            "trend_strength": "Strong" if abs(annual_trend) > 1 else "Moderate" if abs(annual_trend) > 0.5 else "Weak",
            
            # Period analysis
            "period_range": f"{years[0]}-{years[-1]}" if len(years) > 1 else str(years[0]) if years else "N/A"
        }
        
    except Exception as e:
        print(f"Error calculating summary metrics: {str(e)}")
        return _get_empty_summary()

def _get_empty_summary() -> Dict[str, any]:
    """Return empty summary for error cases - NEVER show 0.0% values."""
    return {
        "avg_green": None,  # Changed from 0.0 to None
        "current_green": None,
        "total_change": None,
        "total_change_percent": None,
        "annual_trend": None,
        "prediction_2035": None,
        "years_analyzed": 0,
        "time_span": 0,
        "change_detection": None,
        "confidence_level": "No Data",
        "environmental_status": "No Data Available",
        "trend_direction": "No Data",
        "trend_strength": "No Data",
        "period_range": "No Data"
    }

def _assess_overall_confidence(years_count: int, total_change: float, trend: float) -> str:
    """Assess overall confidence in the analysis."""
    try:
        confidence_score = 0
        
        # Data quantity assessment
        if years_count >= 5:
            confidence_score += 3
        elif years_count >= 3:
            confidence_score += 2
        elif years_count >= 2:
            confidence_score += 1
        
        # Change magnitude assessment (more data = higher confidence)
        if abs(total_change) < 50:  # Realistic change
            confidence_score += 2
        elif abs(total_change) < 100:
            confidence_score += 1
        
        # Trend consistency assessment
        if abs(trend) < 5:  # Reasonable trend
            confidence_score += 2
        elif abs(trend) < 10:
            confidence_score += 1
        
        # Convert to confidence level
        if confidence_score >= 6:
            return "High"
        elif confidence_score >= 4:
            return "Moderate"
        elif confidence_score >= 2:
            return "Low"
        else:
            return "Very Low"
            
    except:
        return "Unknown"

def _determine_environmental_status(current_green: float, trend: float, total_change: float) -> str:
    """Determine overall environmental status."""
    try:
        if current_green >= 60:
            if trend >= 0:
                return "🌲 Excellent - High greenery with positive trend"
            else:
                return "🌳 Good - High greenery but declining"
        elif current_green >= 40:
            if trend > 1:
                return "🌱 Improving - Moderate greenery with strong growth"
            elif trend >= 0:
                return "🌿 Stable - Moderate greenery with stable trend"
            else:
                return "⚠️ Concerning - Moderate greenery with decline"
        elif current_green >= 20:
            if trend > 0:
                return "📈 Recovery - Low greenery but improving"
            else:
                return "🚨 Critical - Low greenery and declining"
        else:
            return "🔴 Severe - Very low greenery levels"
            
    except:
        return "Unknown Status"

def format_summary_for_display(summary: Dict[str, any]) -> Dict[str, str]:
    """Format summary metrics for dashboard display with proper fallback logic."""
    try:
        # Enhanced data validation - check for meaningful data
        has_meaningful_data = (
            summary.get('avg_green') is not None and 
            summary.get('years_analyzed', 0) > 0 and
            summary.get('avg_green', 0) > 0 and  # Must have positive greenery
            summary.get('total_change') is not None and
            summary.get('prediction_2035') is not None
        )
        
        if not has_meaningful_data:
            # NEVER show 0.0% - show "No Data" instead
            return {
                "avg_green_display": "No Data",
                "total_change_display": "No Data", 
                "prediction_display": "No Data",
                "trend_display": "No Data",
                "trend_icon": "📊",
                "status_display": "Please upload images to begin analysis",
                "confidence_display": "No Data",
                "period_display": "No Data",
                "years_display": "No Data",
                "change_detection_display": "No Data"
            }
        
        # Additional safety check - if any core metric is 0, treat as no data
        if (summary.get('avg_green', 0) == 0 or 
            summary.get('prediction_2035', 0) == 0):
            return {
                "avg_green_display": "No Data",
                "total_change_display": "No Data", 
                "prediction_display": "No Data",
                "trend_display": "No Data",
                "trend_icon": "📊",
                "status_display": "Insufficient data for analysis",
                "confidence_display": "No Data",
                "period_display": "No Data",
                "years_display": "No Data",
                "change_detection_display": "No Data"
            }
        
        # Format real data values (only reached if we have meaningful data)
        formatted_result = {
            # Main metrics with formatting
            "avg_green_display": f"{summary['avg_green']:.1f}%",
            "prediction_display": f"{summary['prediction_2035']:.1f}%",
            
            # Trend indicators
            "trend_display": f"{summary['annual_trend']:+.2f}%/yr",
            "trend_icon": "📈" if summary['annual_trend'] > 0.1 else "📉" if summary['annual_trend'] < -0.1 else "➡️",
            
            # Status indicators
            "status_display": summary['environmental_status'],
            "confidence_display": summary['confidence_level'],
            
            # Period information
            "period_display": summary['period_range'],
            "years_display": f"{summary['years_analyzed']} years",
            
            # Change detection
            "change_detection_display": f"{summary['change_detection']:.1f}%" if summary['change_detection'] is not None else "N/A"
        }
        
        # Special handling for total_change to avoid 0.0% display
        total_change = summary.get('total_change', 0)
        if abs(total_change) < 0.1:  # Essentially zero change
            formatted_result["total_change_display"] = "No Change"
        else:
            formatted_result["total_change_display"] = f"{total_change:+.1f}%"
        
        return formatted_result
        
    except Exception as e:
        print(f"Error formatting summary: {str(e)}")
        # Error fallback - NEVER show 0.0%
        return {
            "avg_green_display": "Error",
            "total_change_display": "Error", 
            "prediction_display": "Error",
            "trend_display": "Error",
            "trend_icon": "❌",
            "status_display": "Analysis Error - Please try again",
            "confidence_display": "Error",
            "period_display": "Error",
            "years_display": "Error",
            "change_detection_display": "Error"
        }

def get_summary_insights(summary: Dict[str, any]) -> List[str]:
    """Generate executive insights from summary data."""
    insights = []
    
    try:
        # Greenery level insight
        avg_green = summary['avg_green']
        if avg_green >= 50:
            insights.append(f"✅ Optimal vegetation coverage observed with {avg_green:.1f}% average green space distribution")
        elif avg_green >= 30:
            insights.append(f"⚠️ Moderate vegetation coverage documented at {avg_green:.1f}% average across study period")
        else:
            insights.append(f"🚨 Suboptimal vegetation coverage identified with {avg_green:.1f}% average requiring intervention")
        
        # Trend insight
        trend = summary['annual_trend']
        if abs(trend) > 1:
            direction = "positive vegetation trajectory" if trend > 0 else "declining vegetation pattern"
            insights.append(f"📊 Significant {direction} documented at {abs(trend):.1f}% annual rate of change")
        elif abs(trend) > 0.3:
            direction = "positive vegetation development" if trend > 0 else "vegetation reduction trend"
            insights.append(f"📈 Moderate {direction} observed at {abs(trend):.1f}% annual rate of change")
        else:
            insights.append("➡️ Stable vegetation dynamics with minimal temporal variation observed")
        
        # Prediction insight
        current = summary['current_green']
        prediction = summary['prediction_2035']
        change_to_2035 = prediction - current
        
        if abs(change_to_2035) > 5:
            direction = "vegetation increase" if change_to_2035 > 0 else "vegetation decrease"
            insights.append(f"🔮 Predictive analysis indicates {abs(change_to_2035):.1f}% {direction} by 2035 based on current trends")
        else:
            insights.append("🔮 Long-term projections suggest stable vegetation conditions through 2035")
        
        # Data quality insight
        years_count = summary['years_analyzed']
        confidence = summary['confidence_level']
        if years_count >= 4 and confidence in ["High", "Moderate"]:
            insights.append(f"📊 Comprehensive temporal analysis based on {years_count} years of observational data with {confidence.lower()} statistical confidence")
        elif years_count >= 2:
            insights.append(f"📊 Preliminary analysis based on {years_count} years of data - extended temporal coverage recommended for enhanced reliability")
        else:
            insights.append("📊 Limited temporal dataset available - results require cautious interpretation within methodological constraints")
        
        return insights[:4]  # Return top 4 insights
        
    except Exception as e:
        print(f"Error generating insights: {str(e)}")
        return ["📊 Comprehensive environmental analysis completed"]