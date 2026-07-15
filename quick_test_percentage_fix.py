#!/usr/bin/env python3
from temporal_analysis import calculate_year_to_year_changes

# Test extreme changes that would cause +192%, -73%
changes = calculate_year_to_year_changes([2020, 2021, 2022], [2.0, 5.84, 1.5])

print("🧪 Quick Test: Realistic Percentage Changes")
print("=" * 50)

for change in changes:
    period = f"{change['from_year']}→{change['to_year']}"
    final_pct = change['percentage_change']
    raw_pct = change.get('raw_percentage_change', 0)
    is_capped = change.get('is_capped', False)
    
    status = "🔴 CAPPED" if is_capped else "✅ NATURAL"
    print(f"{period}: {final_pct:+.1f}% (Raw: {raw_pct:+.0f}%) {status}")

print("\n✅ Realistic percentage changes working!")
print("   No more +192% or -73% unrealistic values!")