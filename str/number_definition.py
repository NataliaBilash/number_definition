import matplotlib.pyplot as plt
import pytesseract
import cv2
import imutils
import numpy as np

import text_definiton #распознавание по тесеракт
import parsing_autocod #сайт автомобиля

#открытие картинки из папки и переработка его в rgb прострастве
def open_img(img_path):
    carplate_img = cv2.imread(img_path)
    carplate_img = cv2.cvtColor(carplate_img, cv2.COLOR_BGR2RGB)
    #вывод изображения
    # plt.axis("off")
    # plt.imshow(carplate_img)
    # plt.show()

    return carplate_img

#нахождение координат номера по хаар каскаду
def carplate_extract(image, carplate_haar_cascade):
    carplate_rects = carplate_haar_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)
    for x, y, w, h in carplate_rects:
        carplate_img = image[y+15:y+h-10, x+20:x+w-15]
    
    return carplate_img

#увеличение изображения для лучшего распознования 
def enlarge_img(image, scale_percent):
    witgh=int(image.shape[1] * scale_percent / 100)
    height=int(image.shape[0] * scale_percent / 100)
    dim = (witgh, height)
    resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    return resized_image

def ddepth_img(resized_image):
    sharp_filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    # параметр ddepth отвечает за «глубину» картинки
    # # ddepth=-1 означает, что глубина получившейся картинки будет как у исходной
    sharpen_img = cv2.filter2D(resized_image, ddepth=-1, kernel=sharp_filter)
    return sharpen_img

def main():
    path_to_image = input("Enter the full path to the image: ") #/home/zeroff/git/pic_project/examples/1.jpg
    carplate_img_rgb = open_img(img_path=path_to_image)
    carplate_haar_cascade = cv2.CascadeClassifier('models/haarcascade_russian_plate_number.xml')

    carplate_extract_img = carplate_extract(image=carplate_img_rgb, carplate_haar_cascade=carplate_haar_cascade)
    carplate_extract_img = enlarge_img(image=carplate_extract_img, scale_percent=150)

    
    carplate_extract_img_gray = cv2.cvtColor(carplate_extract_img, cv2.COLOR_RGB2GRAY)
    ret, threshold_image = cv2.threshold(carplate_extract_img_gray, 127, 255, 0)
    carplate_extract_img = ddepth_img(resized_image=threshold_image)
    plt.axis("off")
    plt.imshow(carplate_extract_img)
    plt.show()
    definition_carplate=text_definiton.text_definition(carplate_extract_img)
    text_definiton.write_file(definition_carplate)
    parsing_autocod.parsing(definition_carplate)


if __name__ == "__main__":
    main()