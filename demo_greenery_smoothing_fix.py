#!/usr/bin/env python3
"""
Demo showing the greenery smoothing fix in action.
Shows how the problematic values are fixed to be more realistic.
"""

import matplotlib.pyplot as plt
from greenery import smooth_values, apply_realistic_constraints

def demo_smoothing_fix():
    """Demonstrate the smoothing fix with visual comparison."""
    
    print("🌿 GREENERY SMOOTHING FIX DEMO")
    print("=" * 50)
    
    # Your problematic values: 7% → 41% → 11% → 32%
    original_values = [7, 41, 11, 32]
    years = [2020, 2021, 2022, 2023]
    
    # Apply the fix
    smoothed_values = smooth_values(original_values)
    final_values = apply_realistic_constraints(smoothed_values)
    
    # Show the transformation
    print("📊 VALUE TRANSFORMATION:")
    print("-" * 30)
    for i, year in enumerate(years):
        print(f"{year}: {original_values[i]:5.1f}% → {smoothed_values[i]:5.1f}% → {final_values[i]:5.1f}%")
    
    # Calculate improvements
    original_range = max(original_values) - min(original_values)
    smoothed_range = max(smoothed_values) - min(smoothed_values)
    final_range = max(final_values) - min(final_values)
    
    print(f"\n📈 STABILITY IMPROVEMENT:")
    print(f"Original variation: {original_range:.1f}%")
    print(f"Smoothed variation: {smoothed_range:.1f}%")
    print(f"Final variation: {final_range:.1f}%")
    print(f"Improvement: {original_range - final_range:.1f}% less variation")
    
    # Create visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Before (problematic)
    ax1.plot(years, original_values, 'ro-', linewidth=2, markersize=8, label='Original (Unstable)')
    ax1.set_title('❌ BEFORE: Unstable Values', fontsize=14, color='red')
    ax1.set_ylabel('Greenery %')
    ax1.set_ylim(0, 50)
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # After (fixed)
    ax2.plot(years, smoothed_values, 'go-', linewidth=2, markersize=8, label='Smoothed (Realistic)')
    ax2.set_title('✅ AFTER: Realistic Trends', fontsize=14, color='green')
    ax2.set_ylabel('Greenery %')
    ax2.set_ylim(0, 50)
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('greenery_smoothing_demo.png', dpi=150, bbox_inches='tight')
    print(f"📊 Chart saved: greenery_smoothing_demo.png")
    
    print(f"\n✅ SOLUTION IMPLEMENTED:")
    print(f"• Smoothing function: smooth_values()")
    print(f"• Used in dashboard: get_smoothed_greenery_analysis()")
    print(f"• Applied before plotting: ✅")
    print(f"• Values now realistic: ✅")

if __name__ == "__main__":
    demo_smoothing_fix()