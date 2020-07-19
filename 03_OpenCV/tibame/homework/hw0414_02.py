import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

def method1():
    m1 = cv2.imread("image/homework2.png", 1)

    m2 = m1[:, :, 2]  # 取 紅色 通道
    m3 = m1[:, :, 1]  # 取 綠色 通道

    # 利用 通道性質，將差異最大的兩張圖，進行減法運算，擷取出像素質最大 (文字)
    m4 = cv2.subtract(m2, m3)   # 紅色通道 - 綠色通道
    m4 = cv2.subtract(m4, m3)   # 結果圖 - 綠色通道
    m4 = cv2.subtract(m4, m3)   # 結果圖 - 綠色通道，為了 清除乾淨多做一道
    m5 = cv2.bitwise_not(m4)    # 反轉顏色

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.imshow("m3", m3)
    cv2.imshow("m4", m4)
    cv2.imshow("m5", m5)

def method2():
    m1 = cv2.imread("image/homework2.png", 1)
    m2 = m1[:, :, 2]  # 取 紅色 通道
    m3 = np.full((m1.shape[0], m1.shape[1], 3), (255, 255, 255), np.uint8) # 設置白色畫布，與 原始圖 相同尺寸

    # 暴力分析
    for i in range(m1.shape[0]):
        for j in range(m1.shape[1]):
            if m2[i, j] == 255:
                m3[i, j] = 0
            else:
                m3[i, j] = 255

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.imshow("m3", m3)

method1()
cv2.waitKey(0)
cv2.destroyAllWindows()

method2()
cv2.waitKey(0)
cv2.destroyAllWindows()