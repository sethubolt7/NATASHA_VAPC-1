import tkinter as tk
from tkinter import Tk

from PIL import Image, ImageTk

root: Tk = tk.Tk()
root.geometry("350x780")
root.title("NATASHA")
button_frame = tk.Frame(root, bg="#080721")

text_field3 = tk.Text(button_frame, height=1, width=40)
text_field3.pack(side="top", pady=10)

text_field1 = tk.Text(button_frame, height=2, width=40)
text_field1.pack(side="top", pady=10)

text_field2 = tk.Text(button_frame, height=18, width=50)
text_field2.pack(side="bottom", pady=10)

text_field1.insert(tk.END, "Hello, World!")
text_field3.insert(tk.END, "lisetening......")

# Delete the text from the widget
# text_field1.delete('1.0', tk.END)
button_frame.pack(side="bottom", pady=0)

gif = Image.open('ai.gif')
tkimage = ImageTk.PhotoImage(gif.convert('RGBA'))

label = tk.Label(root, image=tkimage)
label.pack()
button_frame.lift()


def update_label(index):
    global tkimage
    gif.seek(index)
    tkimage = ImageTk.PhotoImage(gif.convert('RGBA'))
    label.config(image=tkimage)
    root.after(50, update_label, (index + 1) % gif.n_frames)


root.after(0, update_label, 1)

root.mainloop()
