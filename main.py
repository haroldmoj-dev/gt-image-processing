import os
from PIL import Image

def resize(input_folder, output_folder, scale_factor):
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
            print(f"Resized and deleted: {filename}\n")

    print("Done resizing!")

def rename(folder):
    valid_extensions = (".png", ".jpg", ".jpeg")

    for filename in os.listdir(folder):
        if filename.lower().endswith(valid_extensions):
            new_filename = filename.replace("1", "_1")

            old_path = os.path.join(folder, filename)
            new_path = os.path.join(folder, new_filename)

            os.rename(old_path, new_path)
            print(f"Renamed: {filename}")
    
    print("Done renaming!")

# For resizing
input_folder = "input"
output_folder = "ex"
scale_factor = 10 
resize(input_folder, output_folder, scale_factor)
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# For renaming
# folder = input("Input name of folder: ")
# rename(folder)