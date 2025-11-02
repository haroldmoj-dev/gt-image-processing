import os
from PIL import Image

def resize(input_folder, scale_factor=10):
    print("------------------------")
    os.makedirs(output_folder, exist_ok=True)
    valid_extensions = (".png", ".jpg", ".jpeg")
    cnt = 0

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_extensions):
            
            input_path = os.path.join(input_folder, filename)

            img = Image.open(input_path)
            new_width = int(img.width * scale_factor)
            new_height = int(img.height * scale_factor)
            resized = img.resize((new_width, new_height), Image.NEAREST)
            print(f"[{cnt+1}] Resized: {filename}")

            os.remove(input_path)
            print(f"[{cnt+1}] Deleted original file: {filename}")

            resized.save(input_path)
            print(f"[{cnt+1}] Saved new file in: {input_path}")
            cnt = cnt + 1

    print(f"Done resizing {cnt} images!")

def crop(input_folder, output_folder):
    print("------------------------")
    valid_extensions = (".png", ".jpg", ".jpeg")
    cnt = 0

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_extensions):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            img = Image.open(input_path).convert("RGBA")

            pixels = img.getchannel("A") 
            bbox = pixels.getbbox()
            
            if bbox == (0, 0, img.width, img.height):
                print(f"Skipped cropping: {filename}")
                continue

            cropped = img.crop(bbox)
            print(f"[{cnt+1}] Cropped: {filename}")

            os.remove(input_path)
            print(f"[{cnt+1}] Deleted original file: {filename}")

            cropped.save(output_path)
            print(f"[{cnt+1}] Saved new file in: {output_path}")
            cnt = cnt + 1
    
    print(f"Done cropping {cnt} images!")

def rename(folder):
    valid_extensions = (".png", ".jpg", ".jpeg")

    for filename in os.listdir(folder):
        if filename.lower().endswith(valid_extensions):
            new_filename = filename.replace("1", "_1")

            old_path = os.path.join(folder, filename)
            new_path = os.path.join(folder, new_filename)

            os.rename(old_path, new_path)
            print(f"Renamed: {filename}")
    
    print("Done renaming!\n")

# --- For resizing and cropping---
input_folder = "input"
output_folder = ""

user_input = input("Is the weapon myth? [Y/N]: ")
if user_input in {"Y", "y"}:
    output_folder = "./images/ex_myth"
else:
    output_folder = "./images/ex"

resize(input_folder)
crop(input_folder, output_folder)

# --- For renaming ----
# folder = input("Input name of folder: ")
# rename(folder)

# --- For virtual environment ---
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

