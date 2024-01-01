import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Kalkulator BMI')
root.geometry('470x580+300+50')
root.resizable(False, False)
root.configure(bg='#f0f1f5')


def BMI():
    tinggi = float(Height.get())
    berat = float(Weight.get())

    massa = tinggi / 100
    bmi = round(float(berat / massa**2), 1)
    label1.config(text=bmi)

    if bmi <= 18.5:
        label2.config(text='Kurus!')
        label3.config(text='Berat badan Anda lebih rendah \n dari normal!')
    elif 18.5 < bmi <= 25:
        label2.config(text='Normal!')
        label3.config(text='Ini menunjukkan bahwa Anda sehat!')
    elif 25 < bmi <= 30:
        label2.config(text='Gemuk!')
        label3.config(
            text='Ini menunjukkan bahwa Anda \n Gemuk!')
    else:
        label2.config(text='Obesitas!')
        label3.config(
            text='Kesehatan mungkin berisiko. Jika tidak \n menurunkan berat badan!')


# Icon judul
image_icon = tk.PhotoImage(file='img/icon.png')
root.iconphoto(False, image_icon)

# Judul Heading
top = tk.PhotoImage(file="img/top.png")
top_image = tk.Label(root, image=top, background="#f0f1f5")
top_image.place(x=-10, y=-10)

# label tinggi dan berat
tk.Label(root, text='Tinggi (cm)', font='arial 12 bold').place(x=80, y=75)
tk.Label(root, text='Berat (kg)', font='arial 12 bold').place(x=310, y=75)

# Frame Bawah
tk.Label(root, width=72, height=18, bg="lightblue").pack(side=tk.BOTTOM)


# Kotak Slider
box = tk.PhotoImage(file='img/box.png')
tk.Label(root, image=box).place(x=20, y=100)
tk.Label(root, image=box).place(x=240, y=100)


# Ukuran
scale = tk.PhotoImage(file='img/scale.png')
tk.Label(root, image=scale, bg='lightblue').place(x=20, y=315)

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
    secondimage.place(x=70, y=560 - size)
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
secondimage.place(x=70, y=550)

tk.Button(root, text='Lihat Laporan', width=20, height=2, font='arial 10 bold', bg='#1f6e68', fg='white',
          command=BMI).place(x=230, y=320)

label1 = tk.Label(root, font='arial 44 bold', bg='lightblue', fg='#fff')
label1.place(x=245, y=380)

label2 = tk.Label(root, font='arial 16 bold', bg='lightblue', fg='#3b3a3a')
label2.place(x=270, y=470)

label3 = tk.Label(root, font='arial 10 bold', bg='lightblue', fg='#3b3a3a')
label3.place(x=200, y=500)

root.mainloop()
