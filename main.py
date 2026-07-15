import os
import cv2
import joblib
import numpy as np
import logging
from typing import List, Optional
from classification import CLASSES
from sliding_window import classify_large_image
from greenery import calculate_green_percentage, get_vegetation_analysis
from change_detection import detect_change
from prediction import predict_future
from simulation import simulate
from suggestion import suggest

# Global Pipeline Log Config
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def run_system_pipeline(image_folder: str = 'test_images/', target_year: int = 2030) -> None:
    """
    End-to-end Command Line Pipeline for Land Cover Analysis.
    Loads model, processes multi-year data, executes detection, and forecasting.
    """
    try:
        logging.info("🌍 LAND COVER CLASSIFICATION & GREENERY PREDICTION SYSTEM")
        logging.info("="*60)

        # 1. Load Trained Model
        model_path = 'models/model.pkl'
        if not os.path.exists(model_path):
            logging.error(f"Model not found at {model_path}. Please train it first.")
            return
        model = joblib.load(model_path)
        logging.info(f"✅ Model loaded successfully.")

        # 2. Identify Test Images
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
            logging.warning(f"Folder '{image_folder}' created. Please add satellite images.")
            return
        
        image_files = sorted([f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
        if not image_files:
            logging.warning(f"No satellite images found in '{image_folder}'.")
            return

        years, green_history, images = [], [], []
        logging.info(f"🚀 Analyzing {len(image_files)} images...")
        
        for i, file_name in enumerate(image_files):
            img_path = os.path.join(image_folder, file_name)
            img = cv2.imread(img_path)
            if img is None: continue
            
            # Map year from file (e.g. area_2022.jpg)
            try:
                year = [int(s) for s in file_name.split('_') if s.isdigit()][0]
            except:
                year = 2020 + i
                
            years.append(year)
            images.append(img)
            
            # Core Processing with Smoothing
            green_pct, mask = calculate_green_percentage(img, method="hsv")  # Use improved HSV method
            green_history.append(green_pct)
            
            # Get detailed vegetation statistics
            veg_analysis = get_vegetation_analysis(img)
            
            # Display Results
            logging.info(f"\n--- Year {year} ({file_name}) ---")
            logging.info(f"🍃 Greenery Percentage: {green_pct:.2f}%")
            if veg_analysis and 'hsv' in veg_analysis:
                hsv_data = veg_analysis['hsv']
                logging.info(f"🌿 HSV Detection: {hsv_data['percentage']:.2f}%")
                logging.info(f"💚 Detection Method: {hsv_data['description']}")
                if 'confidence' in veg_analysis:
                    logging.info(f"🎯 Analysis Confidence: {veg_analysis['confidence']}")
            patch_results = classify_large_image(img, model)
            if patch_results:
                labels = [r['label_index'] for r in patch_results]
                dominant_idx = max(set(labels), key=labels.count)
                logging.info(f"🏢 Dominant Land Cover: {CLASSES[dominant_idx]}")
            logging.info(f"💡 Recommendation: {suggest(green_pct)}")

        # Apply smoothing for realistic temporal trends
        if len(green_history) >= 2:
            from greenery import smooth_values, apply_realistic_constraints
            
            logging.info(f"\n📊 Temporal Trend Analysis:")
            logging.info(f"Raw values: {[f'{v:.1f}%' for v in green_history]}")
            
            # Apply smoothing
            smoothed_values = smooth_values(green_history)
            final_values = apply_realistic_constraints(smoothed_values)
            
            logging.info(f"Smoothed values: {[f'{v:.1f}%' for v in final_values]}")
            
            # Calculate improvement
            raw_range = max(green_history) - min(green_history)
            smooth_range = max(final_values) - min(final_values)
            
            if raw_range > smooth_range + 5:
                logging.info(f"✅ Trend Smoothing Applied:")
                logging.info(f"   • Raw variation: {raw_range:.1f}%")
                logging.info(f"   • Smoothed variation: {smooth_range:.1f}%")
                logging.info(f"   • More realistic temporal progression")
                
                # Use smoothed values for analysis
                green_history = final_values

        # Multi-Year Analysis
        if len(images) >= 2:
            logging.info("\n" + "="*30 + " CHANGE DETECTION " + "="*30)
            _, change_pct = detect_change(images[0], images[-1])
            logging.info(f"🔄 Total Land Area Changed ({years[0]}-{years[-1]}): {change_pct:.2f}%")

        if len(years) >= 2:
            logging.info("\n" + "="*30 + " FUTURE PREDICTION " + "="*30)
            prediction, trend = predict_future(years, green_history, target_year)
            logging.info(f"🔮 Prediction for {target_year}: {prediction:.2f}% Greenery")
            logging.info(f"📈 Yearly Trend: {'Increasing' if trend > 0 else 'Decreasing'} by {abs(trend):.4f}%/yr.")

        # Scenario Simulation
        logging.info("\n" + "="*30 + " SCENARIO SIMULATION " + "="*30)
        current_green = green_history[-1]
        u_inc, p_inc = 10, 5 
        sim_res = simulate(current_green, u_inc, p_inc)
        logging.info(f"🏞️  Current: {current_green:.2f}% | 🧪 Simulated: {sim_res:.2f}%")
        logging.info("✅ System Pipeline complete.")
        
    except Exception as e:
        logging.error(f"Pipeline Error: {str(e)}")

if __name__ == "__main__":
    run_system_pipeline()
