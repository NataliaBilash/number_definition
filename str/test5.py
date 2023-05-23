import matplotlib.pyplot as plt
import pytesseract
import cv2
import imutils
import numpy as np

def open_img(img_path):
    carplate_img = cv2.imread(img_path)
    carplate_img = cv2.cvtColor(carplate_img, cv2.COLOR_BGR2GRAY)

    return carplate_img


def filter_and_egges(carplate_img):
    #наложение фильтра для уменьшения шума
    filter_img = cv2.bilateralFilter(carplate_img, 11,  15, 15) #11 диаметр ядра фильтра, 15 цветовое простратство, 15 координатное простратво
    #углы изображения
    egges_conturs = cv2.Canny(filter_img, 100, 255, 3)

    return egges_conturs

#здесь будут содержаться все контуры
def contures_img(egges_conturs): 
    #контуры изображения
    contures_img = cv2.findContours(egges_conturs.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contures_img = imutils.grab_contours(contures_img) #для сортироваки контуров
    contures_img = sorted(contures_img, key=cv2.contourArea, reverse=True)[0:10] #ищем прямоугольные контуры, только 10 контуров наиболее подъодящих

    return contures_img

#примерный перебор списка контуров
def outout_conturs(contures_img):
    position_num = None #возможная позиция номерного знака
    for i in contures_img:
        epsilon = cv2.arcLength(i, True)
        approx = cv2.approxPolyDP(i, 0.07*epsilon, True) #True указывает на закрытоссть контура
        if len(approx) == 4:
            position_num = approx
            break

    return position_num


def mask_carplate(gray_img, position_num, carplate_img):
    mask = np.zeros(gray_img.shape, np.uint8)
    new_img = cv2.drawContours(mask, [position_num], 0, 255, -1)
    bitwise_img = cv2.bitwise_and(carplate_img, carplate_img, mask=mask)
    
    return bitwise_img

def main():
    img_path = "/home/zeroff/git/pic_project/examples/1.jpg"
    input_img = cv2.imread(img_path)
    carplate_img_gray = open_img(img_path=img_path)
    egges_img = filter_and_egges(carplate_img=carplate_img_gray)
    contures_image = contures_img(egges_conturs=egges_img)
    pos = outout_conturs(contures_img=contures_image)
    print(pos)
    bitwise_img = mask_carplate(carplate_img_gray, pos, input_img)

    cv2.imshow("Example", bitwise_img)
    cv2.waitKey(0) #вывод изображения через opencv
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()