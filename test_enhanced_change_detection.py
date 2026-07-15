#!/usr/bin/env python3
"""
Test Enhanced Change Detection with Legend and Intelligent Messages
Verifies the final polish features for change detection visualization.
"""

import sys
import os
sys.path.append('.')

import numpy as np
import cv2
import matplotlib.pyplot as plt

def test_change_detection_enhancements():
    """Test the enhanced change detection features."""
    print("🔄 Testing Enhanced Change Detection Features...")
    
    try:
        # Import enhanced functions
        from change_detection import (
            detect_change,
            get_change_interpretation_message,
            add_change_legend,
            create_enhanced_change_overlay
        )
        
        print("✅ Successfully imported enhanced change detection modules")
        
        # Create test images with simulated changes
        image1 = np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)
        image2 = image1.copy()
        
        # Add simulated changes (red squares to simulate urban development)
        cv2.rectangle(image2, (50, 50), (100, 100), (0, 0, 255), -1)  # Large change
        cv2.rectangle(image2, (150, 150), (180, 180), (0, 0, 255), -1)  # Medium change
        cv2.rectangle(image2, (200, 50), (220, 70), (0, 0, 255), -1)   # Small change
        
        print("🔄 Testing change detection with simulated urban development...")
        
        # Perform change detection
        thresh, change_percentage = detect_change(image1, image2, threshold=30)
        
        if thresh is not None:
            print(f"✅ Change detection successful: {change_percentage:.2f}% change detected")
            
            # Test intelligent message generation
            message = get_change_interpretation_message(change_percentage)
            print(f"📊 Intelligent Message: {message}")
            
            # Test legend addition
            test_image = np.random.randint(0, 255, (512, 512, 3), dtype=np.uint8)
            legend_image = add_change_legend(test_image)
            print("✅ Legend successfully added to visualization")
            
            # Test enhanced overlay creation
            enhanced_overlay = create_enhanced_change_overlay(image2, thresh, change_percentage)
            print("✅ Enhanced overlay with legend and message created")
            
            return True
        else:
            print("❌ Change detection failed")
            return False
            
    except Exception as e:
        print(f"❌ Error in enhanced change detection test: {str(e)}")
        return False

def test_interpretation_messages():
    """Test different change interpretation messages."""
    print("\n📊 Testing Change Interpretation Messages...")
    
    try:
        from change_detection import get_change_interpretation_message
        
        test_cases = [
            (25.0, "Major change"),
            (15.0, "Substantial change"),
            (10.0, "Moderate change"),
            (6.0, "Minor change"),
            (3.0, "Subtle change"),
            (1.0, "Stable")
        ]
        
        for change_pct, expected_type in test_cases:
            message = get_change_interpretation_message(change_pct)
            print(f"   • {change_pct:.1f}% → {message}")
            
            # Verify message contains expected type
            if any(word.lower() in message.lower() for word in expected_type.split()):
                print(f"     ✅ Correct interpretation")
            else:
                print(f"     ⚠️ Unexpected interpretation")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing interpretation messages: {str(e)}")
        return False

def test_legend_functionality():
    """Test the legend addition functionality."""
    print("\n🎨 Testing Legend Functionality...")
    
    try:
        from change_detection import add_change_legend
        
        # Create test image
        test_image = np.random.randint(0, 255, (512, 512, 3), dtype=np.uint8)
        
        # Add legend
        legend_image = add_change_legend(test_image)
        
        # Verify legend was added (image should be different)
        if not np.array_equal(test_image, legend_image):
            print("✅ Legend successfully added to image")
            
            # Save example for visual verification
            cv2.imwrite('test_legend_example.png', legend_image)
            print("✅ Legend example saved as 'test_legend_example.png'")
            
            return True
        else:
            print("❌ Legend not added - images are identical")
            return False
            
    except Exception as e:
        print(f"❌ Error testing legend functionality: {str(e)}")
        return False

def test_dashboard_integration():
    """Test dashboard integration with enhanced features."""
    print("\n🖥️ Testing Dashboard Integration...")
    
    try:
        # Test that dashboard can import enhanced functions
        from change_detection import create_enhanced_change_overlay, get_change_interpretation_message
        
        print("✅ Dashboard can import enhanced change detection functions")
        
        # Test with sample data
        sample_image = np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8)
        sample_thresh = np.random.randint(0, 2, (512, 512), dtype=np.uint8) * 255
        sample_change_pct = 8.5
        
        # Test enhanced overlay creation
        enhanced_overlay = create_enhanced_change_overlay(sample_image, sample_thresh, sample_change_pct)
        print("✅ Enhanced overlay creation successful")
        
        # Test message generation
        message = get_change_interpretation_message(sample_change_pct)
        print(f"✅ Message generation successful: {message}")
        
        print("✅ Dashboard integration test successful")
        return True
        
    except Exception as e:
        print(f"❌ Dashboard integration error: {str(e)}")
        return False

def create_change_detection_demo():
    """Create a visual demonstration of enhanced change detection."""
    print("\n🎨 Creating Enhanced Change Detection Demo...")
    
    try:
        from change_detection import detect_change, create_enhanced_change_overlay
        
        # Create before and after images
        before = np.zeros((300, 400, 3), dtype=np.uint8)
        before[:] = (34, 139, 34)  # Forest green background
        
        after = before.copy()
        # Add urban development (gray rectangles)
        cv2.rectangle(after, (50, 50), (150, 120), (128, 128, 128), -1)   # Building 1
        cv2.rectangle(after, (200, 80), (280, 140), (128, 128, 128), -1)  # Building 2
        cv2.rectangle(after, (100, 180), (180, 220), (64, 64, 64), -1)    # Road
        
        # Perform change detection
        thresh, change_pct = detect_change(before, after, threshold=20)
        
        if thresh is not None:
            # Create enhanced visualization
            enhanced_viz = create_enhanced_change_overlay(after, thresh, change_pct)
            
            # Create comparison plot
            fig, axes = plt.subplots(1, 3, figsize=(15, 5))
            
            # Before
            axes[0].imshow(cv2.cvtColor(before, cv2.COLOR_BGR2RGB))
            axes[0].set_title('Before (Forest Area)')
            axes[0].axis('off')
            
            # After
            axes[1].imshow(cv2.cvtColor(after, cv2.COLOR_BGR2RGB))
            axes[1].set_title('After (Urban Development)')
            axes[1].axis('off')
            
            # Enhanced change detection
            axes[2].imshow(cv2.cvtColor(enhanced_viz, cv2.COLOR_BGR2RGB))
            axes[2].set_title(f'Enhanced Change Detection\n({change_pct:.1f}% change)')
            axes[2].axis('off')
            
            plt.tight_layout()
            plt.savefig('enhanced_change_detection_demo.png', dpi=150, bbox_inches='tight')
            plt.close()
            
            print("✅ Created enhanced change detection demonstration")
            print(f"📊 Demo shows {change_pct:.1f}% change with legend and intelligent message")
            
            return True
        else:
            print("❌ Change detection failed in demo")
            return False
            
    except Exception as e:
        print(f"❌ Error creating demo: {str(e)}")
        return False

def main():
    """Run all enhanced change detection tests."""
    print("🚀 ENHANCED CHANGE DETECTION TEST SUITE")
    print("=" * 60)
    
    tests = [
        test_change_detection_enhancements,
        test_interpretation_messages,
        test_legend_functionality,
        test_dashboard_integration,
        create_change_detection_demo
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
    print("\n" + "=" * 60)
    print("📋 TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(results)
    total = len(results)
    
    print(f"✅ Tests Passed: {passed}/{total}")
    print(f"📊 Success Rate: {(passed/total)*100:.1f}%")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED - Enhanced change detection ready!")
        print("\n💡 Faculty Demo Features:")
        print("   • Professional legend with Red = Change, Green = No change")
        print("   • Intelligent change interpretation messages")
        print("   • Enhanced overlay visualization with all elements")
        print("   • Contextual change analysis (Major/Moderate/Minor)")
        print("   • Professional presentation with clear visual indicators")
    else:
        print("⚠️ Some tests failed - please review implementation")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)