from PIL import Image
import os

def merge_images(input_folder, output_path):
    row_merged_images = []

    for subfolder in sorted(os.listdir(input_folder)):
        subfolder_path = os.path.join(input_folder, subfolder)

        if os.path.isdir(subfolder_path):
            row_merged_image_path = os.path.join(subfolder_path, "row_merged.png")
            merge_row_images(subfolder_path, row_merged_image_path)
            row_merged_images.append(row_merged_image_path)

    merge_vertically(row_merged_images, output_path)
    print(f"Images merged successfully. Result saved at: {output_path}")
    for image_path in row_merged_images:
        os.remove(image_path)

def merge_row_images(input_folder, output_path):
    images = []

    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".png"):
            image_path = os.path.join(input_folder, filename)
            img = Image.open(image_path)
            images.append(img)

    total_width = sum(img.width for img in images)
    max_height = max(img.height for img in images)

    result_image = Image.new("RGBA", (total_width, max_height))

    x_offset = 0
    for img in images:
        result_image.paste(img, (x_offset, 0))
        x_offset += img.width

    result_image.save(output_path)

def merge_vertically(images, output_path):
    row_images = [Image.open(image) for image in images]

    max_width = max(img.width for img in row_images)
    total_height = sum(img.height for img in row_images)

    result_image = Image.new("RGBA", (max_width, total_height))

    y_offset = 0
    for img in row_images:
        result_image.paste(img, (0, y_offset))
        y_offset += img.height

    result_image.save(output_path)

input_folder = "Rows"
output_path = "final_output.png"

merge_images(input_folder, output_path)
