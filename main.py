import cv2
import pytesseract
from PIL import Image


def video_show(video):
    select_data = None
    choose_video = False
    while True:
        # 获取摄像头两个参数，是否开启和每帧图像
        ret, frame = video.read()
        # 如果摄像头没开启，则打印信息并退出
        if not ret:
            print("视频获取失败！")
            break
        # 如果摄像头正常开启，则输出每帧图像
        cv2.imshow("Video_show", frame)
        # 监控是否按下 Q 键
        if cv2.waitKey(1) & 0xff == ord("q"):
            select_data = cv2.selectROI("Video_show", frame)
            choose_video = True
        # 如果Q键被按下，则切换显示框选区域
        if choose_video:
            # 获取选择框内的图像
            choose_data = frame[select_data[1]:select_data[1] + select_data[3],
                                select_data[0]:select_data[0] + select_data[2]]
            cv2.imshow("choose_video", choose_data)
            do_ocr(choose_data)
        # 如果按下P键，则退出视频
        if cv2.waitKey(1) & 0xff == ord("p"):
            break
    video.release()
    cv2.destroyAllWindows()


def do_ocr(pic):
    num = pytesseract.image_to_string(pic, lang="eng")
    num = num.strip()
    if num == "321321321":
        print(num)


if __name__ == '__main__':
    # cv2.VideoCapture传入0表示打开摄像头
    # video_show(cv2.VideoCapture(0))
    path = "C:\\Users\\JayGoal\\Desktop\\test.png"
    do_ocr(Image.open(path))
