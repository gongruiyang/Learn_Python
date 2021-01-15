from PIL import Image,ImageFilter
# img = Image.open("picture\cup.jpg")
# # 创建一个 与img同高但两倍宽的空白图
# img_output = Image.new("RGB", (2 * img.width, img.height))
# # 将img放在空白图左侧
# img_output.paste(img, (0, 0))
# # 将img进行高斯模糊
# img_filter = img.filter(ImageFilter.GaussianBlur)
# # 将高斯模糊后的img放在空白图的右侧
# img_output.paste(img_filter,(img.width, 0))
# # 将拼接好的原图和高斯模糊的图进行对比展示
# img_output.show()

img = Image.open("picture\cup.jpg")
# img_output = Image.new("RGB", (img.width * 4, img.height))
img_output  = Image.new("RGB", (img.width * 2, img.height))
img_GaussianBlur = img.filter(ImageFilter.GaussianBlur)     # 高斯模糊
img_EDGE_ENHANCE = img.filter(ImageFilter.EDGE_ENHANCE)     # 边缘增强滤镜
img_FIND_EDGES   = img.filter(ImageFilter.FIND_EDGES)       # 寻找边缘滤镜

filters = []
filters.append(img_GaussianBlur)
filters.append(img_EDGE_ENHANCE)
filters.append(img_FIND_EDGES)

img_output.paste(img, (0, 0))
for _filter in filters:
    img_output.paste(_filter, (img.width, 0))
    img_output.show()

# img_output.paste(img, (0, 0))
# img_output.paste(img_GaussianBlur, (img.width, 0))
# img_output.paste(img_EDGE_ENHANCE, (img.width * 2, 0))
# img_output.paste(img_FIND_EDGES, (img.width * 3, 0))

# img_output.show()
