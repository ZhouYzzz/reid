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

df = pandas.read_csv('all.txt', sep=' ', header=None)

env = lmdb.open('lmdb_all', map_size=int(1e12))

num_pairs = df.shape[0]

with env.begin(write=True) as txn:
    # txn is a Transaction object
    for i in xrange(num_pairs):
        print 'Put IMAGE', i+1, '/', num_pairs
        PAIR = df.iloc[i]
        im = imread('.'+PAIR[0])
        im = im.transpose((2,0,1))
        datum = caffe.io.array_to_datum(im, label=int(PAIR[1]))
        str_id = '{:08}'.format(i)
        txn.put(str_id, datum.SerializeToString())

env.close()


