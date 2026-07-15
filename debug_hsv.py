#!/usr/bin/env python3
"""
Debug HSV values in forest images to fine-tune the ranges.
"""

import cv2
import numpy as np
import os
from greenery import calculate_green_percentage

def analyze_forest_images():
    """Analyze HSV distribution in multiple forest images."""
    forest_dir = "data/EuroSAT/Forest"
    
    if not os.path.exists(forest_dir):
        print(f"❌ Forest directory not found: {forest_dir}")
        return
    
    # Get first 5 forest images
    forest_files = [f for f in os.listdir(forest_dir) if f.endswith('.jpg')][:5]
    
    print("🌲 Forest Image HSV Analysis")
    print("=" * 60)
    
    all_h_values = []
    all_s_values = []
    all_v_values = []
    
    for img_file in forest_files:
        img_path = os.path.join(forest_dir, img_file)
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
        
        # Test current detection
        pct, _ = calculate_green_percentage(img, method="hsv")
        print(f"   Current HSV Detection: {pct:.1f}%")
    
    # Overall statistics
    print(f"\n🔍 OVERALL FOREST HSV STATISTICS:")
    print(f"   H: min={np.min(all_h_values):3d} max={np.max(all_h_values):3d} mean={np.mean(all_h_values):5.1f}")
    print(f"   S: min={np.min(all_s_values):3d} max={np.max(all_s_values):3d} mean={np.mean(all_s_values):5.1f}")
    print(f"   V: min={np.min(all_v_values):3d} max={np.max(all_v_values):3d} mean={np.mean(all_v_values):5.1f}")
    
    # Percentile analysis
    h_p25, h_p75 = np.percentile(all_h_values, [25, 75])
    s_p25, s_p75 = np.percentile(all_s_values, [25, 75])
    v_p25, v_p75 = np.percentile(all_v_values, [25, 75])
    
    print(f"\n📊 PERCENTILE RANGES (25th-75th):")
    print(f"   H: {h_p25:5.1f} - {h_p75:5.1f}")
    print(f"   S: {s_p25:5.1f} - {s_p75:5.1f}")
    print(f"   V: {v_p25:5.1f} - {v_p75:5.1f}")
    
    print(f"\n💡 SUGGESTED HSV RANGES:")
    print(f"   Range 1 (Standard Green): H=[35-80], S=[{s_p25:.0f}-255], V=[{v_p25:.0f}-255]")
    print(f"   Range 2 (Blue-Green): H=[80-110], S=[{s_p25:.0f}-255], V=[{v_p25:.0f}-255]")

def test_restrictive_ranges():
    """Test more restrictive HSV ranges."""
    print(f"\n🧪 TESTING RESTRICTIVE RANGES")
    print("=" * 60)
    
    forest_dir = "data/EuroSAT/Forest"
    forest_files = [f for f in os.listdir(forest_dir) if f.endswith('.jpg')][:3]
    
    for img_file in forest_files:
        img_path = os.path.join(forest_dir, img_file)
        img = cv2.imread(img_path)
        
        if img is None:
            continue
            
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # Test different threshold combinations
        test_ranges = [
            {"name": "Conservative", "lower": [80, 100, 60], "upper": [110, 255, 255]},
            {"name": "Moderate", "lower": [80, 80, 50], "upper": [110, 255, 255]},
            {"name": "Liberal", "lower": [80, 60, 40], "upper": [110, 255, 255]},
        ]
        
        print(f"\n📸 {img_file}:")
        
        for test_range in test_ranges:
            lower = np.array(test_range["lower"])
            upper = np.array(test_range["upper"])
            mask = cv2.inRange(hsv, lower, upper)
            
            vegetation_pixels = np.sum(mask > 0)
            total_pixels = img.shape[0] * img.shape[1]
            percentage = (vegetation_pixels / total_pixels) * 100
            
            print(f"   {test_range['name']:>12}: {percentage:5.1f}% (S≥{test_range['lower'][1]}, V≥{test_range['lower'][2]})")

if __name__ == "__main__":
    analyze_forest_images()
    test_restrictive_ranges()