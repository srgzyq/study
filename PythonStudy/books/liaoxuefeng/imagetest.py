# -*- coding: utf-8 -*-

import Image,ImageFilter

# 打卡一个jpg图像文件
im = Image.open('./test.jpg')
'''# 获得图像尺寸:
w, h = im.size
# 缩放到50%:
im.thumbnail((w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('./test2.jpeg','jpeg')
'''

im2 = im.filter(ImageFilter.BLUR)
im2.save('./test3.jpeg','jpeg')
