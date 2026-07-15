#!/usr/bin/env python3
"""
Enhanced Executive Dashboard with Color-Coded Metrics
Adds intelligent color coding to make the dashboard more visually appealing and intuitive.
"""

def get_metric_color_and_delta(metric_type: str, value: str, delta_value: str = None, raw_value: float = None) -> tuple:
    """
    Determine appropriate color coding and delta formatting for metrics.
    
    Returns:
        tuple: (delta_color, formatted_delta, use_delta)
    """
    
    if metric_type == "avg_green":
        # Green coverage: Higher is better
        if raw_value is not None:
            if raw_value >= 60:
                return ("normal", delta_value, True)  # Green (positive)
            elif raw_value >= 40:
                return ("off", delta_value, True)     # Yellow/neutral
            else:
                return ("inverse", delta_value, True) # Red (concerning)
        return ("normal", delta_value, True)
    
    elif metric_type == "total_change":
        # Change: Positive change is good, negative is concerning
        if delta_value and "+" in delta_value:
            return ("normal", delta_value, True)      # Green (positive change)
        elif delta_value and "-" in delta_value:
            return ("inverse", delta_value, True)     # Red (negative change)
        else:
            return ("off", delta_value, True)         # Yellow (no change)
    
    elif metric_type == "prediction":
        # Prediction: Compare with current to determine if improving
        if delta_value and "+" in delta_value:
            return ("normal", delta_value, True)      # Green (improving)
        elif delta_value and "-" in delta_value:
            return ("inverse", delta_value, True)     # Red (declining)
        else:
            return ("off", delta_value, True)         # Yellow (stable)
    
    elif metric_type == "trend":
        # Annual trend: Positive trend is good
        if delta_value and "+" in delta_value:
            return ("normal", delta_value, True)      # Green (positive trend)
        elif delta_value and "-" in delta_value:
            return ("inverse", delta_value, True)     # Red (negative trend)
        else:
            return ("off", delta_value, True)         # Yellow (stable)
    
    else:
        # Default: no special coloring
        return ("normal", delta_value, bool(delta_value))

def create_color_coded_metrics(summary_metrics: dict, formatted_summary: dict) -> dict:
    """
    Create color-coded metric configurations for the executive dashboard.
    
    Returns:
        dict: Metric configurations with color coding
    """
    
    # Extract raw values for intelligent color decisions
    avg_green_raw = summary_metrics.get('avg_green', 0) or 0
    total_change_raw = summary_metrics.get('total_change', 0) or 0
    prediction_raw = summary_metrics.get('prediction_2035', 0) or 0
    current_green_raw = summary_metrics.get('current_green', 0) or 0
    
    # Calculate prediction delta
    prediction_delta = None
    if prediction_raw and current_green_raw:
        delta_val = prediction_raw - current_green_raw
        prediction_delta = f"vs current: {delta_val:+.1f}%"
    
    # Configure each metric with appropriate colors
    metrics_config = {
        "avg_green": {
            "label": "📊 Avg Green Coverage",
            "value": formatted_summary["avg_green_display"],
            "delta": None,  # No delta for average
            "delta_color": "normal",
            "help": "Average vegetation coverage across all analyzed periods"
        },
        
        "total_change": {
            "label": "📈 Total Change",
            "value": formatted_summary["total_change_display"],
            "delta": formatted_summary["trend_display"],
            "delta_color": "normal" if total_change_raw >= 0 else "inverse",
            "help": "Overall change from first to last measurement"
        },
        
        "prediction": {
            "label": "🔮 Prediction (2035)",
            "value": formatted_summary["prediction_display"],
            "delta": prediction_delta,
            "delta_color": "normal" if (prediction_raw - current_green_raw) >= 0 else "inverse" if prediction_delta else "off",
            "help": "Projected vegetation coverage for 2035 based on current trends"
        },
        
        "period": {
            "label": "🎯 Analysis Period",
            "value": formatted_summary["period_display"],
            "delta": formatted_summary["years_display"],
            "delta_color": "normal",  # Always positive (more data is better)
            "help": "Time span and data points analyzed"
        }
    }
    
    return metrics_config

def render_color_coded_executive_summary(summary_metrics: dict, formatted_summary: dict, st_module):
    """
    Render the executive summary with intelligent color coding.
    
    Args:
        summary_metrics: Raw summary data
        formatted_summary: Formatted display data
        st_module: Streamlit module for rendering
    """
    
    # Create color-coded metric configurations
    metrics_config = create_color_coded_metrics(summary_metrics, formatted_summary)
    
    # Create impressive summary dashboard at top
    st_module.markdown("## 📊 Executive Summary Dashboard")
    st_module.markdown("**Comprehensive Analysis Overview** - Key metrics at a glance")
    
    # Main metrics row with color coding
    col1, col2, col3, col4 = st_module.columns(4)
    
    with col1:
        config = metrics_config["avg_green"]
        st_module.metric(
            label=config["label"],
            value=config["value"],
            delta=config["delta"],
            delta_color=config["delta_color"],
            help=config["help"]
        )
    
    with col2:
        config = metrics_config["total_change"]
        st_module.metric(
            label=config["label"],
            value=config["value"],
            delta=config["delta"],
            delta_color=config["delta_color"],
            help=config["help"]
        )
    
    with col3:
        config = metrics_config["prediction"]
        st_module.metric(
            label=config["label"],
            value=config["value"],
            delta=config["delta"],
            delta_color=config["delta_color"],
            help=config["help"]
        )
    
    with col4:
        config = metrics_config["period"]
        st_module.metric(
            label=config["label"],
            value=config["value"],
            delta=config["delta"],
            delta_color=config["delta_color"],
            help=config["help"]
        )

def demo_color_coding_examples():
    """Demo different color coding scenarios."""
    
    print("🎨 EXECUTIVE DASHBOARD COLOR CODING")
    print("=" * 50)
    
    scenarios = [
        {
            "name": "High Performance (Positive)",
            "avg_green": 65.2,
            "total_change": 8.5,
            "prediction": 72.1,
            "current": 65.2
        },
        {
            "name": "Moderate Performance (Mixed)",
            "avg_green": 45.8,
            "total_change": -2.3,
            "prediction": 43.1,
            "current": 45.8
        },
        {
            "name": "Low Performance (Concerning)",
            "avg_green": 28.4,
            "total_change": -12.7,
            "prediction": 22.8,
            "current": 28.4
        }
    ]
    
    for scenario in scenarios:
        print(f"\n📊 {scenario['name']}:")
        
        # Avg Green Coverage
        avg_green = scenario['avg_green']
        if avg_green >= 60:
            color = "🟢 Green (Excellent)"
        elif avg_green >= 40:
            color = "🟡 Yellow (Moderate)"
        else:
            color = "🔴 Red (Concerning)"
        
        print(f"   📊 Avg Green: {avg_green:.1f}% → {color}")
        
        # Total Change
        total_change = scenario['total_change']
        if total_change > 0:
            color = "🟢 Green (Positive)"
        elif total_change < 0:
            color = "🔴 Red (Decline)"
        else:
            color = "🟡 Yellow (Stable)"
        
        print(f"   📈 Total Change: {total_change:+.1f}% → {color}")
        
        # Prediction
        prediction_change = scenario['prediction'] - scenario['current']
        if prediction_change > 0:
            color = "🟢 Green (Improving)"
        elif prediction_change < 0:
            color = "🔴 Red (Declining)"
        else:
            color = "🟡 Yellow (Stable)"
        
        print(f"   🔮 Prediction: {scenario['prediction']:.1f}% ({prediction_change:+.1f}%) → {color}")

if __name__ == "__main__":
    demo_color_coding_examples()
    
    print(f"\n✅ COLOR CODING BENEFITS:")
    print("🟢 Green: Positive values, improvements, good performance")
    print("🟡 Yellow: Moderate values, stable trends, neutral changes")
    print("🔴 Red: Concerning values, declines, negative trends")
    print("📊 Intuitive: Faculty can instantly understand performance")
    print("🎨 Professional: Enhanced visual appeal and clarity")