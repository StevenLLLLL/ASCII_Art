from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont
from pathlib import Path
import cv2
from numpy.ma.extras import row_stack
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


def text_to_image(text, out_png, font_path=r"C:\Windows\Fonts\msyh.ttc", font_size=12, fg=(0, 0, 0), bg=(255, 255, 255), line_gap_ratio=0.0):
    # 读取文本文件
    lines = text.splitlines()
    if not lines:
        raise RuntimeError("内容为空")

    # 准备字体，测量单个字符尺寸
    font = ImageFont.truetype(font_path, font_size)
    bbox = font.getbbox("田")
    cw = max(1, bbox[2] - bbox[0])  # 字符宽度
    ch = max(1, bbox[3] - bbox[1])  # 字符高度

    # 计算画布尺寸
    cols = max(len(line) for line in lines)
    row = len(lines)
    gap = int(ch * line_gap_ratio)  # 行间距
    W = cw * cols
    H = (ch + gap) * row - gap

    # 绘制图像
    pic = Image.new("RGB", (W, H), bg)
    draw = ImageDraw.Draw(pic)
    y = 0
    for line in lines:
        draw.text((0, y), line, font=font, fill=fg)
        y += ch + gap

    # 直接返回函数
    return out_png


def process_vid(v):
    """
    读取视频, 并处理
    :param v: video name
    :return:
    """
    cap = cv2.VideoCapture(v)
    if not cap.isOpened():
        raise RuntimeError("无法打开视频文件")

    fps = cap.get(cv2.CAP_PROP_FPS) or 0.0
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) or 0
    print(f"FPS: {fps}, 总帧数: {total}")

    frame_count = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        frame_count += 1
        if frame_count % 30 == 0:
            print(f"已读取 {frame_count} 帧")
    cap.release()
    print(f"视频总帧数: {frame_count}")


def video_to_ascii(video_path):
    pass


img = Image.open("first_frame.jpg")
resizedImg = process_image(img)
final = pixel_to_chars(resizedImg)
text_to_image(final, "output2.png", font_size=8, line_gap_ratio=0.2)




