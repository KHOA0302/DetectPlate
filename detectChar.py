import easyocr
import matplotlib.pyplot as plt
import numpy as np
import cv2

def draw_and_fill(image, top_left, bottom_right, fill_color=(0, 0, 255), border_color=(0, 255, 0), thickness=2):
    mask = np.zeros_like(image)
    cv2.rectangle(mask, top_left, bottom_right, border_color, thickness=cv2.FILLED)
    cv2.rectangle(image, top_left, bottom_right, border_color, thickness)
    image_with_filled_area = cv2.bitwise_and(image, mask)
    cv2.imwrite('drawAndFill.jpg', image_with_filled_area)
    return image_with_filled_area

def detectChar(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.GaussianBlur(image, (3,3), 0)
    image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                           cv2.THRESH_BINARY, 31, 1)
    image = cv2.bitwise_not(image)
    cv2.imwrite('pretreatment.jpg', image)
    
    reader = easyocr.Reader(['en'], gpu=False)
    text_ = reader.readtext(image)
    threshold = 0.25
    chars = ''
    for t_, t in enumerate(text_):
        print(t)
        chars += t[1]
        bbox, text, score = t
        if score > threshold:
            cv2.rectangle(image, bbox[0], bbox[2], (0, 255, 0), 5)
            cv2.putText(image, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

    cv2.imwrite('resultImg.jpg', image)
    characters_to_remove = "{}[],*~`!@#$%^&*()-_+=;:'\"<>.,?/"
    translation_table = str.maketrans({char: None for char in characters_to_remove})
    chars = chars.translate(translation_table)
    return chars
   