import tensorflow as tf
import numpy as np
import cv2

# Load a pre-trained object detection model
model = tf.keras.models.load_model('model.h5')

# Load an image
image = cv2.imread('image.jpg')

# Pre-process the image for the model
image = cv2.resize(image, (224, 224))
image = np.expand_dims(image, axis=0)

# Make predictions
predictions = model.predict(image)

# Count the number of squares in the image
num_squares = np.sum(predictions[0, :, :, 4] > 0.5)

print("Number of squares in the image: ", num_squares)
