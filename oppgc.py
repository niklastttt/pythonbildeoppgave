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

root.destroy()

im = Image.open(valgt_fil)

print("V=venstre H=høyre O=oppned")
choi = (input("hvliking type rotasjon vil du ha?"))

if choi == ("V"):
    rotated_im = im.rotate(90)  # Rotate the image by 90 degrees clockwise
elif choi == ("H"):
    rotated_im = im.rotate(270)
elif choi == ("O"):
    rotated_im = im.rotate(180)
else:
    print("dette forstår jeg ikke")

name = input("hva skal filen hete")
rotated_im.save(f"{name}.jpg")


