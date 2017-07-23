#Basic Program to show an image
import cv2

img = cv2.imread('/home/davis/PycharmProjects/MachineLearning/MLPractice/fjords.jpg')
cv2.imshow('ImageWindow', img)
cv2.waitKey()

