#!/usr/bin/env python3
"""
Test script to compare different greenery detection methods.
Demonstrates the improvement from RGB to HSV-based vegetation detection.
"""

import cv2
import numpy as np
import os
from greenery import calculate_green_percentage, get_vegetation_statistics

def test_greenery_methods(image_path: str):
    """Compare RGB vs HSV vs Combined greenery detection methods."""
    
    if not os.path.exists(image_path):
        print(f"❌ Image not found: {image_path}")
        return
    
    # Load test image
    image = cv2.imread(image_path)
    if image is None:
        print(f"❌ Could not load image: {image_path}")
        return
    
    print(f"🖼️  Testing image: {os.path.basename(image_path)}")
    print(f"📏 Image size: {image.shape[1]}x{image.shape[0]}")
    print("=" * 60)
    
    # Test all methods
    methods = ["rgb", "hsv", "combined"]
    results = {}
    
    for method in methods:
        print(f"\n🔍 Testing {method.upper()} method:")
        
        # Calculate greenery percentage
        percentage, mask = calculate_green_percentage(image, method=method)
        results[method] = percentage
        
        # Get detailed statistics for HSV method
        if method == "hsv" and mask is not None:
            stats = get_vegetation_statistics(image, mask)
            
            print(f"   🌿 Vegetation: {percentage:.2f}%")
            if stats:
                print(f"   📊 Category: {stats.get('density_category', 'Unknown')}")
                if 'health_score' in stats:
                    print(f"   💚 Health Score: {stats['health_score']:.1f}/255")
                print(f"   🔢 Pixels: {stats.get('pixel_count', 0):,}")
        else:
            print(f"   🌿 Vegetation: {percentage:.2f}%")
    
    # Compare results
    print("\n" + "=" * 60)
    print("📈 COMPARISON RESULTS:")
    print("=" * 60)
    
    for method in methods:
        indicator = "🟢" if method == "hsv" else "🔵" if method == "combined" else "🟡"
        print(f"{indicator} {method.upper():>8}: {results[method]:>6.2f}%")
    
    # Analysis
    print(f"\n💡 ANALYSIS:")
    hsv_result = results.get("hsv", 0)
    rgb_result = results.get("rgb", 0)
    
    if abs(hsv_result - rgb_result) > 5:
        if hsv_result > rgb_result:
            print(f"   ✅ HSV detected {hsv_result - rgb_result:.1f}% more vegetation (likely more accurate)")
        else:
            print(f"   ⚠️  HSV detected {rgb_result - hsv_result:.1f}% less vegetation (filtered out false positives)")
    else:
        print(f"   ℹ️  Similar results between methods (difference: {abs(hsv_result - rgb_result):.1f}%)")
    
    print(f"   🎯 Recommended: Use HSV method for most accurate vegetation detection")

def main():
    """Test with sample images from the project."""
    
    print("🌿 GREENERY DETECTION METHOD COMPARISON")
    print("=" * 60)
    print("Testing improved HSV-based vegetation detection vs legacy RGB method")
    print()
    
    # Test with images from test_images folder if available
    test_folders = ["test_images", "data/EuroSAT/Forest", "data/EuroSAT/AnnualCrop"]
    
    for folder in test_folders:
        if os.path.exists(folder):
            print(f"📁 Checking folder: {folder}")
            
            # Get first few image files
            image_files = [f for f in os.listdir(folder) 
                          if f.lower().endswith(('.jpg', '.jpeg', '.png'))][:3]
            
            if image_files:
                for img_file in image_files:
                    test_greenery_methods(os.path.join(folder, img_file))
                    print()
                break
    else:
        print("❌ No test images found. Please add images to test_images/ folder")
        print("💡 You can test with any satellite or aerial imagery")

if __name__ == "__main__":
    main()