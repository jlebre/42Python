from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def main():
    """
    main
    """
    path = "animal.jpeg"
    print(ft_load(path))
    try:
        img = Image.open(path)
        zoom(img)
    except Exception as error:
        print(f"Error: {error}")

def zoom(img):
    try:
        crop_box = (450, 100, 850, 500)

        c_img = img.crop(crop_box)

        img_arr = np.array(c_img.convert("L"))[..., np.newaxis]

        print(f"New shape after slicing: {img_arr.shape}")
        print(img_arr)
        plt.imshow(img_arr[:, :, 0], cmap="gray")
        plt.title("Zoomed Image")
        plt.show()
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()

# https://www.geeksforgeeks.org/python-pil-image-resize-method/
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html
# https://www.geeksforgeeks.org/how-to-display-an-image-in-grayscale-in-matplotlib/