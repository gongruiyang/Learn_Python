from PIL import Image,ImageEnhance

img = Image.open("picture\cup.jpg")
img_output = Image.new("RGB",(img.width * 3, img.height * 2))

# 获取色彩调整期
img_color = ImageEnhance.Color(img)
img_high = img_color.enhance(1.5)   # 色彩增加
img_low  = img_color.enhance(0.5)   # 色彩减弱
# 将原图复制到最左边，另外两个图以此放在右边
img_output.paste(img, (0, 0))
img_output.paste(img_high, (img.width * 1, 0))
img_output.paste(img_low, (img.width * 2, 0))


# 获取亮度调整期
img_Brightness = ImageEnhance.Brightness(img)
img_high = img_Brightness.enhance(1.5)  # 亮度增强
img_low  = img_Brightness.enhance(0.5)  # 亮度减弱
# 将原图复制到最左边，另外两个图以此放在右边
img_output.paste(img, (0, img.height))
img_output.paste(img_high, (img.width * 1, img.height))
img_output.paste(img_low, (img.width * 2, img.height))
img_output.show()

