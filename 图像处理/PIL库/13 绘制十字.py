from PIL import Image, ImageDraw
img = Image.open('picture\cup.jpg')
pen = ImageDraw.Draw(img)
pen.line([0, 0, img.width, img.height], fill='blue', width=5)
pen.line([0, img.height, img.width, 0], fill='red', width=5)
img.show()