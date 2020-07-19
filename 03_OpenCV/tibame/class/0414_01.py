import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


def ex001():
    ''' 讀取影像 '''
    image = cv2.imread('image/01.png', -1)  # 含透明層
    print(m1.shape)
    image = cv2.imread('image/01.png', 0)
    print(m1.shape)
    image = cv2.imread('image/01.png', 1)
    print(m1.shape)

    cv2.imshow("image", image)
    cv2.waitKey(0)


def ex002():
    ''' 輸入任意鍵關閉影像 '''
    c = cv2.VideoCapture(1)

    while c.isOpened():
        reading, image = c.read()

        if reading:
            cv2.imshow("image", image)
        else:
            break

        if cv2.waitKey(100) != -1:
            break


def ex003():
    ''' 取得來源資訊 '''
    c = cv2.VideoCapture("video/01.mp4")

    print("寬度: ", c.get(3))
    print("高度: ", c.get(4))
    print("FPS: ", c.get(5))
    print("總影格數: ", c.get(7))

    while c.isOpened():
        c.set(1, c.get(1) + 12)  # 快轉
        reading, image = c.read()

        if reading:
            print("當前影格: ", c.get(1))

            cv2.imshow("image", image)
        else:
            break

        if cv2.waitKey(100) != -1:
            break


def ex004():
    ''' 影片儲存、格式設定、釋放 '''
    c = cv2.VideoCapture(1)

    print("寬度: ", c.get(3))
    print("高度: ", c.get(4))

    w = cv2.VideoWriter("video/02.mp4", cv2.VideoWriter_fourcc(*"MP4V"), 30, (640, 480))

    while c.isOpened():
        reading, image = c.read()
        if reading:
            cv2.imshow("image", image)
            w.write(image)
        else:
            break

        if cv2.waitKey(100) != -1:
            break


def ex005():
    ''' 轉換類型，預設讀取的圖片色彩空間都是 BGR'''
    c = cv2.VideoCapture(1)

    while c.isOpened():
        reading, image = c.read()

        # 常用
        cimage1 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        cimage2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cimage3 = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
        cimage4 = cv2.cvtColor(cimage2, cv2.COLOR_GRAY2BGR)

        if reading:
            cv2.imshow("image", image)
            cv2.imshow("cimage1", cimage1)
            cv2.imshow("cimage2", cimage2)
            cv2.imshow("cimage3", cimage3)
            cv2.imshow("cimage4", cimage4)
        else:
            break

        if cv2.waitKey(100) != -1:
            break


def ex006():
    '''
        轉圖片類型
            cv2.imwrite("圖片路徑", 圖片變數, 設定參數)
    '''
    m1 = cv2.imread("image/01.png", 1)
    m2 = cv2.cvtColor(m1, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("image/03.png", m2)
    cv2.imwrite("image/03.jpg", m2, [cv2.IMWRITE_JPEG_QUALITY, 100])

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.waitKey(0)


def ex007():
    '''
        建立純色圖片
            變數 = np.full((維度一長度, 維度二長度…), 初始值, 陣列型態)

            圖像變數 = np.full((高, 寬, 3), 初始顏色值, np.uint8)
    '''
    m1 = np.full((100, 600, 3), (0, 0, 0), np.uint8)
    m2 = np.full((100, 600, 3), (255, 255, 255), np.uint8)
    m3 = np.full((100, 600), 127, np.uint8)

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.imshow("m3", m3)

    cv2.waitKey(0)


def ex008():
    '''
        線條繪畫
            cv2.line(圖像變數, 線的起點, 線的終點, 顏色, 線粗細)
            cv2.rectangle(圖像變數, 矩形左上點, 矩形右下點, 顏色, 線粗細)
            cv2.circle(圖像變數, 中心點, 半徑, 顏色, 線粗細)
    '''
    m1 = np.full((400, 400), 255, np.uint8)
    m2 = np.full((400, 400, 3), (255, 255, 255), np.uint8)

    cv2.line(m1, (10, 10), (300, 10), 0, 2)
    cv2.line(m2, (10, 10), (300, 10), (0, 0, 255), 2)

    cv2.rectangle(m2, (50, 50), (100, 100), (0, 0, 255), 2)
    cv2.rectangle(m2, (150, 50), (200, 100), (0, 0, 255), -1)

    cv2.circle(m2, (50, 50), 20, (0, 255, 0), 2)
    cv2.circle(m2, (150, 50), 20, (0, 255, 0), -1)

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)

    cv2.waitKey(0)


def ex009():
    '''
        PIL圖像變數 = Image.fromarray(OpenCV圖像變數)
        ImageDraw.Draw(PIL圖像變數).text(文字位置, 要寫的文字, 顏色, 設定)
        OpenCV圖像變數 = np.array(PIL圖像變數)
    '''

    m1 = cv2.imread("image/01.png", 1)
    pil_image = Image.fromarray(m1)

    fontpath = "./font/msjh.ttc"
    ImageDraw.Draw(pil_image).text((50, 50), "哈囉~", (0, 0, 255), ImageFont.truetype(fontpath, 32))
    m1 = np.array(pil_image)

    cv2.imshow("m1", m1)
    cv2.waitKey(0)

ex009()

cv2.destroyAllWindows()
