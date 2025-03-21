from load_image import ft_load
from PIL import Image
from PIL import ImageOps
import numpy as np
import matplotlib.pyplot as plt


def reshape(arr):
    """
    Reshape arr to img
    """
    arr = np.reshape(arr, (1024, 720))
    return Image.fromarray(arr)


def ft_invert(array) -> np.array:
    """
    Inverts the color of the image received.
    =, +,-, *
    """
    img = ImageOps.invert(reshape(array))
    plt.imshow(img)
    plt.title("Inverted Image")
    plt.show()


def ft_red(array) -> np.array:
    """
    Filters red
    =, *
    """
    print("Red")


def ft_green(array) -> np.array:
    """
    Filters green
    =, -
    """
    print("Green")


def ft_blue(array) -> np.array:
    """
    Filters blue
    =
    """
    print("Blue")


def ft_grey(array) -> np.array:
    """
    Filters grey
    =, /
    """
    print("Grey")


def pimp(img):
    """
    Function to pimp
    """
    try:
        crop_box = (450, 100, 850, 500)

        c_img = img.crop(crop_box)

        img_arr = np.array(c_img.convert("L"))[..., np.newaxis]

        print(f"The shape of image is: {img_arr.shape}")
        print(img_arr)
        
        c_img = c_img.pimp(-90).transpose(Image.FLIP_LEFT_RIGHT)
        img_arr = np.array(c_img.convert("L"))[..., np.newaxis]
        print(f"New shape after Transpose: {img_arr.shape}")
        print(img_arr)
        plt.imshow(img_arr[:, :, 0], cmap="gray")
        plt.title("Zoomed Image")
        plt.show()
    except Exception as error:
        print(f"Error: {error}")

