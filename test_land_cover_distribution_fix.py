#!/usr/bin/env python3
"""
Test script for Land Cover Distribution - Core DWDM Requirement
Verifies that land cover pie charts and analysis work properly after model fix.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import cv2
import numpy as np
import joblib
import matplotlib.pyplot as plt
from classification import CLASSES
from sliding_window import classify_large_image, calculate_land_cover_percentages, visualize_results
from land_cover_analysis import (create_land_cover_pie_chart, create_land_cover_bar_chart, 
                                analyze_land_cover_diversity, get_land_cover_insights)

def test_model_loading_for_land_cover():
    """Test that model loads properly for land cover analysis."""
    print("🧪 Testing Land Cover Distribution - Core DWDM Requirement")
    print("=" * 60)
    
    print("\n1. Testing Model Loading for Land Cover Analysis:")
    
    # Test model loading (same logic as dashboard)
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
        print(f"   ✅ Model loaded successfully from: {working_path}")
        print(f"   Model type: {type(model).__name__}")
        print(f"   Classes available: {len(CLASSES)}")
        return model
    else:
        print(f"   ❌ Model loading failed - land cover analysis unavailable")
        return None

def test_land_cover_classification(model):
    """Test land cover classification with synthetic image."""
    print("\n2. Testing Land Cover Classification:")
    
    if model is None:
        print("   ❌ No model available - skipping classification test")
        return None
    
    # Create synthetic test image with different land cover types
    test_image = create_synthetic_land_cover_image()
    
    print(f"   Test image size: {test_image.shape}")
    
    # Perform sliding window classification
    try:
        predictions = classify_large_image(test_image, model)
        print(f"   ✅ Classification successful: {len(predictions)} patches analyzed")
        
        if predictions:
            # Calculate land cover percentages
            percentages = calculate_land_cover_percentages(predictions, CLASSES)
            print(f"   ✅ Land cover percentages calculated: {len(percentages)} classes found")
            
            # Show top 3 classes
            sorted_classes = sorted(percentages.items(), key=lambda x: x[1], reverse=True)
            print(f"   Top 3 land cover types:")
            for i, (class_name, pct) in enumerate(sorted_classes[:3], 1):
                print(f"      {i}. {class_name}: {pct:.1f}%")
            
            return percentages
        else:
            print(f"   ⚠️ No predictions generated")
            return None
            
    except Exception as e:
        print(f"   ❌ Classification failed: {str(e)}")
        return None

def test_pie_chart_creation(percentages):
    """Test pie chart creation - core DWDM requirement."""
    print("\n3. Testing Pie Chart Creation (Core DWDM Requirement):")
    
    if percentages is None:
        print("   ❌ No percentage data - creating demo pie chart")
        # Create demo data as requested
        demo_percentages = {
            "Forest": 30.0,
            "Urban": 50.0, 
            "Water": 20.0
        }
        percentages = demo_percentages
        print(f"   📊 Using demo data: {demo_percentages}")
    
    try:
        # Create pie chart
        fig = create_land_cover_pie_chart(percentages, "Land Cover Distribution - DWDM Analysis")
        
        print(f"   ✅ Pie chart created successfully")
        print(f"   Chart title: Land Cover Distribution - DWDM Analysis")
        print(f"   Classes shown: {list(percentages.keys())}")
        print(f"   Percentages: {[f'{v:.1f}%' for v in percentages.values()]}")
        
        # Save chart for verification
        fig.savefig("test_land_cover_pie.png", dpi=150, bbox_inches='tight')
        print(f"   💾 Pie chart saved as: test_land_cover_pie.png")
        
        plt.close(fig)  # Clean up
        return True
        
    except Exception as e:
        print(f"   ❌ Pie chart creation failed: {str(e)}")
        return False

def test_bar_chart_creation(percentages):
    """Test bar chart creation for detailed analysis."""
    print("\n4. Testing Bar Chart Creation:")
    
    if percentages is None:
        percentages = {"Forest": 30.0, "Urban": 50.0, "Water": 20.0}
    
    try:
        # Create bar chart
        fig = create_land_cover_bar_chart(percentages, "Detailed Land Cover Analysis")
        
        print(f"   ✅ Bar chart created successfully")
        print(f"   Shows all {len(percentages)} land cover classes")
        
        # Save chart
        fig.savefig("test_land_cover_bar.png", dpi=150, bbox_inches='tight')
        print(f"   💾 Bar chart saved as: test_land_cover_bar.png")
        
        plt.close(fig)
        return True
        
    except Exception as e:
        print(f"   ❌ Bar chart creation failed: {str(e)}")
        return False

def test_diversity_analysis(percentages):
    """Test diversity metrics calculation."""
    print("\n5. Testing Diversity Analysis (DWDM Metrics):")
    
    if percentages is None:
        percentages = {"Forest": 30.0, "Urban": 50.0, "Water": 20.0}
    
    try:
        # Calculate diversity metrics
        diversity = analyze_land_cover_diversity(percentages)
        
        print(f"   ✅ Diversity analysis completed")
        print(f"   Shannon Diversity: {diversity['shannon_diversity']}")
        print(f"   Simpson Diversity: {diversity['simpson_diversity']}")
        print(f"   Species Richness: {diversity['richness']}")
        print(f"   Evenness: {diversity['evenness']}")
        
        return diversity
        
    except Exception as e:
        print(f"   ❌ Diversity analysis failed: {str(e)}")
        return None

def test_insights_generation(percentages):
    """Test intelligent insights generation."""
    print("\n6. Testing Insights Generation:")
    
    if percentages is None:
        percentages = {"Forest": 30.0, "Urban": 50.0, "Water": 20.0}
    
    try:
        # Generate insights
        insights = get_land_cover_insights(percentages)
        
        print(f"   ✅ Insights generated successfully")
        print(f"   Primary: {insights['primary']}")
        print(f"   Secondary: {insights['secondary']}")
        print(f"   Analysis: {insights['analysis']}")
        
        return insights
        
    except Exception as e:
        print(f"   ❌ Insights generation failed: {str(e)}")
        return None

def create_synthetic_land_cover_image():
    """Create synthetic image with different land cover patterns for testing."""
    # Create 200x200 test image
    img = np.zeros((200, 200, 3), dtype=np.uint8)
    
    # Add different land cover patterns
    # Forest (green areas)
    img[0:100, 0:100] = [34, 139, 34]  # Forest green
    
    # Urban (gray areas)
    img[0:100, 100:200] = [128, 128, 128]  # Urban gray
    
    # Water (blue areas)
    img[100:200, 0:100] = [65, 105, 225]  # Water blue
    
    # Agricultural (brown areas)
    img[100:200, 100:200] = [139, 69, 19]  # Agricultural brown
    
    return img

def test_dashboard_integration():
    """Test integration with dashboard functionality."""
    print("\n7. Testing Dashboard Integration:")
    
    try:
        # Test the same imports used in dashboard
        from dashboard.app import load_model
        
        # Test model loading function
        model = load_model()
        
        if model is not None:
            print(f"   ✅ Dashboard model loading works")
            print(f"   Model ready for land cover analysis")
            return True
        else:
            print(f"   ⚠️ Dashboard model loading returns None")
            print(f"   May need interactive training")
            return False
            
    except Exception as e:
        print(f"   ❌ Dashboard integration test failed: {str(e)}")
        return False

def main():
    """Run comprehensive land cover distribution tests."""
    print("🌿 LAND COVER DISTRIBUTION - CORE DWDM REQUIREMENT FIX")
    print("=" * 70)
    
    # Test 1: Model loading
    model = test_model_loading_for_land_cover()
    
    # Test 2: Classification
    percentages = test_land_cover_classification(model)
    
    # Test 3: Pie chart (core DWDM requirement)
    pie_success = test_pie_chart_creation(percentages)
    
    # Test 4: Bar chart
    bar_success = test_bar_chart_creation(percentages)
    
    # Test 5: Diversity analysis
    diversity = test_diversity_analysis(percentages)
    
    # Test 6: Insights
    insights = test_insights_generation(percentages)
    
    # Test 7: Dashboard integration
    dashboard_ready = test_dashboard_integration()
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 LAND COVER DISTRIBUTION TEST SUMMARY")
    print("=" * 70)
    
    # Check core requirements
    model_available = model is not None
    classification_works = percentages is not None
    pie_chart_works = pie_success
    dwdm_ready = model_available and classification_works and pie_chart_works
    
    print(f"🤖 Model Loading:        {'✅ SUCCESS' if model_available else '❌ FAILED'}")
    print(f"🔍 Classification:       {'✅ SUCCESS' if classification_works else '❌ FAILED'}")
    print(f"🥧 Pie Chart (DWDM):     {'✅ SUCCESS' if pie_chart_works else '❌ FAILED'}")
    print(f"📊 Bar Chart:           {'✅ SUCCESS' if bar_success else '❌ FAILED'}")
    print(f"📈 Diversity Analysis:   {'✅ SUCCESS' if diversity else '❌ FAILED'}")
    print(f"🧠 Insights Generation:  {'✅ SUCCESS' if insights else '❌ FAILED'}")
    print(f"🖥️ Dashboard Ready:      {'✅ SUCCESS' if dashboard_ready else '❌ FAILED'}")
    
    print(f"\n🎓 DWDM REQUIREMENT STATUS:")
    if dwdm_ready:
        print(f"   ✅ Core DWDM requirement SATISFIED")
        print(f"   ✅ Land cover pie charts working")
        print(f"   ✅ Forest/Urban/Water percentages displayed")
        print(f"   ✅ Faculty will see proper data mining results")
    else:
        print(f"   ❌ Core DWDM requirement NOT MET")
        if not model_available:
            print(f"   ❌ Model loading issue - use interactive training")
        if not classification_works:
            print(f"   ❌ Classification pipeline broken")
        if not pie_chart_works:
            print(f"   ❌ Pie chart generation failed")
    
    print(f"\n🏆 FACULTY DEMO IMPACT:")
    if dwdm_ready:
        print(f"   🌟 Shows clear data mining focus")
        print(f"   🌟 Professional land cover analysis")
        print(f"   🌟 Pie charts demonstrate classification results")
        print(f"   🌟 DWDM project requirements fulfilled")
    else:
        print(f"   ⚠️ Missing core DWDM demonstration")
        print(f"   ⚠️ Faculty may question data mining focus")
    
    return dwdm_ready

if __name__ == "__main__":
    success = main()
    print(f"\n{'🎯 LAND COVER DISTRIBUTION READY FOR DWDM EVALUATION! 🎓' if success else '⚠️ NEEDS ATTENTION BEFORE DEMO'}")
    exit(0 if success else 1)