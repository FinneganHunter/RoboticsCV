import cv2

# these test images need to be the exact same size
img1 = cv2.imread('../resources/image1.png')
img2 = cv2.imread('../resources/image2.png')

# add = img1 + img2
# add = cv2.add(img1, img2)
# weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# White background mask
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

dst = cv2.add(img1_bg, img2_fg)  # add image 1 in the background and image 2 in the foreground
img1[0:rows, 0:cols] = dst

# cv2.imshow('any image in code', image name in code)
cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imshow('add', add)
# cv2.imshow('weighted', weighted)
