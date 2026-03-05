"""
Shared PNG export helper used across tools.
Ensures output directories exist before saving.
"""

import os
from PIL.Image import Image as PILImage


def save_image(image: PILImage, output_dir: str, filename: str) -> str:
    """
    Save a PIL image to output_dir/filename.
    Creates output_dir if it does not exist.
    Returns the full saved path.
    """
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, filename)
    image.save(path)
    return path
