from PIL import Image
img1 = Image.open("picture\cup.jpg")
img2 = Image.open("picture\杯子.png").resize(img1.size)
# 分离
r1,g1,b1 = img1.split()
r2,g2,b2 = img2.split()
# 合并
tmp = [r1,g2,b1]
img = Image.merge("RGB",tmp)
img.show()