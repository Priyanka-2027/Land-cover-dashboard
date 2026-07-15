import cv2
import numpy as np
from typing import Optional

def extract_features(image: np.ndarray) -> Optional[np.ndarray]:
    """
    Extract color distribution features from an image.
    1. RGB histogram (8x8x8 bins = 512 features).
    2. Normalize to sum-to-1 for statistical comparison.
    3. Flatten into a feature vector.
    """
    try:
        if image is None:
            return None
            
        # Ensure image is uint8 for histogram calculation
        if image.dtype != np.uint8:
            image = (image * 255).astype(np.uint8)

        # Calculate 3D histogram (8 bins for R, 8 for G, 8 for B)
        # Total features: 8 * 8 * 8 = 512
        hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        
        # Normalize the histogram (min-max normalization or L2 normalization)
        cv2.normalize(hist, hist)
        
        # Flatten and return the feature vector
        return hist.flatten()
    except Exception:
        return np.zeros(512, dtype=np.float32)

def extract_patch_features(patch: np.ndarray) -> np.ndarray:
    """Helper function for feature extraction from a patch."""
    return extract_features(patch)
