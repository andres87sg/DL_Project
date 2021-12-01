# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 19:37:53 2021

@author: Andres
"""

from skimage import io, color
import cv2 as cv

#filename = 'C:/Users/Andres/Desktop/destino 11/Testing/PC/'
#name = 'W32-1-1-E.03_0000_PC.jpg'

filename = 'C:/Users/Andres/Desktop/'
name = 'im_A.jpg'


#img = cv.imread(filename)

rgb = io.imread(filename+name)
lab = color.rgb2lab(rgb)


red_ch = np.copy(rgb)
green_ch = np.copy(rgb)
blue_ch = np.copy(rgb)


L_ch = np.copy(lab)
A_ch = np.copy(lab)
B_ch = np.copy(lab)



red_ch[:,:,1]=0
red_ch[:,:,2]=0

green_ch[:,:,0]=0
green_ch[:,:,2]=0

blue_ch[:,:,0]=0
blue_ch[:,:,1]=0


plt.figure(1)
plt.subplot(2,3,1)
plt.imshow(red_ch)
plt.axis('off')
plt.subplot(2,3,2)
plt.imshow(green_ch)
plt.axis('off')
plt.subplot(2,3,3)
plt.imshow(blue_ch)
plt.axis('off')
           
plt.subplot(2,3,4)
plt.axis('off')
plt.imshow(lab[:,:,0])
plt.subplot(2,3,5)
plt.axis('off')
plt.imshow(lab[:,:,1])
plt.subplot(2,3,6)
plt.axis('off')
plt.imshow(lab[:,:,2])





