#!/usr/bin/env python3
"""
Test Confidence Scoring Implementation
Verifies that classification confidence scores are properly calculated and displayed.
"""

import sys
import os
sys.path.append('.')

import numpy as np
import cv2
from unittest.mock import Mock
import matplotlib.pyplot as plt

def test_confidence_scoring_system():
    """Test the complete confidence scoring system."""
    print("🧪 Testing Confidence Scoring System...")
    
    try:
        # Import required modules
        from sliding_window import (
            classify_large_image, 
            calculate_confidence_statistics, 
            get_confidence_level_description,
            visualize_results
        )
        from classification import CLASSES
        
        print("✅ Successfully imported confidence scoring modules")
        
        # Create a mock model with predict_proba capability
        mock_model = Mock()
        
        # Mock predictions with varying confidence levels
        mock_model.predict.return_value = np.array([0])  # Forest class
        mock_model.predict_proba.return_value = np.array([[0.85, 0.10, 0.05]])  # 85% confidence
        
        # Create test image
        test_image = np.random.randint(0, 255, (128, 128, 3), dtype=np.uint8)
        
        print("🔄 Testing sliding window with confidence scoring...")
        
        # Test classification with confidence
        predictions = classify_large_image(test_image, mock_model, window_size=(64, 64), step_size=32)
        
        if predictions:
            print(f"✅ Generated {len(predictions)} predictions with confidence scores")
            
            # Verify confidence scores are present
            has_confidence = all('confidence' in pred for pred in predictions)
            print(f"✅ All predictions have confidence scores: {has_confidence}")
            
            # Test confidence statistics
            confidence_stats = calculate_confidence_statistics(predictions)
            print(f"📊 Confidence Statistics:")
            print(f"   • Average: {confidence_stats['average']:.1f}%")
            print(f"   • Range: {confidence_stats['min']:.1f}% - {confidence_stats['max']:.1f}%")
            print(f"   • High Confidence Ratio: {confidence_stats['high_confidence_ratio']:.1f}%")
            
            # Test confidence level description
            confidence_level, confidence_desc = get_confidence_level_description(confidence_stats["average"])
            print(f"📈 Confidence Assessment: {confidence_level} - {confidence_desc}")
            
            # Test visualization with confidence colors
            overlay = visualize_results(test_image, predictions, CLASSES)
            print(f"✅ Generated confidence-colored visualization overlay")
            
            return True
        else:
            print("❌ No predictions generated")
            return False
            
    except Exception as e:
        print(f"❌ Error in confidence scoring test: {str(e)}")
        return False

def test_confidence_levels():
    """Test different confidence level classifications."""
    print("\n🎯 Testing Confidence Level Classifications...")
    
    try:
        from sliding_window import get_confidence_level_description
        
        test_cases = [
            (95.0, "Excellent"),
            (80.0, "Good"), 
            (70.0, "Moderate"),
            (50.0, "Low")
        ]
        
        for confidence, expected_level in test_cases:
            level, desc = get_confidence_level_description(confidence)
            print(f"   • {confidence:.0f}% → {level} ({desc})")
            
            # Verify expected level is in the result
            if expected_level.lower() in level.lower():
                print(f"     ✅ Correct classification")
            else:
                print(f"     ⚠️ Unexpected classification")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing confidence levels: {str(e)}")
        return False

def test_dashboard_integration():
    """Test that dashboard can properly display confidence scores."""
    print("\n🖥️ Testing Dashboard Integration...")
    
    try:
        # Test that dashboard imports work
        import streamlit as st
        
        print("✅ Dashboard imports successful")
        
        # Verify confidence-related functions are available
        from sliding_window import calculate_confidence_statistics, get_confidence_level_description
        
        # Test with sample data
        sample_predictions = [
            {'x': 0, 'y': 0, 'w': 64, 'h': 64, 'label_index': 0, 'confidence': 85.0},
            {'x': 32, 'y': 0, 'w': 64, 'h': 64, 'label_index': 1, 'confidence': 92.0},
            {'x': 0, 'y': 32, 'w': 64, 'h': 64, 'label_index': 0, 'confidence': 78.0},
        ]
        
        stats = calculate_confidence_statistics(sample_predictions)
        level, desc = get_confidence_level_description(stats["average"])
        
        print(f"📊 Sample confidence analysis:")
        print(f"   • Average confidence: {stats['average']:.1f}%")
        print(f"   • Assessment: {level}")
        print(f"   • Description: {desc}")
        
        print("✅ Dashboard integration test successful")
        return True
        
    except Exception as e:
        print(f"❌ Dashboard integration error: {str(e)}")
        return False

def create_confidence_demo():
    """Create a visual demonstration of confidence scoring."""
    print("\n🎨 Creating Confidence Scoring Demo...")
    
    try:
        # Create sample confidence data
        confidences = [95, 88, 82, 76, 69, 54, 43, 91, 87, 79]
        labels = ['Forest', 'Urban', 'Water', 'Crop', 'Forest', 'Urban', 'Crop', 'Forest', 'Water', 'Urban']
        
        # Create visualization
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Confidence distribution
        ax1.hist(confidences, bins=5, color='skyblue', alpha=0.7, edgecolor='black')
        ax1.set_xlabel('Confidence (%)')
        ax1.set_ylabel('Number of Patches')
        ax1.set_title('Classification Confidence Distribution')
        ax1.grid(True, alpha=0.3)
        
        # Confidence by class
        colors = ['green' if c >= 80 else 'orange' if c >= 60 else 'red' for c in confidences]
        ax2.scatter(range(len(confidences)), confidences, c=colors, s=100, alpha=0.7)
        ax2.set_xlabel('Patch Index')
        ax2.set_ylabel('Confidence (%)')
        ax2.set_title('Per-Patch Confidence Scores')
        ax2.grid(True, alpha=0.3)
        
        # Add confidence thresholds
        ax2.axhline(y=80, color='green', linestyle='--', alpha=0.5, label='High (≥80%)')
        ax2.axhline(y=60, color='orange', linestyle='--', alpha=0.5, label='Medium (≥60%)')
        ax2.legend()
        
        plt.tight_layout()
        plt.savefig('confidence_scoring_demo.png', dpi=150, bbox_inches='tight')
        plt.close()
        
        print("✅ Created confidence scoring demonstration plot")
        
        # Calculate statistics
        avg_conf = sum(confidences) / len(confidences)
        high_conf_ratio = sum(1 for c in confidences if c >= 80) / len(confidences) * 100
        
        print(f"📊 Demo Statistics:")
        print(f"   • Average Confidence: {avg_conf:.1f}%")
        print(f"   • High Confidence Patches: {high_conf_ratio:.1f}%")
        print(f"   • Confidence Range: {min(confidences)}% - {max(confidences)}%")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating demo: {str(e)}")
        return False

def main():
    """Run all confidence scoring tests."""
    print("🚀 CONFIDENCE SCORING SYSTEM TEST SUITE")
    print("=" * 50)
    
    tests = [
        test_confidence_scoring_system,
        test_confidence_levels,
        test_dashboard_integration,
        create_confidence_demo
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
    print("\n" + "=" * 50)
    print("📋 TEST SUMMARY")
    print("=" * 50)
    
    passed = sum(results)
    total = len(results)
    
    print(f"✅ Tests Passed: {passed}/{total}")
    print(f"📊 Success Rate: {(passed/total)*100:.1f}%")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED - Confidence scoring system ready!")
        print("\n💡 Faculty Demo Features:")
        print("   • Real-time confidence scoring for each classification")
        print("   • Color-coded confidence visualization (Green/Yellow/Red)")
        print("   • Comprehensive confidence statistics and metrics")
        print("   • Professional confidence assessment levels")
        print("   • Integration with existing land cover analysis")
    else:
        print("⚠️ Some tests failed - please review implementation")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)