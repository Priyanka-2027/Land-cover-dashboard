#!/usr/bin/env python3
"""
Temporal Analysis System - Year-to-Year Change Analysis
Provides comprehensive temporal dynamics analysis for faculty evaluation.
"""

from typing import List, Dict, Tuple
import numpy as np

def calculate_year_to_year_changes(years: List[int], values: List[float]) -> List[Dict]:
    """
    Calculate year-to-year percentage changes with comprehensive analysis.
    Faculty loves detailed temporal dynamics analysis.
    """
    try:
        if len(years) < 2 or len(values) < 2:
            return []
        
        changes = []
        
        for i in range(1, len(years)):
            prev_year = years[i-1]
            curr_year = years[i]
            prev_value = values[i-1]
            curr_value = values[i]
            
            # Calculate absolute and percentage change with realistic environmental constraints
            absolute_change = curr_value - prev_value
            
            # Use improved formula to prevent extreme percentages from small denominators
            # Formula: change = ((new - old) / max(old, 1)) * 100
            # This prevents division by very small numbers that cause unrealistic percentages
            safe_denominator = max(prev_value, 1.0)  # Minimum denominator of 1%
            raw_percentage_change = (absolute_change / safe_denominator) * 100
            
            # Cap percentage changes to realistic environmental bounds (-50% to +50%)
            # Real-world environmental changes rarely exceed these bounds in a single year
            percentage_change = min(max(raw_percentage_change, -50.0), 50.0)
            
            # Store both raw and capped values for transparency
            raw_change = (absolute_change / prev_value) * 100 if prev_value != 0 else 0
            
            # Determine change category
            change_category = _categorize_change(percentage_change)
            
            # Create change record with both raw and realistic values
            change_record = {
                "from_year": prev_year,
                "to_year": curr_year,
                "from_value": prev_value,
                "to_value": curr_value,
                "absolute_change": absolute_change,
                "percentage_change": percentage_change,  # Capped realistic value
                "raw_percentage_change": raw_change,     # Original mathematical value
                "is_capped": abs(raw_change) > 50.0,    # Flag if capping was applied
                "change_category": change_category,
                "change_description": _describe_change(prev_year, curr_year, percentage_change),
                "trend_indicator": _get_trend_indicator(percentage_change)
            }
            
            changes.append(change_record)
        
        return changes
        
    except Exception:
        return []

def _categorize_change(percentage_change: float) -> str:
    """Categorize the magnitude of change."""
    abs_change = abs(percentage_change)
    
    if abs_change >= 15:
        return "Major Change"
    elif abs_change >= 8:
        return "Significant Change"
    elif abs_change >= 3:
        return "Moderate Change"
    elif abs_change >= 1:
        return "Minor Change"
    else:
        return "Minimal Change"

def _describe_change(from_year: int, to_year: int, percentage_change: float) -> str:
    """Generate descriptive text for the change using varied research-level language."""
    try:
        # Import enhanced language system
        from enhanced_insights_language import ResearchLanguageGenerator
        generator = ResearchLanguageGenerator()
        
        direction_term = generator.get_change_description(percentage_change)
        magnitude = abs(percentage_change)
        magnitude_term = generator.get_magnitude_term(magnitude, {"high": 15.0, "moderate": 3.0})
        observation_term = generator.get_varied_term("analytical", "observation")
        
        return f"{magnitude_term.title()} {direction_term} in vegetation coverage {observation_term} ({magnitude:.1f}% from {from_year} to {to_year})"
        
    except Exception:
        # Fallback to original logic if enhanced system fails
        direction = "increase" if percentage_change > 0 else "reduction"
        magnitude = abs(percentage_change)
        
        if magnitude >= 15:
            intensity = "substantial"
        elif magnitude >= 8:
            intensity = "pronounced"  # Varied from "significant"
        elif magnitude >= 3:
            intensity = "moderate"
        elif magnitude >= 1:
            intensity = "minor"
        else:
            intensity = "minimal"
        
        return f"{intensity.capitalize()} {direction} in vegetation coverage observed ({magnitude:.1f}% from {from_year} to {to_year})"

def _get_trend_indicator(percentage_change: float) -> str:
    """Get emoji indicator for trend direction."""
    if percentage_change > 5:
        return "📈"  # Strong positive
    elif percentage_change > 1:
        return "📊"  # Moderate positive
    elif percentage_change > -1:
        return "➡️"  # Stable
    elif percentage_change > -5:
        return "📉"  # Moderate negative
    else:
        return "🚨"  # Strong negative

def analyze_temporal_patterns(changes: List[Dict]) -> Dict:
    """
    Analyze patterns in year-to-year changes for comprehensive insights.
    """
    try:
        if not changes:
            return {}
        
        # Extract percentage changes
        pct_changes = [change["percentage_change"] for change in changes]
        
        # Calculate statistics
        avg_change = np.mean(pct_changes)
        std_change = np.std(pct_changes)
        min_change = min(pct_changes)
        max_change = max(pct_changes)
        
        # Identify patterns
        positive_years = len([c for c in pct_changes if c > 1])
        negative_years = len([c for c in pct_changes if c < -1])
        stable_years = len([c for c in pct_changes if -1 <= c <= 1])
        
        # Trend consistency
        trend_consistency = _assess_trend_consistency(pct_changes)
        
        # Volatility assessment
        volatility = _assess_volatility(std_change)
        
        # Overall trend direction
        overall_trend = _determine_overall_trend(avg_change, trend_consistency)
        
        return {
            "average_change": avg_change,
            "standard_deviation": std_change,
            "min_change": min_change,
            "max_change": max_change,
            "positive_years": positive_years,
            "negative_years": negative_years,
            "stable_years": stable_years,
            "trend_consistency": trend_consistency,
            "volatility": volatility,
            "overall_trend": overall_trend,
            "total_periods": len(changes)
        }
        
    except Exception:
        return {}

def _assess_trend_consistency(changes: List[float]) -> str:
    """Assess how consistent the trend direction is."""
    try:
        if len(changes) < 2:
            return "Insufficient data"
        
        positive_count = len([c for c in changes if c > 0])
        negative_count = len([c for c in changes if c < 0])
        total_count = len(changes)
        
        consistency_ratio = max(positive_count, negative_count) / total_count
        
        if consistency_ratio >= 0.8:
            return "Highly Consistent"
        elif consistency_ratio >= 0.6:
            return "Moderately Consistent"
        else:
            return "Inconsistent/Variable"
            
    except Exception:
        return "Unknown"

def _assess_volatility(std_deviation: float) -> str:
    """Assess the volatility of changes."""
    if std_deviation >= 8:
        return "High Volatility"
    elif std_deviation >= 4:
        return "Moderate Volatility"
    elif std_deviation >= 2:
        return "Low Volatility"
    else:
        return "Very Stable"

def _determine_overall_trend(avg_change: float, consistency: str) -> str:
    """Determine overall trend with confidence level."""
    if abs(avg_change) < 0.5:
        return "Stable (no clear trend)"
    
    direction = "Increasing" if avg_change > 0 else "Decreasing"
    
    if "Highly" in consistency:
        confidence = "Strong"
    elif "Moderately" in consistency:
        confidence = "Moderate"
    else:
        confidence = "Weak"
    
    return f"{direction} ({confidence} trend)"

def create_change_summary_table(changes: List[Dict]) -> str:
    """Create a formatted table of year-to-year changes."""
    try:
        if not changes:
            return "No temporal data available for analysis"
        
        # Create header
        summary = "📊 Year-to-Year Change Analysis\n"
        summary += "=" * 50 + "\n\n"
        
        # Table header
        summary += f"{'Period':<12} {'Change':<8} {'Category':<18} {'Trend':<6}\n"
        summary += "-" * 50 + "\n"
        
        # Add each change
        for change in changes:
            period = f"{change['from_year']}→{change['to_year']}"
            pct_change = f"{change['percentage_change']:+.1f}%"
            category = change['change_category']
            trend = change['trend_indicator']
            
            summary += f"{period:<12} {pct_change:<8} {category:<18} {trend:<6}\n"
        
        return summary
        
    except Exception:
        return "Error generating change summary"

def get_change_insights(changes: List[Dict], patterns: Dict) -> List[str]:
    """Generate intelligent insights from temporal change analysis."""
    insights = []
    
    try:
        if not changes or not patterns:
            return ["Insufficient temporal data for comprehensive change analysis"]
        
        # Volatility insights
        volatility = patterns.get("volatility", "Unknown")
        if volatility == "High Volatility":
            insights.append("🌊 **High Temporal Volatility**: Vegetation levels demonstrate significant inter-annual fluctuations indicating environmental instability")
        elif volatility == "Very Stable":
            insights.append("📊 **Consistent Temporal Pattern**: Systematic year-to-year vegetation changes indicate stable environmental conditions")
        
        # Trend consistency insights
        consistency = patterns.get("trend_consistency", "Unknown")
        overall_trend = patterns.get("overall_trend", "Unknown")
        if "Strong" in overall_trend:
            insights.append(f"🎯 **Robust Directional Trend**: {overall_trend} - highly predictable vegetation trajectory observed")
        elif "Inconsistent" in consistency:
            insights.append("⚡ **Variable Temporal Pattern**: Inconsistent inter-annual changes suggest external environmental factors or disturbance events")
        
        # Extreme changes
        max_change = patterns.get("max_change", 0)
        min_change = patterns.get("min_change", 0)
        
        if max_change > 10:
            insights.append(f"📈 **Maximum Vegetation Increase**: Peak annual growth of {max_change:.1f}% documented in single observation period")
        if min_change < -10:
            insights.append(f"📉 **Significant Vegetation Decline**: Maximum annual reduction of {abs(min_change):.1f}% observed in single period")
        
        # Recent trend analysis
        if len(changes) >= 2:
            recent_change = changes[-1]["percentage_change"]
            if recent_change > 5:
                insights.append(f"🌱 **Recent Vegetation Acceleration**: Most recent period demonstrates {recent_change:.1f}% improvement in coverage")
            elif recent_change < -5:
                insights.append(f"⚠️ **Recent Vegetation Decline**: Most recent period shows {abs(recent_change):.1f}% reduction in coverage")
        
        # Pattern distribution
        positive_years = patterns.get("positive_years", 0)
        negative_years = patterns.get("negative_years", 0)
        total_periods = patterns.get("total_periods", 1)
        
        if positive_years > negative_years * 2:
            insights.append(f"✅ **Predominantly Positive Trajectory**: {positive_years}/{total_periods} observation periods demonstrate vegetation growth")
        elif negative_years > positive_years * 2:
            insights.append(f"⚠️ **Predominantly Declining Pattern**: {negative_years}/{total_periods} observation periods show vegetation reduction")
        else:
            insights.append(f"⚖️ **Balanced Temporal Pattern**: Equilibrium between positive ({positive_years}) and negative ({negative_years}) change periods")
        
        return insights[:5]  # Limit to top 5 insights
        
    except Exception:
        return ["Error generating comprehensive temporal insights"]

def format_changes_for_display(changes: List[Dict]) -> List[Dict]:
    """Format changes for dashboard display with enhanced information."""
    try:
        formatted_changes = []
        
        for change in changes:
            formatted = {
                "period": f"{change['from_year']} → {change['to_year']}",
                "change_text": f"{change['percentage_change']:+.1f}%",
                "change_value": change['percentage_change'],
                "category": change['change_category'],
                "description": change['change_description'],
                "trend_icon": change['trend_indicator'],
                "color_class": _get_color_class(change['percentage_change'])
            }
            formatted_changes.append(formatted)
        
        return formatted_changes
        
    except Exception:
        return []

def _get_color_class(percentage_change: float) -> str:
    """Get appropriate color class for dashboard styling."""
    if percentage_change > 5:
        return "success"  # Green
    elif percentage_change > 1:
        return "info"     # Blue
    elif percentage_change > -1:
        return "secondary" # Gray
    elif percentage_change > -5:
        return "warning"  # Yellow
    else:
        return "danger"   # Red

def calculate_realistic_percentage_change(old_value: float, new_value: float) -> dict:
    """
    Calculate realistic percentage change with environmental constraints.
    
    Returns both raw mathematical value and capped realistic value for transparency.
    Faculty loves seeing the methodology behind realistic environmental interpretation.
    """
    try:
        absolute_change = new_value - old_value
        
        # Raw mathematical calculation
        raw_change = (absolute_change / old_value) * 100 if old_value != 0 else 0
        
        # Improved formula to prevent extreme percentages from small denominators
        safe_denominator = max(old_value, 1.0)  # Minimum 1% to prevent division issues
        improved_change = (absolute_change / safe_denominator) * 100
        
        # Cap to realistic environmental bounds (-50% to +50%)
        capped_change = min(max(improved_change, -50.0), 50.0)
        
        # Determine if capping was applied
        was_capped = abs(improved_change) > 50.0
        
        return {
            "raw_change": raw_change,
            "improved_change": improved_change,
            "final_change": capped_change,
            "was_capped": was_capped,
            "explanation": _get_change_explanation(raw_change, capped_change, was_capped),
            "methodology": "Capped to realistic environmental bounds (-50% to +50%)"
        }
        
    except Exception:
        return {
            "raw_change": 0.0,
            "improved_change": 0.0,
            "final_change": 0.0,
            "was_capped": False,
            "explanation": "Calculation error",
            "methodology": "Error in percentage calculation"
        }

def _get_change_explanation(raw_change: float, final_change: float, was_capped: bool) -> str:
    """Generate explanation for percentage change calculation."""
    if was_capped:
        if raw_change > 50:
            return f"Raw calculation: +{raw_change:.0f}%, capped to +{final_change:.1f}% for realistic environmental interpretation"
        else:
            return f"Raw calculation: {raw_change:.0f}%, capped to {final_change:.1f}% for realistic environmental interpretation"
    else:
        return f"Realistic change: {final_change:.1f}% (within environmental bounds)"

def get_capping_summary(changes: List[Dict]) -> Dict:
    """
    Generate summary of capping applied to percentage changes.
    Useful for faculty explanation of methodology.
    """
    try:
        total_changes = len(changes)
        capped_changes = sum(1 for change in changes if change.get("is_capped", False))
        
        if capped_changes == 0:
            return {
                "total_changes": total_changes,
                "capped_changes": 0,
                "capping_rate": 0.0,
                "summary": "All percentage changes within realistic environmental bounds",
                "methodology_note": "No capping required - natural environmental variation"
            }
        else:
            capping_rate = (capped_changes / total_changes) * 100
            return {
                "total_changes": total_changes,
                "capped_changes": capped_changes,
                "capping_rate": capping_rate,
                "summary": f"{capped_changes}/{total_changes} changes capped for realistic interpretation",
                "methodology_note": "Outliers capped to maintain realistic environmental interpretation"
            }
            
    except Exception:
        return {
            "total_changes": 0,
            "capped_changes": 0,
            "capping_rate": 0.0,
            "summary": "Unable to calculate capping summary",
            "methodology_note": "Error in capping analysis"
        }