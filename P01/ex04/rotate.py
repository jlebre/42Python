from load_image import ft_load
from PIL import Image
from PIL import ImageOps
import numpy as np
import matplotlib.pyplot as plt


def main():
    """
    main
    """
    try:
        path = "animal.jpeg"
        img = Image.open(path)
        rotate(img)
    except Exception as error:
        print(f"Error: {error}")

def rotate(img):
    """
    Function to rotate
    """
    try:
        crop_box = (450, 100, 850, 500)

        c_img = img.crop(crop_box)

        img_arr = np.array(c_img.convert("L"))[..., np.newaxis]

        print(f"The shape of image is: {img_arr.shape}")
        print(img_arr)
        
        c_img = c_img.rotate(-90).transpose(Image.FLIP_LEFT_RIGHT)
        img_arr = np.array(c_img.convert("L"))[..., np.newaxis]
        print(f"New shape after Transpose: {img_arr.shape}")
        print(img_arr)
        plt.imshow(img_arr[:, :, 0], cmap="gray")
        plt.title("Zoomed Image")
        plt.show()
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
