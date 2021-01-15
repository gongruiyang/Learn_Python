from PIL import Image
img1 = Image.open("picture\cup.jpg")
# img1_bigger = Image.eval(img1, lambda x: x / 10)
# print(img1.getpixel((100,100)))
# print(img1_bigger.getpixel((100,100)))
# img1_bigger.show()
print(img1.size)
img1.thumbnail((200, 100))
print(img1.size)
