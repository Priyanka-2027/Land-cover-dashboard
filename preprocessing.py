import cv2
import numpy as np
from typing import Optional, Tuple

def preprocess_image(image: np.ndarray, size: Tuple[int, int] = (64, 64)) -> Optional[np.ndarray]:
    """
    Production-grade preprocessing for satellite images.
    Converts BGR to RGB, resizes, reduces noise, and normalizes.
    """
    try:
        if image is None:
            return None
        
        # Convert BGR (OpenCV) to RGB
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Standardize Resolution
        resized_image = cv2.resize(rgb_image, size, interpolation=cv2.INTER_AREA)
        
        # Noise Reduction
        blurred_image = cv2.GaussianBlur(resized_image, (3, 3), 0)
        
        # Normalization [0, 1]
        return blurred_image.astype(np.float32) / 255.0
    except Exception:
        return None

def preprocess_patch(patch: np.ndarray) -> np.ndarray:
    """Preprocess a single patch for model inference."""
    try:
        patch = cv2.resize(patch, (64, 64), interpolation=cv2.INTER_AREA)
        patch = cv2.GaussianBlur(patch, (3, 3), 0)
        return patch.astype(np.float32) / 255.0
    except Exception:
        return np.zeros((64, 64, 3), dtype=np.float32)
