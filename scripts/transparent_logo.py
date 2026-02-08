import sys
import subprocess

# Ensure Pillow is installed
try:
    from PIL import Image
    import numpy as np
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow", "numpy"])
    from PIL import Image
    import numpy as np

def remove_black_background(input_path, output_path):
    print(f"Processing {input_path}...")
    try:
        img = Image.open(input_path).convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            # Check if pixel is close to black (tolerance 30)
            if item[0] < 30 and item[1] < 30 and item[2] < 30:
                newData.append((item[0], item[1], item[2], 0)) # Fully transparent
            else:
                newData.append(item)

        img.putdata(newData)
        img.save(output_path, "PNG")
        print(f"Success! Saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

input_file = r"C:\Users\USER\.gemini\antigravity\brain\a128483d-5cd0-4f75-8590-120d3b9ca5b7\sercaia_logo_source_black_1770279385668.png"
output_file = r"C:\Users\USER\.gemini\antigravity\brain\a128483d-5cd0-4f75-8590-120d3b9ca5b7\sercaia_logo_transparent_v9.png"

remove_black_background(input_file, output_file)
