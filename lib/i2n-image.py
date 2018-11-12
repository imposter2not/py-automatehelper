#! python3
"""
eyetip.py
tip functions
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

def findMe(waldo):
	# image = cv2.imread(im)
	image = cv2.imread('imagelook.png')
	template = cv2.imread(waldo)
	 
	# resize images
	image = cv2.resize(image, (0,0), fx=1, fy=1) 
	template = cv2.resize(template, (0,0), fx=1, fy=1) 
	 
	# Convert to grayscale
	imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
	 
	# Find template
	result = cv2.matchTemplate(image,template, cv2.TM_CCOEFF)
	#result = cv2.matchTemplate(imageGray,templateGray, cv2.TM_CCOEFF)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	top_left = max_loc
	# h,w = templateGray.shape
	# bottom_right = (top_left[0] + w, top_left[1] + h)
	# cv2.rectangle(image,top_left, bottom_right,(0,0,255),4)
	# Show result
	# cv2.imshow("Template", template)
	# print(top_left)
	# print(top_left[0] + 41)
	# print(top_left[1] + 177)
	me = (top_left[0] + 41, top_left[1] + 177)
	return(me)

def findIt(waldo):
	# image = cv2.imread(im)
	image = cv2.imread('imagelook.png')
	template = cv2.imread(waldo)
	 
	# resize images
	image = cv2.resize(image, (0,0), fx=1, fy=1) 
	template = cv2.resize(template, (0,0), fx=1, fy=1) 
	 
	# Convert to grayscale
	imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
	 
	# Find template
	result = cv2.matchTemplate(image,template, cv2.TM_CCOEFF)
	#result = cv2.matchTemplate(imageGray,templateGray, cv2.TM_CCOEFF)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	top_left = max_loc
	# h,w = templateGray.shape
	# bottom_right = (top_left[0] + w, top_left[1] + h)
	# cv2.rectangle(image,top_left, bottom_right,(0,0,255),4)
	# cv2.imshow("Result", image)
	 
	# # cv2.moveWindow("Template", 10, 50);
	# cv2.moveWindow("Result", 150, 50)
	
	# cv2.waitKey(0)
	return(top_left)

	# Show result
	# cv2.imshow("Template", template)
	# print(top_left)

	
"""

#threshold matching
img_rgb = cv2.imread('goldfind1.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('gold.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
	cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255),2)

cv2.imshow('Detected',img_rgb)

#feature/bruteforce matching
img1 = cv2.imread('sk-progress.png',0)
img2 = cv2.imread('shot.jpg',0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
plt.imshow(img3)
plt.show()
"""
#Template matching example
#https://pythonspot.com/en/object-detection-with-templates/
# image = cv2.imread('images/testing/intown/2.png')
# template = cv2.imread('images/titleX.png')
 
# # resize images
# image = cv2.resize(image, (0,0), fx=1, fy=1) 
# template = cv2.resize(template, (0,0), fx=1, fy=1) 
 
# # Convert to grayscale
# imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
 
# # Find template
# result = cv2.matchTemplate(image,template, cv2.TM_CCOEFF)
# #result = cv2.matchTemplate(imageGray,templateGray, cv2.TM_CCOEFF)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
# top_left = max_loc
# h,w = templateGray.shape
# bottom_right = (top_left[0] + w, top_left[1] + h)
# cv2.rectangle(image,top_left, bottom_right,(0,0,255),4)

# print(top_left)
# Show result
# cv2.imshow("Template", template)
#cv2.imshow("Result", image)
 
# cv2.moveWindow("Template", 10, 50);
#cv2.moveWindow("Result", 150, 50);
 
#cv2.waitKey(0)
