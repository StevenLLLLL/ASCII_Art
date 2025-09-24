from PIL import Image
import cv2
from tqdm import tqdm
import numpy

chars = "　·一二田国黑"

img = Image.open("test.png")
gray_img = img.convert("L")
width = 100
w, h = gray_img.size
height = int(h * (width / w))
resized_img = gray_img.resize((width, height))

resized_img.save("resized_test.png")
