import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pilgram
from tkinter.filedialog import askopenfilename
import tkinter as tk

root = tk.Tk()

root.withdraw()

valgt_fil = askopenfilename()

root.destroy()

im = Image.open(valgt_fil)


# Open the desired Image you want to add text on
i = Image.open(valgt_fil)

# To add 2D graphics in an image call draw Method

Im = ImageDraw.Draw(i)

choice = input("hvilken tekst vil du ha")

Im.text((255,25), (choice), (255,0,0))


names = input("hva skal filen hete")
i.save(f"{names}.jpg")
    