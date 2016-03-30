#!/usr/bin/python

'''
Testing the net: passing all 90000 imgs and 900 labels
to the net and save label and feature to `result.txt`
'''

import sys, os
CAFFE_ROOT = '/home/zhouyz14/caffe'
sys.path.insert(0,CAFFE_ROOT+'/python')

import caffe
import numpy as np
import pandas as pd

caffe.set_mode_gpu()
caffe.set_device(2)

net = caffe.Net('deploy.prototxt',\
                'snapshots/stage1_alex_reid_iter_100000.caffemodel', caffe.TEST)

dim = net.blobs['feat'].data.shape[1]

result = np.zeros([0,dim+1])

for i in xrange(1484):
    blobs_out = net.forward()
    print 'TEST', 64*(i+1) ,'/', 94987
    # blobs_out : ['feat': np.array, 'label': np.array]
    label = np.expand_dims(blobs_out['label'].copy(),1)
    feat = blobs_out['feat'].copy()
    info = np.hstack((label,feat))
    result = np.vstack((result, info))

np.save('result', result)
