from PIL import Image
import os
import requests
from io import BytesIO

# Function to optimize an image
def optimize_image(image_path, output_path, size=(800, 800), quality=85):
    with Image.open(image_path) as img:
        img.thumbnail(size)
        img.save(output_path, quality=quality)

# Directory containing images
image_dir = "tajweed-quran"
output_dir = "optimize-tajweed-quran"

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process each image
for filename in os.listdir(image_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(image_dir, filename)
        output_path = os.path.join(output_dir, filename)
        optimize_image(image_path, output_path)
