#!/usr/bin/python
import sys, os
HOME = '/home/zhouyz14'
sys.path.insert(0, HOME+'/caffe/python')
ROOT = HOME+'/proj/prid_2011'

import caffe
import lmdb
from cv2 import imread
import numpy as np
import lmdb
import pandas

df = pandas.read_csv('test.txt', sep=' ', header=None)

env = lmdb.open('lmdb_reid_test2', map_size=int(1e12))

num_pairs = df.shape[0]

with env.begin(write=True) as txn:
    # txn is a Transaction object
    for i in xrange(num_pairs):
        print 'Put Pair', i, '/', num_pairs
        PAIR = df.iloc[i]
        im1 = imread('.'+PAIR[0])
        im2 = imread('.'+PAIR[1])
        im1 = im1.transpose((2,0,1))
        im2 = im2.transpose((2,0,1))
        data = np.vstack((im1,im2))
        #datum = caffe.proto.caffe_pb2.Datum()
        #datum.channels = 6
        #datum.height = 128
        #datum.width = 64
        #datum.
        #datum.label = int(PAIR[2])
        datum = caffe.io.array_to_datum(data, label=int(not int(PAIR[2])))
        str_id = '{:08}'.format(i)
        txn.put(str_id, datum.SerializeToString())

env.close()


