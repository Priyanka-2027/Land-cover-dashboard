#!/usr/bin/env python3
"""
Comprehensive test of greenery detection across different land cover types.
"""

import cv2
import numpy as np
import os
from greenery import calculate_green_percentage

def test_all_categories():
    """Test greenery detection on different EuroSAT categories."""
    categories = [
        ("Forest", "60-90%"),
        ("AnnualCrop", "40-80%"),
        ("HerbaceousVegetation", "50-85%")
    ]
    
    print("🌍 Comprehensive EuroSAT Greenery Test")
    print("=" * 70)
    
    for category, expected_range in categories:
        category_dir = f"data/EuroSAT/{category}"
        
        if not os.path.exists(category_dir):
            print(f"❌ Category not found: {category}")
            continue
            
        print(f"\n📁 {category} (Expected: {expected_range})")
        print("-" * 50)
        
        # Get first 5 images from category
        image_files = [f for f in os.listdir(category_dir) if f.endswith('.jpg')][:5]
        
        hsv_percentages = []
        rgb_percentages = []
        
        for img_file in image_files:
            img_path = os.path.join(category_dir, img_file)
            img = cv2.imread(img_path)
            
            if img is None:
                continue
                
            # Test both methods
            hsv_pct, _ = calculate_green_percentage(img, method="hsv")
            rgb_pct, _ = calculate_green_percentage(img, method="rgb")
            
            hsv_percentages.append(hsv_pct)
            rgb_percentages.append(rgb_pct)
            
            print(f"   {img_file:20s}: HSV={hsv_pct:5.1f}%  RGB={rgb_pct:5.1f}%")
        
        if hsv_percentages:
            hsv_avg = np.mean(hsv_percentages)
            rgb_avg = np.mean(rgb_percentages)
            hsv_std = np.std(hsv_percentages)
            
            print(f"\n   📊 SUMMARY:")
            print(f"      HSV Average: {hsv_avg:5.1f}% ± {hsv_std:4.1f}%")
            print(f"      RGB Average: {rgb_avg:5.1f}%")
            
            # Evaluation
            if category == "Forest" and 60 <= hsv_avg <= 90:
                print(f"      ✅ HSV results are realistic for {category}")
            elif category == "AnnualCrop" and 40 <= hsv_avg <= 80:
                print(f"      ✅ HSV results are realistic for {category}")
            elif category == "HerbaceousVegetation" and 50 <= hsv_avg <= 85:
                print(f"      ✅ HSV results are realistic for {category}")
            else:
                print(f"      ⚠️  HSV results may need adjustment for {category}")

def test_urban_simulation():
    """Test with simulated urban/mixed images."""
    print(f"\n🏙️  URBAN/MIXED SIMULATION TEST")
    print("=" * 70)
    
    # Create simulated urban image (should be 10-40% green)
    urban_img = np.zeros((300, 300, 3), dtype=np.uint8)
    
    # 70% gray buildings/roads
    urban_img[0:210, :] = [128, 128, 128]  # Gray
    
    # 30% green parks/trees
    urban_img[210:300, :] = [0, 128, 0]    # Green
    
    hsv_pct, _ = calculate_green_percentage(urban_img, method="hsv")
    rgb_pct, _ = calculate_green_percentage(urban_img, method="rgb")
    
    print(f"Simulated Urban (30% green expected):")
    print(f"   HSV: {hsv_pct:5.1f}%")
    print(f"   RGB: {rgb_pct:5.1f}%")
    
    if 25 <= hsv_pct <= 35:
        print(f"   ✅ HSV urban detection is accurate")
    else:
        print(f"   ⚠️  HSV urban detection needs adjustment")

if __name__ == "__main__":
    test_all_categories()
    test_urban_simulation()