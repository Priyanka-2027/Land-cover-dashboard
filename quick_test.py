import cv2
import sys
import os
sys.path.append('.')
from greenery import calculate_green_percentage

# Test forest images
folder = 'data/EuroSAT/Forest'
if os.path.exists(folder):
    files = [f for f in os.listdir(folder) if f.endswith('.jpg')][:3]
    print("🌲 Forest Images:")
    for f in files:
        img = cv2.imread(os.path.join(folder, f))
        if img is not None:
            pct, _ = calculate_green_percentage(img, "hsv")
            print(f"   {f}: {pct:.1f}%")

# Test crop images  
folder = 'data/EuroSAT/AnnualCrop'
if os.path.exists(folder):
    files = [f for f in os.listdir(folder) if f.endswith('.jpg')][:3]
    print("\n🌾 Crop Images:")
    for f in files:
        img = cv2.imread(os.path.join(folder, f))
        if img is not None:
            pct, _ = calculate_green_percentage(img, "hsv")
            print(f"   {f}: {pct:.1f}%")