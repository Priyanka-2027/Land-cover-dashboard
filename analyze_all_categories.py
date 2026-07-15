#!/usr/bin/env python3
"""
Analyze HSV values across all vegetation categories to optimize ranges.
"""

import cv2
import numpy as np
import os

def analyze_category_hsv(category_name):
    """Analyze HSV distribution for a specific category."""
    category_dir = f"data/EuroSAT/{category_name}"
    
    if not os.path.exists(category_dir):
        print(f"❌ Category not found: {category_name}")
        return
    
    print(f"\n🔍 {category_name} HSV Analysis")
    print("=" * 60)
    
    # Get first 3 images
    image_files = [f for f in os.listdir(category_dir) if f.endswith('.jpg')][:3]
    
    all_h_values = []
    all_s_values = []
    all_v_values = []
    
    for img_file in image_files:
        img_path = os.path.join(category_dir, img_file)
        img = cv2.imread(img_path)
        
        if img is None:
            continue
            
        # Convert to HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # Get statistics
        h_vals = hsv[:,:,0].flatten()
        s_vals = hsv[:,:,1].flatten()
        v_vals = hsv[:,:,2].flatten()
        
        all_h_values.extend(h_vals)
        all_s_values.extend(s_vals)
        all_v_values.extend(v_vals)
        
        print(f"\n📸 {img_file}:")
        print(f"   H: min={np.min(h_vals):3d} max={np.max(h_vals):3d} mean={np.mean(h_vals):5.1f}")
        print(f"   S: min={np.min(s_vals):3d} max={np.max(s_vals):3d} mean={np.mean(s_vals):5.1f}")
        print(f"   V: min={np.min(v_vals):3d} max={np.max(v_vals):3d} mean={np.mean(v_vals):5.1f}")
    
    if all_h_values:
        # Overall statistics
        print(f"\n📊 OVERALL {category_name} STATISTICS:")
        print(f"   H: min={np.min(all_h_values):3d} max={np.max(all_h_values):3d} mean={np.mean(all_h_values):5.1f}")
        print(f"   S: min={np.min(all_s_values):3d} max={np.max(all_s_values):3d} mean={np.mean(all_s_values):5.1f}")
        print(f"   V: min={np.min(all_v_values):3d} max={np.max(all_v_values):3d} mean={np.mean(all_v_values):5.1f}")
        
        # Percentile analysis for vegetation pixels
        h_p25, h_p75 = np.percentile(all_h_values, [25, 75])
        s_p25, s_p75 = np.percentile(all_s_values, [25, 75])
        v_p25, v_p75 = np.percentile(all_v_values, [25, 75])
        
        print(f"\n📈 PERCENTILE RANGES (25th-75th):")
        print(f"   H: {h_p25:5.1f} - {h_p75:5.1f}")
        print(f"   S: {s_p25:5.1f} - {s_p75:5.1f}")
        print(f"   V: {v_p25:5.1f} - {v_p75:5.1f}")

if __name__ == "__main__":
    categories = ["Forest", "AnnualCrop", "HerbaceousVegetation"]
    
    for category in categories:
        analyze_category_hsv(category)