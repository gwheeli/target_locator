#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 14:13:31 2022

@author: alex_wheelis

this script runs the detection program

"""

# importing libraries
import cv2
import detection_algo_v2
import numpy as np

RED_VAL_MAX = 100
RED_VAL_MIN = 0

GRN_VAL_MAX = 120
GRN_VAL_MIN = 80

BLU_VAL = 155

BLU_IDX = 0
GRN_IDX = 1
RED_IDX = 2


"""testing """
import glob
vid_files = glob.glob("/Users/alex_wheelis/Downloads/Data_collection/*mp4")
file = vid_files[4]
#----------------------- end test

cap = cv2.VideoCapture(file)

color = (40, 147, 200)

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

#FIGURE OUT COLOR




# TRACK
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video  file")
   
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  frame_center_y, frame_center_x, _ = frame.shape
  
  # perform a blue filter
  blue = frame[..., BLU_IDX] > BLU_VAL
  red= frame[..., RED_IDX] < RED_VAL_MAX 
  green = (frame[..., GRN_IDX] > GRN_VAL_MIN) & (frame[..., GRN_IDX] < GRN_VAL_MAX)
    
  blue_objects = cv2.bitwise_and(blue.astype(np.uint8), red.astype(np.uint8), green.astype(np.uint8))
    
  blue_objects[blue_objects == 1] = 255
  targets = detection_algo_v2.find_targets_process(blue_objects)
  print(targets)
  
  # display the origin
  cv2.putText(frame, "(0,0)", \
                    (int(frame_center_x/2) + 15, int(frame_center_y/2)), fontFace = cv2.FONT_HERSHEY_DUPLEX,\
                        fontScale = 1.0, color = (255, 0, 0), thickness = 3)
  cv2.circle(frame, (int(frame_center_x/2), int(frame_center_y/2)),\
             radius = 5, color = (0, 0, 255),thickness = -1 )
  if ret == True:
   
    # Display the resulting frame
    for target_x, target_y in targets:
        #cv2.circle(frame, (target_x, target_y), radius = 10, color = (0, 0, 255),thickness = -1 )
        # if you want the coordinates for GCS, USE THESE
        cv2.putText(frame, f"{target_x - frame_center_x/2}, {-1*(target_y - frame_center_y/2)}", \
                    (target_x, target_y), fontFace = cv2.FONT_HERSHEY_DUPLEX,\
                        fontScale = 2.0, color = (255, 0, 0), thickness = 3)
    
        cv2.circle(frame, (target_x, target_y), radius = 5, color = (0, 255, 0), thickness = -1)
        
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