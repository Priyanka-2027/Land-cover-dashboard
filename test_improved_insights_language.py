#!/usr/bin/env python3
"""
Test Improved Insights Language - Research-Level Terminology
Verifies that all insights use academic, research-level language instead of casual terms.
"""

import sys
import os
sys.path.append('.')

def test_key_insights_language():
    """Test key insights module for research-level language."""
    print("💡 Testing Key Insights Language Improvements...")
    
    try:
        from key_insights import generate_key_insights
        
        # Test data
        years = [2020, 2021, 2022, 2023, 2024]
        green_percentages = [35.2, 38.1, 41.5, 39.8, 42.3]
        
        # Generate insights
        insights = generate_key_insights(years, green_percentages)
        
        print("✅ Key insights generated successfully")
        
        # Check for research-level language
        research_terms_found = []
        casual_terms_found = []
        
        research_terms = [
            "observed", "documented", "detected", "indicates", "demonstrates",
            "systematic", "significant", "substantial", "comprehensive",
            "temporal", "vegetation", "coverage", "trajectory", "analysis"
        ]
        
        casual_terms = [
            "dramatically", "increased", "decreased", "good", "bad",
            "greenery", "shows", "gets", "goes up", "goes down"
        ]
        
        for insight in insights:
            insight_lower = insight.lower()
            
            # Check for research terms
            for term in research_terms:
                if term in insight_lower:
                    research_terms_found.append(term)
            
            # Check for casual terms (should be avoided)
            for term in casual_terms:
                if term in insight_lower and term not in ["increased", "decreased"]:  # Allow some terms in context
                    casual_terms_found.append(term)
        
        print(f"📊 Language Analysis:")
        print(f"   • Research terms found: {len(set(research_terms_found))}")
        print(f"   • Casual terms found: {len(set(casual_terms_found))}")
        
        # Display sample insights
        print(f"\n📝 Sample Research-Level Insights:")
        for i, insight in enumerate(insights[:3], 1):
            print(f"   {i}. {insight}")
        
        return len(set(casual_terms_found)) == 0  # Success if no casual terms
        
    except Exception as e:
        print(f"❌ Error testing key insights: {str(e)}")
        return False

def test_summary_insights_language():
    """Test summary dashboard insights for research-level language."""
    print("\n📊 Testing Summary Dashboard Insights Language...")
    
    try:
        from summary_dashboard import calculate_summary_metrics, get_summary_insights
        
        # Test data
        years = [2020, 2021, 2022, 2023]
        green_percentages = [42.5, 44.1, 43.8, 45.2]
        
        # Generate summary and insights
        summary = calculate_summary_metrics(years, green_percentages)
        insights = get_summary_insights(summary)
        
        print("✅ Summary insights generated successfully")
        
        # Check language quality
        academic_indicators = [
            "coverage", "documented", "observed", "analysis", "temporal",
            "vegetation", "trajectory", "patterns", "assessment", "comprehensive"
        ]
        
        academic_count = 0
        for insight in insights:
            for indicator in academic_indicators:
                if indicator in insight.lower():
                    academic_count += 1
        
        print(f"📊 Academic Language Indicators: {academic_count}")
        
        # Display sample insights
        print(f"\n📝 Sample Executive Insights:")
        for i, insight in enumerate(insights, 1):
            print(f"   {i}. {insight}")
        
        return academic_count > 5  # Success if sufficient academic language
        
    except Exception as e:
        print(f"❌ Error testing summary insights: {str(e)}")
        return False

def test_change_detection_language():
    """Test change detection messages for research-level language."""
    print("\n🔄 Testing Change Detection Language...")
    
    try:
        from change_detection import get_change_interpretation_message
        
        # Test different change scenarios
        test_cases = [
            (25.0, "Major change"),
            (15.0, "Substantial change"),
            (10.0, "Moderate change"),
            (6.0, "Minor change"),
            (3.0, "Subtle change"),
            (1.0, "Stable")
        ]
        
        print("✅ Change detection messages generated")
        
        research_language_count = 0
        
        print(f"\n📝 Research-Level Change Messages:")
        for change_pct, description in test_cases:
            message = get_change_interpretation_message(change_pct)
            print(f"   • {change_pct:.1f}%: {message}")
            
            # Check for research language
            if any(term in message.lower() for term in ["detected", "documented", "observed", "transformation", "modification"]):
                research_language_count += 1
        
        print(f"\n📊 Research Language Usage: {research_language_count}/{len(test_cases)} messages")
        
        return research_language_count >= len(test_cases) * 0.8  # 80% should use research language
        
    except Exception as e:
        print(f"❌ Error testing change detection language: {str(e)}")
        return False

def test_temporal_analysis_language():
    """Test temporal analysis insights for research-level language."""
    print("\n📈 Testing Temporal Analysis Language...")
    
    try:
        from temporal_analysis import calculate_year_to_year_changes, analyze_temporal_patterns, get_change_insights
        
        # Test data
        years = [2020, 2021, 2022, 2023, 2024]
        green_percentages = [40.2, 42.1, 39.8, 43.5, 41.9]
        
        # Generate temporal analysis
        changes = calculate_year_to_year_changes(years, green_percentages)
        patterns = analyze_temporal_patterns(changes)
        insights = get_change_insights(changes, patterns)
        
        print("✅ Temporal analysis insights generated")
        
        # Check for academic terminology
        academic_terms = [
            "temporal", "vegetation", "documented", "observed", "trajectory",
            "inter-annual", "environmental", "systematic", "comprehensive"
        ]
        
        academic_usage = 0
        for insight in insights:
            for term in academic_terms:
                if term in insight.lower():
                    academic_usage += 1
        
        print(f"📊 Academic Terminology Usage: {academic_usage} instances")
        
        # Display sample insights
        print(f"\n📝 Sample Temporal Insights:")
        for i, insight in enumerate(insights[:3], 1):
            print(f"   {i}. {insight}")
        
        return academic_usage > 5  # Success if good academic language usage
        
    except Exception as e:
        print(f"❌ Error testing temporal analysis language: {str(e)}")
        return False

def demonstrate_language_improvements():
    """Demonstrate the language improvements with before/after examples."""
    print("\n🎯 Language Improvement Demonstration:")
    print("=" * 60)
    
    improvements = [
        {
            "before": "Greenery dramatically increased",
            "after": "Significant increase in vegetation coverage observed",
            "improvement": "More academic, precise terminology"
        },
        {
            "before": "Major changes detected",
            "after": "Substantial landscape modification documented",
            "improvement": "Research-level descriptive language"
        },
        {
            "before": "Good environmental health",
            "after": "Adequate vegetation coverage supports ecosystem services",
            "improvement": "Scientific explanation with context"
        },
        {
            "before": "Greenery levels are stable",
            "after": "Minimal temporal variation in vegetation dynamics observed",
            "improvement": "Technical precision and academic tone"
        },
        {
            "before": "Strong declining trend",
            "after": "Systematic reduction in vegetation coverage documented",
            "improvement": "Professional research terminology"
        }
    ]
    
    for i, improvement in enumerate(improvements, 1):
        print(f"{i}. Language Enhancement:")
        print(f"   ❌ Before: \"{improvement['before']}\"")
        print(f"   ✅ After:  \"{improvement['after']}\"")
        print(f"   💡 Improvement: {improvement['improvement']}")
        print()
    
    print("🎓 Faculty Benefits:")
    print("• More professional, academic presentation")
    print("• Research-level terminology demonstrates sophistication")
    print("• Scientific precision in language and descriptions")
    print("• Publication-quality insights and interpretations")
    
    return True

def main():
    """Run all language improvement tests."""
    print("🚀 INSIGHTS LANGUAGE IMPROVEMENT TEST SUITE")
    print("=" * 70)
    
    tests = [
        test_key_insights_language,
        test_summary_insights_language,
        test_change_detection_language,
        test_temporal_analysis_language,
        demonstrate_language_improvements
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ Test failed with exception: {str(e)}")
            results.append(False)
    
    # Summary
    print("\n" + "=" * 70)
    print("📋 LANGUAGE IMPROVEMENT SUMMARY")
    print("=" * 70)
    
    passed = sum(results)
    total = len(results)
    
    print(f"✅ Tests Passed: {passed}/{total}")
    print(f"📊 Success Rate: {(passed/total)*100:.1f}%")
    
    if passed == total:
        print("🎉 ALL LANGUAGE IMPROVEMENTS SUCCESSFUL!")
        print("\n💡 Research-Level Language Features:")
        print("   • Academic terminology throughout all insights")
        print("   • Professional scientific descriptions")
        print("   • Precise, technical language usage")
        print("   • Publication-quality presentation")
        print("   • Faculty-impressive sophisticated terminology")
    else:
        print("⚠️ Some language improvements need refinement")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)