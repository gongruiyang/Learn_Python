from PIL import Image, ImageDraw
width = 300
height = 300
img = Image.new("RGB", (width, height), "blue")
pen = ImageDraw.Draw(img)

def get_color(x,y):
    a = x // 100 + y // 100
    if a == 0:
        return (255, 0, 0)
    if a == 1:
        return (0, 255, 0)
    if a == 2:
        return (0, 0, 255)
    if a == 3:
        return (0, 0, 0)
    if a == 4:
        return (255, 255, 255)

for x in range(width):
    for y in range(height):
        pen.point((x,y), fill=get_color(x,y))
img.show()