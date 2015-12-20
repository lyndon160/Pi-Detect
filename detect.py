#! /usr/bin/env python
import numpy as np
import cv
from subprocess import call
import time
import logging

def compute_histogram(src, h_bins = 30, s_bins = 32):
    #create images
    hsv = cv.CreateImage(cv.GetSize(src), 8, 3)
    hplane = cv.CreateImage(cv.GetSize(src), 8, 1)
    splane = cv.CreateImage(cv.GetSize(src), 8, 1)
    vplane = cv.CreateImage(cv.GetSize(src), 8, 1)

    planes = [hplane, splane]
    cv.CvtColor(src, hsv, cv.CV_BGR2HSV)
    cv.Split(hsv, hplane, splane, vplane, None)

    #compute histogram  (why not use v_plane?)
    hist = cv.CreateHist((h_bins, s_bins), cv.CV_HIST_ARRAY,
            ranges = ((0, 180),(0, 255)), uniform = True)
    cv.CalcHist(planes, hist)      #compute histogram
    cv.NormalizeHist(hist, 1.0)    #normalize hist

    return hist



LOG_FILENAME = 'intrusions.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO, format ="%(asctime)s - %(message)s")

logging.info("Start")

# Take init picture
call(["fswebcam","img.jpg", "-r 320", "-q"])
# Load it

imgA = cv.LoadImage('img.jpg',cv.CV_LOAD_IMAGE_COLOR)
time.sleep(0.20)
i=0
#Start loop where taking and loading pictures
while(1):
    call(["fswebcam","img.jpg", "-r 320", "-q"])

    imgB = cv.LoadImage('img.jpg',cv.CV_LOAD_IMAGE_COLOR)
    hist1= compute_histogram(imgA)
    hist2= compute_histogram(imgB)
    sc= cv.CompareHist(hist1, hist2, cv.CV_COMP_BHATTACHARYYA)
    if(sc>0.4):
    	logging.info("Intrusion "+ str(i) + ": " + str(sc))
    	call(["fswebcam", str(i)+".jpg", "-r 1280", "-q"])
        i+=1
    imgA = imgB
    if(i==600):
        i=0
     
