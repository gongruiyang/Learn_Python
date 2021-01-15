from PIL import Image
img1 = Image.open("picture\cup.jpg")
img_rotate = img1.rotate(90)
img_rotate.show()