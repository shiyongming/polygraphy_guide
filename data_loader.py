import os
from PIL import Image
import numpy as np

folder_path = 'calib_dataset_30/'
#folder_path = 'calib_dataset_1/'

def images():
    for image_path in os.listdir(folder_path):
        filename = folder_path + image_path
        image_array = np.asarray(Image.open(filename)).transpose(2, 0, 1)/ 255.0
        image_array = image_array.astype(np.float32)
        image_array = image_array.reshape(-1,3,32,32)
        print(image_array)
        yield {"input_0": image_array}
