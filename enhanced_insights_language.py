#!/usr/bin/env python3
"""
Enhanced Insights Language System
Provides varied, research-level terminology to eliminate repetition.
"""

import random
from typing import List, Dict

# All vocabulary pools — module-level so they're shared across calls
_TREND_DESCRIPTORS = {
    "positive_strong": [
        "Consistent upward trajectory",
        "Sustained vegetation expansion",
        "Progressive greenery enhancement",
        "Systematic ecological improvement",
        "Continuous environmental recovery",
        "Steady biodiversity augmentation",
        "Persistent vegetation proliferation",
        "Incremental ecosystem restoration",
    ],
    "positive_moderate": [
        "Moderate recovery phase",
        "Gradual vegetation establishment",
        "Incremental greenery development",
        "Steady ecological stabilization",
        "Progressive environmental improvement",
        "Measured vegetation enhancement",
        "Controlled ecosystem regeneration",
        "Phased environmental restoration",
    ],
    "negative_strong": [
        "Accelerated vegetation depletion",
        "Systematic ecological degradation",
        "Progressive environmental deterioration",
        "Continuous habitat fragmentation",
        "Sustained biodiversity reduction",
        "Persistent vegetation regression",
        "Ongoing ecosystem disruption",
        "Cumulative environmental stress",
    ],
    "negative_moderate": [
        "Localized decline observed",
        "Gradual vegetation reduction",
        "Moderate ecological stress",
        "Incremental habitat modification",
        "Measured environmental change",
        "Selective vegetation loss",
        "Targeted ecosystem alteration",
        "Focused environmental pressure",
    ],
    "stable": [
        "Equilibrium vegetation dynamics",
        "Stable ecological baseline",
        "Consistent environmental conditions",
        "Maintained ecosystem balance",
        "Steady-state vegetation patterns",
        "Balanced ecological metrics",
        "Uniform environmental stability",
        "Homeostatic ecosystem function",
    ],
}

_MAGNITUDE_DESCRIPTORS = {
    "high":     ["substantial", "considerable", "pronounced", "extensive",
                 "marked", "appreciable", "prominent", "conspicuous"],
    "moderate": ["moderate", "measurable", "discernible", "observable",
                 "detectable", "perceptible", "evident", "apparent"],
    "low":      ["minimal", "slight", "marginal", "limited",
                 "modest", "subtle", "minor", "negligible"],
}

_TEMPORAL_DESCRIPTORS = {
    "recent":    ["contemporary", "current", "latest", "most recent",
                  "present-day", "ongoing", "immediate", "proximate"],
    "historical":["baseline", "initial", "foundational", "reference",
                  "antecedent", "precedent", "original", "primary"],
    "long_term": ["longitudinal", "extended", "multi-year", "comprehensive",
                  "sustained", "prolonged", "continuous", "persistent"],
}

_CHANGE_DESCRIPTORS = {
    "increase":       ["expansion", "augmentation", "enhancement", "proliferation",
                       "amplification", "escalation", "intensification", "growth"],
    "decrease":       ["reduction", "diminishment", "contraction", "depletion",
                       "attenuation", "regression", "decline", "deterioration"],
    "transformation": ["modification", "alteration", "conversion", "transition",
                       "metamorphosis", "evolution", "adaptation", "restructuring"],
}

_ANALYTICAL_TERMS = {
    "observation": ["documented", "recorded", "identified", "detected",
                    "observed", "noted", "established", "confirmed"],
    "analysis":    ["analysis reveals", "examination indicates", "assessment demonstrates",
                    "evaluation shows", "investigation confirms", "study establishes",
                    "research documents", "findings suggest"],
    "prediction":  ["projections indicate", "models suggest", "forecasts predict",
                    "extrapolations show", "simulations demonstrate", "estimates project",
                    "calculations predict", "algorithms forecast"],
}

# Per-pool usage tracking to avoid repetition
_used: Dict[str, set] = {}


def _pick(pool_name: str, pool: Dict[str, List[str]], key: str) -> str:
    """Pick a term from pool[key] that hasn't been used recently."""
    terms = pool.get(key, [])
    if not terms:
        return key  # fallback to the key itself

    tracker_key = f"{pool_name}:{key}"
    used_set = _used.setdefault(tracker_key, set())

    available = [t for t in terms if t not in used_set]
    if not available:
        used_set.clear()
        available = terms

    chosen = random.choice(available)
    used_set.add(chosen)
    return chosen


class ResearchLanguageGenerator:
    """Generates varied, research-level language for insights."""

    def get_trend_description(self, slope: float) -> str:
        if slope > 1.0:
            key = "positive_strong"
        elif slope > 0.2:
            key = "positive_moderate"
        elif slope < -1.0:
            key = "negative_strong"
        elif slope < -0.2:
            key = "negative_moderate"
        else:
            key = "stable"
        return _pick("trend", _TREND_DESCRIPTORS, key)

    def get_magnitude_term(self, value: float,
                           thresholds: Dict[str, float] = None) -> str:
        if thresholds is None:
            thresholds = {"high": 10.0, "moderate": 3.0}
        if abs(value) >= thresholds["high"]:
            key = "high"
        elif abs(value) >= thresholds["moderate"]:
            key = "moderate"
        else:
            key = "low"
        return _pick("magnitude", _MAGNITUDE_DESCRIPTORS, key)

    def get_temporal_term(self, period: str = "recent") -> str:
        return _pick("temporal", _TEMPORAL_DESCRIPTORS, period)

    def get_change_description(self, change_value: float) -> str:
        if change_value > 0:
            key = "increase"
        elif change_value < 0:
            key = "decrease"
        else:
            key = "transformation"
        return _pick("change", _CHANGE_DESCRIPTORS, key)

    def get_analytical_phrase(self, analysis_type: str = "observation") -> str:
        return _pick("analytical", _ANALYTICAL_TERMS, analysis_type)

    # Kept for backward-compat with any callers using the old signature
    def get_varied_term(self, category: str, subcategory: str = None) -> str:
        pool_map = {
            "trend_descriptors": (_TREND_DESCRIPTORS, "stable"),
            "magnitude":         (_MAGNITUDE_DESCRIPTORS, "moderate"),
            "temporal":          (_TEMPORAL_DESCRIPTORS, "recent"),
            "change":            (_CHANGE_DESCRIPTORS, "transformation"),
            "analytical":        (_ANALYTICAL_TERMS, "observation"),
        }
        pool, default_key = pool_map.get(category, ({}, ""))
        key = subcategory if subcategory else default_key
        return _pick(category, pool, key)


def enhance_temporal_insights(years: List[int],
                               green_percentages: List[float]) -> List[str]:
    """Generate enhanced temporal insights with varied language."""
    import numpy as np
    gen = ResearchLanguageGenerator()
    insights = []

    try:
        if len(green_percentages) >= 2:
            slope = float(np.polyfit(range(len(years)), green_percentages, 1)[0])

            trend_desc  = gen.get_trend_description(slope)
            magnitude   = gen.get_magnitude_term(slope, {"high": 1.0, "moderate": 0.3})
            analytical  = gen.get_analytical_phrase("analysis")
            insights.append(
                f"🌱 **Temporal Vegetation Dynamics**: {analytical.title()} "
                f"{trend_desc} with {magnitude} annual rate of {abs(slope):.1f}% "
                f"since {years[0]}"
            )

            if len(green_percentages) >= 3:
                recent_change = green_percentages[-1] - green_percentages[-2]
                if abs(recent_change) > 2.0:
                    change_desc  = gen.get_change_description(recent_change)
                    temporal     = gen.get_temporal_term("recent")
                    mag2         = gen.get_magnitude_term(recent_change)
                    insights.append(
                        f"📈 **{temporal.title()} Vegetation Dynamics**: "
                        f"{mag2.title()} {abs(recent_change):.1f}% {change_desc} "
                        f"documented during {years[-1]}"
                    )

            if len(green_percentages) > 2:
                net = green_percentages[-1] - green_percentages[0]
                if abs(net) > 5.0:
                    temporal2    = gen.get_temporal_term("long_term")
                    change_desc2 = gen.get_change_description(net)
                    obs          = gen.get_analytical_phrase("observation")
                    insights.append(
                        f"📊 **{temporal2.title()} Environmental Assessment**: "
                        f"{abs(net):.1f}% net {change_desc2} {obs} "
                        f"across {years[0]}–{years[-1]} study period"
                    )
    except Exception:
        pass

    return insights


def enhance_prediction_insights(prediction_data: Dict,
                                 years: List[int],
                                 green_percentages: List[float]) -> List[str]:
    """Generate enhanced prediction insights with varied language."""
    gen = ResearchLanguageGenerator()
    insights = []

    try:
        if "prediction" in prediction_data and "target_year" in prediction_data:
            prediction   = prediction_data["prediction"]
            target_year  = prediction_data["target_year"]
            current      = green_percentages[-1] if green_percentages else 50.0
            change       = prediction - current

            pred_phrase  = gen.get_analytical_phrase("prediction")

            if change > 5.0:
                change_desc = gen.get_change_description(change)
                magnitude   = gen.get_magnitude_term(change)
                insights.append(
                    f"🌟 **Predictive Environmental Modeling**: "
                    f"{pred_phrase.title()} {magnitude} {change:.1f}% vegetation "
                    f"{change_desc} trajectory toward {target_year}"
                )
            elif change < -5.0:
                change_desc = gen.get_change_description(change)
                magnitude   = gen.get_magnitude_term(abs(change))
                insights.append(
                    f"⚠️ **Environmental Risk Projection**: "
                    f"{pred_phrase.title()} {magnitude} {abs(change):.1f}% "
                    f"vegetation {change_desc} by {target_year}"
                )
            else:
                stability = gen.get_trend_description(0)  # stable
                insights.append(
                    f"📊 **Environmental Stability Forecast**: "
                    f"{pred_phrase.title()} {stability} through {target_year}"
                )
    except Exception:
        pass

    return insights
