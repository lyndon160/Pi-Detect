# Pi-Detect

A small script that detects movement and takes a photo as well as providing a live video feed.
Run alongside a webserver to the directory this is ran and you have a live video feed available through the browser.

Change the sleep time to change the frame rate (note that the frame rate will be limited if using a low power device like the RPI due to the processing of each image).

Changing the threshold will change the sensitivity for detecting movement.

Changing the resolution will give you a better quality video feed (though lower fps) and more accurate motion detection but will also increase the processing time of each frame.


To run the program use:

    python detect.py

To run a simple web server use:

    python -m SimpleHTTPServer 80



# Requirements
USB camera

Raspberry pi or other computer.




#TODO
Import a facial recognition algorithm so photos are only taken when a face is detected.

Upload Javascript webpage that live updates video.
