import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


def ex014():
    # threshold 閥值函數
    # m1 = cv2.imread("image/01.png", 1)
    m1 = cv2.imread("image/homework2.png", 1)

    th, m2 = cv2.threshold(m1, 254, 255, cv2.THRESH_BINARY)
    m2 = m2[:, :, 2]
    m2 = cv2.bitwise_not(m2)

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.waitKey(0)


def ex015():
    # 灰階通道處理
    m1 = cv2.imread("image/01.png", 0)

    th, m2 = cv2.threshold(m1, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    print(th)  # 檢視 門檻值

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.waitKey(0)


def ex016():
    # 彩色通道，個別處理
    # m1 = cv2.imread("image/01.png", 1)
    m1 = cv2.imread("image/homework2.png", 1)

    m2 = m1.copy()

    th, m2[:, :, 0] = cv2.threshold(m1[:, :, 0], 254, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    print(th)
    th, m2[:, :, 1] = cv2.threshold(m1[:, :, 1], 254, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    print(th)
    th, m2[:, :, 2] = cv2.threshold(m1[:, :, 2], 254, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    print(th)

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.waitKey(0)


def ex017():
    '''
        adaptiveThreshold 局部判斷二值化 (只接受 單一通道的 色彩空間)

        結果圖像 = cv2.adaptiveThreshold(
            圖像變數,
            最大值,
            方法一,
            方法二,
            區塊大小,
            微調值
        )

        方法一、
            cv2.ADAPTIVE_THRESH_MEAN_C：
                計算區塊大小內的 平均值 再減去 微調值
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C：
                計算區塊大小內的 高斯加權 平均值值 再減去微調值

        方法二、
            cv2.THRESH_BINARY：
                黑白兩色
            cv2.THRESH_BINARY_INV
                黑白兩色後反轉
    '''
    m1 = cv2.imread("image/01.png", 1)
    # m1 = cv2.imread("image/homework2.png", 0)
    # m1 = cv2.imread("image/homework2.png", 1)

    m2 = cv2.adaptiveThreshold(m1[:, :, 2], 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 5)

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.waitKey(0)


def ex018():
    ''' Canny 有效抓取 邊緣(顏色交接處)

        結果圖像 = cv2.Canny(
            圖像變數,
            門檻值1, (大門檻)
            門檻值2  (小門檻)
        )

        先用大的門檻值檢測邊緣，再用小的門檻值將檢測出來的結果線條連起。
    '''
    m1 = cv2.imread("image/road.jpg", 1)
    # m1 = cv2.imread("image/01.png", 1)

    m2 = cv2.Canny(m1, 500, 300)

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.waitKey(0)


def ex019():
    '''
        平均值模糊法(統計範圍內的色彩值平均)
    '''
    m1 = cv2.imread("image/01.png", 1)
    # m1 = cv2.imread("image/04.jpg", 1)
    m2 = cv2.blur(m1, (25, 25))

    '''
        中值模糊法(將處理範圍內的色彩值做排序，取順序在中間的)

        數值必須是 奇數
    '''
    m3 = cv2.medianBlur(m1, 25)

    '''
        直方圖均衡化法 (只接受單一通道)
        可以加強 色階 對比，有銳利化效果。
    '''
    m4 = m1.copy()
    for i in range(3):
        m4[:, :, i] = cv2.equalizeHist(m1[:, :, i])

    # 範圍 模糊
    m5 = m1.copy()
    m5[50: 150, 50: 150] = cv2.blur(m5[50: 150, 50: 150], (15, 15))

    cv2.imshow("orimg", m1)
    cv2.imshow("blur", m2)
    cv2.imshow("medianBlur", m3)
    cv2.imshow("equalizeHist", m4)
    cv2.imshow("area-blur", m5)

    cv2.waitKey(0)


def ex020():
    '''
        erode 侵蝕 (色彩值 低的 會侵蝕 色彩值 高的)
    '''
    m1 = cv2.imread("image/01.png", 1)
    # m1 = cv2.imread("image/04.jpg", 1)

    m2 = cv2.erode(m1, np.ones((7, 7))) # np.ones(高, 寬)
    m3 = cv2.erode(m1, np.ones((7, 1)))
    m4 = cv2.erode(m1, np.ones((1, 7)))

    cv2.imshow("orimg", m1)
    cv2.imshow("erode_7 * 7", m2)
    cv2.imshow("erode_7 * 1", m3)
    cv2.imshow("erode_1 * 7", m4)
    cv2.waitKey(0)


def ex021():
    '''
        dilate 膨脹 (色彩值 低的會侵蝕 色彩值 高的)
    '''
    m1 = cv2.imread("image/01.png", 1)
    # m1 = cv2.imread("image/04.jpg", 1)

    m2 = cv2.dilate(m1, np.ones((7, 7)))
    m3 = cv2.dilate(m1, np.ones((7, 1)))
    m4 = cv2.dilate(m1, np.ones((1, 7)))

    cv2.imshow("orimg", m1)
    cv2.imshow("dilate_7 * 7", m2)
    cv2.imshow("dilate_7 * 1", m3)
    cv2.imshow("dilate_1 * 7", m4)
    cv2.waitKey(0)


def ex022():
    '''
        dilate 膨脹 + erode 侵蝕
    '''
    m1 = cv2.imread("image/01.png", 1)
    # m1 = cv2.imread("image/04.jpg", 1)

    m2 = cv2.dilate(m1, np.ones((8, 8)))
    m2 = cv2.erode(m2, np.ones((8, 8)))

    m3 = cv2.erode(m1, np.ones((8, 8)))
    m3 = cv2.dilate(m3, np.ones((8, 8)))

    m4 = cv2.erode(m1, np.ones((8, 8)))
    m5 = cv2.dilate(m3, np.ones((8, 8)))
    m6 = m4 - m5
    m7 = m5 - m4


    cv2.imshow("orimg", m1)
    cv2.imshow("dilate > erode", m2)
    cv2.imshow("erode > dilate", m3)
    cv2.imshow("Gradient_erode-dilate", m6)
    cv2.imshow("Gradient_dilate-erode", m7)


    cv2.waitKey(0)


def ex023():
    '''
        結果圖像 = cv2.morphologyEx(圖像變數, 方法, 結構陣列)
            方法:
                cv2.MORPH_OPEN      開方法, 先執行 erode 侵蝕，後執行 dilate 膨脹
                cv2.MORPH_CLOSE     閉方法, 先執行 dilate 膨脹、後執行 erode 侵蝕
                cv2.MORPH_GRADIENT  執行 dilate 膨脹與 erode 侵蝕 產生 的 變化差
    '''
    m1 = cv2.imread("image/01.png", 1)
    # m1 = cv2.imread("image/04.jpg", 1)

    m2 = cv2.morphologyEx(m1, cv2.MORPH_OPEN, np.ones((8, 8)))      # erode > dilate
    m3 = cv2.morphologyEx(m1, cv2.MORPH_CLOSE, np.ones((8, 8)))     # dilate > erode
    m4 = cv2.morphologyEx(m1, cv2.MORPH_GRADIENT, np.ones((8, 8)))  # dilate - erode

    cv2.imshow("orimg", m1)
    cv2.imshow("MORPH_OPEN", m2)
    cv2.imshow("MORPH_CLOSE", m3)
    cv2.imshow("MORPH_GRADIENT", m4)
    cv2.waitKey(0)



def ex024():
    '''
        判斷圖像裡的各項素是否在指定色彩範圍內：
            結果圖像 = cv2.inRange(圖像變數, 顏色下限, 顏色上限)

        傳回一張與傳入變數相同大小的黑白圖像，在範圍內的像素會被設白色，否為則黑色
    '''
    m1 = cv2.imread("image/01.png", 1)

    m2 = cv2.inRange(m1[:, :, 2], 255, 255)
    m2 = cv2.bitwise_not(m2)

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.waitKey(0)


def ex025():
    '''
        判斷圖像裡的各項素是否在指定色彩範圍內：
            結果圖像 = cv2.inRange(圖像變數, 顏色下限, 顏色上限)

        傳回一張與傳入變數相同大小的黑白圖像，在範圍內的像素會被設白色，否為則黑色
    '''
    m1 = cv2.imread("image/01.png", 1)

    # 去除 字
    m2 = cv2.inRange(m1, (0, 0, 0), (100, 100, 100))    # 1D
    m2 = cv2.cvtColor(m2, cv2.COLOR_GRAY2BGR)           # 1D to 3D
    m2 = cv2.add(m1, m2)                                # 白色區塊變白色，黑色區塊保留。(遮罩效果 mask)
    m2 = cv2.dilate(m2, np.ones((5, 5)))
    m2 = cv2.erode(m2, np.ones((5, 5)))


    # 去除大字
    m3 = cv2.inRange(m1, (0, 0, 0), (100, 100, 100))
    m3 = cv2.cvtColor(m3, cv2.COLOR_GRAY2BGR)
    m3 = cv2.dilate(m3, np.ones((5, 5)))
    m3 = cv2.add(m1, m3)

    # 去除 小字
    m4 = m1.copy
    m4 = cv2.cvtColor(m1, cv2.COLOR_BGR2GRAY)
    th, m4 = cv2.threshold(m4, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    m4 = cv2.cvtColor(m4, cv2.COLOR_GRAY2BGR)
    m4 = cv2.dilate(m4, np.ones((2, 2)))
    m4 = cv2.erode(m4, np.ones((5, 5)))
    m4 = cv2.add(m1, m4)

    # 去除 Logo、先抓 logo 做成遮色片，遮去 logo
    m5 = m2[:, :, 0] 
    m5 = cv2.inRange(m5, 127, 255)
    m5 = cv2.bitwise_not(m5)
    m5 = cv2.dilate(m5, np.ones((5, 5)))
    m5 = cv2.cvtColor(m5, cv2.COLOR_GRAY2BGR)
    m5 = cv2.add(m1, m5)                                # 白色區塊變白色，黑色區塊保留。(遮罩效果 mask)

    # 只留 大字
    m6 = cv2.inRange(m1, (0, 0, 0), (100, 100, 100))
    m6 = cv2.cvtColor(m6, cv2.COLOR_GRAY2BGR)
    m6 = cv2.dilate(m6, np.ones((5, 5)))
    m6 = cv2.bitwise_not(m6)
    m6 = cv2.add(m1, m6)

    # 只留 小字
    m7 = cv2.cvtColor(m1, cv2.COLOR_BGR2GRAY)
    th, m7 = cv2.threshold(m7, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    m7 = cv2.cvtColor(m7, cv2.COLOR_GRAY2BGR)
    m7 = cv2.bitwise_not(m7)
    m7 = cv2.erode(m7, np.ones((2, 2)))
    m7 = cv2.dilate(m7, np.ones((5, 5)))
    m7 = cv2.add(m1, m7)

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.imshow("m3", m3)
    cv2.imshow("m4", m4)
    cv2.imshow("m5", m5)
    cv2.imshow("m6", m6)
    cv2.imshow("m7", m7)

    cv2.waitKey(0)


def ex026():
    '''
        輪廓點, 輪廓階層資料 = cv2.findContours(
            圖像變數(需二值化圖),
            類型,
            方法
        )

            類型:
                cv2.RETR_EXTERNAL： 只儲存最外層的輪廓
                cv2.RETR_LIST    ： 儲存所有輪廓，但不建立階層資料
                cv2.RETR_CCOMP   ： 儲存所有輪廓，但階層資料只包留兩層，首階層為物件外圍，第二階層為內部空心部分的輪廓，如果更內部有其餘物件，包含於首階層
                cv2.RETR_TREE    ： 儲存所有輪廓與其對應的階層資料
            方法:
                cv2.CHAIN_APPROX_NONE  ： 儲存所有輪廓點
                cv2.CHAIN_APPROX_SIMPLE： 簡化輪廓點，一條線只儲存頭尾
    '''
    m1 = cv2.imread("image/03.png", 1)
    # m1 = cv2.imread("image/01.png", 1)

    m2 = cv2.cvtColor(m1, cv2.COLOR_BGR2GRAY)
    th, m2 = cv2.threshold(m2, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    ct, th = cv2.findContours(m2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # print (th)

    m3 = np.full(m1.shape, 0, np.uint8)
    '''
        drawContours 繪製輪廓：
            cv2.drawContours(
                圖像變數,
                存取全部輪廓的變數,
                要繪製的輪廓索引,
                顏色,
                粗細
            )
    '''
    # 畫輪廓點
    cv2.drawContours(m3, ct, -1, (0, 255, 255), 3)
    # 畫內輪廓
    m4 = m1.copy()
    cv2.drawContours(m4, ct, -1, (0, 255, 255), 3)

    '''
        boundingRect 取得包覆指定輪廓點的最小正矩形：
            X 座標, Y 座標, 寬度, 高度 = cv2.boundingRect(指定的輪廓)
    '''
    m5 = m1.copy()

    x, y, w, h = cv2.boundingRect(m2)
    # print(x, y, w, h)
    cv2.rectangle(m5, (x, y), (x + w, y + h), (0, 255, 255), 3)

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.imshow("m3", m3)
    cv2.imshow("m4", m4)
    cv2.imshow("m5", m5)

    cv2.waitKey(0)


def ex027():
    # boundingRect 最小內框擷取、drawContours
    m1 = cv2.imread("image/01.png", 1)
    m2 = cv2.cvtColor(m1, cv2.COLOR_BGR2GRAY)
    th, m2 = cv2.threshold(m2, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    ct, th = cv2.findContours(m2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    m3 = np.full(m1.shape, 0, np.uint8)
    for d in range(0, len(ct)):
        x, y, w, h = cv2.boundingRect(ct[d])

        # 利用 輪廓點數量，做篩選
        if len(ct[d]) > 50:
            cv2.drawContours(m3, ct, d, (0, 0, 255), 2)
            # cv2.imshow('m3' + str(d), m1[y: y + h, x: x + w])

    m4 = np.full(m1.shape, 0, np.uint8)
    for d in range(1, len(ct)):     # 第一個數據是原圖最外框，可以跳過
        x, y, w, h = cv2.boundingRect(ct[d])

        # 利用 最小矩形的寬 做篩選
        if w > m1.shape[1] * 0.3:   # 分析圖片最小矩形框的寬度 > (分析圖片寬度 * 0.2)
            cv2.drawContours(m4, ct, d, (0, 0, 255), 2)
            cv2.imshow('m4' + str(d), m1[y: y + h, x: x + w])
            cv2.rectangle(m1, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.imshow("m3", m3)

    cv2.waitKey(0)


def ex028():
    # 抓文字、同性質圖片 可用相同演算法
    # m1 = cv2.imread("image/01.png", 1)
    # m1 = cv2.imread("image/02.png", 1)
    # m1 = cv2.imread("image/03.png", 1)
    m1 = cv2.imread("image/02.jpg", 1)


    m2 = cv2.cvtColor(m1, cv2.COLOR_BGR2GRAY)
    th, m2 = cv2.threshold(m2, 240, 255, cv2.THRESH_BINARY)
    m3 = cv2.erode(m2, np.ones((7, 21)))
    ct, th = cv2.findContours(m3, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    m4 = np.full(m1.shape, 255, np.uint8)
    cv2.drawContours(m4, ct, -1, (0, 0, 0), 1)

    m5 = m1.copy()
    for d in range(1, len(ct)):
        x, y, w, h = cv2.boundingRect(ct[d])

        # 過濾 小尺寸的圖形
        if w > 20:
            cv2.imshow("m5" + str(d), m1[y: y + h, x: x + w])
            cv2.rectangle(m5, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.imshow("m3", m3)
    cv2.imshow("m4", m4)
    cv2.imshow("m5", m5)

    cv2.waitKey(0)


def ex029():
    m1 = cv2.imread("image/02.jpg", 1)

    m2 = cv2.cvtColor(m1, cv2.COLOR_BGR2GRAY)
    th, m2 = cv2.threshold(m2, 200, 255, cv2.THRESH_BINARY)
    m3 = cv2.erode(m2, np.ones((11, 20)))
    ct, th = cv2.findContours(m3, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    m4 = np.full(m1.shape, 255, np.uint8)
    cv2.drawContours(m4, ct, -1, (0, 0, 0), 1)

    m5 = m1.copy()
    for d in range(1, len(ct)):
        x, y, w, h = cv2.boundingRect(ct[d])

        if w > 30:
            cv2.imshow("m5" + str(d), m1[y: y + h, x: x + w])
            cv2.rectangle(m5, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.imshow("m3", m3)
    cv2.imshow("m4", m4)
    cv2.imshow("m5", m5)

    cv2.waitKey(0)

def ex030():
    m1 = cv2.imread('./image/01.png', 1)

    th, m2 = cv2.threshold(m1, 240, 255, cv2.THRESH_BINARY)
    m2 = cv2.erode(m2, np.ones((1, 15)))

    m2 = cv2.cvtColor(m2, cv2.COLOR_BGR2GRAY)
    ct, th = cv2.findContours(m2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for d in range(1, len(ct)):
        x, y, w, h = cv2.boundingRect(ct[d])
        if w > h * 2:
            m3 = m1[y: y+h, x: x+w]

            cv2.imshow('m3' + str(d), m3)
    cv2.waitKey(0)

ex030()

cv2.destroyAllWindows()
