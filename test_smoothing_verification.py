#!/usr/bin/env python3
"""
Test to verify the smoothing function works correctly with the example values.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from greenery import smooth_values

def test_smoothing_example():
    """Test smoothing with the exact example values from the issue."""
    
    # Your problematic values: 7% → 41% → 11% → 32%
    original_values = [7, 41, 11, 32]
    
    print("🧪 TESTING GREENERY SMOOTHING")
    print("=" * 50)
    
    print(f"Original values: {original_values}")
    print(f"Range: {max(original_values) - min(original_values):.1f}%")
    
    # Apply smoothing
    smoothed = smooth_values(original_values)
    
    print(f"Smoothed values: {[round(v, 1) for v in smoothed]}")
    print(f"Range: {max(smoothed) - min(smoothed):.1f}%")
    
    # Verify the smoothing logic
    expected_middle_1 = (7 + 41 + 11) / 3  # Should be ~19.7
    expected_middle_2 = (41 + 11 + 32) / 3  # Should be ~28.0
    
    print("\n📊 DETAILED VERIFICATION:")
    print(f"First value (unchanged): {smoothed[0]} (expected: 7)")
    print(f"Second value (smoothed): {smoothed[1]:.1f} (expected: {expected_middle_1:.1f})")
    print(f"Third value (smoothed): {smoothed[2]:.1f} (expected: {expected_middle_2:.1f})")
    print(f"Fourth value (unchanged): {smoothed[3]} (expected: 32)")
    
    # Check if smoothing improved stability
    original_range = max(original_values) - min(original_values)
    smoothed_range = max(smoothed) - min(smoothed)
    improvement = original_range - smoothed_range
    
    print(f"\n✅ IMPROVEMENT:")
    print(f"Stability improved by: {improvement:.1f}% (less variation)")
    print(f"Values are now more realistic: {'✅' if improvement > 0 else '❌'}")
    
    return smoothed

if __name__ == "__main__":
    test_smoothing_example()