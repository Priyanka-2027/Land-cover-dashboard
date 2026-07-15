#!/usr/bin/env python3
"""
Complete Demo Readiness Test
Simulates the full user experience to ensure demo is faculty-ready.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import cv2
import numpy as np
import joblib
from classification import CLASSES

def test_complete_workflow():
    """Test the complete landcover analysis workflow."""
    print("🎯 COMPLETE DEMO READINESS TEST")
    print("=" * 60)
    
    # Test 1: Model Loading (Critical Bug Fix)
    print("\n1. 🤖 Testing Model Loading (Critical Bug Fix)")
    print("-" * 40)
    
    try:
        # Test the same loading logic as dashboard
        possible_paths = [
            'models/model.pkl',
            '../models/model.pkl',
            os.path.join('..', 'models', 'model.pkl'),
            os.path.join(os.path.dirname(__file__), 'models', 'model.pkl')
        ]
        
        model = None
        working_path = None
        
        for model_path in possible_paths:
            if os.path.exists(model_path):
                try:
                    model = joblib.load(model_path)
                    working_path = model_path
                    break
                except Exception as e:
                    continue
        
        if model is not None:
            print(f"✅ Model Loading: SUCCESS")
            print(f"   Path: {working_path}")
            print(f"   Type: {type(model).__name__}")
            print(f"   Classes: {len(model.classes_) if hasattr(model, 'classes_') else 'Unknown'}")
            model_ready = True
        else:
            print(f"❌ Model Loading: FAILED")
            print(f"   No model found in any expected location")
            model_ready = False
            
    except Exception as e:
        print(f"❌ Model Loading: ERROR - {str(e)}")
        model_ready = False
    
    # Test 2: Core Analysis Functions
    print("\n2. 🌿 Testing Core Analysis Functions")
    print("-" * 40)
    
    try:
        from greenery import calculate_green_percentage, get_vegetation_analysis
        
        # Create test image
        test_img = np.zeros((100, 100, 3), dtype=np.uint8)
        test_img[20:80, 20:80] = [34, 139, 34]  # Green square
        
        # Test HSV-based greenery detection
        green_pct, mask = calculate_green_percentage(test_img, method="hsv")
        print(f"✅ Greenery Detection: {green_pct:.1f}% (HSV method)")
        
        # Test vegetation analysis
        veg_analysis = get_vegetation_analysis(test_img)
        if veg_analysis:
            print(f"✅ Vegetation Analysis: {veg_analysis['hsv']['percentage']:.1f}%")
        
        greenery_ready = True
        
    except Exception as e:
        print(f"❌ Greenery Analysis: ERROR - {str(e)}")
        greenery_ready = False
    
    # Test 3: Prediction System
    print("\n3. 🔮 Testing Prediction System")
    print("-" * 40)
    
    try:
        from prediction import predict_future, generate_prediction_plot
        
        # Test data
        years = [2020, 2021, 2022, 2023]
        green_percentages = [45.2, 47.8, 44.1, 46.5]
        target_year = 2025
        
        # Test prediction
        prediction, slope, model_info = predict_future(years, green_percentages, target_year)
        print(f"✅ Prediction: {prediction:.1f}% for {target_year}")
        print(f"✅ Model Info: {model_info.get('equation', 'Available')}")
        
        prediction_ready = True
        
    except Exception as e:
        print(f"❌ Prediction System: ERROR - {str(e)}")
        prediction_ready = False
    
    # Test 4: Change Detection
    print("\n4. 🔄 Testing Change Detection")
    print("-" * 40)
    
    try:
        from change_detection import detect_change, create_change_comparison
        
        # Create test images
        img1 = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        img2 = img1.copy()
        img2[40:60, 40:60] = [255, 0, 0]  # Add red change area
        
        # Test change detection
        thresh, change_pct = detect_change(img1, img2, threshold=50)
        print(f"✅ Change Detection: {change_pct:.1f}% area changed")
        
        # Test comparison visualization
        comparison = create_change_comparison(img1, img2, thresh)
        print(f"✅ Change Visualization: {comparison.shape} comparison image")
        
        change_ready = True
        
    except Exception as e:
        print(f"❌ Change Detection: ERROR - {str(e)}")
        change_ready = False
    
    # Test 5: Temporal Analysis
    print("\n5. 📊 Testing Temporal Analysis")
    print("-" * 40)
    
    try:
        from temporal_analysis import calculate_year_to_year_changes, analyze_temporal_patterns
        
        years = [2020, 2021, 2022, 2023]
        values = [45.2, 47.8, 44.1, 46.5]
        
        # Test year-to-year changes
        changes = calculate_year_to_year_changes(years, values)
        print(f"✅ Year-to-Year Changes: {len(changes)} periods analyzed")
        
        # Test pattern analysis
        patterns = analyze_temporal_patterns(changes)
        print(f"✅ Pattern Analysis: {patterns.get('overall_trend', 'Available')}")
        
        temporal_ready = True
        
    except Exception as e:
        print(f"❌ Temporal Analysis: ERROR - {str(e)}")
        temporal_ready = False
    
    # Test 6: Key Insights
    print("\n6. 🧠 Testing Key Insights Generation")
    print("-" * 40)
    
    try:
        from key_insights import generate_key_insights, get_insight_summary_stats
        
        years = [2020, 2021, 2022, 2023]
        green_percentages = [45.2, 47.8, 44.1, 46.5]
        prediction_data = {"prediction": 48.0, "target_year": 2025}
        
        # Test insights generation
        insights = generate_key_insights(years, green_percentages, prediction_data)
        print(f"✅ Key Insights: {len(insights)} insights generated")
        
        # Test summary stats
        stats = get_insight_summary_stats(insights)
        print(f"✅ Insight Stats: {stats['total_insights']} total, {stats['critical_alerts']} alerts")
        
        insights_ready = True
        
    except Exception as e:
        print(f"❌ Key Insights: ERROR - {str(e)}")
        insights_ready = False
    
    # Test 7: Report Generation
    print("\n7. 📄 Testing Report Generation")
    print("-" * 40)
    
    try:
        from report_generator import generate_comprehensive_report
        
        years = [2020, 2021, 2022, 2023]
        green_percentages = [45.2, 47.8, 44.1, 46.5]
        prediction_data = {"prediction": 48.0, "target_year": 2025}
        
        # Test report generation
        report = generate_comprehensive_report(
            years=years,
            green_percentages=green_percentages,
            prediction_data=prediction_data
        )
        
        print(f"✅ Report Generation: {len(report):,} characters")
        print(f"✅ Sections: {report.count('##')} main sections")
        
        # Check for limitations section
        if "Research Limitations" in report:
            print(f"✅ Limitations Section: Included (academic credibility)")
        
        report_ready = True
        
    except Exception as e:
        print(f"❌ Report Generation: ERROR - {str(e)}")
        report_ready = False
    
    # Test 8: Validation System
    print("\n8. 🔬 Testing Validation System")
    print("-" * 40)
    
    try:
        from validation_system import assess_prediction_confidence
        
        years = [2020, 2021, 2022, 2023]
        values = [45.2, 47.8, 44.1, 46.5]
        model_info = {"r_squared": 0.742, "equation": "y = 0.5x + 45"}
        
        # Test validation assessment
        validation = assess_prediction_confidence(years, values, model_info)
        print(f"✅ Validation: {validation['overall_confidence']}")
        print(f"✅ Score: {validation['validation_score']}/16")
        
        validation_ready = True
        
    except Exception as e:
        print(f"❌ Validation System: ERROR - {str(e)}")
        validation_ready = False
    
    # Summary Report
    print("\n" + "=" * 60)
    print("📊 DEMO READINESS SUMMARY")
    print("=" * 60)
    
    components = [
        ("🤖 Model Loading", model_ready),
        ("🌿 Greenery Analysis", greenery_ready),
        ("🔮 Prediction System", prediction_ready),
        ("🔄 Change Detection", change_ready),
        ("📊 Temporal Analysis", temporal_ready),
        ("🧠 Key Insights", insights_ready),
        ("📄 Report Generation", report_ready),
        ("🔬 Validation System", validation_ready)
    ]
    
    ready_count = sum(1 for _, ready in components if ready)
    total_count = len(components)
    
    for name, ready in components:
        status = "✅ READY" if ready else "❌ ISSUE"
        print(f"{name:<25} {status}")
    
    print(f"\n📈 Overall Readiness: {ready_count}/{total_count} ({ready_count/total_count*100:.0f}%)")
    
    if ready_count == total_count:
        print(f"\n🎉 DEMO STATUS: ✅ FULLY READY FOR FACULTY EVALUATION")
        print(f"   All systems operational - demo will run flawlessly!")
    elif ready_count >= total_count * 0.8:
        print(f"\n⚠️ DEMO STATUS: 🟡 MOSTLY READY (minor issues)")
        print(f"   Core functionality working - demo should succeed")
    else:
        print(f"\n🚨 DEMO STATUS: ❌ NOT READY (major issues)")
        print(f"   Critical components failing - needs attention")
    
    # Faculty Impression Factors
    print(f"\n🎓 FACULTY IMPRESSION FACTORS:")
    
    impressive_features = [
        ("Interactive Model Training", model_ready),
        ("HSV-based Vegetation Detection", greenery_ready),
        ("Mathematical Model Justification", prediction_ready),
        ("Year-to-Year Change Analysis", temporal_ready),
        ("Intelligent Key Insights", insights_ready),
        ("Comprehensive Report Generation", report_ready),
        ("Multi-dimensional Validation", validation_ready),
        ("Research Limitations Section", report_ready)
    ]
    
    for feature, ready in impressive_features:
        icon = "🌟" if ready else "⭕"
        print(f"   {icon} {feature}")
    
    impressive_count = sum(1 for _, ready in impressive_features if ready)
    print(f"\n🏆 Faculty Impact Score: {impressive_count}/{len(impressive_features)} impressive features")
    
    return ready_count == total_count

if __name__ == "__main__":
    success = test_complete_workflow()
    print(f"\n{'🎯 DEMO READY FOR FACULTY! 🎓' if success else '⚠️ NEEDS ATTENTION BEFORE DEMO'}")
    exit(0 if success else 1)