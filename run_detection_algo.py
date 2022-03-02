#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 14:13:31 2022

@author: alex_wheelis

this script runs the detection program

"""

# importing libraries
import cv2
import detection_algo


# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('/Users/alex_wheelis/Downloads/IMG_3440.MOV')
   
color = (180, 254, 180)

"""
TODO: calibrate the color from a video

"""





"""
#----------------
success, frame = cap.read()
targets = detection_algo.find_targets_process(frame, color)
print(targets)
#----------------
"""

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video  file")
   
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  targets = detection_algo.find_targets_process(frame, color)
  print(targets)
  # run algorithm on 
  
  if ret == True:
   
    # Display the resulting frame
    for target_x, target_y in targets:
        cv2.circle(frame, (target_x, target_y), radius = 10, color = (0, 0, 255),thickness = -1 )

    cv2.imshow('Frame', frame)
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
   
  # Break the loop
  else: 
    break
   
# When everything done, release 
# the video capture object

cap.release()
   
# Closes all the frames
cv2.destroyAllWindows()