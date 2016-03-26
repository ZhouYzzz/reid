#!/usr/bin/python

import os

BENCHMARK = os.path.join(os.environ['HOME'],'proj','prid_2011')
CAM_A = os.path.join(BENCHMARK,'multi_shot','cam_a')
CAM_B = os.path.join(BENCHMARK,'multi_shot','cam_b')

for PERSON in os.listdir(CAM_A):
    LABEL = int(PERSON[-4:])
    if LABEL <= 200:
        PATH = os.path.join(CAM_A,PERSON)
        for IMG in os.listdir(PATH):
            print PATH+'/'+IMG, LABEL

for PERSON in os.listdir(CAM_B):
    LABEL = int(PERSON[-4:])
    if LABEL <= 200:
        PATH = os.path.join(CAM_B,PERSON)
        for IMG in os.listdir(PATH):
            print PATH+'/'+IMG, LABEL

