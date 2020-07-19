import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

imagePath = input('請輸入檔案名稱: ')
content = input('請輸入浮水印內容: ')
size = int(input('請輸入尺寸: '))

m1 = cv2.imread("image/" + imagePath, 1)

if type(m1) != type(None):
    pil_image = Image.fromarray(m1)
    ImageDraw.Draw(pil_image).text((50, 50), content, (0, 0, 255), ImageFont.truetype("./font/msjh.ttc", size))
    m1 = np.array(pil_image)
    cv2.imshow("m1", m1)
else:
    print('檔案名稱錯誤')

cv2.waitKey(0)
cv2.destroyAllWindows()