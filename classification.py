import os
import cv2
import numpy as np
import joblib
import logging
from typing import List, Tuple, Optional
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from preprocessing import preprocess_image
from features import extract_features

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Actual EuroSAT Classes
CLASSES: List[str] = [
    'AnnualCrop', 'Forest', 'HerbaceousVegetation', 'Highway', 
    'Industrial', 'Pasture', 'PermanentCrop', 'Residential', 
    'River', 'SeaLake'
]

def apply_augmentation(image: np.ndarray) -> List[np.ndarray]:
    """Generates 6 augmentations (Original + 2 Flips + 3 Rotations)."""
    if image is None:
        return []
    
    aug = [image]
    # Flips
    aug.append(cv2.flip(image, 1)) # Horizontal Flip
    aug.append(cv2.flip(image, 0)) # Vertical Flip
    # Rotations
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    for angle in [90, 180, 270]:
        matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, matrix, (w, h))
        aug.append(rotated)
    return aug

def load_dataset(data_dir: str) -> Tuple[Optional[np.ndarray], Optional[np.ndarray]]:
    if not os.path.exists(data_dir):
        logging.error(f"Dataset path '{data_dir}' not found.")
        return None, None
        
    X, y = [], []
    for idx, class_name in enumerate(CLASSES):
        class_path = os.path.join(data_dir, class_name)
        if not os.path.isdir(class_path):
            logging.warning(f"Class folder '{class_name}' missing skip.")
            continue
            
        logging.info(f"Loading {class_name}...")
        files = [f for f in os.listdir(class_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        for img_name in files:
            image = cv2.imread(os.path.join(class_path, img_name))
            if image is not None:
                for aug_img in apply_augmentation(image):
                    prep = preprocess_image(aug_img)
                    feat = extract_features(prep)
                    if feat is not None:
                        X.append(feat)
                        y.append(idx)
                        
    return np.array(X), np.array(y)

def train_model(data_dir: str, save_path: str = 'models/model.pkl') -> Optional[RandomForestClassifier]:
    X, y = load_dataset(data_dir)
    if X is None or len(X) == 0:
        logging.error("No data loaded. Check'data/EuroSAT/' subfolders.")
        return None
        
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    logging.info(f"Training on {len(X_train)} samples...")
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1, class_weight='balanced')
    model.fit(X_train, y_train)
    
    accuracy = accuracy_score(y_test, model.predict(X_test))
    logging.info(f"✅ Model Accuracy: {accuracy * 100:.2f}%")
    
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    joblib.dump(model, save_path)
    logging.info(f"💾 Model saved to: {save_path}")
    return model

def predict_land_cover(model, image_path: str) -> str:
    image = cv2.imread(image_path)
    if image is not None:
        p = preprocess_image(image)
        f = extract_features(p).reshape(1, -1)
        return CLASSES[model.predict(f)[0]]
    return "Unknown"

if __name__ == "__main__":
    train_model('data/EuroSAT/')
