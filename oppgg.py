import os
from PIL import Image
import pilgram
from tkinter.filedialog import askopenfilename
import tkinter as tk
from PIL import ImageOps



root = tk.Tk()
# Hide the window
root.withdraw()

# Now you are free to popup any dialog that you need
valgt_fil = askopenfilename()

root.destroy()

img = Image.open(valgt_fil)

border = (0, 30, 0, 30) # left, top, right, bottom
ImageOps.crop(img, border)

img.show()