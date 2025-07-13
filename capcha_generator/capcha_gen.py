from io import BytesIO
from tkinter import *
from random import randint
from tkinter import messagebox
from captcha.image import ImageCaptcha
from PIL import ImageTk, Image

image = ImageCaptcha()

# Generate first CAPTCHA
captcha_text = str(randint(100000, 999999))
data = image.generate(captcha_text)
image.write(captcha_text, 'out.png')

def verify():
    user_input = t1.get("0.0", END).strip()
    if user_input == captcha_text:
        messagebox.showinfo("Success", "Verified")
    else:
        messagebox.showinfo("Alert", "Not verified")
        refresh()

def refresh():
    global captcha_text, photo
    captcha_text = str(randint(100000, 999999))
    image.write(captcha_text, 'out.png')
    img = Image.open("out.png")
    photo = ImageTk.PhotoImage(img)
    l1.config(image=photo)
    l1.image = photo  # keep reference!

# GUI Setup
root = Tk()
root.title("Captcha Generator")

img = Image.open("out.png")
photo = ImageTk.PhotoImage(img)

l1 = Label(root, image=photo, height=400, width=600)
t1 = Text(root, height=4, width=30)
b1 = Button(root, text="Submit", command=verify)
b2 = Button(root, text="Refresh", command=refresh)

l1.pack(pady=10)
t1.pack()
b1.pack(pady=5)
b2.pack()

root.mainloop()
