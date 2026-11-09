import base64
import os

img_path = "/Users/airi/.gemini/antigravity/scratch/scarameow-petter/scarameow.png"
with open(img_path, "rb") as f:
    img_b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

print(f"Base64 length: {len(img_b64)}")
