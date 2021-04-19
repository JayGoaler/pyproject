import time

import cv2
import pytesseract


def video_show(video):
    select_data = None
    choose_video = False
    while True:
        # 获取摄像头两个参数，是否开启和每帧图像
        ret, frame = video.read()
        # 如果摄像头没开启，则打印信息并退出
        if not ret:
            # print("视频获取失败！")
            video = cv2.VideoCapture("C:\\Users\\JayGoal\\Desktop\\test.mp4")
            ret, frame = video.read()
            # break
        # 如果摄像头正常开启，则输出每帧图像
        cv2.imshow("Video_show", frame)
        # 监控是否按下 Q 键
        if cv2.waitKey(1) & 0xff == ord("s"):
            select_data = cv2.selectROI("Video_show", frame)
            choose_video = True
        # 如果Q键被按下，则切换显示框选区域
        if choose_video:
            # 获取选择框内的图像
            choose_data = frame[select_data[1]:select_data[1] + select_data[3],
                                select_data[0]:select_data[0] + select_data[2]]
            cv2.imshow("choose_video", choose_data)
            do_ocr(choose_data)
        if cv2.waitKey(1) & 0xff == ord('c'):
            choose_video = False
            cv2.destroyWindow("choose_video")
        # 如果按下P键，则退出视频
        if cv2.waitKey(1) & 0xff == ord("q"):
            break
    video.release()
    cv2.destroyAllWindows()


def do_ocr(pic):
    num = pytesseract.image_to_string(pic, lang="eng")
    num = num.strip().replace(' ', '')
    target = '081824303132'
    if num == target:
        times = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("找到特定值！：" + num + "，当前时间：" + times)


if __name__ == '__main__':
    path = "C:\\Users\\JayGoal\\Desktop\\test.mp4"
    # cv2.VideoCapture传入0表示打开摄像头
    video_show(cv2.VideoCapture(path))
    # do_ocr(Image.open(path))

