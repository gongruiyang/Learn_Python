from PIL import Image
img1 = Image.open("picture\cup.jpg")
img2 = img1.copy()
img2.show()
print(id(img1))
print(id(img2))
