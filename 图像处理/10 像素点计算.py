from PIL import Image

img = Image.open("picture\cup.jpg")

img_high = img.point(lambda x: x * 1.5)
img_low  = img.point(lambda x: x * 0.5)

img_output = Image.new("RGB",(img.width * 3, img.height))
img_output.paste(img, (0, 0))
img_output.paste(img_high, (img.width, 0))
img_output.paste(img_low, (img.width * 2, 0))
img_output.show()