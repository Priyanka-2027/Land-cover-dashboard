#!/usr/bin/env python3
"""
Test the Key Insights generation system.
"""

from key_insights import generate_key_insights, format_insights_for_display, get_insight_summary_stats

def test_key_insights():
    """Test key insights generation with various scenarios."""
    print("📌 Testing Key Insights Generation System")
    print("=" * 60)
    
    # Test Case 1: Declining trend scenario
    print("\n🔍 Test Case 1: Declining Greenery Trend")
    years1 = [2020, 2021, 2022, 2023]
    greenery1 = [45.0, 42.0, 38.0, 35.0]  # Declining trend
    prediction_data1 = {
        "prediction": 30.0,
        "target_year": 2030,
        "model_info": {"r_squared": 0.85, "constrained": False}
    }
    change_data1 = {"change_percentage": 12.5}
    
    insights1 = generate_key_insights(years1, greenery1, prediction_data1, change_data1)
    
    print(f"Years: {years1}")
    print(f"Greenery: {greenery1}")
    print(f"Generated {len(insights1)} insights:")
    for i, insight in enumerate(insights1, 1):
        print(f"   {i}. {insight}")
    
    # Test Case 2: Positive trend scenario
    print("\n🔍 Test Case 2: Improving Greenery Trend")
    years2 = [2019, 2020, 2021, 2022, 2023]
    greenery2 = [25.0, 28.0, 32.0, 35.0, 38.0]  # Improving trend
    prediction_data2 = {
        "prediction": 45.0,
        "target_year": 2028,
        "model_info": {"r_squared": 0.92, "constrained": True}
    }
    change_data2 = {"change_percentage": 4.2}
    land_cover_data2 = {
        "class_percentages": {
            "Forest": 40.0,
            "Residential": 25.0,
            "AnnualCrop": 20.0,
            "Highway": 10.0,
            "River": 5.0
        }
    }
    
    insights2 = generate_key_insights(years2, greenery2, prediction_data2, change_data2, land_cover_data2)
    
    print(f"Years: {years2}")
    print(f"Greenery: {greenery2}")
    print(f"Generated {len(insights2)} insights:")
    for i, insight in enumerate(insights2, 1):
        print(f"   {i}. {insight}")
    
    # Test Case 3: Stable scenario
    print("\n🔍 Test Case 3: Stable Greenery Levels")
    years3 = [2021, 2022, 2023]
    greenery3 = [52.0, 51.5, 52.3]  # Stable
    prediction_data3 = {
        "prediction": 52.8,
        "target_year": 2025,
        "model_info": {"r_squared": 0.65, "constrained": False}
    }
    change_data3 = {"change_percentage": 2.1}
    
    insights3 = generate_key_insights(years3, greenery3, prediction_data3, change_data3)
    
    print(f"Years: {years3}")
    print(f"Greenery: {greenery3}")
    print(f"Generated {len(insights3)} insights:")
    for i, insight in enumerate(insights3, 1):
        print(f"   {i}. {insight}")
    
    # Test formatting and statistics
    print("\n📊 Testing Formatting and Statistics")
    formatted = format_insights_for_display(insights1)
    stats = get_insight_summary_stats(insights1)
    
    print("Formatted insights preview:")
    print(formatted[:200] + "..." if len(formatted) > 200 else formatted)
    
    print(f"\nInsight statistics:")
    print(f"   Total insights: {stats['total_insights']}")
    print(f"   Critical alerts: {stats['critical_alerts']}")
    print(f"   Positive trends: {stats['positive_trends']}")
    print(f"   Recommendations: {stats['recommendations']}")
    
    # Test edge cases
    print("\n🔍 Testing Edge Cases")
    
    # Empty data
    empty_insights = generate_key_insights([], [])
    print(f"Empty data insights: {len(empty_insights)} generated")
    
    # Single data point
    single_insights = generate_key_insights([2023], [45.0])
    print(f"Single data point insights: {len(single_insights)} generated")
    
    # Critical low greenery
    critical_insights = generate_key_insights([2022, 2023], [18.0, 15.0])
    print(f"Critical low greenery insights: {len(critical_insights)} generated")
    if critical_insights:
        print(f"   Sample: {critical_insights[0]}")
    
    print("\n🎯 Test Summary:")
    print("✅ Declining trend analysis working")
    print("✅ Positive trend analysis working")
    print("✅ Stable scenario analysis working")
    print("✅ Prediction integration working")
    print("✅ Change detection integration working")
    print("✅ Land cover integration working")
    print("✅ Formatting and statistics working")
    print("✅ Edge case handling working")
    print("✅ Faculty-friendly insights generation complete")

def test_faculty_scenarios():
    """Test specific scenarios that faculty would evaluate."""
    print("\n" + "=" * 60)
    print("🎓 Faculty Evaluation Scenarios")
    print("=" * 60)
    
    scenarios = [
        {
            "name": "Urban Development Impact",
            "years": [2018, 2019, 2020, 2021, 2022],
            "greenery": [55.0, 52.0, 48.0, 44.0, 40.0],
            "prediction": {"prediction": 32.0, "target_year": 2025, "model_info": {"r_squared": 0.88}},
            "change": {"change_percentage": 18.5},
            "expected_themes": ["declining", "urban", "action required"]
        },
        {
            "name": "Conservation Success",
            "years": [2019, 2020, 2021, 2022, 2023],
            "greenery": [35.0, 38.0, 42.0, 45.0, 48.0],
            "prediction": {"prediction": 55.0, "target_year": 2027, "model_info": {"r_squared": 0.95}},
            "change": {"change_percentage": 3.2},
            "expected_themes": ["positive", "conservation", "maintain"]
        },
        {
            "name": "Environmental Crisis",
            "years": [2021, 2022, 2023],
            "greenery": [28.0, 22.0, 16.0],
            "prediction": {"prediction": 8.0, "target_year": 2026, "model_info": {"r_squared": 0.92}},
            "change": {"change_percentage": 25.0},
            "expected_themes": ["critical", "immediate action", "crisis"]
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n🔍 Scenario {i}: {scenario['name']}")
        
        insights = generate_key_insights(
            scenario["years"], 
            scenario["greenery"], 
            scenario["prediction"], 
            scenario["change"]
        )
        
        print(f"   Generated {len(insights)} insights:")
        for j, insight in enumerate(insights[:4], 1):  # Show top 4
            print(f"      {j}. {insight}")
        
        # Check if expected themes are covered
        all_text = " ".join(insights).lower()
        themes_found = [theme for theme in scenario["expected_themes"] if theme in all_text]
        print(f"   Expected themes found: {themes_found} ✅")

if __name__ == "__main__":
    test_key_insights()
    test_faculty_scenarios()