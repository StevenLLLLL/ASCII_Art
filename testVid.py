import cv2
cap = cv2.VideoCapture("testVid.mp4")
if not cap.isOpened():
    raise RuntimeError("无法打开视频文件")

fps = cap.get(cv2.CAP_PROP_FPS) or 0.0
total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) or 0
print(f"FPS: {fps}, 总帧数: {total}")

ok, frame = cap.read()
if not ok:
    raise RuntimeError("无法读取视频帧")

cv2.imwrite('first_frame.jpg', frame)
cap.release()
print("已保存第一帧为 first_frame.jpg")