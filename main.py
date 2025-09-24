from PIL import Image, ImageEnhance, ImageFilter
import cv2
from tqdm import tqdm
import numpy

# 字符集, 从浅到深排列
CHARS = "   一丨丶丿乙亅二十丁七八九了人入刀力乃又三干于工土士才下上小大山川千口囗日月木水火之也女子寸巾乎手心户牛犬王田由甲申白目石舌立本朴加台去可司古布半交向佑左右吉名各同吏衣米耳肉舟见贝车言足里金长门雨鱼鸟黄黑龍龘"
CHARS = CHARS[::-1]  # 反转字符集, 使得浅色对应"密集"字符, 深色对应"稀疏"字符


def process_image(m):
    """
    1. 转灰度图, 2. 调整大小, 3. 增强对比度, 4. 锐化
    :param m: 未处理生图
    :return:
    """
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
    """
    灰度值转字符, 返回字符串
    :param m: 处理后的图片
    :return:
    """
    global CHARS
    pixels = m.load()
    w, h = m.size
    result = ""
    for i in range(h):
        line = ""
        for j in range(w):
            gray = pixels[j, i]
            idx = int(gray / 255 * (len(CHARS) - 1))  # 灰度值映射到字符集索引
            line += CHARS[idx]
        result += line + "\n"
    return result


img = Image.open("test4.jpg")
resizedImg = process_image(img)
final = pixel_to_chars(resizedImg)
with open("output2.txt", "w", encoding="utf-8") as f:
    f.write(final)



