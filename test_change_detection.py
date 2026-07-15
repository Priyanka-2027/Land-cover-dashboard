#!/usr/bin/env python3
"""
Test the enhanced change detection with labels and overlays.
"""

import cv2
import numpy as np
from change_detection import detect_change, get_change_heatmap, get_change_contours, create_change_comparison

def create_test_images():
    """Create synthetic before/after images for testing."""
    # Before image: mostly green
    before = np.zeros((300, 300, 3), dtype=np.uint8)
    before[:, :] = [0, 128, 0]  # Green background
    
    # After image: some areas changed to gray (development)
    after = before.copy()
    after[50:150, 50:150] = [128, 128, 128]  # Gray square (development)
    after[200:250, 200:250] = [64, 64, 64]   # Darker gray (more development)
    
    return before, after

def test_enhanced_change_detection():
    """Test all the enhanced change detection features."""
    print("🔍 Testing Enhanced Change Detection")
    print("=" * 50)
    
    # Create test images
    before, after = create_test_images()
    
    # Test change detection
    thresh, change_pct = detect_change(before, after, threshold=30)
    print(f"Change detected: {change_pct:.2f}%")
    
    if thresh is not None:
        print("✅ Change detection successful")
        
        # Test overlay heatmap
        heatmap = get_change_heatmap(after, thresh)
        print("✅ Overlay heatmap created")
        
        # Test contour analysis
        contours = get_change_contours(after, thresh)
        print("✅ Contour analysis created")
        
        # Test comparison view
        comparison = create_change_comparison(before, after, thresh)
        print("✅ Before/After comparison created")
        
        # Save test results
        cv2.imwrite("test_before.jpg", before)
        cv2.imwrite("test_after.jpg", after)
        cv2.imwrite("test_heatmap.jpg", heatmap)
        cv2.imwrite("test_contours.jpg", contours)
        cv2.imwrite("test_comparison.jpg", comparison)
        
        print("\n📁 Test images saved:")
        print("   • test_before.jpg - Original image")
        print("   • test_after.jpg - Changed image")
        print("   • test_heatmap.jpg - Overlay with labels")
        print("   • test_contours.jpg - Contour analysis")
        print("   • test_comparison.jpg - Side-by-side comparison")
        
    else:
        print("❌ Change detection failed")

if __name__ == "__main__":
    test_enhanced_change_detection()