# import cv2
# import os
# import glob
# import random
# import shutil
# import argparse
# import numpy as np
# from PyQt5.QtCore import QObject, pyqtSignal

# class ImageProcessor(QObject):
    # progress_resize = pyqtSignal(int)
    # progress_sketch = pyqtSignal(int)
    # progress_combine = pyqtSignal(int)
    # progress_split = pyqtSignal(int)

    # def __init__(self, color_folder, output_folder, size, split_ratio, remove_process_files):
        # self.color_folder = color_folder
        # self.output_folder = output_folder
        # self.size = size
        # self.split_ratio = split_ratio
        # self.remove_process_files = remove_process_files

    # def resize_image(self, image, size):
        # # Resize the image to the desired size
        # resized_image = cv2.resize(image, (size, size))
        # return resized_image

    # def resize_image_folder(self, input_folder, output_folder, size):
        # # Create the output folder if it doesn't exist
        # if not os.path.exists(output_folder):
            # os.makedirs(output_folder)

        # # Get a list of image files in the input folder
        # image_files = glob.glob(os.path.join(input_folder, "*/*.jpg")) + glob.glob(os.path.join(input_folder, "*/*.png"))
        # current_image = 0
        # total_images = len(image_files)
        # # Loop through each file in the image_files list
        # for image_path in image_files:
            # # Read the image
            # image = cv2.imread(image_path)

            # # Resize the image
            # resized_image = self.resize_image(image, size)

            # # Get the filename from the image path
            # _, filename = os.path.split(image_path)

            # # Save the resized image to the output folder
            # resized_image_path = os.path.join(output_folder, filename)
            # cv2.imwrite(resized_image_path, resized_image)

            # print(f"Resized {filename} and saved to output folder.")
            # # Calculate the progress percentage and emit the signal
            # progress = int((current_image / total_images) * 100)
            # self.progress_resize.emit(progress)
            # current_image += 1

    # def combine_images(self, original_folder, sketch_folder, output_folder):
        # # Create the output folder if it doesn't exist
        # if not os.path.exists(output_folder):
            # os.makedirs(output_folder)

        # # Get the list of image filenames in the original folder
        # original_images = os.listdir(original_folder)
        # sketch_images = os.listdir(sketch_folder)

        # # Loop through each file in the original folder
        # for filename in original_images:
            # # Read the original image
            # original_image_path = os.path.join(original_folder, filename)
            # # Get the corresponding sketch image 
            # sketch_filename = filename
            # sketch_image_path = os.path.join(sketch_folder, sketch_filename)

            # # Read the original image
            # original_image = cv2.imread(original_image_path)
            # # Read the sketch image
            # sketch_image = cv2.imread(sketch_image_path)

            # # Combine the original and sketch images horizontally
            # combined_image = cv2.hconcat([original_image, sketch_image])

            # # Save the combined image to the output folder
            # combined_filename = filename.replace(".", "_combined.")
            # combined_image_path = os.path.join(output_folder, combined_filename)
            # cv2.imwrite(combined_image_path, combined_image)

            # print(f"Combined {filename} and saved to {output_folder}.")

    # def split_dataset(self, input_folder, train_folder, val_folder, split_ratio):
        # # Create the train and validation folders if they don't exist
        # if not os.path.exists(train_folder):
            # os.makedirs(train_folder)
        # if not os.path.exists(val_folder):
            # os.makedirs(val_folder)

        # # Get the list of image filenames in the input folder
        # image_files = os.listdir(input_folder)

        # # Shuffle the image files randomly
        # random.shuffle(image_files)

        # # Calculate the number of images for the train and validation sets based on the split ratio
        # num_images = len(image_files)
        # num_train = int(num_images * split_ratio)
        # num_val = num_images - num_train

        # # Split the images into train and validation sets
        # train_images = image_files[:num_train]
        # val_images = image_files[num_train:]

        # # Copy the train images to the train folder
        # for filename in train_images:
            # src_path = os.path.join(input_folder, filename)
            # dst_path = os.path.join(train_folder, filename)
            # shutil.copy(src_path, dst_path)

        # # Copy the validation images to the validation folder
        # for filename in val_images:
            # src_path = os.path.join(input_folder, filename)
            # dst_path = os.path.join(val_folder, filename)
            # shutil.copy(src_path, dst_path)

        # print("Dataset split into train and validation sets.")

    # def color_to_sketch(self, color_folder, sketch_folder):
        # # Create the sketch folder if it doesn't exist
        # if not os.path.exists(sketch_folder):
            # os.makedirs(sketch_folder)

        # # Loop through each file in the color folder
        # for filename in os.listdir(color_folder):
            # # Read the color image
            # color_image_path = os.path.join(color_folder, filename)
            # color_image = cv2.imread(color_image_path)

            # # Convert the color image to grayscale (sketch)
            # gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

            # # Save the grayscale image as the sketch image
            # sketch_filename = filename
            # sketch_image_path = os.path.join(sketch_folder, sketch_filename)
            # cv2.imwrite(sketch_image_path, gray_image)

            # print(f"Converted {filename} to sketch and saved to sketch folder.")

    # def run(self):
        # # Create the in_process folder if it doesn't exist
        # in_process_folder = "processing"
        # if not os.path.exists(in_process_folder):
            # os.makedirs(in_process_folder)

        # # Create the resized folder if it doesn't exist
        # resized_images_folder = os.path.join(in_process_folder, "_resized")
        # if not os.path.exists(resized_images_folder):
            # os.makedirs(resized_images_folder)

        # # Resize the images in the color folder and save them to the output folder
        # self.resize_image_folder(self.color_folder, resized_images_folder, self.size)

        # # Create the sketch folder if it doesn't exist
        # sketch_images_folder = os.path.join(in_process_folder, "_sketched")
        # if not os.path.exists(sketch_images_folder):
            # os.makedirs(sketch_images_folder)

        # # Convert color images to sketch
        # self.color_to_sketch(resized_images_folder, sketch_images_folder)

        # # Create the combined folder if it doesn't exist
        # combined_images_folder = os.path.join(in_process_folder, "_combined")
        # if not os.path.exists(combined_images_folder):
            # os.makedirs(combined_images_folder)

        # # Combine the resized color and sketch images
        # self.combine_images(resized_images_folder, sketch_images_folder, combined_images_folder)

        # # Split the dataset into train and validation sets
        # train_folder = os.path.join(self.output_folder, "train")
        # val_folder = os.path.join(self.output_folder, "val")
        # self.split_dataset(combined_images_folder, train_folder, val_folder, self.split_ratio)

        # if self.remove_process_files:
            # shutil.rmtree(in_process_folder)


# if __name__ == "__main__":
    # # Create the command-line argument parser
    # parser = argparse.ArgumentParser(description="Script to resize, combine, and split a folder of images.")
    # parser.add_argument("--color-folder", type=str, help="Path to the folder containing color images.", required=True)
    # parser.add_argument("--output-folder", type=str, help="Path to the output folder for combined images.", default="output_dataset")
    # parser.add_argument("--resize", type=int, help="Desired square size for resized images.", default=450)
    # parser.add_argument("--split-ratio", type=float, help="Split ratio (between 0 and 1) for train and validation sets.", default=0.8)
    # parser.add_argument("--clean-process", type=bool, help="Remove the process folder after finishing the dataset.", default=False)

    # # Parse the command-line arguments
    # args = parser.parse_args()

    # # Create an instance of the ImageProcessor class with the provided arguments
    # processor = ImageProcessor(args.color_folder, args.output_folder, args.resize, args.split_ratio, args.clean_process)

    # # Execute the image processing operations
    # processor.run()
    
import cv2
import os
import glob
import random
import shutil
import argparse
import numpy as np
from PyQt5.QtCore import QObject, pyqtSignal

class ImageProcessor(QObject):
    progress_filter = pyqtSignal(int)
    progress_resize = pyqtSignal(int)
    progress_sketch = pyqtSignal(int)
    progress_combine = pyqtSignal(int)
    progress_split = pyqtSignal(int)
    process_name = ''
    
    def __init__(self, color_folder, filter_list, output_folder, size, split_ratio, remove_process_files):
        super().__init__()  # Call the __init__ method of the QObject superclass
        self.color_folder = color_folder
        self.filter_list = filter_list
        self.output_folder = output_folder
        self.size = size
        self.split_ratio = split_ratio
        self.remove_process_files = remove_process_files
        
    def filter_and_delete_images(self, in_folder, strings, out_folder):
        # Get the list of image filenames in the folder
        # Get a list of image files in the input folder
        images_to_filter = glob.glob(os.path.join(in_folder, "*/*.jpg"))
        current_image = 1
        total_images = len(images_to_filter)
        # Loop through each file in the folder
        for image_path in images_to_filter:

            # Get the filename from the image path
            _, filename = os.path.split(image_path)
            # Check if any of the strings exist in the filename
            if any(string in filename for string in strings):
                print(f"Filtered out {filename} !")
            else:
                inp = image_path
                outp = os.path.join(out_folder, filename)
                print(inp)
                print(outp)
                shutil.copy(inp,outp)
                
            # Calculate the progress percentage and emit the signal
            progress = int((current_image / total_images) * 100)
            self.progress_filter.emit(progress)
            current_image += 1
                

    def resize_image(self, image, size):
        # Resize the image to the desired size
        resized_image = cv2.resize(image, (size, size))
        return resized_image

    def resize_image_folder(self, input_folder, output_folder, size):
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Get a list of image files in the input folder
        image_files = glob.glob(os.path.join(input_folder, "*.jpg"))
        current_image = 1
        total_images = len(image_files)
        # Loop through each file in the image_files list
        for image_path in image_files:
            # Read the image
            image = cv2.imread(image_path)

            # Resize the image
            resized_image = self.resize_image(image, size)

            # Get the filename from the image path
            _, filename = os.path.split(image_path)

            # Save the resized image to the output folder
            resized_image_path = os.path.join(output_folder, filename)
            cv2.imwrite(resized_image_path, resized_image)

            print(f"Resized {filename} and saved to output folder.")
            # Calculate the progress percentage and emit the signal
            progress = int((current_image / total_images) * 100)
            self.progress_resize.emit(progress)
            current_image += 1

    def combine_images(self, original_folder, sketch_folder, output_folder):
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Get the list of image filenames in the original folder
        original_images = os.listdir(original_folder)
        sketch_images = os.listdir(sketch_folder)
        current_image = 1
        total_images = len(original_images)
        # Loop through each file in the original folder
        for filename in original_images:
            # Read the original image
            original_image_path = os.path.join(original_folder, filename)
            # Get the corresponding sketch image 
            sketch_filename = filename
            sketch_image_path = os.path.join(sketch_folder, sketch_filename)

            # Read the original image
            original_image = cv2.imread(original_image_path)
            # Read the sketch image
            sketch_image = cv2.imread(sketch_image_path)

            # Combine the original and sketch images horizontally
            combined_image = cv2.hconcat([original_image, sketch_image])

            # Save the combined image to the output folder
            combined_filename = filename.replace(".", "_combined.")
            combined_image_path = os.path.join(output_folder, combined_filename)
            cv2.imwrite(combined_image_path, combined_image)

            print(f"Combined {filename} and saved to {output_folder}.")
            # Emit the progress signal
            progress = int((current_image / total_images) * 100)
            self.progress_combine.emit(progress)
            current_image += 1

    def split_dataset(self, input_folder, train_folder, val_folder, split_ratio):
        # Create the train and validation folders if they don't exist
        if not os.path.exists(train_folder):
            os.makedirs(train_folder)
        if not os.path.exists(val_folder):
            os.makedirs(val_folder)

        # Get the list of image filenames in the input folder
        image_files = os.listdir(input_folder)

        # Shuffle the image files randomly
        random.shuffle(image_files)

        # Calculate the number of images for the train and validation sets based on the split ratio
        num_images = len(image_files)
        num_train = int(num_images * split_ratio)
        num_val = num_images - num_train

        # Split the images into train and validation sets
        train_images = image_files[:num_train]
        val_images = image_files[num_train:]
        
        
        # Copy the train images to the train folder       
        current_image = 1
        total_images = len(train_images)
        for filename in train_images:
            src_path = os.path.join(input_folder, filename)
            dst_path = os.path.join(train_folder, filename)
            shutil.copy(src_path, dst_path)
            # Emit the progress signal
            progress = int((current_image / total_images) * 100)
            self.progress_split.emit(progress)
            current_image += 1
            
       # Copy the validation images to the validation folder 
        current_image = 1
        total_images = len(val_images)
        for filename in val_images:
            src_path = os.path.join(input_folder, filename)
            dst_path = os.path.join(val_folder, filename)
            shutil.copy(src_path, dst_path)
            progress = int((current_image / total_images) * 100)
            self.progress_split.emit(progress)
            current_image += 1

        print("Dataset split into train and validation sets.")

        
    def color_to_sketch(self, input_folder, output_folder):
        # Create the sketch folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            
        # get images
        images_to_sketch = os.listdir(input_folder)
        
        # set current and total images int for statusbar
        current_image = 1
        total_images = len(images_to_sketch)
        # Loop through each file in the color folder
        for filename in images_to_sketch:
            # Read the color image
            color_image_path = os.path.join(input_folder, filename)
            color_image = cv2.imread(color_image_path)

            # Convert the color image to grayscale (sketch)
            gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

            # Save the grayscale image as the sketch image
            sketch_filename = filename
            sketch_image_path = os.path.join(output_folder, sketch_filename)
            cv2.imwrite(sketch_image_path, gray_image)

            print(f"Converted {filename} to sketch and saved to sketch folder.")
            # Emit the progress signal
            progress = int((current_image / total_images) * 100)
            # emit status
            self.progress_sketch.emit(progress)
            current_image += 1

    def run(self):
        # Create the in_process folder if it doesn't exist
        in_process_folder = "processing"
        if not os.path.exists(in_process_folder):
            os.makedirs(in_process_folder)

        # Create the filtered folder if it doesn't exist
        filtered_images_folder = os.path.join(in_process_folder, "_filtered")
        if not os.path.exists(filtered_images_folder):
            os.makedirs(filtered_images_folder)

        # Filter unwanted images
        self.filter_and_delete_images(self.color_folder, self.filter_list, filtered_images_folder)

        # Create the resized folder if it doesn't exist
        resized_images_folder = os.path.join(in_process_folder, "_resized")
        if not os.path.exists(resized_images_folder):
            os.makedirs(resized_images_folder)

        # Resize the filtered images in the filtered_images_folder and save them to the output folder
        self.resize_image_folder(filtered_images_folder, resized_images_folder, self.size)

        # Create the sketch folder if it doesn't exist
        sketch_images_folder = os.path.join(in_process_folder, "_sketched")
        if not os.path.exists(sketch_images_folder):
            os.makedirs(sketch_images_folder)

        # Convert color images to sketch
        self.color_to_sketch(resized_images_folder, sketch_images_folder)

        # Create the combined folder if it doesn't exist
        combined_images_folder = os.path.join(in_process_folder, "_combined")
        if not os.path.exists(combined_images_folder):
            os.makedirs(combined_images_folder)

        # Combine the resized color and sketch images
        self.combine_images(resized_images_folder, sketch_images_folder, combined_images_folder)

        # Split the dataset into train and validation sets
        train_folder = os.path.join(self.output_folder, "train")
        val_folder = os.path.join(self.output_folder, "val")
        self.split_dataset(combined_images_folder, train_folder, val_folder, self.split_ratio)

        if self.remove_process_files:
            shutil.rmtree(in_process_folder)
        # Emit the progress signal
        self.progress_combine.emit(100)


if __name__ == "__main__":
    # Create the command-line argument parser
    parser = argparse.ArgumentParser(description="Script to resize, combine, and split a folder of images.")
    parser.add_argument("--color-folder", type=str, help="Path to the folder containing color images.", required=True)
    parser.add_argument("--output-folder", type=str, help="Path to the output folder for combined images.", default="output_dataset")
    parser.add_argument("--resize", type=int, help="Desired square size for resized images.", default=450)
    parser.add_argument("--split-ratio", type=float, help="Split ratio (between 0 and 1) for train and validation sets.", default=0.8)
    parser.add_argument("--clean-process", type=bool, help="Remove the process folder after finishing the dataset.", default=False)

    # Parse the command-line arguments
    args = parser.parse_args()

    # Create an instance of the ImageProcessor class with the provided arguments
    processor = ImageProcessor(args.color_folder, args.output_folder, args.resize, args.split_ratio, args.clean_process)

    # Connect the progress signals to update the progress in the GUI
    processor.progress_resize.connect(update_resize_progress)
    processor.progress_sketch.connect(update_sketch_progress)
    processor.progress_combine.connect(update_combine_progress)
    processor.progress_split.connect(update_split_progress)

    # Execute the image processing operations
    processor.run()
