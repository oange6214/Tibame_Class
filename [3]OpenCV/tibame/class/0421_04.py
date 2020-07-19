import pytesseract as pt
import numpy as np
import cv2, glob
from pyzbar import pyzbar


def ex031():
    '''
        利用 OCR 光學分析 文字
    '''
    m1 = cv2.imread('./image/word_001.png', 1)

    result = pt.image_to_string(m1, "eng", "")
    result2 = pt.image_to_string(m1, "chi_tra", "")

    print(result)
    print(result2)

    cv2.imshow('m1', m1)
    cv2.waitKey(0)


def ex032():
    '''
        分析不清楚原因:
            一、尺寸大小
            二、密度
            三、解析度
    '''
    # m1 = cv2.imread("image/01.png", 1)
    # m1 = cv2.imread("image/02.png", 1)
    m1 = cv2.imread("image/03.png", 1)

    ret = pt.image_to_string(m1, 'eng', '')

    print(ret)
    print('-------------------')

    th, m2 = cv2.threshold(m1, 240, 255, cv2.THRESH_BINARY)
    m2 = cv2.erode(m2, np.ones((1, 15)))

    m2 = cv2.cvtColor(m2, cv2.COLOR_BGR2GRAY)
    ct, th = cv2.findContours(m2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for d in range(1, len(ct)):
        x, y, w, h = cv2.boundingRect(ct[d])
        if w > h * 2:
            m3 = m1[y: y + h, x: x + w]

            # 放大
            nh = 100
            nw = int((nh / m3.shape[0]) * m3.shape[1])
            m3 = cv2.resize(m3, (nw, nh))

            ret = pt.image_to_string(m3, 'eng', '')
            print(ret)

            cv2.imshow('m3' + str(d), m3)
    cv2.waitKey(0)


def ex033():
    '''
        密度高的問題，導致難以分辨，盡管 圖片放大 N 倍
    '''

    m1 = cv2.imread('./image/01.png', 1)
    ret = pt.image_to_string(m1, 'eng', '')

    print(ret)
    print('-------------------')

    # 去除 字
    m2 = cv2.inRange(m1, (0, 0, 0), (100, 100, 100))  # 1D
    m2 = cv2.cvtColor(m2, cv2.COLOR_GRAY2BGR)  # 1D to 3D
    m2 = cv2.add(m1, m2)  # 白色區塊變白色，黑色區塊保留。(遮罩效果 mask)
    m2 = cv2.dilate(m2, np.ones((5, 5)))
    m2 = cv2.erode(m2, np.ones((5, 5)))

    # 去除 Logo、先抓 logo 做成遮色片，遮去 logo
    m3 = m2[:, :, 0]
    m3 = cv2.inRange(m3, 127, 255)
    m3 = cv2.bitwise_not(m3)
    m3 = cv2.dilate(m3, np.ones((5, 5)))
    m3 = cv2.cvtColor(m3, cv2.COLOR_GRAY2BGR)
    m3 = cv2.add(m1, m3)  # 白色區塊變白色，黑色區塊保留。(遮罩效果 mask)

    # 放大
    nh = 600
    nw = int((nh / m3.shape[0]) * m3.shape[1])
    m3 = cv2.resize(m3, (nw, nh))

    ret = pt.image_to_string(m3, 'eng', '')
    print(ret)

    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    cv2.imshow("m3", m3)

    cv2.waitKey(0)


def ex034():
    '''
        設定值全以字串的方式傳入，常用的設定如下：
            設定只可以出現的字元：
                -c tessedit_char_whitelist=字元
            設定不可以出現的字元：
                -c tessedit_char_blacklist=字元
        手寫 數字 密度高 大幅降低辨識能力
        手寫尺寸建議使用 18 大小
    '''

    # m1 = cv2.imread('./image/06.png', 1)
    m1 = cv2.imread('./image/07.png', 1)

    ret = pt.image_to_string(m1, 'eng')
    print(ret.replace('\n', '\t'))
    print('--------------------------')

    ret = pt.image_to_string(m1, 'eng', '-c tessedit_char_whitelist=1234567890')
    print(ret.replace('\n', '\t'))

    cv2.imshow("m1", m1)
    cv2.waitKey(0)


def ex035():
    '''
        手寫 數字 密度高 大幅降低辨識能力
    '''

    img_path_list = glob.glob(r'./image/mnint/*.png')

    img_list = []
    for img_path in img_path_list:
        img_list.append(cv2.imread(img_path, 1))

    for img in img_list:
        ret = pt.image_to_string(img, 'eng')
        print(ret.replace('\n', '\t'))
        print('- ' * 10)

        ret = pt.image_to_string(img, 'eng', '-c tessedit_char_whitelist=1234567890')
        print(ret.replace('\n', '\t'))
        print('=' * 30)


def ex036():
    '''
        使用 手寫 訓練 語言包
    '''

    m1 = cv2.imread('./image/my.png', 1)

    ret = pt.image_to_string(m1, 'my')
    print(ret.replace('\n', '\t'))

    cv2.imshow("m1", m1)
    cv2.waitKey(0)


def ex037():
    '''
        QRcode、Code 39 辨識
        pyzbar 無法使用
    '''

    m1 = cv2.imread('./image/m1.png', 1)  # QR code
    # m2 = cv2.imread('./image/m3.png', 1) # Code 39

    ret = pyzbar.decode(m1)
    for d in ret:
        print(d.type)
        try:
            print(d.data.decode('utf-8').encode('sjis').decode('utf-8'))
        except:
            print(d.data.decode('utf-8'))

        x, y, w, h = d.rect
        cv2.rectangle(m1, (x, y), (x + w, y + h), (0, 255, 255), 2)

    cv2.imshow('m1', m1)
    cv2.waitKey(0)
ex037()

def ex038():
    '''
        pyzbar QRcode、Code 39 辨識
    '''
    c = cv2.VideoCapture(0)

    while c.isOpened():
        r, m1 = c.read()
        if r:
            ret = pyzbar.decode(m1)
            for d in ret:
                print(d.type)
                try:
                    print(d.data.decode('utf-8').encode('sjis').decode('utf-8'))
                except:
                    print(d.data.decode('utf-8'))

                x, y, w, h = d.rect
                cv2.rectangle(m1, (x, y), (x + w, y + h), (0, 255, 255), 2)

            cv2.imshow('m1', m1)

            if cv2.waitKey(100) != -1:
                c.release()
                break


def ex039():
    '''
        CascadeClassifier 特徵門檻
        classifier.detectMultiScale 辨識器
    '''
    m1 = cv2.imread('./image/05.jpg', 1)
    classifier = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')

    ret = classifier.detectMultiScale(m1, minNeighbors=3, minSize=(10, 10))

    for x, y, w, h in ret:
        cv2.rectangle(m1, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('m1', m1)
    cv2.waitKey(0)


def ex040():
    classifier = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')

    c = cv2.VideoCapture(0)

    while c.isOpened():
        r, m1 = c.read()
        if r:
            ret = classifier.detectMultiScale(m1, minNeighbors=25, minSize=(20, 20))

            for x, y, w, h in ret:
                cv2.rectangle(m1, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.imshow('m1', m1)

            if cv2.waitKey(100) != -1:
                c.release()
                break


def ex041():
    '''
        自己訓練的
    '''
    m1 = cv2.imread('./classifier_training/Data/Image.jpeg', 1)
    m2 = cv2.imread('./classifier_training/Data/Image.jpg', 1)
    m3 = cv2.imread('./classifier_training/Data/Image.png', 1)
    img_list = [m1, m2, m3]

    classifier = cv2.CascadeClassifier('./classifier_training/xml/cascade.xml')

    i = 0
    for img in img_list:
        ret = classifier.detectMultiScale(img, minNeighbors=10, minSize=(10, 10))
        for x, y, w, h in ret:
            cv2.rectangle(img, (x, y),(x + w, y + h), (0, 0, 255), 2)

        cv2.imshow('m' + str(i), img)
        i += 1

    cv2.waitKey(0)



cv2.destroyAllWindows()
