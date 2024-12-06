from PIL import Image, ImageEnhance, ImageTk
from tkinter import filedialog
import tkinter

tkinter.Tk().withdraw()
#note-This might have errors and it isnt made for commercial use
def main():
	def contrast_adjust():
		myimg = filedialog.askopenfilename()
		if myimg:
			img = Image.open(myimg)
			contrast_value = float(input("Enter contrast value (1.0 is normal, 0.0 to 2.0): "))
			en = ImageEnhance.Contrast(img)
			img = en.enhance(contrast_value)
			myimg=filedialog.asksaveasfile()
			img.show()

	def brightness_adjust():
		myimg = filedialog.askopenfilename()
		if myimg:
			img = Image.open(myimg)
			brightness_value = float(input("Enter brightness value (1.0 is normal, 0.0 to 2.0): "))
			en = ImageEnhance.Brightness(img)
			img = en.enhance(brightness_value)
			myimg = filedialog.asksaveasfile()
			img.show()


	def crop_adjust():
		myimg = filedialog.askopenfilename()
		if myimg:
			img = Image.open(myimg)
			print("Enter crop dimensions:")
			imgcropped = img.crop(box=(200, 200, 200, 200))
			myimg = filedialog.asksaveasfile()
			imgcropped.show()


	print("Welcome to image editor")

	while True:
		userinput = input("\nWhat aspect of the image would you like to edit? (B-Brightness, C-Contrast, CR-Crop, Q-Quit): ").upper()

		if userinput == "C":
			contrast_adjust()
		elif userinput == "B":
			brightness_adjust()
		elif userinput == "CR":
			crop_adjust()
		elif userinput == "Q":
			print("Thank you for using the image editor. Goodbye!")
			break
		else:
			print("Invalid input. Please try again.")
