# import cv2
from cv2 import cv2
import numpy as np

c = cv2.VideoCapture("./video/homework3.mp4")

def method1():
    while c.isOpened():
        rd, image = c.read()

        if rd:
            # ---------> 前處理 <----------
            m1 = image[:, :, 0]  # 取 藍色通道
            m2 = image[:, :, 2]  # 取 紅色通道
            m3 = cv2.subtract(m1, m2)  # 紅色通道 - 藍色通道

            # ---------> 二值化 <----------
            th, m4 = cv2.threshold(m3, 55, 255, cv2.THRESH_BINARY)

            # ---------> 最小方框點 <----------
            x, y, w, h = cv2.boundingRect(m4)

            # ---------> 畫方框在原始圖片上 <----------
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 3)

            cv2.imshow("image", image)
            cv2.imshow("m1", m1)
            cv2.imshow("m2", m2)
            cv2.imshow("m3", m3)
            cv2.imshow("m4", m4)
        else:
            break

        if cv2.waitKey(10) != -1:
            break

def method2():
    while c.isOpened():
        rd, image = c.read()

        if rd:
            # ---------> 前處理 <----------
            m1 = image[:, :, 2]  # 取 紅色通道

            # ---------> 二值化 <----------
            th, m2 = cv2.threshold(m1, 50, 255, cv2.THRESH_BINARY)
            m3 = cv2.bitwise_not(m2)

            # ---------> 最小方框點 <----------
            x, y, w, h = cv2.boundingRect(m3)

            # ---------> 畫方框在原始圖片上 <----------
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 3)

            cv2.imshow("image", image)
            cv2.imshow("m1", m1)
            cv2.imshow("m2", m2)
            cv2.imshow("m3", m3)
        else:
            break

        if cv2.waitKey(10) != -1:
            break

def method3():
    while c.isOpened():
        rd, image = c.read()

        if rd:
            # ---------> 前處理 <----------
            m1 = image[:, :, 2]  # 取 紅色通道

            # ---------> 二值化 <----------
            th, m2 = cv2.threshold(m1, 60, 255, cv2.THRESH_BINARY)
            m3 = cv2.bitwise_not(m2)

            # ---------> 侵蝕 <----------
            m3 = cv2.morphologyEx(m3, cv2.MORPH_CLOSE, np.ones((11, 11)))

            # ---------> 輪廓串列 <----------
            ct, th = cv2.findContours(m3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

            m4 = np.full(m1.shape, 255, np.uint8)
            cv2.drawContours(m4, ct, -1, (0, 0, 0), 1)

            for d in range( len(ct)):
                x, y, w, h = cv2.boundingRect(ct[d])
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)

            cv2.imshow("image", image)
            cv2.imshow("m1", m1)
            cv2.imshow("m2", m2)
            cv2.imshow("m3", m3)
            cv2.imshow("m4", m4)
        else:
            break

        if cv2.waitKey(10) != -1:
            break

def method4():
    while c.isOpened():
        rd, image = c.read()

        if rd:
            # ---------> 前處理 <----------
            m0 = cv2.medianBlur(image, 5)
            m1 = m0[:, :, 2]  # 取 紅色通道

            # ---------> 二值化 <----------
            th, m2 = cv2.threshold(m1, 60, 255, cv2.THRESH_BINARY)
            m3 = cv2.bitwise_not(m2)

            # ---------> 最小方框點 <----------
            x, y, w, h = cv2.boundingRect(m3)

            # ---------> 畫方框在原始圖片上 <----------
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 3)

            cv2.imshow("image", image)
            cv2.imshow("m0", m0)
            cv2.imshow("m1", m1)
            cv2.imshow("m2", m2)
            cv2.imshow("m3", m3)
        else:
            break

        if cv2.waitKey(10) != -1:
            break

def method5():
    while c.isOpened():
        rd, image = c.read()

        if rd:
            # ---------> 前處理 <----------
            m0 = cv2.medianBlur(image, 5)
            m1 = m0[:, :, 2]  # 取 紅色通道

            # ---------> 二值化 <----------
            th, m2 = cv2.threshold(m1, 60, 255, cv2.THRESH_BINARY)
            m3 = cv2.bitwise_not(m2)

            # ---------> 侵蝕 <----------
            m3 = cv2.morphologyEx(m3, cv2.MORPH_CLOSE, np.ones((11, 11)))

            # ---------> 輪廓串列 <----------
            ct, th = cv2.findContours(m3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

            m4 = np.full(m1.shape, 255, np.uint8)
            cv2.drawContours(m4, ct, -1, (0, 0, 0), 1)

            for d in range( len(ct)):
                x, y, w, h = cv2.boundingRect(ct[d])
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)

            cv2.imshow("image", image)
            cv2.imshow("m1", m1)
            cv2.imshow("m2", m2)
            cv2.imshow("m3", m3)
            cv2.imshow("m4", m4)
        else:
            break

        if cv2.waitKey(10) != -1:
            break

def method6():
    while c.isOpened():
        rd, image = c.read()

        if rd:
            # ---------> 前處理 <----------
            m1 = image[:, :, 0]  # 取 藍色通道
            m2 = image[:, :, 2]  # 取 紅色通道
            m3 = cv2.subtract(m1, m2)  # 紅色通道 - 藍色通道

            # ---------> 二值化 <----------
            th, m3 = cv2.threshold(m3, 50, 255, cv2.THRESH_BINARY)
            m4 = cv2.bitwise_not(m3)

            m5 = cv2.Canny(m4, 100, 30)

            # ---------> 最小方框點 <----------
            x, y, w, h = cv2.boundingRect(m5)

            # ---------> 畫方框在原始圖片上 <----------
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 3)

            cv2.imshow("image", image)
            cv2.imshow("m1", m1)
            cv2.imshow("m2", m2)
            cv2.imshow("m3", m3)
            cv2.imshow("m4", m4)
            cv2.imshow("m5", m5)
        else:
            break

        if cv2.waitKey(10) != -1:
            break

def method7():
    while c.isOpened():
        rd, image = c.read()

        if rd:
            # ---------> 前處理 <----------
            m1 = image[:, :, 0]  # 取 藍色通道
            m2 = image[:, :, 2]  # 取 紅色通道
            m3 = cv2.subtract(m1, m2)  # 紅色通道 - 藍色通道

            # ---------> 二值化 <----------
            m3 = cv2.adaptiveThreshold(m3, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 9)

            # ---------> Canny 運算 <----------
            m4 = cv2.Canny(m3, 100, 30)

            # ---------> 最小方框點 <----------
            x, y, w, h = cv2.boundingRect(m4)

            # ---------> 畫方框在原始圖片上 <----------
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 3)

            cv2.imshow("image", image)
            cv2.imshow("m1", m1)
            cv2.imshow("m2", m2)
            cv2.imshow("m3", m3)
            cv2.imshow("m4", m4)


        else:
            break

        if cv2.waitKey(10) != -1:
            break

def method8():
    while c.isOpened():
        rd, image = c.read()

        if rd:
            # ---------> 前處理 <----------
            m1 = image[:, :, 0]  # 取 藍色通道
            m2 = image[:, :, 2]  # 取 紅色通道
            m3 = cv2.subtract(m1, m2)  # 紅色通道 - 藍色通道
            m3 = cv2.subtract(m3, m2)  # 紅色通道 - 藍色通道

            # ---------> 最小方框點 <----------
            x, y, w, h = cv2.boundingRect(m3)

            # ---------> 畫方框在原始圖片上 <----------
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 3)

            cv2.imshow("image", image)
            cv2.imshow("m1", m1)
            cv2.imshow("m2", m2)
            cv2.imshow("m3", m3)

        else:
            break

        if cv2.waitKey(10) != -1:
            break


def method9():
    while c.isOpened():
        rd, image = c.read()
        
        if rd:
            # ---------> 前處理 <----------  cv2.inRange(圖像變數, 顏色下限, 顏色上限)
            m1 = cv2.inRange(image, (75, 50, 40), (255, 100, 75))
            # ---------> 最小方框點 <----------
            x, y, w, h = cv2.boundingRect(m1)

            # ---------> 畫方框在原始圖片上 <----------
            ltk = 6 # 多計算線條寬度
            cv2.rectangle(image, (x-ltk, y-ltk), (x + w + ltk, y + h + ltk), (0, 255, 255), ltk)

            cv2.imshow("image", image)
            cv2.imshow("m1", m1)

        else:
            break

        if cv2.waitKey(10) != -1:
            break

# method1()
# cv2.destroyAllWindows()

# method2()
# cv2.destroyAllWindows()

# method3()   # 不建議使用 畫點再畫出輪廓，太多雜質需要處理、微調參數
# cv2.destroyAllWindows()

# method4() # 前處理 增加 中值模糊。能不用就不用 模糊 很吃效能
# cv2.destroyAllWindows()

# method5() # method3 雜訊改善，利用模糊解決。同 method4() 一樣，用到模糊效能會降低。
# cv2.destroyAllWindows()

# method6() # 搭配 canny() 線條抓取
# cv2.destroyAllWindows()

# method7() # threshold >> 改 >> adaptiveThreshold
# cv2.destroyAllWindows()

# method8() # 僅通道 處理，僅通道效果不佳，需要再加強對比
# cv2.destroyAllWindows()

method9() # 僅用 inRange() 抓取特定顏色範圍
cv2.destroyAllWindows()
