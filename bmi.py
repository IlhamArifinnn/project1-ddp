import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Kalkulator BMI')
root.geometry('470x580+300+50')
root.resizable(False, False)
root.configure(bg='#f0f1f5')


def BMI():
    h = float(Height.get())
    w = float(Weight.get())

    m = h / 100
    bmi = round(float(w / m**2), 1)
    label1.config(text=bmi)

    if bmi <= 18.5:
        label2.config(text='Kurus!')
        label3.config(text='Berat badan Anda lebih rendah dari normal!')
    elif 18.5 < bmi <= 25:
        label2.config(text='Normal!')
        label3.config(text='Ini menunjukkan bahwa Anda sehat!')
    elif 25 < bmi <= 30:
        label2.config(text='Overweight!')
        label3.config(
            text='Ini menunjukkan bahwa seseorang \n sedikit overweight. \n Seorang dokter mungkin menyarankan untuk \n menurunkan berat badan untuk alasan kesehatan!')
    else:
        label2.config(text='Obesitas!')
        label3.config(
            text='Kesehatan mungkin berisiko. Jika tidak \n menurunkan berat badan!')


# Icon
image_icon = tk.PhotoImage(file='img/icon.png')
root.iconphoto(False, image_icon)

# Top
top = tk.PhotoImage(file="img/top.png")
top_image = tk.Label(root, image=top, background="#f0f1f5")
top_image.place(x=-10, y=-10)

# Bottom box
tk.Label(root, width=72, height=18, bg="lightblue").pack(side=tk.BOTTOM)

# Two boxes
box = tk.PhotoImage(file='img/box.png')
tk.Label(root, image=box).place(x=20, y=100)
tk.Label(root, image=box).place(x=240, y=100)

# Scale
scale = tk.PhotoImage(file='img/scale.png')
tk.Label(root, image=scale, bg='lightblue').place(x=20, y=310)

# Slider1
current_value = tk.DoubleVar()


def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    Height.set(get_current_value())

    size = int(float(get_current_value()))
    img = (Image.open('img/man.png'))
    resized_image = img.resize((50, 10 + size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=550 - size)
    secondimage.image = photo2


style = ttk.Style()
style.configure('TScale', background='white')
slider = ttk.Scale(root, from_=0, to=250, orient='horizontal', style='TScale', command=slider_changed,
                   variable=current_value)
slider.place(x=80, y=250)

# Slider2
current_value2 = tk.DoubleVar()


def get_current_value2():
    return '{: .2f}'.format(current_value2.get())


def slider_changed2(event):
    Weight.set(get_current_value2())


style2 = ttk.Style()
style2.configure('TScale', background='white')
slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style='TScale', command=slider_changed2,
                    variable=current_value2)
slider2.place(x=300, y=250)

# Entry box
Height = tk.StringVar()
Weight = tk.StringVar()
height = tk.Entry(root, textvariable=Height, width=5, font='arial 50', bg='#fff', fg='#000', bd=0, justify=tk.CENTER)
height.place(x=35, y=160)
Height.set(get_current_value())

weight = tk.Entry(root, textvariable=Weight, width=5, font='arial 50', bg='#fff', fg='#000', bd=0, justify=tk.CENTER)
weight.place(x=255, y=160)
Weight.set(get_current_value2())

# Man image
secondimage = tk.Label(root, bg='lightblue')
secondimage.place(x=70, y=530)

tk.Button(root, text='Lihat Laporan', width=15, height=2, font='arial 10 bold', bg='#1f6e68', fg='white',
          command=BMI).place(x=280, y=340)

label1 = tk.Label(root, font='arial 60 bold', bg='lightblue', fg='#fff')
label1.place(x=125, y=305)

label2 = tk.Label(root, font='arial 20 bold', bg='lightblue', fg='#3b3a3a')
label2.place(x=280, y=430)

label3 = tk.Label(root, font='arial 10 bold', bg='lightblue', fg='#fff')
label3.place(x=200, y=500)

root.mainloop()
