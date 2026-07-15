#!/usr/bin/env python3
"""
Test the critical executive summary fix.
Verifies that 0.0% values are NEVER shown - this kills impression instantly.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from summary_dashboard import calculate_summary_metrics, format_summary_for_display

def test_no_data_fallback():
    """Test that empty data never shows 0.0% values."""
    
    print("🚨 CRITICAL FIX: Executive Summary 0.0% Problem")
    print("=" * 60)
    
    print("❌ PROBLEM: Showing 0.0% values kills impression instantly")
    print("✅ SOLUTION: Proper fallback logic with 'No Data' display")
    
    # Test Case 1: Completely empty data
    print(f"\n🧪 Test 1: Empty Data")
    print("-" * 30)
    
    empty_years = []
    empty_values = []
    
    summary = calculate_summary_metrics(empty_years, empty_values)
    formatted = format_summary_for_display(summary)
    
    print(f"Input: years={empty_years}, values={empty_values}")
    print(f"Avg Green: {formatted['avg_green_display']}")
    print(f"Total Change: {formatted['total_change_display']}")
    print(f"Prediction: {formatted['prediction_display']}")
    
    # Verify no 0.0% values
    has_zero_percent = any("0.0%" in value for value in formatted.values())
    print(f"❌ Contains 0.0%: {has_zero_percent}")
    print(f"✅ Shows 'No Data': {'No Data' in formatted['avg_green_display']}")
    
    # Test Case 2: None values
    print(f"\n🧪 Test 2: None Values")
    print("-" * 30)
    
    none_years = [2020, 2021]
    none_values = [None, None]
    
    summary2 = calculate_summary_metrics(none_years, none_values)
    formatted2 = format_summary_for_display(summary2)
    
    print(f"Input: years={none_years}, values={none_values}")
    print(f"Avg Green: {formatted2['avg_green_display']}")
    print(f"Total Change: {formatted2['total_change_display']}")
    print(f"Prediction: {formatted2['prediction_display']}")
    
    has_zero_percent2 = any("0.0%" in value for value in formatted2.values())
    print(f"❌ Contains 0.0%: {has_zero_percent2}")
    print(f"✅ Shows 'No Data': {'No Data' in formatted2['avg_green_display']}")
    
    # Test Case 3: Zero values (should also be treated as no data)
    print(f"\n🧪 Test 3: Zero Values")
    print("-" * 30)
    
    zero_years = [2020, 2021]
    zero_values = [0.0, 0.0]
    
    summary3 = calculate_summary_metrics(zero_years, zero_values)
    formatted3 = format_summary_for_display(summary3)
    
    print(f"Input: years={zero_years}, values={zero_values}")
    print(f"Avg Green: {formatted3['avg_green_display']}")
    print(f"Total Change: {formatted3['total_change_display']}")
    print(f"Prediction: {formatted3['prediction_display']}")
    
    has_zero_percent3 = any("0.0%" in value for value in formatted3.values())
    print(f"❌ Contains 0.0%: {has_zero_percent3}")
    print(f"✅ Shows 'No Data': {'No Data' in formatted3['avg_green_display']}")
    
    # Test Case 4: Valid data (should show real percentages)
    print(f"\n🧪 Test 4: Valid Data")
    print("-" * 30)
    
    valid_years = [2020, 2021, 2022]
    valid_values = [35.2, 38.7, 42.1]
    
    summary4 = calculate_summary_metrics(valid_years, valid_values)
    formatted4 = format_summary_for_display(summary4)
    
    print(f"Input: years={valid_years}, values={valid_values}")
    print(f"Avg Green: {formatted4['avg_green_display']}")
    print(f"Total Change: {formatted4['total_change_display']}")
    print(f"Prediction: {formatted4['prediction_display']}")
    
    has_real_data = "%" in formatted4['avg_green_display'] and "No Data" not in formatted4['avg_green_display']
    print(f"✅ Shows real percentages: {has_real_data}")
    
    return not (has_zero_percent or has_zero_percent2 or has_zero_percent3) and has_real_data

def test_faculty_impression():
    """Test the faculty impression scenarios."""
    
    print(f"\n🎓 FACULTY IMPRESSION TEST:")
    print("-" * 40)
    
    # Scenario: Faculty opens dashboard with no data
    print("Scenario: Faculty opens dashboard before uploading images")
    
    summary = calculate_summary_metrics([], [])
    formatted = format_summary_for_display(summary)
    
    print(f"\nWhat faculty sees:")
    print(f"📊 Avg Green Coverage: {formatted['avg_green_display']}")
    print(f"📈 Total Change: {formatted['total_change_display']}")
    print(f"🔮 Prediction (2035): {formatted['prediction_display']}")
    print(f"🎯 Analysis Period: {formatted['period_display']}")
    
    # Check impression
    if "0.0%" in str(formatted.values()):
        print(f"\n❌ IMPRESSION: KILLED - Shows unprofessional 0.0% values")
        return False
    else:
        print(f"\n✅ IMPRESSION: PROFESSIONAL - Shows 'No Data' instead of 0.0%")
        return True

def show_before_after():
    """Show the before/after comparison."""
    
    print(f"\n📊 BEFORE/AFTER COMPARISON:")
    print("-" * 40)
    
    print("❌ BEFORE (Kills Impression):")
    print("   📊 Avg Green Coverage: 0.0%")
    print("   📈 Total Change: 0.0%")
    print("   🔮 Prediction (2035): 0.0%")
    print("   🎯 Analysis Period: N/A")
    
    print("\n✅ AFTER (Professional):")
    print("   📊 Avg Green Coverage: No Data")
    print("   📈 Total Change: No Data")
    print("   🔮 Prediction (2035): No Data")
    print("   🎯 Analysis Period: No Data")
    print("   💡 Status: Please upload images to begin analysis")

if __name__ == "__main__":
    success = test_no_data_fallback()
    faculty_success = test_faculty_impression()
    show_before_after()
    
    print(f"\n🏆 CRITICAL FIX STATUS:")
    print(f"✅ No 0.0% values: {success}")
    print(f"✅ Faculty impression: {faculty_success}")
    print(f"✅ Professional fallback: 'No Data' display implemented")
    
    if success and faculty_success:
        print(f"\n🎉 SUCCESS: Executive summary will never kill impression!")
    else:
        print(f"\n❌ FAILURE: Still showing 0.0% values - needs more work")