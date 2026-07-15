#!/usr/bin/env python3
"""
Debug the 0.0% issue in specific scenarios.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from summary_dashboard import calculate_summary_metrics, format_summary_for_display

def debug_scenario(name, years, values):
    """Debug a specific scenario to see where 0.0% comes from."""
    
    print(f"\n🔍 DEBUGGING: {name}")
    print("-" * 40)
    print(f"Input: years={years}, values={values}")
    
    # Step 1: Calculate summary
    summary = calculate_summary_metrics(years, values)
    print(f"\nSummary metrics:")
    for key, value in summary.items():
        print(f"  {key}: {value}")
    
    # Step 2: Format for display
    formatted = format_summary_for_display(summary)
    print(f"\nFormatted display:")
    for key, value in formatted.items():
        print(f"  {key}: {value}")
    
    # Step 3: Check for 0.0%
    has_zero_percent = any("0.0%" in str(value) for value in formatted.values())
    print(f"\n❌ Contains 0.0%: {has_zero_percent}")
    
    if has_zero_percent:
        print("🚨 FOUND 0.0% VALUES:")
        for key, value in formatted.items():
            if "0.0%" in str(value):
                print(f"   {key}: {value}")
    
    return has_zero_percent

if __name__ == "__main__":
    print("🔍 DEBUGGING 0.0% ISSUE")
    print("=" * 50)
    
    # Test the problematic scenarios
    scenarios = [
        ("Single image", [2023], [42.5]),
        ("Two images", [2022, 2023], [38.2, 41.7]),
        ("Zero values", [2020, 2021], [0.0, 0.0]),
    ]
    
    for name, years, values in scenarios:
        has_issue = debug_scenario(name, years, values)
        if has_issue:
            print(f"\n🚨 ISSUE FOUND IN: {name}")
        else:
            print(f"\n✅ NO ISSUE IN: {name}")