from PIL import Image, ImageDraw, ImageFont
import random
img = Image.new("RGB", (100, 100), "white")
pen = ImageDraw.Draw(img)

# 获取一个随机颜色
def get_color():
    return (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))
# 获取一个随机大写字符
def get_char():
    return chr(random.randint(65, 90))
# 图片每个点的颜色随机
for x in range(img.width):
    for y in range(img.height):
        pen.point((x,y), fill=get_color())
# 在图片上生成4个随机字母
img_font = ImageFont.truetype('simsun.ttc', 36)
for i in range(4):
    pen.text((10 + i * 20, 50), get_char(), font=img_font, fill="red")

# 干扰线
for i in range(2):
    pen.line([10, 10, 80, 80], fill="green", width=4)

img.show()