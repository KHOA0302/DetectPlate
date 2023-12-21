import cv2
from matplotlib import pyplot as plt 
from detectChar import detectChar
from detectChar import draw_and_fill
from detectPlate import detectPlate
  
if __name__ == '__main__':
    filename = './imgs/whose-number-plate-is-this.jpg'
    image = cv2.imread(filename)
    originalImg  = image
    
    # top_left, bottom_right = detectPlate(filename)
    # image = draw_and_fill(image, top_left, bottom_right)
    # char = detectChar(image)
    # print(char)

    fig = plt.figure(figsize=(10, 7))  
    rows = 2
    columns = 3

    Image1 = originalImg
    Image2 = cv2.imread('tensorImg.jpg') 
    Image3 = cv2.imread('drawAndFill.jpg') 
    Image4 = cv2.imread('pretreatment.jpg') 
    Image5 = cv2.imread('resultImg.jpg') 
    
    fig.add_subplot(rows, columns, 1) 

    plt.imshow(Image1) 
    plt.axis('off') 
    plt.title("Original") 
    
    fig.add_subplot(rows, columns, 2) 
    
    plt.imshow(Image2) 
    plt.axis('off') 
    plt.title("Detect plate") 
    
    fig.add_subplot(rows, columns, 4) 
    
    plt.imshow(Image3) 
    plt.axis('off') 
    plt.title("Pretreatment") 
    
    fig.add_subplot(rows, columns, 5) 
    
    plt.imshow(Image4) 
    plt.axis('off') 
    plt.title("Pretreatment") 

    fig.add_subplot(rows, columns, 6) 
    
    plt.imshow(Image5) 
    plt.axis('off') 
    plt.title("Detect char") 

    plt.show() 