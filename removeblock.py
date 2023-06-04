import base64
import json
import os
import os.path as osp

import numpy as np
import PIL.Image
from labelme import utils

'''
删除文件名中的空格 图像文件和json文件对齐
'''
if __name__ == '__main__':
    jpgs_path   = "datasets/JPEGImages"
    pngs_path   = "datasets/SegmentationClass"
    classes     = ["_background_","cell"]
    
    count = os.listdir("./datasets/before/") # 全部的图像数量
    for i in range(0, len(count)):
        path = os.path.join("./datasets/before", count[i]) # 获取文件路径

        if os.path.isfile(path) and path.endswith('json'):  # 加载json文件，修改json文件中的imagePath参数为没有空格的文件名
            with open(path,"rb") as f:
                params = json.load(f)
                imagePath = params['imagePath']
                imagePath = imagePath.replace(' ','')
                params['imagePath'] = imagePath
            newpath = path.replace(' ','') # 新的文件名
            with open(newpath,"w") as f:
                json.dump(params,f)         # 保存json文件


        if os.path.isfile(path) and path.endswith('png'):  #判断文件是否为png图像文件，把带空格的文件名，重命名为没有空格的文件名
            newpath = path.replace(' ','')
            os.rename(path, newpath)
           