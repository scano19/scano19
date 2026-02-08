import sys
import subprocess

try:
    from PIL import Image, ImageFilter
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageFilter

def create_perfect_transparent(input_path, output_path):
    print(f"Processing {input_path}...")
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()
    
    newData = []
    # Aggressive threshold for black/dark colors
    threshold = 50 
    
    for item in datas:
        # Check standard RGB black
        if item[0] < threshold and item[1] < threshold and item[2] < threshold:
            newData.append((0, 0, 0, 0))
        else:
            newData.append(item)
            
    img.putdata(newData)
    
    # Optional: Smooth edges to avoid jagged pixelation
    # img = img.filter(ImageFilter.SMOOTH_MORE)
    
    img.save(output_path, "PNG")
    print(f"Saved clean transparent logo to {output_path}")

input_file = r"C:\Users\USER\.gemini\antigravity\brain\a128483d-5cd0-4f75-8590-120d3b9ca5b7\sercaia_logo_source_black_1770279385668.png"
output_file = r"C:\Users\USER\.gemini\antigravity\brain\a128483d-5cd0-4f75-8590-120d3b9ca5b7\sercaia_logo_final_v10.png"

create_perfect_transparent(input_file, output_file)
