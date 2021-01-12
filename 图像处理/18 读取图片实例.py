from PIL import Image
import numpy as np
import os
import pickle

# 读取图片目录
image_dir = './picture/'
# 保存图片的目录
result_dir = './result/'
# 保存数组的文件
array_file = './array.bin'

# 读取picture目录下的图片，将图片保存成大的一维数组，将数组保存到文件
def image_to_file():
    # 获取文件名列表
    file_name_list = os.listdir(image_dir)
    # 读取图片
    for file_name in file_name_list:
        img = Image.open(image_dir + file_name)
        r, g, b = img.split()
        # 将rgb转化为一维数组
        r_array = np.array(r).reshape(-1)
        g_array = np.array(g).reshape(-1)
        b_array = np.array(b).reshape(-1)
        # 将 三个一维数组 拼接为 一个一维数组
        arrs = np.concatenate((r_array,g_array,b_array))
        img_arrs = np.concatenate((arrs,img_arrs))

    # 将一维数组保存到文件中
    with open(array_file, 'wb') as f:
        pickle.dump(img_arrs, f)

# 读取文件中的内容，转换图片
def file_to_image():
    with open(array_file, 'rb') as f:
        images=pickle.load(f)
        # 一维数组中 8, 3, 250, 250
        images.reshape()

# if __name___ == '__main__':
image_to_file()
