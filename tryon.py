import sys
import os
from PIL import Image

# 1. Setup paths to find the 'fashn_vton' package inside 'fashnvton/src'
project_root = os.getcwd()
fashn_src_path = os.path.join(project_root, "fashnvton", "src")
sys.path.append(fashn_src_path)

# 2. Import the correct class from the package
from fashn_vton.pipeline import TryOnPipeline

# 3. Initialize pipeline
weights_dir = os.path.join(project_root, "fashnvton", "weights")
# The class in your source is named TryOnPipeline
pipeline = TryOnPipeline(weights_dir=weights_dir, device="cpu")

# 4. Load your images
person = Image.open("WhatsApp Image 2026-03-11 at 12.11.41 PM.jpeg").convert("RGB")
garment = Image.open("Screenshot 2026-03-11 at 1.12.30 PM.png").convert("RGB")

# 5. Run try-on
print("🚀 Running Virtual Try-On (this may take a few minutes on CPU)...")
result = pipeline(
    person_image=person,
    garment_image=garment,
    category="one-pieces",  # "tops" | "bottoms" | "one-pieces"
)

# 6. Save output
result.images[0].save("output3.png")
print("✅ Done! Saved to output3.png")