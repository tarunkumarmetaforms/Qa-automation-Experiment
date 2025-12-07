"""Base64 encoding/decoding utilities for browser screenshots"""

import base64
import io
import numpy as np
from PIL import Image


def image_to_png_base64_url(
    image: np.ndarray | Image.Image, add_data_prefix: bool = False
) -> str:
    """Convert an image to a PNG base64-encoded string.

    Args:
        image: NumPy array or PIL Image
        add_data_prefix: Whether to add 'data:image/png;base64,' prefix

    Returns:
        Base64-encoded PNG string
    """
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image.astype('uint8'), 'RGB')

    buffered = io.BytesIO()
    image.save(buffered, format='PNG')
    img_str = base64.b64encode(buffered.getvalue()).decode()

    if add_data_prefix:
        return f'data:image/png;base64,{img_str}'
    return img_str


def png_base64_url_to_image(png_base64_url: str) -> Image.Image:
    """Convert a base64-encoded PNG string to a PIL Image.

    Args:
        png_base64_url: Base64-encoded PNG string (with or without data URL prefix)

    Returns:
        PIL Image object
    """
    # Remove data URL prefix if present
    if png_base64_url.startswith('data:image'):
        png_base64_url = png_base64_url.split(',', 1)[1]

    # Decode base64 to bytes
    img_data = base64.b64decode(png_base64_url)

    # Convert to PIL Image
    return Image.open(io.BytesIO(img_data))

