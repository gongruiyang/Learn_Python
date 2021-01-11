# 导入包
from PIL import Image

# 以 默认方式 打开图片
# img1 = Image.open("picture/cup.jpg","RGB")
# img1.show()
# img1.show()
# img1 = Image.open("picture/cup.jpg").convert(mode='RGB')
# img2 = Image.new("RGB", img1.size, (255,255,255))

# 显示图片
# img1.show()
# img2.show()

# 查看图片信息
# print('图像格式：',img1.format)
# print('图像大小（宽度，高度）：',img1.size)
# print('图片的高度：',img1.height,'图片的宽度：',img1.width)
# print('获取(100,100)处像素值：',img1.getpixel((100,100)))
# print(type(img1.getpixel((100,100))))
# print(type(img1.size))

# 混合两张图片 原理：img1 * (1 - alpha) + img2 * alpha
# img1 = Image.open("picture/cup.jpg").convert("RGB")
# img2 = Image.new("RGB", img1.size, "red")
# img3 = Image.blend(img1, img2, alpha=0.5)
# img3.show()

# 按像素缩放图片
# img1.show()
# img1_bigger = Image.eval(img1,lambda x:x*2)
# img1_bigger.show()

# 按尺寸进行缩放图片
# img2 = img1.copy()
# print(img2.size)
# img2.thumbnail((200,160))
# print(img2.size)
# img2.show()