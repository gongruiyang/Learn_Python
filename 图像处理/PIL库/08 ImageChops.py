from PIL import Image,ImageChops
img1 = Image.open("picture\cup.jpg")
img2 = Image.open("picture\杯子.png").resize(img1.size)

# add函数
# ImageChops.add(img1, img2).show()

# subtract函数
# ImageChops.subtract(img1,img2).show()

# darker函数
# ImageChops.darker(img1,img2).show()

# lighter函数
# ImageChops.lighter(img1,img2).show()

# multiply函数
# ImageChops.multiply(img1,img2).show()

# screen函数
# ImageChops.screen(img1,img2).show()

# invert函数
# ImageChops.invert(img1).show()

# difference函数
ImageChops.difference(img1,img2).show()