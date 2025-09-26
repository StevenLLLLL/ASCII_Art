import cv2


def input_vid(v):
    """
    读取视频, 并输出帧数
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


input_vid("testVid.mp4")