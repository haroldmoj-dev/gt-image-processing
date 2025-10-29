import os
from PIL import Image

def resize(input_folder, output_folder, scale_factor=10):
    os.makedirs(output_folder, exist_ok=True)
    valid_extensions = (".png", ".jpg", ".jpeg")

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_extensions):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Open and resize
            img = Image.open(input_path)
            new_width = int(img.width * scale_factor)
            new_height = int(img.height * scale_factor)
            resized = img.resize((new_width, new_height), Image.NEAREST)

            resized.save(output_path)
            os.remove(input_path)
            print(f"Resized and deleted: {filename}")

    print("Done resizing!\n")

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

def crop(folder):
    valid_extensions = (".png", ".jpg", ".jpeg")

    for filename in os.listdir(folder):
        if filename.lower().endswith(valid_extensions):
            image_path = os.path.join(folder, filename)
            img = Image.open(image_path).convert("RGBA")

            pixels = img.getchannel("A") 
            bbox = pixels.getbbox()
            
            if bbox == (0, 0, img.width, img.height):
                print(f"Skipped cropping: {filename}")
                continue

            cropped = img.crop(bbox)
            cropped.save(image_path)
            print(f"Cropped: {filename}")
    
    print("Done cropping!\n")

# --- For resizing and cropping---
input_folder = input("Name of input folder: ")
output_folder = input("Name of output folder: ")
resize(input_folder, output_folder)
crop(output_folder)

# --- For renaming ----
# folder = input("Input name of folder: ")
# rename(folder)

# --- For virtual environment ---
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

