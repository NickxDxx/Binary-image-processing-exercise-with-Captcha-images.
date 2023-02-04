import pytesseract as pt
from PIL import Image
from PIL import ImageFilter
import csv
import numpy as np
from cv2 import cv2





def start():
    screen_shot = Image.open('screen_shot .png')
    image = screen_shot.crop((350, 660, 590,730))
    image_1 = image.convert("1")
    image.show()
    image_1.show()
    '''Crop the image to Captcha size'''
    # image_1 = image.convert('L').convert("1").filter()
    # image_1.show()

    '''Use Python algoritm convert pixel data from single list to 2d array accroding to pixel size (Height and length)'''
    list1 = list(image_1.getdata())
    final_list = []
    for time in range(0,70):
        row = list1[:240]
        final_list.append(row)
        del list1[:240]
    
    # for x in final_list:
    #     with open("Original one1 .csv", 'a', newline="") as file:
    #         writer = csv.writer(file)
    #         writer.writerow(x)

    filtered_single_0_array = final_list
    '''black 0, white 255'''
    
    '''detect pixel(black) relationship in a 3x3 square with other pixel, elimate single pixel with no nearby pixels, first step'''
    for x in range(len(final_list)):
        for y in range(len(final_list[x])):
            count = 0
            if final_list[x][y] == 0:
                try:
                    if final_list[x][y-1] == 0:
                        count +=1
                except:
                    # no left
                    pass
                try:
                    if final_list[x][y+1] == 0:
                        count+=1
                except:
                    # no right
                    pass
                try:
                    if final_list[x-1][y] == 0:
                        count+=1
                except:
                    # no up
                    pass
                try:
                    if final_list[x+1][y] == 0:
                        count += 1
                except:
                    # no down
                    pass
                    
                '''try crossline pixel'''
                try:
                    if  final_list[x - 1][y - 1] == 0:
                        count += 1
                except:
                    pass
                try:
                    if  final_list[x - 1][y + 1] == 0:
                        count += 1
                except:
                    pass
                try:
                    if  final_list[x + 1][y + 1] == 0:
                        count += 1
                except:
                    pass
                try:
                    if  final_list[x + 1][y - 1] == 0:
                        count += 1
                except:
                    pass
                if count >=1 :
                    final_list[x][y] = 0
                else:
                    final_list[x][y] = 255
    image2 = Image.fromarray(np.uint8(final_list), 'L')
    image2.show()
    #
    # for x in range(len(final_list)):
    #     for y in range(len(final_list[x])):
    #         count = 0
    #         if final_list[x][y] == 255:
    #             try:
    #                 if final_list[x][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if final_list[x][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x - 1][y] == 0:
    #                     count += 1
    #             except:
    #                 # no up
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x - 1][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x - 1][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             if count >= 5:
    #                 final_list[x][y] = 0
    
    '''Show white holes Captcha filled inside characters, 3x3 box over 6 black neighbours'''

    for x in range(len(final_list)):
        for y in range(len(final_list[x])):
            count = 0
            if final_list[x][y] == 255:
                try:
                    if final_list[x][y-1] == 0:
                        count +=1
                except:
                    # no left
                    pass
                try:
                    if final_list[x][y+1] == 0:
                        count+=1
                except:
                    # no right
                    pass
                try:
                    if final_list[x-1][y] == 0:
                        count+=1
                except:
                    # no up
                    pass
                try:
                    if final_list[x+1][y] == 0:
                        count += 1
                except:
                    # no down
                    pass
                '''try crossline pixel'''
                try:
                    if  final_list[x - 1][y - 1] == 0:
                        count += 1
                except:
                    pass
                try:
                    if  final_list[x - 1][y + 1] == 0:
                        count += 1
                except:
                    pass
                try:
                    if  final_list[x + 1][y + 1] == 0:
                        count += 1
                except:
                    pass
                try:
                    if  final_list[x + 1][y - 1] == 0:
                        count += 1
                except:
                    pass
                if count >=6 :
                    final_list[x][y] = 255
                else:
                    final_list[x][y] = 0
    image2 = Image.fromarray(np.uint8(final_list), 'L')
    image2.show()
    for x in range(len(final_list)):
        for y in range(len(final_list[x])):
            if final_list[x][y] == 0:
                final_list[x][y] =244
            if final_list[x][y] == 255:
                final_list[x][y] =0
            if final_list[x][y] == 244:
                final_list[x][y] =255
:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x - 1][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x - 1][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             if count >= 5:
    #                 final_list[x][y] = 0
    # for x in range(len(final_list)):
    #     for y in range(len(final_list[x])):
    #         count = 0
    #         if final_list[x][y] == 255:
    #             try:
    #                 if final_list[x][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if final_list[x][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x - 1][y] == 0:
    #                     count += 1
    #             except:
    #                 # no up
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x - 1][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x - 1][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             if count >= 5:
    #                 final_list[x][y] = 0

    # for x in range(len(final_list)):
    #     for y in range(len(final_list[x])):
    #         count = 0
    #         if final_list[x][y] == 0:
    #             try:
    #                 if final_list[x][y-1] == 0:
    #                     count +=1
    #             except:
    #                 # no left
    #                 pass
    #             try:
    #                 if final_list[x][y+1] == 0:
    #                     count+=1
    #             except:
    #                 # no right
    #                 pass
    #             try:
    #                 if final_list[x-1][y] == 0:
    #                     count+=1
    #             except:
    #                 # no up
    #                 pass
    #             try:
    #                 if final_list[x+1][y] == 0:
    #                     count += 1
    #             except:
    #                 # no down
    #                 pass
    #             '''try crossline pixel'''
    #             try:
    #                 if  final_list[x - 1][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x - 1][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             if count >=2 :
    #                 final_list[x][y] = 0
    #             else:
    #                 final_list[x][y] = 255
    # #
    # for x in final_list:
    #     with open("varient filter 1s .csv", 'a', newline="") as file:
    #         writer = csv.writer(file)
    #         writer.writerow(x)
    # #
    
    
    image2 = Image.fromarray(np.uint8(final_list), 'L').filter(ImageFilter.GaussianBlur(1.2))
    image2.show()
    pt.pytesseract.tesseract_cmd = 'C:/Projects/Garbage/tesseract.exe'
    text1 = pt.image_to_string(image2,config='--psm 6')
    print("Read test 1  "+ text1)
    
    
    
    
    # list1 = list(image2.getdata())
    # final_list = []
    # for time in range(0,70):
    #     row = list1[:240]
    #     final_list.append(row)
    #     del list1[:240]
    # # for x in final_list:
    # #     with open("varient filter 2s .csv", 'a', newline="") as file:
    # #         writer = csv.writer(file)
    # #         writer.writerow(x)
    # image2.save("Pillow.png")
    # image3 = cv2.imread("Pillow.png", cv2.IMREAD_GRAYSCALE)
    # contours, hierarchy = cv2.findContours(image3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # for contour in contours:
    #     if cv2.contourArea(contour) < 300:
    #         cv2.drawContours(thresh, contour, -1, (255, 255, 255), 3)
    # cv2.imshow("1", thresh)
    # cv2.waitKey()
    # # image4 = Image.fromarray(np.uint8(final_list), 'L').filter(ImageFilter.MinFilter)
    # # image4.show()
    #
    # pt.pytesseract.tesseract_cmd = 'C:/Projects/Garbage/tesseract.exe'
    # text1 = pt.image_to_string(image2,config='--psm 6')
    # print("Read test 1  "+ text1)

start()import pytesseract as pt
from PIL import Image
from PIL import ImageFilter
import csv
import numpy as np
from cv2 import cv2





def start():
    screen_shot = Image.open('screen_shot .png')
    image = screen_shot.crop((350, 660, 590,730))
    image_1 = image.convert("1")
    image.show()
    image_1.show()
    # image_1 = image.convert('L').convert("1").filter()
    # image_1.show()


    list1 = list(image_1.getdata())
    final_list = []
    for time in range(0,70):
        row = list1[:240]
        final_list.append(row)
        del list1[:240]
    # for x in final_list:
    #     with open("Original one1 .csv", 'a', newline="") as file:
    #         writer = csv.writer(file)
    #         writer.writerow(x)

    filtered_single_0_array = final_list
    '''black 0, white 255'''
    for x in range(len(final_list)):
        for y in range(len(final_list[x])):
            count = 0
            if final_list[x][y] == 0:
                try:
                    if final_list[x][y-1] == 0:
                        count +=1
                except:
                    # no left
                    pass
                try:
                    if final_list[x][y+1] == 0:
                        count+=1
                except:
                    # no right
                    pass
                try:
                    if final_list[x-1][y] == 0:
                        count+=1
                except:
                    # no up
                    pass
                try:
                    if final_list[x+1][y] == 0:
                        count += 1
                except:
                    # no down
                    pass
                '''try crossline pixel'''
                try:
                    if  final_list[x - 1][y - 1] == 0:
                        count += 1
                except:
                    pass
                try:
                    if  final_list[x - 1][y + 1] == 0:
                        count += 1
                except:
                    pass
                try:
                    if  final_list[x + 1][y + 1] == 0:
                        count += 1
                except:
                    pass
                try:
                    if  final_list[x + 1][y - 1] == 0:
                        count += 1
                except:
                    pass
                if count >=1 :
                    final_list[x][y] = 0
                else:
                    final_list[x][y] = 255
    image2 = Image.fromarray(np.uint8(final_list), 'L')
    image2.show()
    #
    # for x in range(len(final_list)):
    #     for y in range(len(final_list[x])):
    #         count = 0
    #         if final_list[x][y] == 255:
    #             try:
    #                 if final_list[x][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if final_list[x][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x - 1][y] == 0:
    #                     count += 1
    #             except:
    #                 # no up
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x - 1][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x - 1][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             if count >= 5:
    #                 final_list[x][y] = 0

    '''As the captcha image be fiex with holes all over the image, inside the text skeleton it also be filled with white holes'''
    '''Find black pixels skeletion, detect each white pixel has over 6 black neighboours and keep them'''
    
    for x in range(len(final_list)):
        for y in range(len(final_list[x])):
            count = 0
            if final_list[x][y] == 255:
                try:
                    if final_list[x][y-1] == 0:
                        count +=1
                except:
                    # no left
                    pass
                try:
                    if final_list[x][y+1] == 0:
                        count+=1
                except:
                    # no right
                    pass
                try:
                    if final_list[x-1][y] == 0:
                        count+=1
                except:
                    # no up
                    pass
                try:
                    if final_list[x+1][y] == 0:
                        count += 1
                except:
                    # no down
                    pass
                '''try crossline pixel'''
                try:
                    if  final_list[x - 1][y - 1] == 0:
                        count += 1
                except:
                    pass
                try:
                    if  final_list[x - 1][y + 1] == 0:
                        count += 1
                except:
                    pass
                try:
                    if  final_list[x + 1][y + 1] == 0:
                        count += 1
                except:
                    pass
                try:
                    if  final_list[x + 1][y - 1] == 0:
                        count += 1
                except:
                    pass
                if count >=6 :
                    final_list[x][y] = 255
                else:
                    final_list[x][y] = 0
    image2 = Image.fromarray(np.uint8(final_list), 'L')
    image2.show()
    for x in range(len(final_list)):
        for y in range(len(final_list[x])):
            if final_list[x][y] == 0:
                final_list[x][y] =244
            if final_list[x][y] == 255:
                final_list[x][y] =0
            if final_list[x][y] == 244:
                final_list[x][y] =255
                
                
                
                
    # for x in range(len(final_list)):
    #     for y in range(len(final_list[x])):
    #         count = 0
    #         if final_list[x][y] == 255:
    #             try:
    #                 if final_list[x][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if final_list[x][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x - 1][y] == 0:
    #                     count += 1
    #             except:
    #                 # no up
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x - 1][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x - 1][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             if count >= 5:
    #                 final_list[x][y] = 0
    # for x in range(len(final_list)):
    #     for y in range(len(final_list[x])):
    #         count = 0
    #         if final_list[x][y] == 255:
    #             try:
    #                 if final_list[x][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if final_list[x][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x - 1][y] == 0:
    #                     count += 1
    #             except:
    #                 # no up
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x - 1][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x - 1][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             if count >= 5:
    #                 final_list[x][y] = 0

    # for x in range(len(final_list)):
    #     for y in range(len(final_list[x])):
    #         count = 0
    #         if final_list[x][y] == 0:
    #             try:
    #                 if final_list[x][y-1] == 0:
    #                     count +=1
    #             except:
    #                 # no left
    #                 pass
    #             try:
    #                 if final_list[x][y+1] == 0:
    #                     count+=1
    #             except:
    #                 # no right
    #                 pass
    #             try:
    #                 if final_list[x-1][y] == 0:
    #                     count+=1
    #             except:
    #                 # no up
    #                 pass
    #             try:
    #                 if final_list[x+1][y] == 0:
    #                     count += 1
    #             except:
    #                 # no down
    #                 pass
    #             '''try crossline pixel'''
    #             try:
    #                 if  final_list[x - 1][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x - 1][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y + 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             try:
    #                 if  final_list[x + 1][y - 1] == 0:
    #                     count += 1
    #             except:
    #                 pass
    #             if count >=2 :
    #                 final_list[x][y] = 0
    #             else:
    #                 final_list[x][y] = 255
    # #
    # for x in final_list:
    #     with open("varient filter 1s .csv", 'a', newline="") as file:
    #         writer = csv.writer(file)
    #         writer.writerow(x)
    # #
    
    
    image2 = Image.fromarray(np.uint8(final_list), 'L').filter(ImageFilter.GaussianBlur(1.2))
    image2.show()
    pt.pytesseract.tesseract_cmd = 'C:/Projects/Garbage/tesseract.exe'
    text1 = pt.image_to_string(image2,config='--psm 6')
    print("Read test 1  "+ text1)
    
    
    # list1 = list(image2.getdata())
    # final_list = []
    # for time in range(0,70):
    #     row = list1[:240]
    #     final_list.append(row)
    #     del list1[:240]
    # # for x in final_list:
    # #     with open("varient filter 2s .csv", 'a', newline="") as file:
    # #         writer = csv.writer(file)
    # #         writer.writerow(x)
    # image2.save("Pillow.png")
    # image3 = cv2.imread("Pillow.png", cv2.IMREAD_GRAYSCALE)
    # contours, hierarchy = cv2.findContours(image3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # for contour in contours:
    #     if cv2.contourArea(contour) < 300:
    #         cv2.drawContours(thresh, contour, -1, (255, 255, 255), 3)
    # cv2.imshow("1", thresh)
    # cv2.waitKey()
    # # image4 = Image.fromarray(np.uint8(final_list), 'L').filter(ImageFilter.MinFilter)
    # # image4.show()
    #
    # pt.pytesseract.tesseract_cmd = 'C:/Projects/Garbage/tesseract.exe'
    # text1 = pt.image_to_string(image2,config='--psm 6')
    # print("Read test 1  "+ text1)

start()
