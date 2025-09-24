from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
import cv2
from tqdm import tqdm
import numpy

CHARS = "   一丨丶丿乙亅二十丁七八九了人入刀力乃又三干于工土士才下上小大山川千口囗日月木水火之也女子寸巾乎手心户牛犬王田由甲申白目石舌立本朴加台去可司古布半交向佑左右吉名各同吏衣米耳肉舟见贝车言足里金长门雨鱼鸟黄黑龍龘"
CHARS = CHARS[::-1]


def process_image(m):
    gray_img = m.convert("L")
    width = 50
    w, h = gray_img.size
    height = int(h * (width / w))
    resized_img = gray_img.resize((width, height))
    enhancer = ImageEnhance.Contrast(resized_img)
    resized_img = enhancer.enhance(1.5)
    resized_img = resized_img.filter(ImageFilter.SHARPEN)
    return resized_img


def pixel_to_chars(m):
    global CHARS
    pixels = m.load()
    w, h = m.size
    result = ""
    for i in range(h):
        line = ""
        for j in range(w):
            gray = pixels[j, i]
            idx = int(gray / 255 * (len(CHARS) - 1))
            line += CHARS[idx]
        result += line + "\n"
    return result


img = Image.open("test4.jpg")
resizedImg = process_image(img)
final = pixel_to_chars(resizedImg)
with open("output2.txt", "w", encoding="utf-8") as f:
    f.write(final)



