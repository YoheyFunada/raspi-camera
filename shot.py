#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import picamera

from datetime import datetime

with picamera.PiCamera() as camera:
 camera.resolution = (1024, 768)
 camera.start_preview()
 # Camera warm-up time
 time.sleep(2)
 #image name
 now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
 image_name = str(now)+".jpg"

 camera.capture(image_name)
