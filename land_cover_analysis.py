#!/usr/bin/env python3
"""
Land Cover Distribution Analysis - Critical for DWDM Projects
Provides comprehensive land cover classification statistics and visualizations.
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import Dict, List, Tuple

# Set style for professional plots
plt.style.use('default')

def create_land_cover_pie_chart(class_percentages: Dict[str, float], title: str = "Land Cover Distribution") -> plt.Figure:
    """
    Create professional pie chart for land cover distribution.
    Critical for DWDM evaluation - shows clear data mining results.
    """
    try:
        # Filter out classes with very small percentages for cleaner visualization
        filtered_data = {k: v for k, v in class_percentages.items() if v >= 1.0}
        
        # Group small percentages into "Other"
        small_percentages = {k: v for k, v in class_percentages.items() if v < 1.0}
        if small_percentages:
            other_total = sum(small_percentages.values())
            if other_total > 0:
                filtered_data["Other"] = other_total
        
        if not filtered_data:
            # Fallback for empty data
            filtered_data = {"No Data": 100.0}
        
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Prepare data
        labels = list(filtered_data.keys())
        sizes = list(filtered_data.values())
        
        # Professional color scheme
        colors = plt.cm.Set3(np.linspace(0, 1, len(labels)))
        
        # Create pie chart with professional styling
        wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', 
                                         colors=colors, startangle=90,
                                         textprops={'fontsize': 11, 'fontweight': 'bold'})
        
        # Enhance text appearance
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(10)
        
        # Add title
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        
        # Equal aspect ratio ensures circular pie
        ax.axis('equal')
        
        # Add legend with percentages
        legend_labels = [f"{label}: {size:.1f}%" for label, size in zip(labels, sizes)]
        ax.legend(wedges, legend_labels, title="Land Cover Classes", 
                 loc="center left", bbox_to_anchor=(1, 0, 0.5, 1),
                 fontsize=10)
        
        plt.tight_layout()
        return fig
        
    except Exception as e:
        # Fallback simple chart
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.text(0.5, 0.5, f"Error creating pie chart: {str(e)}", 
               ha='center', va='center', transform=ax.transAxes)
        ax.set_title(title)
        return fig

def create_land_cover_bar_chart(class_percentages: Dict[str, float], title: str = "Land Cover Distribution") -> plt.Figure:
    """
    Create horizontal bar chart for detailed land cover analysis.
    Shows all classes including small percentages.
    """
    try:
        if not class_percentages:
            # Fallback for empty data
            class_percentages = {"No Data": 100.0}
        
        # Sort by percentage (descending)
        sorted_data = dict(sorted(class_percentages.items(), key=lambda x: x[1], reverse=True))
        
        # Create figure
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Prepare data
        labels = list(sorted_data.keys())
        values = list(sorted_data.values())
        
        # Create horizontal bar chart
        bars = ax.barh(labels, values, color=plt.cm.Set3(np.linspace(0, 1, len(labels))))
        
        # Add value labels on bars
        for i, (bar, value) in enumerate(zip(bars, values)):
            ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, 
                   f'{value:.1f}%', ha='left', va='center', fontweight='bold')
        
        # Styling
        ax.set_xlabel('Percentage (%)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Land Cover Classes', fontsize=12, fontweight='bold')
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        ax.grid(axis='x', alpha=0.3)
        
        # Set x-axis limit to accommodate labels
        ax.set_xlim(0, max(values) * 1.15)
        
        plt.tight_layout()
        return fig
        
    except Exception as e:
        # Fallback simple chart
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.text(0.5, 0.5, f"Error creating bar chart: {str(e)}", 
               ha='center', va='center', transform=ax.transAxes)
        ax.set_title(title)
        return fig

def analyze_land_cover_diversity(class_percentages: Dict[str, float]) -> Dict[str, float]:
    """
    Calculate land cover diversity metrics for DWDM analysis.
    Returns Shannon diversity index and other ecological metrics.
    """
    try:
        if not class_percentages:
            return {"shannon_diversity": 0.0, "simpson_diversity": 0.0, "richness": 0}
        
        # Convert percentages to proportions
        total = sum(class_percentages.values())
        proportions = [v/total for v in class_percentages.values() if v > 0]
        
        # Shannon Diversity Index: H = -Σ(pi * ln(pi))
        shannon_diversity = -sum(p * np.log(p) for p in proportions if p > 0)
        
        # Simpson Diversity Index: D = 1 - Σ(pi²)
        simpson_diversity = 1 - sum(p**2 for p in proportions)
        
        # Species richness (number of different classes)
        richness = len([v for v in class_percentages.values() if v > 0])
        
        # Evenness (how evenly distributed the classes are)
        max_diversity = np.log(richness) if richness > 1 else 1
        evenness = shannon_diversity / max_diversity if max_diversity > 0 else 0
        
        return {
            "shannon_diversity": round(shannon_diversity, 3),
            "simpson_diversity": round(simpson_diversity, 3),
            "richness": richness,
            "evenness": round(evenness, 3)
        }
        
    except Exception:
        return {"shannon_diversity": 0.0, "simpson_diversity": 0.0, "richness": 0, "evenness": 0.0}

def get_land_cover_insights(class_percentages: Dict[str, float]) -> Dict[str, str]:
    """
    Generate intelligent insights about land cover distribution.
    Provides DWDM-style analysis and interpretation.
    """
    try:
        if not class_percentages:
            return {"primary": "No data available", "secondary": "", "analysis": ""}
        
        # Sort by percentage
        sorted_classes = sorted(class_percentages.items(), key=lambda x: x[1], reverse=True)
        
        # Primary land cover
        primary_class, primary_pct = sorted_classes[0]
        
        # Secondary land cover
        secondary_class, secondary_pct = sorted_classes[1] if len(sorted_classes) > 1 else ("None", 0)
        
        # Generate insights
        insights = {}
        
        # Primary analysis
        if primary_pct > 60:
            insights["primary"] = f"Dominated by {primary_class} ({primary_pct:.1f}%)"
        elif primary_pct > 40:
            insights["primary"] = f"Primarily {primary_class} ({primary_pct:.1f}%)"
        else:
            insights["primary"] = f"Mixed landscape with {primary_class} as largest component ({primary_pct:.1f}%)"
        
        # Secondary analysis
        if secondary_pct > 20:
            insights["secondary"] = f"Significant {secondary_class} presence ({secondary_pct:.1f}%)"
        elif secondary_pct > 10:
            insights["secondary"] = f"Notable {secondary_class} areas ({secondary_pct:.1f}%)"
        else:
            insights["secondary"] = f"Minor {secondary_class} coverage ({secondary_pct:.1f}%)"
        
        # Overall analysis
        diversity_metrics = analyze_land_cover_diversity(class_percentages)
        richness = diversity_metrics["richness"]
        shannon = diversity_metrics["shannon_diversity"]
        
        if richness <= 2:
            insights["analysis"] = "Low diversity landscape - dominated by few land cover types"
        elif richness <= 4:
            insights["analysis"] = f"Moderate diversity (Shannon: {shannon:.2f}) - mixed land use patterns"
        else:
            insights["analysis"] = f"High diversity (Shannon: {shannon:.2f}) - complex heterogeneous landscape"
        
        return insights
        
    except Exception:
        return {"primary": "Analysis error", "secondary": "", "analysis": ""}

def create_temporal_land_cover_comparison(yearly_data: Dict[int, Dict[str, float]]) -> plt.Figure:
    """
    Create temporal comparison of land cover changes across years.
    Shows evolution of land cover distribution over time.
    """
    try:
        if not yearly_data or len(yearly_data) < 2:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.text(0.5, 0.5, "Need at least 2 years of data for temporal comparison", 
                   ha='center', va='center', transform=ax.transAxes)
            ax.set_title("Temporal Land Cover Comparison")
            return fig
        
        # Prepare data
        years = sorted(yearly_data.keys())
        all_classes = set()
        for year_data in yearly_data.values():
            all_classes.update(year_data.keys())
        all_classes = sorted(list(all_classes))
        
        # Create stacked area chart
        fig, ax = plt.subplots(figsize=(14, 8))
        
        # Prepare data matrix
        data_matrix = []
        for year in years:
            year_values = [yearly_data[year].get(class_name, 0) for class_name in all_classes]
            data_matrix.append(year_values)
        
        data_matrix = np.array(data_matrix).T  # Transpose for plotting
        
        # Create stacked area plot
        ax.stackplot(years, *data_matrix, labels=all_classes, alpha=0.8)
        
        # Styling
        ax.set_xlabel('Year', fontsize=12, fontweight='bold')
        ax.set_ylabel('Percentage (%)', fontsize=12, fontweight='bold')
        ax.set_title('Temporal Land Cover Distribution', fontsize=16, fontweight='bold', pad=20)
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 100)
        
        plt.tight_layout()
        return fig
        
    except Exception as e:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.text(0.5, 0.5, f"Error creating temporal comparison: {str(e)}", 
               ha='center', va='center', transform=ax.transAxes)
        ax.set_title("Temporal Land Cover Comparison")
        return fig


def get_pie_chart_insight(class_percentages: Dict[str, float]) -> str:
    """
    Generate a single dominant-class insight sentence shown below the pie chart.
    Format: "ClassName (XX%) dominates land use, indicating <context>"
    """
    try:
        if not class_percentages:
            return "Insufficient classification data to generate land use insight."

        dominant = max(class_percentages, key=class_percentages.get)
        pct = class_percentages[dominant]

        context_map = {
            "Residential":           "dense residential settlement and urban expansion",
            "Industrial":            "significant industrial activity and infrastructure development",
            "AnnualCrop":            "active agricultural cultivation and seasonal land use",
            "PermanentCrop":         "established perennial agriculture and orchard coverage",
            "Forest":                "high biodiversity habitat and carbon sequestration capacity",
            "HerbaceousVegetation":  "open grassland or shrubland ecosystem presence",
            "Highway":               "extensive transport infrastructure and connectivity networks",
            "Pasture":               "livestock grazing land and pastoral land management",
            "River":                 "riparian corridor and freshwater ecosystem presence",
            "SeaLake":               "significant water body coverage and aquatic habitat",
        }

        # Normalise key — strip spaces, try exact then partial match
        context = None
        for key, desc in context_map.items():
            if key.lower() in dominant.lower() or dominant.lower() in key.lower():
                context = desc
                break
        if context is None:
            context = "predominant land cover type across the study area"

        # Dominance qualifier
        if pct >= 60:
            qualifier = "strongly dominates"
        elif pct >= 40:
            qualifier = "dominates"
        else:
            qualifier = "leads"

        return f"{dominant} ({pct:.1f}%) {qualifier} land use, indicating {context}."

    except Exception:
        return "Land use distribution analysis completed."
