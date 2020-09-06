#!/usr/bin/env python
# coding: utf-8

# # 作業
# 
# 思考一下我們前面有提到圖片是矩陣，但維度可能會不一樣
# 例如灰階圖只有兩個維度，RGB 彩圖則有 3 個維度
# 
# 假如今天我們把 RGB 3 個維度拆開來看會有甚麼不同的效果呢？

# In[1]:


pip install --user opencv-python


# In[2]:


import cv2
import os
img_path = os.getcwd() + '\\lena.png'
img = cv2.imread(img_path, cv2.IMREAD_COLOR)
#img_Green = cv2.imread(img_path, cv2.IMREAD_COLOR)
#img_Blue = cv2.imread(img_path, cv2.IMREAD_COLOR)
r = img.copy()
r[:, :, 0] = 0
r[:, :, 1] = 0

g = img.copy()
g[:, :, 0] = 0
g[:, :, 2] = 0

b = img.copy()
b[:, :, 1] = 0
b[:, :, 2] = 0

while True:
    cv2.imshow ('Red', r)
    cv2.imshow ('Green', g)
    cv2.imshow ('Blue', b)
    
    
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break


# In[ ]:




