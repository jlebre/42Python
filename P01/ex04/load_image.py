from PIL import Image
import numpy as np

def ft_load(path: str) -> np.array:
    """
    Load image
    """
    try:
        img = Image.open(path)
        img = img.convert("RGB")
        img_arr = np.array(img)

        print(f"The shape of image is: {img_arr.shape}")

        return img_arr

    except FileNotFoundError:
        print("File not found")
    except Exception as error:
        print(f"Error: {error}")
