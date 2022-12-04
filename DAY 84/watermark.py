import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

FONT_NAME = "Courier"
YELLOW = "#f7f5dd"
#-----------function-------------#
def add_watermark():
    image = filedialog.askopenfile(initialdir="Pictures", title="Select an image")
    open_image = Image.open(image)

    image_width, image_height = open_image.size
    draw = ImageDraw.Draw(open_image)

    font_size = int(image_width/6)

    font = ImageFont.truetype('courier.ttf', font_size)

    x, y = int(image_width/2), int(image_height/1.75)

    draw.text((x,y), font=font, fill='#f7f5dd', stroke_width=5, anchor='ms')

    open_image.show()



#-------------------UI Setup---------------#

window = tk.Tk()
#window.geometry("600x500")
window.config(padx=35, pady=20)
window.title("Welcome to Sacred's Watermark App")

#label
app_label = tk.Label(text="Add Watermark to your picture", font=(FONT_NAME, 15))
app_label.grid(column=0, row=0)


text = tk.Text(window, height=1, width=30)
text.grid(row=1, column=0)

#button
photo_label = tk.Button(text="Add Photo", width=12, command=add_watermark, font=(FONT_NAME, 12))
photo_label.grid(column=0, row=3)









window.mainloop()