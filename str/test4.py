import pytesseract 
import matplotlib.pyplot as plt 
import cv2 
import glob 
import os 
import matplotlib.image as mpimg

# specifying the path to the number plate images folder as shown below 
file_path = os.getcwd() + "/license_plates/**/*.jpg" 
NP_list = [] 
predicted_NP = [] 
 
for file_path in glob.glob(file_path, recursive = True): 
     
    NP_file = file_path.split("/")[-1] 
    number_plate, _ = os.path.splitext(NP_file) 
    ''' 
    Here we will append the actual number plate to a list 
    ''' 
    NP_list.append(number_plate) 
     
    ''' 
    Reading each number plate image file using openCV 
    ''' 
    NP_img = cv2.imread(file_path) 
     
    ''' 
    We will then pass each number plate image file 
    to the Tesseract OCR engine utilizing the Python library 
    wrapper for it. We get back predicted_res for 
    number plate. We append the predicted_res in a 
    list and compare it with the original number plate 
    ''' 
    predicted_res = pytesseract.image_to_string(NP_img, lang ='eng', 
    config ='--oem 3 --psm 6 -c tessedit_char_whitelist = ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') 
     
    filter_predicted_res = "".join(predicted_res.split()).replace(":", "").replace("-", "") 
    predicted_NP.append(filter_predicted_res)



print("Original Number Plate", "\t", "Predicted Number Plate", "\t", "Accuracy") 
print("--------------------", "\t", "-----------------------", "\t", "--------") 
 
def estimate_predicted_accuracy(ori_list, pre_list): 
    for ori_plate, pre_plate in zip(ori_list, pre_list): 
        acc = "0 %" 
        number_matches = 0 
        if ori_plate == pre_plate: 
            acc = "100 %" 
        else: 
            if len(ori_plate) == len(pre_plate): 
                for o, p in zip(ori_plate, pre_plate): 
                    if o == p: 
                        number_matches += 1 
                acc = str(round((number_matches / len(ori_plate)), 2) * 100) 
                acc += "%" 
        print(ori_plate, "\t", pre_plate, "\t", acc) 
 
estimate_predicted_accuracy(NP_list, predicted_NP) 

for img in os.listdir("/home/zeroff/git/pic_project/examples"):  
    test_NP = mpimg.imread("6TRJ244.jpg") 
 
plt.imshow(test_NP) 
plt.axis('off') 
plt.title('6TRJ244 license plate') 
plt.show() 


    # image resizing 
resize_test_NP = cv2.resize( 
    test_NP, None, fx = 2, fy = 2,  
    interpolation = cv2.INTER_CUBIC) 
 
    # converting image to grayscale 
grayscale_resize_test_NP = cv2.cvtColor( 
    resize_test_NP, cv2.COLOR_BGR2GRAY) 
 
    # denoising the image 
gaussian_blur_NP = cv2.GaussianBlur( 
    grayscale_resize_test_NP,(5, 5), 0) 

new_pre_res_W5KHN = pytesseract.image_to_string(gaussian_blur_NP, lang ='eng') 
filter_new_pre_res_W5KHN = "".join(new_pre_res_W5KHN.split()).replace(":", "").replace("-", "") 
print(filter_new_pre_res_W5KHN) 
