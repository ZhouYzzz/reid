#!/usr/bin/python
import _init_path
import caffe
import sys

caffe.set_mode_gpu()
caffe.set_device(0)
CAFFE = '/home/zhouyz14/caffe/'
# net = caffe.Net('train_val.prototxt', CAFFE+\
#                 'models/bvlc_alexnet/bvlc_alexnet.caffemodel', caffe.TEST)

net = caffe.Net(sys.argv[1], \
                'snapshots/stage1_alex_reid_iter_100000.caffemodel', caffe.TEST)

