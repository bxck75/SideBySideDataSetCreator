# SideBySideDataSetCreator
Processes a folder of images into a pix2pix sidebyside dataset of a train and validate folder.
The process:
            filters unwanted images with a list of strings, 
            resizes, 
            sketch clones,
            combines resized original and sketch sbs, 
            splits images into train and val folder

There is a simple Gui to set the params of the ImageProcessor.
ImageProcessingThread is wrapper around ImageProcessor to make the progress bars work.
make_sbs_image_set  houses the main application qtpy with mdiarea 
ImageProcessingApp is a mdiQwidget

Usage: python make_sbs_image_set.py

rough codei will revisit this and add more then only org->sketch
