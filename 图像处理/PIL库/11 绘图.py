from PIL import ImageDraw,Image,ImageFont
img = Image.new("RGB", (300, 300))
pen = ImageDraw.Draw(img)
pen.rectangle((10,10,250,250),fill='black',outline='red')
img_font = ImageFont.truetype('SIMLI.TTF',20)
pen.text((20,20),'这是一个测试', fill='white', font=img_font)
img.show()