import os
from PIL import Image
import pilgram
from tkinter.filedialog import askopenfilename
import tkinter as tk

# Create the window
root = tk.Tk()
# Hide the window
root.withdraw()

# Now you are free to popup any dialog that you need
valgt_fil = askopenfilename()

im = Image.open(valgt_fil)

print("hvilket filter")
choice = input("insta eller moon")
if choice == ("moon"):
    name = input("hva skal den hete")
    pilgram.moon(im).save(f"{name}.jpg")
elif choice == ("insta"):
    name2 = input("hva skal den hete")
    pilgram._1977(im).save(f"{name2}.jpg")


