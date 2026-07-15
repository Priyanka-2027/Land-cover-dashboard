#!/usr/bin/env python3
"""
Test script to verify the HSV greenery detection fix.
This will help debug why green percentages are too low.
"""

import cv2
import numpy as np
import os
from greenery import calculate_green_percentage

def create_test_image():
    """Create a synthetic test image with known green content."""
    # Create a 300x300 test image
    img = np.zeros((300, 300, 3), dtype=np.uint8)
    
    # Fill with different colors
    # Top half: Green vegetation (should be detected)
    img[0:150, :] = [0, 128, 0]  # Dark green
    
    # Bottom left quarter: Bright green (should be detected)
    img[150:300, 0:150] = [0, 255, 0]  # Bright green
    
    # Bottom right quarter: Blue (should NOT be detected)
    img[150:300, 150:300] = [255, 0, 0]  # Blue
    
    return img

def test_hsv_ranges():
    """Test HSV ranges with known green colors."""
    print("🧪 Testing HSV Greenery Detection")
    print("=" * 50)
    
    # Test with synthetic image
    test_img = create_test_image()
    
    print("📊 Testing with synthetic image (75% green expected):")
    
    # Test all methods
    methods = ["hsv", "rgb", "combined"]
    for method in methods:
        percentage, mask = calculate_green_percentage(test_img, method=method)
        print(f"   {method.upper():>8}: {percentage:>6.2f}%")
    
    print("\n" + "=" * 50)
    
    # Test with real images if available
    test_folders = ["test_images", "data/EuroSAT/Forest", "data/EuroSAT/AnnualCrop"]
    
    for folder in test_folders:
        if os.path.exists(folder):
            print(f"📁 Testing with real images from: {folder}")
            
            # Get first few image files
            image_files = [f for f in os.listdir(folder) 
                          if f.lower().endswith(('.jpg', '.jpeg', '.png'))][:3]
            
            if image_files:
                for img_file in image_files:
                    img_path = os.path.join(folder, img_file)
                    img = cv2.imread(img_path)
                    
                    if img is not None:
                        print(f"\n🖼️  {img_file}:")
                        
                        for method in methods:
                            percentage, _ = calculate_green_percentage(img, method=method)
                            print(f"   {method.upper():>8}: {percentage:>6.2f}%")
                break
    
    print("\n" + "=" * 50)
    print("💡 Expected Results:")
    print("   • Synthetic image: ~75% (3/4 of image is green)")
    print("   • Forest images: 60-90% (dense vegetation)")
    print("   • Crop images: 40-80% (agricultural vegetation)")
    print("   • Urban areas: 10-40% (parks, trees, lawns)")
    print("\n✅ If values are still too low, HSV ranges need further adjustment")

def debug_hsv_values(image_path: str):
    """Debug HSV values in a specific image to understand the ranges."""
    if not os.path.exists(image_path):
        print(f"❌ Image not found: {image_path}")
        return
    
    img = cv2.imread(image_path)
    if img is None:
        print(f"❌ Could not load image: {image_path}")
        return
    
    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Sample some pixels to see HSV ranges
    h, w = hsv.shape[:2]
    sample_points = [
        (h//4, w//4),    # Top-left quadrant
        (h//4, 3*w//4),  # Top-right quadrant  
        (3*h//4, w//4),  # Bottom-left quadrant
        (3*h//4, 3*w//4) # Bottom-right quadrant
    ]
    
    print(f"\n🔍 HSV Analysis for: {os.path.basename(image_path)}")
    print("Sample HSV values from different regions:")
    
    for i, (y, x) in enumerate(sample_points):
        h_val, s_val, v_val = hsv[y, x]
        bgr_val = img[y, x]
        print(f"   Region {i+1}: H={h_val:3d} S={s_val:3d} V={v_val:3d} | BGR=({bgr_val[0]:3d},{bgr_val[1]:3d},{bgr_val[2]:3d})")
    
    # Show overall HSV statistics
    h_mean, s_mean, v_mean = np.mean(hsv, axis=(0,1))
    print(f"   Average:  H={h_mean:5.1f} S={s_mean:5.1f} V={v_mean:5.1f}")

if __name__ == "__main__":
    test_hsv_ranges()
    
    # Debug specific image if provided
    import sys
    if len(sys.argv) > 1:
        debug_hsv_values(sys.argv[1])