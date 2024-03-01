#!/usr/bin/env python3
# This Python script adds caption to image files using pillow

import os
import sys
import argparse
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps


def add_caption(directory):
    # Open the desired Image you want to add text on
    files = os.listdir(directory)
    for filename in files:
        full_name = os.path.join(directory, filename)
        # Check if the current file is a regular file (not a directory)
        if os.path.isfile(full_name):
            print(full_name)

            try:
                i = Image.open(full_name)
            except IOError:
                continue
            number = int(full_name.split(' ')[1].split('.')[0])
            years_ago = (len(files) - number) * 100
            if years_ago > 1950:
                caption = "År: " + str(years_ago - 1950) + " f.Kr"
            else:
                caption = "År: " + str(1950 - years_ago)
            print(caption)

            i = ImageOps.exif_transpose(i)
            # Call draw Method to add 2D graphics in an image
            Im = ImageDraw.Draw(i)
            mf = ImageFont.truetype('Lato-Black.ttf', 35)
            # Add Text to an image
            Im.text((500, 150), caption, fill=(0, 0, 0), font=mf)

            # Display edited image
            # i.show()
            # Save the edited image
            new_filename = filename.split('.')[0] + "_captioned." + filename.split('.')[1]
            new_fullname = os.path.join(directory+"/captioned/", new_filename)
            print(new_fullname)
            i.save(new_fullname)


def run(args):
    parser = argparse.ArgumentParser(description='Add caption to imagefiles in the specified directory')
    parser.add_argument('-d', '--directory', metavar='S', required=True,
                        help='The directory where the image files are located')
    args = parser.parse_args()
    path = os.path.join(args.directory, 'captioned')
    os.mkdir(path)
    add_caption(args.directory)


if __name__ == '__main__':
    run(sys.argv)