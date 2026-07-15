def suggest(green: float) -> str:
    """
    Generate automated environmental recommendations based on current greenery levels.
    """
    try:
        if green < 30.0:
            return "Urgent plantation required - Critical greenery levels detected"
        elif 30.0 <= green <= 50.0:
            return "Control urban expansion - Moderate greenery maintenance needed"
        else:
            return "Maintain current greenery levels - Healthy environmental state"
    except Exception:
        return "Environmental maintenance recommended"

def get_simulation_recommendation(current: float, simulated: float) -> str:
    """Provide feedback on the sustainability of proposed simulation scenarios."""
    try:
        if simulated > current:
            return "Increase plantation to balance urban growth 🌱"
        elif simulated < current:
            return "Reduce urban expansion to preserve greenery 🏙️"
        else:
            return "Current plan maintains environmental balance ⚖️"
    except Exception:
        return "Continue environmental monitoring 📊"
