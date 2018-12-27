#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import picamera

from datetime import datetime

with picamera.PiCamera() as camera:
 camera.sharpness = 0
 camera.contrast = 0
 camera.brightness = 60
 camera.saturation = 0
 camera.ISO = 0
 camera.video_stabilization = False
 camera.exposure_compensation = 0
 camera.exposure_mode = 'auto'
 camera.meter_mode = 'average'
 camera.awb_mode = 'auto'
 camera.image_effect = 'none'
 camera.color_effects = None
 camera.rotation = 0
 camera.hflip = False
 camera.vflip = False
 camera.crop = (0.0, 0.0, 1.0, 1.0)
 camera.resolution = (1024, 768)
 camera.start_preview()
 # Camera warm-up time
 time.sleep(2)
 #image name
 now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
 image_name = str(now)+".jpg"

 camera.capture(image_name)
