from PIL import Image
import os

# Function to optimize and convert an image to WebP
def optimize_and_convert_to_webp(image_path, output_path, size=(800, 800), quality=90):
    with Image.open(image_path) as img:
        img.thumbnail(size)  # Resize the image
        # Save the image in WebP format
        webp_output_path = os.path.splitext(output_path)[0] + '.webp'
        img.save(webp_output_path, format='webp', quality=quality)

# Directory containing images
image_dir = "tajweed-quran"
output_dir = "optimized-webp-tajweed-quran"

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process each image
for filename in os.listdir(image_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(image_dir, filename)
        output_path = os.path.join(output_dir, filename)
        optimize_and_convert_to_webp(image_path, output_path)
