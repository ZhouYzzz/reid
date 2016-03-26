#!/usr/bin/python
import sys, os
HOME = '/home/zhouyz14'
sys.path.insert(0, HOME+'/caffe/python')
ROOT = HOME+'/proj/prid_2011'

import caffe
import lmdb
from cv2 import imread
import numpy as np

# cam1
CAM_A = '/multi_shot/cam_a'
CAM_B = '/multi_shot/cam_b'

NUM_A = 20
NUM_B = 20
NUM_AB = 60

# generate similar pairs
for LABEL in xrange(1,201):
    IMG_As = os.listdir(ROOT+CAM_A+'/person_%04d'%LABEL)
    IMG_Bs = os.listdir(ROOT+CAM_B+'/person_%04d'%LABEL)

    # from A: 20 pairs
    choice_1 = np.random.choice(IMG_As, NUM_A)
    choice_2 = np.random.choice(IMG_As, NUM_A)
    for i in xrange(NUM_A):
        print CAM_A+'/person_%04d'%LABEL+'/'+choice_1[i], \
            CAM_A+'/person_%04d'%LABEL+'/'+choice_2[i], 0

    # from B: 20 pairs
    choice_1 = np.random.choice(IMG_Bs, NUM_B)
    choice_2 = np.random.choice(IMG_Bs, NUM_B)
    for i in xrange(NUM_B):
        print CAM_B+'/person_%04d'%LABEL+'/'+choice_1[i], \
            CAM_B+'/person_%04d'%LABEL+'/'+choice_2[i], 0

    # from A & B: 60 pairs
    choice_1 = np.random.choice(IMG_As, NUM_AB)
    choice_2 = np.random.choice(IMG_Bs, NUM_AB)
    for i in xrange(NUM_AB):
        print CAM_A+'/person_%04d'%LABEL+'/'+choice_1[i], \
            CAM_B+'/person_%04d'%LABEL+'/'+choice_2[i], 0

# generate dissimilar pairs

all_choice = []
for LABEL in xrange(1,201):
    IMG_As = os.listdir(ROOT+CAM_A+'/person_%04d'%LABEL)
    IMG_Bs = os.listdir(ROOT+CAM_B+'/person_%04d'%LABEL)

    choice_1 = np.random.choice(IMG_As, NUM_A).tolist()
    choice_2 = np.random.choice(IMG_Bs, NUM_B).tolist()

    for i in xrange(NUM_A):
        choice_1[i] = CAM_A + '/person_%04d'%LABEL +'/'+ choice_1[i]

    for i in xrange(NUM_B):
        choice_2[i] = CAM_B + '/person_%04d'%LABEL +'/'+ choice_2[i]

    choice = choice_1 + choice_2
    choice = np.random.permutation(choice)
    all_choice.append(choice)

all_choice = np.array(all_choice)

ITER = 1000
for COL in xrange(NUM_A+NUM_B):
    for _ in xrange(ITER):
        c = all_choice[:, COL]
        l = np.random.choice(c, 2, replace=False).tolist()
        print l[0], l[1], 1




