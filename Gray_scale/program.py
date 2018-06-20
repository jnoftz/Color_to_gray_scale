import os
from tkinter import *
import numpy
import cv2
import sqlite3
from PIL import Image, ImageTk

'''
# TODO: 1: Implement Yield into piping the color code data back and forth.
        2: (DONE CLI not GUI)Change from hardcoded image to filedialog.askopenfilename.
        3: create_image needs to have % coded because the function does not support non hardcoded numbers.
        4: (DONE) Canvas Should be able to do % of screen I need to do some more reading on this function, if it does 
        not I need to code this before doing create_image issue.
        5: (DONE)Remove hard code for gray image and have it pull from the change_to_gray_scale class.
        6: Add comments to the code so it doesn't look like total shit. 
        7: (DONE)remove hard coded name from gray_img
'''


def main():

    image_path = locate_image()
    change_to_gray_scale(image_path)
    image_str = (image_path.strip(".jpg") + "_colorless.jpg")  # Added because imwrite returns bool and not an object.
    gray_image_name = os.path.split(image_str)[1]

    window = Tk()
    w = window.winfo_screenwidth()  # Gets the with of the screen.
    h = window.winfo_screenheight()  # Gets the height of the screen.

    window.geometry("%sx%s" % (w, h))  # String formatting to take the H & W of the screen to create the Canvas.
    w = Canvas(window, width=w, height=h)

    # open_button = Button(window, text="Open Image", command=display_image).pack()

    color_img = ImageTk.PhotoImage(Image.open(image_path))
    gray_img = ImageTk.PhotoImage(Image.open(gray_image_name))

    w.create_image(450, 400, image=color_img)
    w.create_image(1350, 400, image=gray_img)
    w.pack()

    window.mainloop()

# def display_image_window():

# def open_file():
#     filename = filedialog.askopenfilename(title='open')
#     return filename


def locate_image():
    path = input("What is the location of the image you would like to us? ")
    return os.path.abspath(path)


def display_slide_bar():
    pass


def save_color():
    pass


def save_gray_scale():
    pass


def change_to_color():
    pass


def change_to_gray_scale(path):
    color_image = path
    img = cv2.imread(color_image, 0)
    gray_img = cv2.imwrite(color_image.strip(".jpg") + "_colorless.jpg", img)
    return gray_img  # imwrite returns a bool and not an object. So I wrote a string format as a work around.


if __name__ == '__main__':
    main()
