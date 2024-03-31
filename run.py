import os
import subprocess

subprocess.check_call(["pip", "install", "Pillow"])
subprocess.check_call(["pip", "install", "pyzbar"])

from PIL import Image
from pyzbar.pyzbar import decode

source_directory = "Source"
if not os.path.exists(source_directory):
    os.makedirs(source_directory)

def read_barcodes_from_images(directory, output_directory):
    barcodes = []
    for filename in os.listdir(directory):
        image_path = os.path.join(directory, filename)
        image = Image.open(image_path)
        try:
            decoded_barcodes = decode(image)
            if len(decoded_barcodes) > 0:
                for barcode in decoded_barcodes:
                    barcode_data = barcode.data.decode("utf-8")
                    barcodes.append(barcode_data)
            else:
                output_path = os.path.join(output_directory, filename)
                image.save(output_path)
        except:
            output_path = os.path.join(output_directory, filename)
            image.save(output_path)
    return barcodes

def save_barcodes_to_file(barcodes, output_file):
    with open(output_file, "w") as file:
        for barcode in barcodes:
            file.write(barcode + "\n")

if __name__ == "__main__":
    images_directory = source_directory
    output_directory = "failed_images"
    output_file = "barcodes.txt"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    supported_formats = [".jpg", ".jpeg", ".png", ".gif"]

    barcodes = read_barcodes_from_images(images_directory, output_directory)
    save_barcodes_to_file(barcodes, output_file)