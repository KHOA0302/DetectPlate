from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2
from detectChar import detectChar
from detectChar import draw_and_fill
from detectPlate import detectPlate

# setup
window = tk.Tk()
    
def show_full_image_bg(event):
        global resized_tk_bg
        # current ratio 
        canvas_ratio_bg = event.width / event.height
        # get coordinates 
        if canvas_ratio_bg > image_ratio_bg: # canvas is wider than the image
            height = int(event.height)
            width = int(height * image_ratio_bg) 
        else: # canvas is narrower than the image
            width = int(event.width) 
            height = int(width / image_ratio_bg)
        resized_image_bg = image_original_bg.resize((width, height))
        resized_tk_bg = ImageTk.PhotoImage(resized_image_bg)
        canvas_bg.create_image(
            int(event.width / 2),
            int(event.height / 2),
            anchor = 'center',
            image = resized_tk_bg)
        
def file_dialog():
    filename = filedialog.askopenfilename(
        initialdir="/Downloads", title="Select A File",
        filetype=(("jpeg files", "*.jpg"), ("all files", "*.*"))
    )
    top_left, bottom_right = detectPlate(filename)
    img = Image.open(filename)  
    photo = ImageTk.PhotoImage(img)
    return filename, top_left, bottom_right

def use_photo_image():
    def show_full_image(event):
        global resized_tk
        # current ratio 
        canvas_ratio = event.width / event.height
        # get coordinates 
        if canvas_ratio > image_ratio: # canvas is wider than the image
            height = int(event.height)
            width = int(height * image_ratio) 
        else: # canvas is narrower than the image
            width = int(event.width) 
            height = int(width / image_ratio)
        resized_image = image_original.resize((width, height))
        resized_tk = ImageTk.PhotoImage(resized_image)
        canvas.create_image(
            int(event.width / 2),
            int(event.height / 2),
            anchor = 'center',
            image = resized_tk)

    def show_full_image_2(event):
        global resized_tk_2
        # current ratio 
        canvas_ratio_2 = event.width / event.height
        # get coordinates 
        if canvas_ratio_2 > image_ratio_2: # canvas is wider than the image
            height = int(event.height)
            width = int(height * image_ratio_2) 
        else: # canvas is narrower than the image
            width = int(event.width) 
            height = int(width / image_ratio_2)
        resized_image_2 = image_original_2.resize((width, height))
        resized_tk_2 = ImageTk.PhotoImage(resized_image_2)
        canvas_2.create_image(
            int(event.width / 2),
            int(event.height / 2),
            anchor = 'center',
            image = resized_tk_2)
     
    #Change GRID LAYOUT 
    window.columnconfigure((0), weight = 1, uniform = 'a')
    window.rowconfigure((0), weight = 1,  uniform = 'a')

    def show_full_image_ld(event):
        global resized_tk_ld
        # current ratio 
        canvas_ratio_ld = event.width / event.height
        # get coordinates 
        if canvas_ratio_ld > image_ratio_ld: # canvas is wider than the image
            height = int(event.height)
            width = int(height * image_ratio_ld) 
        else: # canvas is narrower than the image
            width = int(event.width) 
            height = int(width / image_ratio_ld)
        resized_image_ld = image_original_ld.resize((width, height))
        resized_tk_ld = ImageTk.PhotoImage(resized_image_ld)
        canvas_bg.create_image(
            int(event.width / 2),
            int(event.height / 2),
            anchor = 'center',
            image = resized_tk_ld)

    image_original_ld = Image.open('./imgs/loading.jpg') 
    image_ratio_ld = image_original_ld.size[0] / image_original_ld.size[1]
    image_tk_bg = ImageTk.PhotoImage(image_original_ld)
    canvas_bg = tk.Canvas(window, background = 'black', bd = 0, highlightthickness = 0, relief = 'ridge')
    canvas_bg.grid(column = 0, columnspan = 5, row = 0, rowspan=5, sticky = 'nsew')
    canvas_bg.bind('<Configure>', show_full_image_ld)

    #Input NAME IMG
    filename, top_left, bottom_right = file_dialog()

    window.columnconfigure((0,1,2,3,4), weight = 1, uniform = 'a')
    window.rowconfigure((0,1,2,3,4), weight = 1,  uniform = 'a')

    canvas_bg.grid_remove() 
    #Display CAR
    image_original = Image.open(filename) 
    image_ratio = image_original.size[0] / image_original.size[1]
    image_tk = ImageTk.PhotoImage(image_original)

    canvas = tk.Canvas(window, background = '#282A36', bd = 0, highlightthickness = 0, relief = 'ridge')
    canvas.grid(column = 2, columnspan = 3, row = 0, rowspan=4, sticky = 'nsew')
    canvas.bind('<Configure>', show_full_image)

    # Display PLATE
    image_original_2 = image_original.crop((top_left[0],  top_left[1], bottom_right[0], bottom_right[1]))
    image_ratio_2 = image_original_2.size[0] / image_original_2.size[1]
    image_tk_2 = ImageTk.PhotoImage(image_original_2)

    canvas_2 = tk.Canvas(window, background = '#282A36', bd = 0, highlightthickness = 0, relief = 'ridge')
    canvas_2.grid(column = 0, columnspan = 2, row = 0, rowspan=3, sticky = 'nsew')
    canvas_2.bind('<Configure>', show_full_image_2)
    
    #mess
    image_mess = draw_and_fill(cv2.imread(filename), top_left, bottom_right)
    # image_mess = sharpen_image(image_mess)
    message = detectChar(image_mess)
    canvas_3 = tk.Canvas(window, background = '#282A36', bd = 0, highlightthickness = 0, relief = 'ridge')
    canvas_3.create_text(72, 12, anchor='nw', text=message, fill='white', font=('Arial', 24))
    canvas_3.grid(column = 0, columnspan = 2, row = 3, rowspan=1, sticky = 'nsew')

    #EXIT btn
    button_frame = ttk.Frame(window)
    button_ctk = ctk.CTkButton(button_frame, text = 'Thoát', compound = 'left', command= window.destroy)
    button_ctk.pack(pady = 10)
    button_frame.grid(column = 0, row = 4, columnspan=2, rowspan=1, sticky = 'nsew')
   
    #Change BROW_IMG_BOX position
    labelFrame = ttk.LabelFrame(window, text="Open File")
    labelFrame.grid(column=2, row=4,  columnspan=3, padx=20, pady=20)
    button = ttk.Button(labelFrame, text="Browse A File", command=use_photo_image)
    button.grid(column=2, row=4,  columnspan=3)

window.geometry('600x400')
window.title('Plate detection')

# grid layout
window.columnconfigure((0,1,2,3,4), weight = 1, uniform = 'a')
window.rowconfigure((0,1,2,3,4), weight = 1,  uniform = 'a')

#background
image_original_bg = Image.open('./imgs/bg.jpg') 
image_ratio_bg = image_original_bg.size[0] / image_original_bg.size[1]
image_tk_bg = ImageTk.PhotoImage(image_original_bg)
canvas_bg = tk.Canvas(window, background = '#282A36', bd = 0, highlightthickness = 0, relief = 'ridge')
canvas_bg.grid(column = 0, columnspan = 5, row = 0, rowspan=5, sticky = 'nsew')
canvas_bg.bind('<Configure>', show_full_image_bg)

def removeGridBg():
    canvas_bg.grid_remove()
#brow img
labelFrame = ttk.LabelFrame(window, text="Open File")
labelFrame.grid(column=1, row=2, columnspan=3,padx=20, pady=20)
button = ttk.Button(labelFrame, text="Browse A File", command=lambda: [removeGridBg(), use_photo_image()])
button.grid(column=1, row=2, columnspan=3) 


# run
window.mainloop()


