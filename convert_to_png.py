from PIL import Image
import os
import pillow_heif

source_folder = "C:/Users/Pichau/Downloads/heic-folder/"
target_folder = "C:/Users/Pichau/Downloads/projetos-py/img-convertida"

if not os.path.exists(target_folder):
    os.makedirs(target_folder)
for filename in os.listdir(source_folder):

    if filename.lower().endswith(".heic"):
        # Construct full paths for source and target images
        source_path = os.path.join(source_folder, filename)
        target_path = os.path.join(
            target_folder, os.path.splitext(filename)[0] + ".png")
        heif_file = pillow_heif.open_heif(source_path)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",

        )
        image.save(target_path, format("png"))
        print(f"Converted '{filename}' to '{target_path}'.")
