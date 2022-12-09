import tkinter as tk

window = tk.Tk()
window.title("DISAPPAERING TEXT WRRITING APP")
window.minsize(400,400)

counter = 0

def text_disappear():
    textbox.delete(1.0, tk.END)
    textbox.insert(tk.END, "")

def check_text():
    global counter, text
    if text == textbox.get(1.0, tk.END):
        if counter == 6:
            window.after(1000, text_disappear)
            counter -= 1
        window.after(1000, check_text)
        counter += 1
    else:
        window.after(1000, check_text)
        text = textbox.get(1.0, tk.END)
        counter = 0

title = tk.Label(window, text="Hi there, Welcome to the DISAPPEARING TEXT WRITING APP")
title.grid(row=0, column=1)

text = ""
textbox = tk.Text(height=10, width=35, yscrollcommand=True)
textbox.focus()
textbox.grid(row=3, column=1, padx=10, pady=10)

window.after(1000, check_text)
window.mainloop()