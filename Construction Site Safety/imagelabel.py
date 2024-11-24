import os

# Paths to your dataset directories
labels_dir = "C:\\Users\\venka\\OneDrive\\Documents\\GitHub\\Projects\\Construction Site Safety\\AI_ConstructionSiteMonitoring\\data\\train\\labels"  # Path to the directory containing label files
images_dir = "C:\\Users\\venka\\OneDrive\\Documents\\GitHub\\Projects\\Construction Site Safety\\AI_ConstructionSiteMonitoring\\data\\train\\images"  # Path to the directory containing image files

# Supported image extensions
image_extensions = {".jpg", ".jpeg", ".png", ".bmp"}

# Get a set of image file basenames (without extensions) in the images directory
image_basenames = {
    os.path.splitext(image)[0] for image in os.listdir(images_dir) if os.path.splitext(image)[1].lower() in image_extensions
}

# Iterate through label files and check if their corresponding image exists
for label_file in os.listdir(labels_dir):
    if label_file.endswith(".txt"):  # Ensure it's a label file
        label_basename = os.path.splitext(label_file)[0]
        if label_basename not in image_basenames:
            # If no corresponding image exists, delete the label file
            label_path = os.path.join(labels_dir, label_file)
            os.remove(label_path)
            print(f"Deleted label file: {label_path}")

print("Cleanup complete.")
