#!/usr/bin/python
import sys, os
HOME = '/home/zhouyz14'
sys.path.insert(0, HOME+'/caffe/python')
ROOT = HOME+'/proj/prid_2011'

import numpy as np

# cam1
CAM_A = '/multi_shot/cam_a'
CAM_B = '/multi_shot/cam_b'

for LABEL in xrange(1,201):
    for IMG in os.listdir('.'+CAM_A+'/person_%04d'%LABEL):
        print CAM_A+'/person_%04d'%LABEL+'/'+IMG, LABEL

    for IMG in os.listdir('.'+CAM_B+'/person_%04d'%LABEL):
        print CAM_B+'/person_%04d'%LABEL+'/'+IMG, LABEL

for LABEL in xrange(201,386):
    for IMG in os.listdir('.'+CAM_A+'/person_%04d'%LABEL):
        print CAM_A+'/person_%04d'%LABEL+'/'+IMG, LABEL

for LABEL in xrange(201,750):
    for IMG in os.listdir('.'+CAM_B+'/person_%04d'%LABEL):
        print CAM_B+'/person_%04d'%LABEL+'/'+IMG, LABEL+185


