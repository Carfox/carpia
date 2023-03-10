import cv2
import numpy as np
from keras.models import load_model
model = load_model('gestos.h5')

def process_image():
        img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
        print("Image shape:", img.shape)
        img = cv2.resize(img, (320, 120))
        img = img.reshape((1, 120, 320, 1))
        img = img.astype('float32')
        img /= 255.0
        prediccion = model.predict(img)
        category = np.argmax(prediccion)
        return category
