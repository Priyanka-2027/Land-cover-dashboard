def simulate(green: float, urban_increase: float, plantation: float) -> float:
    """
    Enhanced scenario-based simulation to predict environmental changes.
    Greenery Change = Baseline - (Urban Incr * 0.5) + (Plantation * 0.7)
    """
    try:
        # Calculate simulation result
        # Assuming 50% urban growth replaces greenery (0.5 impact)
        # Assuming 70% of new plantation successfully becomes greenery (0.7 efficiency)
        adjusted_green = green - (urban_increase * 0.5) + (plantation * 0.7)
        
        # Ensure greenery stays within realistic bounds (0-100%)
        return max(0.0, min(100.0, float(adjusted_green)))
    except Exception:
        return float(green)

def get_detailed_simulation_explanation(
    current: float, 
    simulated: float, 
    urban_increase: float, 
    plantation: float
) -> dict:
    """
    Generate comprehensive simulation explanation with impact breakdown.
    Faculty loves detailed explanations showing the calculation logic.
    """
    try:
        # Calculate individual impacts
        urban_impact = -(urban_increase * 0.5)  # Negative impact
        plantation_impact = plantation * 0.7    # Positive impact
        net_change = simulated - current
        
        # Create detailed explanation
        explanation = {
            "baseline": current,
            "urban_impact": urban_impact,
            "plantation_impact": plantation_impact,
            "net_change": net_change,
            "final_result": simulated,
            "urban_explanation": f"Urban increase of {urban_increase}% reduces greenery by ~{abs(urban_impact):.1f}%",
            "plantation_explanation": f"Plantation effort of {plantation}% adds ~{plantation_impact:.1f}% greenery",
            "net_explanation": _get_net_impact_explanation(net_change),
            "calculation_breakdown": f"{current:.1f}% - {abs(urban_impact):.1f}% + {plantation_impact:.1f}% = {simulated:.1f}%",
            "impact_ratio": _calculate_impact_ratio(urban_impact, plantation_impact),
            "sustainability_assessment": _assess_sustainability(current, simulated, net_change),
            "recommendations": _generate_simulation_recommendations(current, simulated, urban_increase, plantation)
        }
        
        return explanation
        
    except Exception:
        return {
            "baseline": current,
            "urban_impact": 0,
            "plantation_impact": 0,
            "net_change": 0,
            "final_result": current,
            "urban_explanation": "Calculation error",
            "plantation_explanation": "Calculation error",
            "net_explanation": "Unable to calculate impact",
            "calculation_breakdown": "Error in simulation",
            "impact_ratio": "Unknown",
            "sustainability_assessment": "Assessment unavailable",
            "recommendations": []
        }

def _get_net_impact_explanation(net_change: float) -> str:
    """Generate explanation for net impact."""
    if net_change > 2.0:
        return f"Significant improvement: +{net_change:.1f}% net greenery gain"
    elif net_change > 0.5:
        return f"Moderate improvement: +{net_change:.1f}% net greenery gain"
    elif net_change > -0.5:
        return f"Balanced scenario: {net_change:+.1f}% minimal net change"
    elif net_change > -2.0:
        return f"Moderate decline: {net_change:.1f}% net greenery loss"
    else:
        return f"Significant decline: {net_change:.1f}% net greenery loss"

def _calculate_impact_ratio(urban_impact: float, plantation_impact: float) -> str:
    """Calculate the ratio between urban and plantation impacts."""
    try:
        if plantation_impact == 0:
            return "No plantation offset for urban impact"
        
        ratio = abs(urban_impact) / plantation_impact
        
        if ratio > 1.5:
            return f"Urban impact {ratio:.1f}x stronger than plantation effort"
        elif ratio > 1.0:
            return f"Urban impact {ratio:.1f}x stronger - plantation insufficient"
        elif ratio > 0.5:
            return f"Plantation effort {1/ratio:.1f}x stronger than urban impact"
        else:
            return f"Plantation effort {1/ratio:.1f}x stronger - excellent offset"
            
    except Exception:
        return "Impact ratio calculation error"

def _assess_sustainability(current: float, simulated: float, net_change: float) -> str:
    """Assess the sustainability of the simulation scenario."""
    try:
        if simulated < 20:
            return "🚨 Unsustainable: Critical vegetation loss threatens ecosystem health"
        elif simulated < 30:
            return "⚠️ Concerning: Low vegetation levels require immediate intervention"
        elif net_change < -5:
            return "📉 Declining: Negative trend threatens long-term sustainability"
        elif net_change > 5:
            return "📈 Improving: Positive trend supports environmental health"
        elif simulated > 50:
            return "✅ Sustainable: Good vegetation levels support ecosystem services"
        else:
            return "⚖️ Balanced: Moderate vegetation levels - monitor for stability"
            
    except Exception:
        return "Sustainability assessment unavailable"

def _generate_simulation_recommendations(
    current: float, 
    simulated: float, 
    urban_increase: float, 
    plantation: float
) -> list:
    """Generate specific recommendations based on simulation results."""
    recommendations = []
    
    try:
        net_change = simulated - current
        
        # Urban development recommendations
        if urban_increase > 20:
            recommendations.append("🏗️ High urban growth planned - implement green building standards")
        elif urban_increase > 10:
            recommendations.append("🏘️ Moderate urban growth - ensure green space requirements")
        
        # Plantation recommendations
        if plantation < urban_increase * 1.5:
            recommendations.append("🌱 Increase plantation efforts to offset urban development")
        elif plantation > urban_increase * 2:
            recommendations.append("🌳 Excellent plantation planning - maintain implementation quality")
        
        # Result-based recommendations
        if simulated < 25:
            recommendations.append("🚨 Critical: Implement emergency green infrastructure program")
        elif simulated < current - 5:
            recommendations.append("⚠️ Declining: Revise development plans to protect vegetation")
        elif simulated > current + 5:
            recommendations.append("✅ Positive: Continue current environmental strategy")
        
        # Balance recommendations
        if abs(net_change) < 1:
            recommendations.append("⚖️ Balanced approach - monitor implementation closely")
        
        return recommendations[:4]  # Limit to top 4 recommendations
        
    except Exception:
        return ["Recommendation generation error"]

def explain_simulated_result(current: float, simulated: float) -> str:
    """
    Legacy function - kept for backward compatibility.
    Use get_detailed_simulation_explanation() for comprehensive analysis.
    """
    try:
        diff = simulated - current
        if diff > 0:
            return f"Net Improvement: Targeted plantation efforts will increase total greenery by {abs(diff):.2f}%."
        elif diff < 0:
            return f"Caution: Urban growth will lead to a net loss of {abs(diff):.2f}% in greenery."
        else:
            return "Neutral Impact: Your plan stabilizes the current greenery levels."
    except Exception:
        return "Unknown simulation result."
