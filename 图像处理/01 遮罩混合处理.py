from PIL import Image
img1 = Image.open("picture\cup.jpg")
img2 = Image.open("picture\杯子.png").resize(img1.size)
r, g, b = img2.split()
Image.composite(img1, img2, b).show()
