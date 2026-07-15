import cv2
import numpy as np
from typing import Tuple, Optional

def detect_change(image1: np.ndarray, image2: np.ndarray, threshold: int = 50) -> Tuple[Optional[np.ndarray], float]:
    """
    Advanced multi-year change detection with improved thresholding.
    Uses adaptive thresholding to reduce noise and highlight major changes only.
    """
    try:
        # Resize both to 512x512 for better detail preservation
        img1 = cv2.resize(image1, (512, 512))
        img2 = cv2.resize(image2, (512, 512))
        
        # Convert to Grayscale
        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        
        # Apply Gaussian blur to reduce noise
        gray1 = cv2.GaussianBlur(gray1, (5, 5), 0)
        gray2 = cv2.GaussianBlur(gray2, (5, 5), 0)
        
        # Absolute Difference Image
        diff = cv2.absdiff(gray1, gray2)
        
        # Apply improved thresholding - higher threshold for major changes only
        _, thresh = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)
        
        # Apply morphological operations to clean up noise
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        
        # Calculate change percentage
        change_pixels = np.sum(thresh > 0)
        total_pixels = thresh.size
        change_percentage = (change_pixels / total_pixels) * 100
        
        return thresh, float(change_percentage)
    except Exception:
        return None, 0.0

def get_change_heatmap(image: np.ndarray, thresh: np.ndarray) -> np.ndarray:
    """
    Create professional change overlay with intelligent labeling.
    Shows changes with clear red highlighting and adds contextual labels.
    """
    try:
        # Resize original image to match the 512x512 result
        canvas = cv2.resize(image, (512, 512))
        
        # Create colored overlay for changes
        overlay = canvas.copy()
        
        # Apply bright red highlighting to changed areas
        overlay[thresh > 0] = [0, 0, 255]  # Bright red for maximum visibility
        
        # Blend with original image (60% original, 40% overlay for better contrast)
        result = cv2.addWeighted(canvas, 0.6, overlay, 0.4, 0)
        
        # Add intelligent labels based on change patterns
        result = _add_change_labels(result, thresh)
        
        return result
    except Exception:
        return cv2.resize(image, (512, 512))

def get_change_contours(image: np.ndarray, thresh: np.ndarray) -> np.ndarray:
    """
    Advanced visualization: Draw contours with intelligent labels.
    Creates publication-ready visualization with contextual information.
    """
    try:
        # Resize original image to match threshold
        canvas = cv2.resize(image, (512, 512))
        
        # Find contours of change areas
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Filter out small contours (noise reduction)
        min_area = 100  # Minimum area for significant changes
        major_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]
        
        # Draw contours with different colors and labels based on size
        label_positions = []
        
        for i, contour in enumerate(major_contours):
            area = cv2.contourArea(contour)
            
            # Get contour center for labeling
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                label_positions.append((cx, cy, area))
            
            if area > 1000:  # Large changes - red
                cv2.drawContours(canvas, [contour], -1, (0, 0, 255), 3)
            elif area > 500:  # Medium changes - orange
                cv2.drawContours(canvas, [contour], -1, (0, 165, 255), 2)
            else:  # Small changes - yellow
                cv2.drawContours(canvas, [contour], -1, (0, 255, 255), 2)
        
        # Add intelligent labels
        canvas = _add_contour_labels(canvas, label_positions)
        
        return canvas
    except Exception:
        return cv2.resize(image, (512, 512))

def _add_change_labels(image: np.ndarray, thresh: np.ndarray) -> np.ndarray:
    """
    Add intelligent labels to change detection overlay.
    Analyzes change patterns to provide contextual information.
    """
    try:
        result = image.copy()
        
        # Calculate change statistics
        change_pixels = np.sum(thresh > 0)
        total_pixels = thresh.size
        change_percentage = (change_pixels / total_pixels) * 100
        
        # Find contours for spatial analysis
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        major_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]
        
        # Determine change type based on patterns
        if change_percentage > 15:
            main_label = "Major Land Use Change"
            color = (0, 0, 255)  # Red
        elif change_percentage > 8:
            main_label = "Moderate Development"
            color = (0, 165, 255)  # Orange
        elif change_percentage > 3:
            main_label = "Minor Changes Detected"
            color = (0, 255, 255)  # Yellow
        else:
            main_label = "Minimal Change"
            color = (0, 255, 0)  # Green
        
        # Add main label at top
        cv2.putText(result, main_label, (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        
        # Add specific labels based on change distribution
        if len(major_contours) > 5:
            cv2.putText(result, "Multiple Change Areas", (10, 60), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        elif len(major_contours) > 0:
            # Analyze largest contour position for context
            largest_contour = max(major_contours, key=cv2.contourArea)
            M = cv2.moments(largest_contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                
                # Position-based labeling
                if cy < 170:  # Top third
                    context_label = "Northern Region Change"
                elif cy > 340:  # Bottom third
                    context_label = "Southern Region Change"
                else:  # Middle
                    context_label = "Central Area Change"
                
                cv2.putText(result, context_label, (10, 60), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        # Add change percentage
        cv2.putText(result, f"Change: {change_percentage:.1f}%", (10, 490), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        return result
    except Exception:
        return image

def _add_contour_labels(image: np.ndarray, label_positions: list) -> np.ndarray:
    """
    Add labels to contour visualization based on change area sizes.
    """
    try:
        result = image.copy()
        
        # Sort by area (largest first)
        label_positions.sort(key=lambda x: x[2], reverse=True)
        
        for i, (cx, cy, area) in enumerate(label_positions[:3]):  # Label top 3 changes
            if area > 1000:
                label = "Major Change"
                color = (0, 0, 255)  # Red
            elif area > 500:
                label = "Urban Expansion"
                color = (0, 165, 255)  # Orange
            else:
                label = "Development"
                color = (0, 255, 255)  # Yellow
            
            # Add label with background for readability
            label_text = f"{label} ({int(area)}px)"
            text_size = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)[0]
            
            # Background rectangle
            cv2.rectangle(result, (cx-5, cy-text_size[1]-5), 
                         (cx+text_size[0]+5, cy+5), (0, 0, 0), -1)
            
            # Text
            cv2.putText(result, label_text, (cx, cy), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        
        return result
    except Exception:
        return image

def get_change_interpretation_message(change_percentage: float, contour_count: int = 0) -> str:
    """
    Generate intelligent change detection message based on analysis.
    Provides faculty-friendly interpretation of detected changes.
    """
    try:
        if change_percentage > 20:
            return "🚨 Significant land use transformation detected - substantial anthropogenic landscape modification observed"
        elif change_percentage > 12:
            return "⚠️ Notable development activity documented - measurable infrastructure expansion patterns identified"
        elif change_percentage > 8:
            return "📊 Moderate landscape modification observed - systematic development patterns documented"
        elif change_percentage > 5:
            return "🔍 Minor landscape changes detected - limited-scale development activity observed"
        elif change_percentage > 2:
            return "📈 Subtle environmental variation documented - natural fluctuation or minimal anthropogenic influence"
        else:
            return "✅ Stable landscape conditions maintained - no significant spatial changes detected"
    except Exception:
        return "📊 Comprehensive change detection analysis completed"

def add_change_legend(image: np.ndarray) -> np.ndarray:
    """
    Add professional legend to change detection visualization.
    Shows clear color coding for change/no-change areas.
    """
    try:
        result = image.copy()
        h, w = result.shape[:2]
        
        # Legend background (semi-transparent)
        legend_height = 80
        legend_width = 200
        legend_x = w - legend_width - 10
        legend_y = 10
        
        # Create legend background
        overlay = result.copy()
        cv2.rectangle(overlay, (legend_x, legend_y), 
                     (legend_x + legend_width, legend_y + legend_height), 
                     (0, 0, 0), -1)
        result = cv2.addWeighted(result, 0.8, overlay, 0.2, 0)
        
        # Legend border
        cv2.rectangle(result, (legend_x, legend_y), 
                     (legend_x + legend_width, legend_y + legend_height), 
                     (255, 255, 255), 2)
        
        # Legend title
        cv2.putText(result, "CHANGE LEGEND", (legend_x + 10, legend_y + 20), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # Red circle for change
        cv2.circle(result, (legend_x + 20, legend_y + 40), 8, (0, 0, 255), -1)
        cv2.putText(result, "Red = Change", (legend_x + 35, legend_y + 45), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
        
        # Green circle for no change
        cv2.circle(result, (legend_x + 20, legend_y + 60), 8, (0, 255, 0), -1)
        cv2.putText(result, "Green = No change", (legend_x + 35, legend_y + 65), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
        
        return result
    except Exception:
        return image

def create_enhanced_change_overlay(image: np.ndarray, thresh: np.ndarray, change_percentage: float) -> np.ndarray:
    """
    Create enhanced change overlay with legend and intelligent message.
    Combines all visual elements for professional presentation.
    """
    try:
        # Start with the change heatmap
        result = get_change_heatmap(image, thresh)
        
        # Add the legend
        result = add_change_legend(result)
        
        # Add intelligent interpretation message
        message = get_change_interpretation_message(change_percentage)
        
        # Add message at bottom with background for readability
        h, w = result.shape[:2]
        message_y = h - 30
        
        # Message background
        text_size = cv2.getTextSize(message, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
        cv2.rectangle(result, (10, message_y - text_size[1] - 10), 
                     (text_size[0] + 20, message_y + 10), (0, 0, 0), -1)
        
        # Message text
        cv2.putText(result, message, (15, message_y), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        return result
    except Exception:
        return cv2.resize(image, (512, 512))
    """
    Create side-by-side comparison: Original + Overlay.
    Shows before/after with change overlay for clear visualization.
    """
    try:
        # Resize images to consistent size
        img1_resized = cv2.resize(image1, (400, 400))
        img2_resized = cv2.resize(image2, (400, 400))
        thresh_resized = cv2.resize(thresh, (400, 400))
        
        # Create overlay on second image
        overlay = img2_resized.copy()
        overlay[thresh_resized > 0] = [0, 0, 255]  # Red for changes
        result_overlay = cv2.addWeighted(img2_resized, 0.6, overlay, 0.4, 0)
        
        # Add labels to images
        img1_labeled = img1_resized.copy()
        cv2.putText(img1_labeled, "BEFORE", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
        
        result_labeled = result_overlay.copy()
        cv2.putText(result_labeled, "AFTER + CHANGES", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
        
        # Calculate and add change statistics
        change_pixels = np.sum(thresh_resized > 0)
        total_pixels = thresh_resized.size
        change_percentage = (change_pixels / total_pixels) * 100
        
        cv2.putText(result_labeled, f"Change: {change_percentage:.1f}%", (10, 370), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        
        # Combine side by side
        comparison = np.hstack([img1_labeled, result_labeled])
        
        return comparison
    except Exception:
        # Fallback: simple side-by-side
        img1_resized = cv2.resize(image1, (400, 400))
        img2_resized = cv2.resize(image2, (400, 400))
        return np.hstack([img1_resized, img2_resized])

def create_change_comparison(image1: np.ndarray, image2: np.ndarray, thresh: np.ndarray) -> np.ndarray:
    """
    Create side-by-side comparison: Original + Overlay.
    Shows before/after with change overlay for clear visualization.
    """
    try:
        # Resize images to consistent size
        img1_resized = cv2.resize(image1, (400, 400))
        img2_resized = cv2.resize(image2, (400, 400))
        thresh_resized = cv2.resize(thresh, (400, 400))
        
        # Create overlay on second image
        overlay = img2_resized.copy()
        overlay[thresh_resized > 0] = [0, 0, 255]  # Red for changes
        result_overlay = cv2.addWeighted(img2_resized, 0.6, overlay, 0.4, 0)
        
        # Add labels to images
        img1_labeled = img1_resized.copy()
        cv2.putText(img1_labeled, "BEFORE", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
        
        result_labeled = result_overlay.copy()
        cv2.putText(result_labeled, "AFTER + CHANGES", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
        
        # Calculate and add change statistics
        change_pixels = np.sum(thresh_resized > 0)
        total_pixels = thresh_resized.size
        change_percentage = (change_pixels / total_pixels) * 100
        
        cv2.putText(result_labeled, f"Change: {change_percentage:.1f}%", (10, 370), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        
        # Combine side by side
        comparison = np.hstack([img1_labeled, result_labeled])
        
        return comparison
    except Exception:
        # Fallback: simple side-by-side
        img1_resized = cv2.resize(image1, (400, 400))
        img2_resized = cv2.resize(image2, (400, 400))
        return np.hstack([img1_resized, img2_resized])


def get_change_scale(change_percentage: float) -> dict:
    """
    Return a clear impact-scale classification for a change percentage.

    Scale:
        < 5%   → Minor
        5–15%  → Moderate
        > 15%  → Significant

    Returns a dict with keys: label, emoji, color, description, recommendation
    """
    try:
        if change_percentage < 5:
            return {
                "label":          "Minor",
                "emoji":          "🟢",
                "color":          "success",
                "range":          "< 5%",
                "description":    "Minimal landscape modification — consistent with natural seasonal variation",
                "recommendation": "Routine monitoring sufficient; no immediate intervention required",
            }
        elif change_percentage <= 15:
            return {
                "label":          "Moderate",
                "emoji":          "🟡",
                "color":          "warning",
                "range":          "5–15%",
                "description":    "Measurable landscape transformation — indicative of localised development activity",
                "recommendation": "Continued observation recommended; assess drivers of change",
            }
        else:
            return {
                "label":          "Significant",
                "emoji":          "🔴",
                "color":          "error",
                "range":          "> 15%",
                "description":    "Substantial spatial transformation detected — anthropogenic or major ecological event likely",
                "recommendation": "Detailed field investigation and conservation assessment advised",
            }
    except Exception:
        return {
            "label":          "Unknown",
            "emoji":          "⬜",
            "color":          "info",
            "range":          "N/A",
            "description":    "Change scale could not be determined",
            "recommendation": "Verify input data and re-run analysis",
        }
