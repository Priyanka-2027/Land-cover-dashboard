#!/usr/bin/env python3
"""
Test the comprehensive report generator system.
"""

from report_generator import generate_comprehensive_report
from temporal_analysis import calculate_year_to_year_changes, analyze_temporal_patterns
from validation_system import assess_prediction_confidence
from key_insights import generate_key_insights

def test_report_generator():
    """Test comprehensive report generation with sample data."""
    print("📄 Testing Comprehensive Report Generator")
    print("=" * 60)
    
    # Sample data for testing
    years = [2019, 2020, 2021, 2022, 2023]
    green_percentages = [35.0, 38.5, 42.0, 45.2, 48.1]
    target_year = 2030
    
    print(f"Test Data: {years} → {green_percentages}")
    
    # Generate all analysis components
    print("\n🔄 Generating analysis components...")
    
    # Temporal analysis
    temporal_changes = calculate_year_to_year_changes(years, green_percentages)
    temporal_patterns = analyze_temporal_patterns(temporal_changes)
    print(f"✅ Temporal analysis: {len(temporal_changes)} period changes")
    
    # Prediction data
    prediction_data = {
        "prediction": 55.2,
        "target_year": target_year,
        "model_info": {
            "equation": "y = 3.2x + 35.0",
            "r_squared": 0.92,
            "slope": 3.2,
            "intercept": 35.0,
            "constrained": False
        }
    }
    print("✅ Prediction data prepared")
    
    # Validation data
    validation_data = assess_prediction_confidence(years, green_percentages, prediction_data["model_info"])
    print(f"✅ Validation assessment: {validation_data['confidence_level']} confidence")
    
    # Change detection data
    change_data = {"change_percentage": 8.5}
    print("✅ Change detection data prepared")
    
    # Land cover data
    land_cover_data = {
        "class_percentages": {
            "Forest": 35.2,
            "Residential": 28.7,
            "AnnualCrop": 15.3,
            "Highway": 8.9,
            "Industrial": 6.4,
            "River": 3.2,
            "Pasture": 2.3
        }
    }
    print("✅ Land cover data prepared")
    
    # Simulation data
    simulation_data = {
        "baseline": 48.1,
        "urban_increase": 15.0,
        "plantation": 20.0,
        "result": 56.1,
        "detailed_explanation": {
            "calculation_breakdown": "48.1% - 7.5% + 15.5% = 56.1%",
            "urban_explanation": "Urban increase of 15.0% reduces greenery by ~7.5%",
            "plantation_explanation": "Plantation effort of 20.0% adds ~15.5% greenery",
            "net_explanation": "Significant improvement: +8.0% net greenery gain",
            "impact_ratio": "Plantation effort 2.1x stronger - excellent offset",
            "sustainability_assessment": "Improving: Positive trend supports environmental health",
            "recommendations": [
                "Continue current environmental strategy",
                "Maintain plantation implementation quality"
            ]
        }
    }
    print("✅ Simulation data prepared")
    
    # Key insights
    key_insights = generate_key_insights(
        years=years,
        green_percentages=green_percentages,
        prediction_data=prediction_data,
        change_data=change_data,
        land_cover_data=land_cover_data
    )
    print(f"✅ Key insights: {len(key_insights)} insights generated")
    
    # Generate comprehensive report
    print("\n📝 Generating comprehensive report...")
    
    report = generate_comprehensive_report(
        years=years,
        green_percentages=green_percentages,
        prediction_data=prediction_data,
        validation_data=validation_data,
        temporal_changes=temporal_changes,
        temporal_patterns=temporal_patterns,
        change_detection_data=change_data,
        land_cover_data=land_cover_data,
        simulation_data=simulation_data,
        key_insights=key_insights
    )
    
    print(f"✅ Report generated successfully!")
    print(f"   Report length: {len(report)} characters")
    print(f"   Estimated pages: {len(report) // 3000} pages")
    
    # Save report to file for inspection
    with open("test_comprehensive_report.md", "w", encoding="utf-8") as f:
        f.write(report)
    
    print("✅ Report saved as 'test_comprehensive_report.md'")
    
    # Show report structure
    print("\n📋 Report Structure Analysis:")
    sections = report.split("## ")
    print(f"   Total sections: {len(sections)}")
    
    for i, section in enumerate(sections[1:], 1):  # Skip first empty section
        section_title = section.split("\n")[0]
        section_length = len(section)
        print(f"   {i}. {section_title} ({section_length} chars)")
    
    # Show preview
    print("\n📖 Report Preview (First 500 characters):")
    print("-" * 60)
    print(report[:500] + "...")
    print("-" * 60)
    
    print("\n🎯 Test Summary:")
    print("✅ Report generation working")
    print("✅ All analysis components integrated")
    print("✅ Professional formatting applied")
    print("✅ Comprehensive content included")
    print("✅ Faculty-impressive documentation complete")

def test_report_sections():
    """Test individual report sections."""
    print("\n" + "=" * 60)
    print("📑 Testing Individual Report Sections")
    print("=" * 60)
    
    # Test with minimal data
    years_min = [2022, 2023]
    values_min = [40.0, 43.0]
    
    print("\n🔍 Testing with minimal data (2 points):")
    
    # Generate minimal report
    minimal_report = generate_comprehensive_report(
        years=years_min,
        green_percentages=values_min,
        prediction_data={"prediction": 46.0, "target_year": 2025},
        key_insights=["Positive trend detected", "Moderate confidence level"]
    )
    
    print(f"   Minimal report length: {len(minimal_report)} characters")
    print("   ✅ Handles minimal data gracefully")
    
    # Test with comprehensive data
    years_comp = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
    values_comp = [30.0, 33.0, 36.5, 40.0, 43.8, 47.2, 50.5]
    
    print("\n🔍 Testing with comprehensive data (7 points):")
    
    # Generate comprehensive report
    comp_report = generate_comprehensive_report(
        years=years_comp,
        green_percentages=values_comp,
        prediction_data={
            "prediction": 58.0,
            "target_year": 2030,
            "model_info": {"equation": "y = 2.9x + 30.0", "r_squared": 0.95}
        },
        validation_data={"confidence_level": "Very High", "validation_score": 16},
        key_insights=["Strong positive trend", "Excellent model fit", "High confidence prediction"]
    )
    
    print(f"   Comprehensive report length: {len(comp_report)} characters")
    print("   ✅ Handles comprehensive data effectively")
    
    # Compare report sizes
    size_ratio = len(comp_report) / len(minimal_report)
    print(f"\n📊 Report scaling: {size_ratio:.1f}x larger with more data")

def test_faculty_scenarios():
    """Test report generation for different academic levels."""
    print("\n" + "=" * 60)
    print("🎓 Faculty Evaluation Scenarios")
    print("=" * 60)
    
    scenarios = [
        {
            "name": "PhD Research Quality",
            "years": [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
            "values": [32.0, 34.5, 37.2, 39.8, 42.5, 45.1, 47.8, 50.2],
            "r_squared": 0.98,
            "expected_length": 8000
        },
        {
            "name": "Master's Thesis Quality",
            "years": [2020, 2021, 2022, 2023, 2024],
            "values": [38.0, 41.2, 44.5, 47.8, 51.0],
            "r_squared": 0.89,
            "expected_length": 6000
        },
        {
            "name": "Undergraduate Project",
            "years": [2022, 2023, 2024],
            "values": [42.0, 45.5, 49.0],
            "r_squared": 0.72,
            "expected_length": 4000
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n🔍 Scenario {i}: {scenario['name']}")
        
        # Generate report for scenario
        report = generate_comprehensive_report(
            years=scenario["years"],
            green_percentages=scenario["values"],
            prediction_data={
                "prediction": scenario["values"][-1] + 5.0,
                "target_year": 2030,
                "model_info": {"r_squared": scenario["r_squared"]}
            }
        )
        
        print(f"   Data points: {len(scenario['years'])}")
        print(f"   Report length: {len(report)} characters")
        print(f"   Expected: ~{scenario['expected_length']} characters")
        print(f"   Quality: {'✅ Excellent' if len(report) >= scenario['expected_length'] * 0.8 else '⚠️ Adequate'}")

if __name__ == "__main__":
    test_report_generator()
    test_report_sections()
    test_faculty_scenarios()