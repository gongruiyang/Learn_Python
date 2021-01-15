from PIL import Image
img1 = Image.open("picture\cup.jpg")
# 将img1拷贝两份
img2 = img1.copy()
img3 = img1.copy().resize((500,400))
# 将img3整张图片剪切出来
img_region = img3.crop((0,0,img3.width,img3.height))
# 将剪切出来的img_region左上角的点定位放在img2的(30,30)处
img2.paste(img_region,(30,30))
img2.show()