import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model('model.h5')

img = image.load_img('test_image.jpg', target_size=(64,64))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0

result = model.predict(img_array)

if result[0][0] > 0.5:
    print("Dog 🐶")
else:
    print("Cat 🐱")