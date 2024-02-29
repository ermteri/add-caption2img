# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps


def add_caption(directory):

    # Open the desired Image you want to add text on
    for filename in os.listdir(directory):
        full_name = os.path.join(directory, filename)
        # Check if the current file is a regular file (not a directory)
        if os.path.isfile(full_name):
            print(full_name)

            try:
                i = Image.open(full_name)
            except IOError:
                continue
            number = int(full_name.split(' ')[1].split('.')[0])
            years_ago = (81 - number) * 100
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    add_caption('./ingaro')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
