import os
from PIL import Image
import pilgram
from tkinter.filedialog import askopenfilename
import tkinter as tk



root = tk.Tk()
# Hide the window
root.withdraw()

# Now you are free to popup any dialog that you need
valgt_fil = askopenfilename()

root.destroy()

print("100")
print("500")
print("1000")
print("1080")
choice = input("hvem vil hu ha av de over")
if choice == ("100"):
    size = (100,100)
elif choice == ("500"):
    size = (500,500)
elif choice == ("1000"):
    size = (1000,1000)
elif choice == ("1080"):
    size = (1080,1920)
else: print("vi har ikke dette alternativet")



im = Image.open(valgt_fil)

with Image.open(valgt_fil) as im:
    im.thumbnail(size)
name = input("hvilket navn skal filen ha")
im.save(f"{name}.jpg")