"""
Utility to stitch several images to create a collage of an image, without loss of quality.
Majority of logic and source code taken and modelled
into a Python script from: https://www.programmersought.com/article/2467117924/
"""

import PIL.Image as Image
import os

IMAGES_PATH = "./img/extended/"

# Image format
IMAGES_FORMAT = ['.png', '.PNG']

# The size of each small picture, if square
# IMAGE_SIZE = 4096

# The sizes of each small picture, if rectangular
IMAGE_SIZE_C = 1766
IMAGE_SIZE_R = 1043

IMAGE_ROW = 2
IMAGE_COLUMN = 2
IMAGE_SAVE_PATH = './img/final.png'


# Define image stitching function
def image_compose(image_names):
    """
    Function that creates a blank canvas and puts all the images
    onto it, one by one, depending upon the chosen rows, coloumns
    and each image's size.

    :param image_names: List of images to stitch
    :return: The stitched image saved to directory, and return None
    """

    # Create a new canvas on which all the images would be placed
    to_image = Image.new('RGBA', (IMAGE_COLUMN * IMAGE_SIZE_C, IMAGE_ROW * IMAGE_SIZE_R))

    # Loop through all pictures, paste each picture
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_SIZE_C, IMAGE_SIZE_R), Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE_C, (y - 1) * IMAGE_SIZE_R))

    return to_image.save(IMAGE_SAVE_PATH)  # save the new image


if __name__ == "__main__":
    # Get all image names under the photo collection address
    image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
                   os.path.splitext(name)[1] == item]

    # Simple judgment on the number of parameters and the size of the actual picture set
    if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
        raise ValueError(
            "The number of parameters and the number of requirements for the composite image does not match!")

    image_compose(image_names)
