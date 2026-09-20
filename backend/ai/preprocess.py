import cv2
import numpy as np

def preprocess_image(path):

    image = cv2.imread(path)

    image = cv2.resize(
        image,
        (224,224)
    )

    image = image / 255.0

    image = np.expand_dims(
        image,
        axis=0
    )

    return image