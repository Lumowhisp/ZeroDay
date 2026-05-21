#!/usr/bin/env python3
"""
Error Level Analysis (ELA) Prototype Script
DocShield AI — Phase 1 Proof-of-Concept

This script analyzes a JPEG image by resaving it at a known quality level
and calculating the absolute pixel difference between the original and 
the resaved version. Areas with different compression histories (i.e. tampered/spliced)
will display higher error levels (glowing pixels).
"""

import os
import sys
import numpy as np
from PIL import Image, ImageChops

def run_ela(image_path, quality=90, scale=15):
    """
    Performs Error Level Analysis on the target image.
    
    Parameters:
    - image_path (str): Path to the input image.
    - quality (int): JPEG quality to resave and compare (default: 90).
    - scale (int): Multiplication factor to amplify the differences (default: 15).
    """
    if not os.path.exists(image_path):
        print(f"Error: Input file '{image_path}' does not exist.")
        sys.exit(1)
        
    print(f"Processing: {image_path}")
    print(f"Parameters: Resave Quality = {quality}, Error Amplification Scale = {scale}")
    
    # 1. Open original image
    original = Image.open(image_path).convert('RGB')
    
    # Create temp filename for re-saved image
    temp_filename = f"temp_resaved_{quality}.jpg"
    
    try:
        # 2. Resave image at the specified JPEG quality
        original.save(temp_filename, 'JPEG', quality=quality)
        
        # 3. Open the re-saved image
        resaved = Image.open(temp_filename)
        
        # 4. Calculate absolute difference between original and resaved
        diff = ImageChops.difference(original, resaved)
        
        # 5. Extract extreme bounds to auto-scale if necessary, otherwise multiply by scale factor
        extrema = diff.getextrema()
        max_diff = max([ex[1] for ex in extrema])
        if max_diff == 0:
            max_diff = 1
            
        # Scale the difference image to enhance visibility
        # ELA heatmap = difference * scale
        ela_data = np.array(diff) * scale
        ela_data = np.clip(ela_data, 0, 255).astype(np.uint8)
        ela_image = Image.fromarray(ela_data)
        
        # Save ELA result
        output_filename = f"ela_result_{os.path.basename(image_path)}"
        ela_image.save(output_filename)
        print(f"Success! ELA heatmap saved to: {output_filename}")
        
    finally:
        # Clean up temporary file
        if os.path.exists(temp_filename):
            os.remove(temp_filename)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ela_demo.py <path_to_image> [quality] [scale]")
        print("Example: python ela_demo.py sample_doc.jpg 90 15")
        sys.exit(1)
        
    img_path = sys.argv[1]
    q = int(sys.argv[2]) if len(sys.argv) > 2 else 90
    s = int(sys.argv[3]) if len(sys.argv) > 3 else 15
    
    run_ela(img_path, q, s)
