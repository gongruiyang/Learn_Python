from PIL import Image, ImageDraw
img = Image.open("picture\cup.jpg")
pen = ImageDraw.Draw(img)

# 正宗的黄色(255,255,0) 正宗红色(255，0，0)
def modify_color(x,y):
    old_color = img.getpixel((x,y))
    if old_color[0] > 60 and old_color[1] > 60 and old_color[2] < 60 :
        return (255, 0, 0)
    else:
        return old_color

for x in range(img.width):
    for y in range(img.height):
        pen.point((x,y), fill=modify_color(x, y))
img.show()
