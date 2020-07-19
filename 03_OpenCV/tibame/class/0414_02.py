import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


def ex010():
    '''
        圖片加、減
            除了使用函式外， numpy 陣列也可以直接做運算(而若運算結果值低於 0 或者高於 255，則超過的部分會從另一端繼續計算)
    '''

    m1 = cv2.imread("image/01.png", 1)
    m2 = np.full(m1.shape, (127, 127, 127), np.uint8)
    m3 = cv2.add(m1, m2)
    m4 = cv2.subtract(m1, m2)
    m5 = cv2.absdiff(m1, m2)
    m6 = cv2.bitwise_not(m1)

    m7 = m1 + 100  # numpy 陣列計算
    m8 = m1 + 300  # 超過太多 變黑色

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.imshow("m3", m3)
    cv2.imshow("m4", m4)
    cv2.imshow("m5", m5)
    cv2.imshow("m6", m6)
    cv2.imshow("m7", m7)
    cv2.imshow("m8", m8)

    cv2.waitKey(0)


def ex010_1():
    ''' 輸入 v、b 操作顏色 暗、亮 '''

    m1 = cv2.imread("image/01.png", 1)
    m2 = np.array([])
    m3 = np.full(m1.shape, 10, np.uint8)

    val = True
    while True:
        cv2.imshow('m1', m1)

        k = cv2.waitKey(0)
        if k == 98:
            if m2.shape[0] == 0 or val == False:
                m2 = m1.copy()
            val = True
            m2 = cv2.add(m2, m3)
        elif k == 118:
            if m2.shape[0] == 0 or val == True:
                m2 = m1.copy()
            val = False
            m2 = cv2.subtract(m2, m3)

        cv2.imshow("m2", m2)

        if k == 27:
            break


def ex011():
    '''
        翻轉
        1: 左右翻轉
        0: 上下翻轉
        -1: 左右、上下皆翻轉
    '''

    m1 = cv2.imread("image/02.jpg", 1)

    # 固定寬度、等比縮放
    # nw = 200
    # nh = int((nw / m1.shape[1]) * m1.shape[0])

    # 固定高度、等比縮放
    nh = 200
    nw = int((nh / m1.shape[0]) * m1.shape[1])

    m2 = cv2.resize(m1, (nw, nh))

    m3 = cv2.flip(m1, 1)
    m4 = cv2.flip(m1, 0)
    m5 = cv2.flip(m1, -1)

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.imshow("m3", m3)
    cv2.imshow("m4", m4)
    cv2.imshow("m5", m5)

    cv2.waitKey(0)


def ex012():
    '''
        變換矩陣 = cv2.getRotationMatrix2D(旋轉中心, 角度, 縮放比率)
        結果圖像 = cv2.warpAffine(圖像變數, 變換矩陣, 輸出的圖像大小 (Tuple類型： (寬, 高)) )
    '''

    m1 = cv2.imread("image/02.jpg", 1)
    m1_cen = (m1.shape[0] / 2, m1.shape[1] / 2)
    roma = cv2.getRotationMatrix2D(m1_cen, 45, 0.8)
    m2 = cv2.warpAffine(m1, roma, (m1.shape[0], m1.shape[0]))

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)

    cv2.waitKey(0)


def ex013():
    '''
        圖像變數[ Y 軸範圍起始: Y 軸範圍結束, X 軸範圍起始: X 軸範圍結束]
        numpy 函式庫可以透過這種形式存取或讀取矩陣範圍
    '''
    m1 = cv2.imread("image/01.png", 1)

    m2 = m1[0:100, 0:200]
    m3 = m1[::2, ::3]  # 高度步進為 2 時，是指 每隔 1 行取 1 行；寬度步進為 3 時，是指 每隔 2 行取 1 行。

    m4 = np.full((500, 500, 3), 255, np.uint8)
    # m4[100:384, 100:384] = m1 # 範圍要跟 m1 尺寸相同

    offset = 50
    m4[offset:m1.shape[0] + offset, offset:m1.shape[1] + offset] = m1  # 範圍要跟 m1 尺寸相同

    # m4[100:200, 100:200] = m1[100:200, 100:200]  # 範圍要跟 m1 尺寸相同

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.imshow("m3", m3)
    cv2.imshow("m4", m4)

    cv2.waitKey(0)


def ex014():
    ''' 圖片的像素讀取、寫入 '''
    m1 = cv2.imread("image/01.png", 1)
    m2 = np.full((500, 500, 3), 255, np.uint8)

    print(m1[100, 100])  # 回傳 B G R 的像素值
    m2[100: 200, 100: 200] = [0, 0, 255]  # 指定像素點範圍內，設 紅色通道像素值為 255
    m1[:, :] = 255  # 所有像素點設 255

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.waitKey(0)


ex014()

cv2.destroyAllWindows()
