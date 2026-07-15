#!/usr/bin/env python3
"""
Demo showing the realistic percentage change fix in action.
Shows how problematic +192% and -73% changes are fixed.
"""

from temporal_analysis import calculate_year_to_year_changes, calculate_realistic_percentage_change

def demo_percentage_fix():
    """Demonstrate the percentage change fix with real examples."""
    
    print("📉 REALISTIC PERCENTAGE CHANGE FIX DEMO")
    print("=" * 50)
    
    # Your problematic examples
    print("🔴 PROBLEMATIC EXAMPLES (BEFORE FIX):")
    print("-" * 40)
    
    # Example 1: +192% change
    old1, new1 = 2.0, 5.84
    raw_change1 = ((new1 - old1) / old1) * 100
    realistic1 = calculate_realistic_percentage_change(old1, new1)
    
    print(f"Case 1: {old1}% → {new1}%")
    print(f"  Raw calculation: {raw_change1:+.0f}% ❌ (unrealistic)")
    print(f"  Fixed calculation: {realistic1['final_change']:+.1f}% ✅ (realistic)")
    
    # Example 2: -73% change  
    old2, new2 = 15.0, 4.05
    raw_change2 = ((new2 - old2) / old2) * 100
    realistic2 = calculate_realistic_percentage_change(old2, new2)
    
    print(f"\nCase 2: {old2}% → {new2}%")
    print(f"  Raw calculation: {raw_change2:+.0f}% ❌ (unrealistic)")
    print(f"  Fixed calculation: {realistic2['final_change']:+.1f}% ✅ (realistic)")
    
    # Show the temporal analysis in action
    print(f"\n✅ TEMPORAL ANALYSIS WITH FIX:")
    print("-" * 40)
    
    # Test data that would cause extreme percentages
    years = [2020, 2021, 2022, 2023]
    values = [2.0, 5.84, 15.0, 4.05]  # Your problematic values
    
    changes = calculate_year_to_year_changes(years, values)
    
    for change in changes:
        from_year = change['from_year']
        to_year = change['to_year']
        from_val = change['from_value']
        to_val = change['to_value']
        raw_pct = change['raw_percentage_change']
        realistic_pct = change['percentage_change']
        is_capped = change['is_capped']
        
        print(f"{from_year}→{to_year}: {from_val:.1f}% → {to_val:.1f}%")
        print(f"  Raw: {raw_pct:+.0f}% | Realistic: {realistic_pct:+.1f}% {'🔴 (Capped)' if is_capped else '✅'}")
    
    # Show the methodology
    print(f"\n🔧 FIX METHODOLOGY:")
    print("-" * 40)
    print("1. Improved Formula:")
    print("   change = ((new - old) / max(old, 1)) * 100")
    print("   • Prevents division by tiny values")
    print("   • Uses minimum denominator of 1%")
    
    print("\n2. Realistic Capping:")
    print("   change = min(max(change, -50), 50)")
    print("   • Caps to environmental bounds ±50%")
    print("   • Stores both raw and capped values")
    
    print(f"\n📊 IMPACT:")
    print("-" * 40)
    capped_count = sum(1 for c in changes if c['is_capped'])
    total_count = len(changes)
    
    print(f"• Changes processed: {total_count}")
    print(f"• Changes capped: {capped_count}")
    print(f"• Capping rate: {(capped_count/total_count)*100:.0f}%")
    print(f"• Result: Realistic environmental interpretation ✅")
    
    print(f"\n🎓 FACULTY BENEFITS:")
    print("-" * 40)
    print("• No more mathematically correct but meaningless values")
    print("• Realistic environmental constraints applied")
    print("• Transparent methodology with raw values preserved")
    print("• Professional temporal analysis ready for presentation")

if __name__ == "__main__":
    demo_percentage_fix()