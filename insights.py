import numpy as np
from typing import List, Dict, Tuple, Optional
from datetime import datetime

def generate_comprehensive_insights(
    years: List[int], 
    green_percentages: List[float], 
    land_cover_data: Optional[List[Dict]] = None,
    confidence_stats: Optional[List[Dict]] = None
) -> Dict[str, List[str]]:
    """
    Generate comprehensive environmental insights from multi-year analysis.
    Provides automatic analysis for top-grade DWDM evaluation.
    """
    insights = {
        "critical": [],
        "trends": [],
        "recommendations": [],
        "opportunities": [],
        "technical": []
    }
    
    try:
        if len(years) < 2 or len(green_percentages) < 2:
            insights["technical"].append("Insufficient temporal data for comprehensive trend analysis")
            return insights
        
        # Vegetation Trend Analysis
        vegetation_insights = _analyze_vegetation_trends(years, green_percentages)
        insights["trends"].extend(vegetation_insights["trends"])
        insights["critical"].extend(vegetation_insights["critical"])
        insights["recommendations"].extend(vegetation_insights["recommendations"])
        
        # Change Rate Analysis
        change_insights = _analyze_change_rates(years, green_percentages)
        insights["trends"].extend(change_insights["trends"])
        insights["opportunities"].extend(change_insights["opportunities"])
        
        # Temporal Pattern Analysis
        pattern_insights = _analyze_temporal_patterns(years, green_percentages)
        insights["trends"].extend(pattern_insights["trends"])
        insights["recommendations"].extend(pattern_insights["recommendations"])
        
        # Land Cover Analysis (if available)
        if land_cover_data:
            landcover_insights = _analyze_land_cover_patterns(land_cover_data)
            insights["trends"].extend(landcover_insights["trends"])
            insights["opportunities"].extend(landcover_insights["opportunities"])
        
        # Confidence Analysis (if available)
        if confidence_stats:
            confidence_insights = _analyze_confidence_patterns(confidence_stats)
            insights["technical"].extend(confidence_insights["technical"])
        
        # Environmental Risk Assessment
        risk_insights = _assess_environmental_risks(years, green_percentages)
        insights["critical"].extend(risk_insights["critical"])
        insights["recommendations"].extend(risk_insights["recommendations"])
        
        # Future Outlook
        future_insights = _generate_future_outlook(years, green_percentages)
        insights["opportunities"].extend(future_insights["opportunities"])
        insights["recommendations"].extend(future_insights["recommendations"])
        
    except Exception as e:
        insights["technical"].append(f"Analysis error encountered: {str(e)}")
    
    return insights

def _analyze_vegetation_trends(years: List[int], green_percentages: List[float]) -> Dict[str, List[str]]:
    """Analyze vegetation trends and generate insights."""
    insights = {"trends": [], "critical": [], "recommendations": []}
    
    # Calculate overall trend
    total_change = green_percentages[-1] - green_percentages[0]
    time_span = years[-1] - years[0]
    annual_rate = total_change / time_span if time_span > 0 else 0
    
    # Trend classification
    if abs(annual_rate) < 0.5:
        insights["trends"].append(f"Vegetation levels remain relatively stable ({annual_rate:+.2f}%/year)")
    elif annual_rate > 0:
        if annual_rate > 2:
            insights["trends"].append(f"Significant vegetation recovery detected (+{annual_rate:.2f}%/year)")
            insights["opportunities"].append("Positive environmental trend - consider expanding conservation efforts")
        else:
            insights["trends"].append(f"Gradual vegetation improvement observed (+{annual_rate:.2f}%/year)")
    else:
        if annual_rate < -2:
            insights["critical"].append(f"Rapid vegetation loss detected ({annual_rate:.2f}%/year)")
            insights["recommendations"].append("Immediate intervention required to prevent further degradation")
        else:
            insights["trends"].append(f"Moderate vegetation decline observed ({annual_rate:.2f}%/year)")
            insights["recommendations"].append("Monitor closely and consider preventive measures")
    
    # Current state assessment
    current_green = green_percentages[-1]
    if current_green < 20:
        insights["critical"].append(f"Critical vegetation levels detected ({current_green:.1f}%)")
        insights["recommendations"].append("Emergency reforestation and conservation measures needed")
    elif current_green < 35:
        insights["critical"].append(f"Below-optimal vegetation coverage ({current_green:.1f}%)")
        insights["recommendations"].append("Increase green infrastructure and urban planning controls")
    elif current_green > 60:
        insights["trends"].append(f"Healthy vegetation coverage maintained ({current_green:.1f}%)")
    
    return insights

def _analyze_change_rates(years: List[int], green_percentages: List[float]) -> Dict[str, List[str]]:
    """Analyze year-over-year change rates."""
    insights = {"trends": [], "opportunities": []}
    
    # Calculate year-over-year changes
    changes = []
    for i in range(1, len(green_percentages)):
        change = green_percentages[i] - green_percentages[i-1]
        changes.append(change)
    
    if changes:
        # Find periods of significant change
        max_increase = max(changes)
        max_decrease = min(changes)
        
        if max_increase > 3:
            max_idx = changes.index(max_increase) + 1
            insights["trends"].append(f"Significant vegetation recovery in {years[max_idx]} (+{max_increase:.1f}%)")
            insights["opportunities"].append("Identify and replicate successful conservation practices from this period")
        
        if max_decrease < -3:
            min_idx = changes.index(max_decrease) + 1
            insights["trends"].append(f"Major vegetation loss occurred in {years[min_idx]} ({max_decrease:.1f}%)")
        
        # Volatility analysis
        volatility = np.std(changes)
        if volatility > 2:
            insights["trends"].append(f"High environmental volatility detected (σ={volatility:.1f}%)")
        elif volatility < 0.5:
            insights["trends"].append("Stable environmental conditions with minimal year-to-year variation")
    
    return insights

def _analyze_temporal_patterns(years: List[int], green_percentages: List[float]) -> Dict[str, List[str]]:
    """Analyze temporal patterns and inflection points."""
    insights = {"trends": [], "recommendations": []}
    
    # Detect trend changes (inflection points)
    if len(green_percentages) >= 3:
        # Calculate moving differences
        early_trend = green_percentages[len(green_percentages)//2] - green_percentages[0]
        late_trend = green_percentages[-1] - green_percentages[len(green_percentages)//2]
        
        if early_trend > 0 and late_trend < 0:
            insights["trends"].append("Environmental degradation accelerated in recent years")
            insights["recommendations"].append("Investigate recent policy or development changes")
        elif early_trend < 0 and late_trend > 0:
            insights["trends"].append("Environmental recovery trend established in recent years")
            insights["recommendations"].append("Continue and expand current conservation strategies")
        
        # Acceleration analysis
        if len(years) >= 4:
            mid_point = len(years) // 2
            early_rate = (green_percentages[mid_point] - green_percentages[0]) / (years[mid_point] - years[0])
            late_rate = (green_percentages[-1] - green_percentages[mid_point]) / (years[-1] - years[mid_point])
            
            if abs(late_rate - early_rate) > 1:
                if late_rate > early_rate:
                    insights["trends"].append("Environmental improvement is accelerating")
                else:
                    insights["trends"].append("Environmental degradation is accelerating")
    
    return insights

def _analyze_land_cover_patterns(land_cover_data: List[Dict]) -> Dict[str, List[str]]:
    """Analyze land cover classification patterns."""
    insights = {"trends": [], "opportunities": []}
    
    # This would analyze land cover changes over time if multiple years of data available
    # For now, analyze current state
    if land_cover_data:
        latest_data = land_cover_data[-1] if isinstance(land_cover_data, list) else land_cover_data
        
        # Analyze dominant land uses
        if "Forest" in str(latest_data) and "40" in str(latest_data):
            insights["trends"].append("Forest coverage represents significant portion of landscape")
            insights["opportunities"].append("Leverage existing forest areas for carbon sequestration programs")
        
        if "Urban" in str(latest_data):
            insights["trends"].append("Urban development pressure detected in analysis area")
            insights["opportunities"].append("Implement green building standards and urban forest initiatives")
    
    return insights

def _analyze_confidence_patterns(confidence_stats: List[Dict]) -> Dict[str, List[str]]:
    """Analyze classification confidence patterns."""
    insights = {"technical": []}
    
    if confidence_stats:
        latest_stats = confidence_stats[-1] if isinstance(confidence_stats, list) else confidence_stats
        avg_conf = latest_stats.get("average", 0)
        
        if avg_conf >= 85:
            insights["technical"].append("High-quality classification results with excellent confidence levels")
        elif avg_conf >= 75:
            insights["technical"].append("Good classification reliability suitable for decision-making")
        elif avg_conf < 65:
            insights["technical"].append("Classification confidence below optimal - consider model retraining")
    
    return insights

def _assess_environmental_risks(years: List[int], green_percentages: List[float]) -> Dict[str, List[str]]:
    """Assess environmental risks based on trends."""
    insights = {"critical": [], "recommendations": []}
    
    current_green = green_percentages[-1]
    trend = green_percentages[-1] - green_percentages[0]
    
    # Risk assessment matrix
    if current_green < 25 and trend < -5:
        insights["critical"].append("CRITICAL: Severe environmental degradation with declining trend")
        insights["recommendations"].append("Declare environmental emergency and implement immediate restoration")
    elif current_green < 30 or trend < -10:
        insights["critical"].append("HIGH RISK: Environmental conditions approaching critical thresholds")
        insights["recommendations"].append("Accelerate conservation efforts and restrict development")
    elif current_green < 40 and trend < 0:
        insights["recommendations"].append("MODERATE RISK: Implement preventive conservation measures")
    
    return insights

def _generate_future_outlook(years: List[int], green_percentages: List[float]) -> Dict[str, List[str]]:
    """Generate future outlook and opportunities."""
    insights = {"opportunities": [], "recommendations": []}
    
    # Simple linear projection for next 5 years
    if len(years) >= 2:
        trend = (green_percentages[-1] - green_percentages[0]) / (years[-1] - years[0])
        future_projection = green_percentages[-1] + (trend * 5)
        
        if future_projection > green_percentages[-1] + 5:
            insights["opportunities"].append("Positive trajectory suggests significant environmental improvement potential")
            insights["recommendations"].append("Maintain current conservation momentum and consider expansion")
        elif future_projection < green_percentages[-1] - 5:
            insights["opportunities"].append("Current trends indicate need for intervention to prevent degradation")
            insights["recommendations"].append("Implement aggressive conservation strategies to reverse negative trends")
        else:
            insights["opportunities"].append("Stable environmental trajectory with opportunities for targeted improvements")
    
    return insights

def format_insights_for_display(insights: Dict[str, List[str]]) -> str:
    """Format insights for professional dashboard display."""
    formatted = []
    
    if insights["critical"]:
        formatted.append("🚨 **CRITICAL FINDINGS:**")
        for insight in insights["critical"]:
            formatted.append(f"• {insight}")
        formatted.append("")
    
    if insights["trends"]:
        formatted.append("📈 **TREND ANALYSIS:**")
        for insight in insights["trends"]:
            formatted.append(f"• {insight}")
        formatted.append("")
    
    if insights["recommendations"]:
        formatted.append("💡 **RECOMMENDATIONS:**")
        for insight in insights["recommendations"]:
            formatted.append(f"• {insight}")
        formatted.append("")
    
    if insights["opportunities"]:
        formatted.append("🌟 **OPPORTUNITIES:**")
        for insight in insights["opportunities"]:
            formatted.append(f"• {insight}")
        formatted.append("")
    
    if insights["technical"]:
        formatted.append("🔧 **TECHNICAL NOTES:**")
        for insight in insights["technical"]:
            formatted.append(f"• {insight}")
    
    return "\n".join(formatted)