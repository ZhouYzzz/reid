#!/usr/bin/python

import os

BENCHMARK = os.path.join(os.environ['HOME'],'proj','prid_2011')
CAM_A = os.path.join(BENCHMARK,'single_shot','cam_a')
CAM_B = os.path.join(BENCHMARK,'single_shot','cam_b')

for PERSON in os.listdir(CAM_A):
    LABEL = int(PERSON[-8:-4])
    if LABEL <= 200:
        print CAM_A+'/'+PERSON, LABEL

for PERSON in os.listdir(CAM_B):
    LABEL = int(PERSON[-8:-4])
    if LABEL <= 200:
        print CAM_B+'/'+PERSON, LABEL
