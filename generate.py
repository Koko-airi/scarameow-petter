import base64
import os

gif_path = "/Users/airi/.gemini/antigravity/scratch/scarameow-petter/scarameow.gif"
with open(gif_path, "rb") as f:
    gif_b64 = "data:image/gif;base64," + base64.b64encode(f.read()).decode("utf-8")

with open("/Users/airi/.gemini/antigravity/scratch/scarameow-petter/template.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace any previous placeholder or old image references
final_html = html.replace("__IMAGE_BASE64__", gif_b64)

scratch_file = "/Users/airi/.gemini/antigravity/scratch/scarameow-petter/index.html"
with open(scratch_file, "w", encoding="utf-8") as f:
    f.write(final_html)

artifact_file = "/Users/airi/.gemini/antigravity/brain/24616610-e6f6-4d6a-b4fb-040c79607b10/scarameow_petter.html"
with open(artifact_file, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Generated index.html and scarameow_petter.html with animated GIF (base64 len: {len(gif_b64)})!")
