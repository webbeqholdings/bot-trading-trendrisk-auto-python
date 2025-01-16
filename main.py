import cv2 
import pytesseract
import matplotlib.pyplot as plt
from IPython.display import Image
from pylab import rcParams
import numpy as np
from pprint import pprint
from pytesseract import Output
import os
import time
from PIL import Image

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
print('Shine')
rcParams['figure.figsize'] = 8, 16
file_name = "img/test.png"

folder_today = "img/2025-01-16/Screen Laptop"
output_folder = "img/2025-01-16/crop-size/"
imgX = 20
imgY = 20
imgWidth = 713
imgHeight = 270

def get_image_files(folder_path):
    # Lọc các file có đuôi là hình ảnh
    return [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

def delete_all_files_in_folder(folder):
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # Xóa file hoặc liên kết
                print(f"Đã xóa: {file_path}")
            elif os.path.isdir(file_path):
                os.rmdir(file_path)  # Xóa thư mục rỗng nếu có
        except Exception as e:
            print(f"Không thể xóa {file_path}. Lỗi: {e}")

def ensure_folder_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Đã tạo thư mục: {folder}")
    else:
        print(f"Thư mục đã tồn tại: {folder}")

def process_files_every_15_seconds():
    while True:
        image_files = get_image_files(folder_today)
        

        ensure_folder_exists(output_folder)
        delete_all_files_in_folder(output_folder)

        for file_name in image_files:
            print(f"Xử lý file: {folder_today + '/' + file_name}")
            img_path = folder_today + '/' + file_name
            img = Image.open(img_path)
            _width, _height = img.size
            cropped_img = img.crop((_width/3 + 80 , _height/3 + 70, (_width/3 + 550), (_height/3 + 220)))

            cropped_img_path = os.path.join(output_folder, file_name)
            cropped_img.save(cropped_img_path)

        # --------------------------------------------------
        cropped_files = get_image_files('img/2025-01-16/crop-size')

        for file_name in cropped_files:
            img_cv2 = cv2.imread('img/2025-01-16/crop-size/' + file_name)
            plt.imshow(cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB))
            # plt.show()
            text_out = pytesseract.image_to_string(img_cv2)
            
            print(f"Text in {file_name} = {text_out}")


        # Chờ 15 giây trước khi lặp lại toàn bộ vòng lặp
        time.sleep(15)

print("process_files_every_15_seconds...")
process_files_every_15_seconds()


# ====================================================================
# file_name="img/2025-01-16/crop-size/2025-01-16_16-37-06.815.png"
# file_name="img/test.png"
# file_name="img/test2.png"
# img = cv2.imread(file_name)
# # plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# # plt.show() # POP UP IMAGE
# text_out = pytesseract.image_to_string(img)
# print(text_out)