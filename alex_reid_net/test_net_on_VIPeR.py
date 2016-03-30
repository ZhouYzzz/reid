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
caffe.set_device(0)

proto_a = 'deploy_VIPeR_a.prototxt'
proto_b = 'deploy_VIPeR_b.prototxt'
model = 'snapshots/stage1_alex_reid_iter_100000.caffemodel'
# generate A feats
net_a = caffe.Net(proto_a, model, caffe.TEST)

dim = net_a.blobs['feat'].data.shape[1]

result_a = np.zeros([0,dim+1])

for i in xrange(632):
    blobs_out = net_a.forward()
    print 'TEST', i+1 ,'/', 632
    # blobs_out : ['feat': np.array, 'label': np.array]
    label = np.expand_dims(blobs_out['label'].copy(),1)
    feat = blobs_out['feat'].copy()
    info = np.hstack((label,feat))
    result_a = np.vstack((result_a, info))

# np.savetxt('result_a.txt', result_a)

del net_a

# generate B feats
net_b = caffe.Net(proto_b, model, caffe.TEST)

dim = net_b.blobs['feat'].data.shape[1]

result_b = np.zeros([0,dim+1])

for i in xrange(632):
    blobs_out = net_b.forward()
    print 'TEST', i+1 ,'/', 632
    # blobs_out : ['feat': np.array, 'label': np.array]
    label = np.expand_dims(blobs_out['label'].copy(),1)
    feat = blobs_out['feat'].copy()
    info = np.hstack((label,feat))
    result_b = np.vstack((result_b, info))

# np.savetxt('result_a.txt', result)

del net_b
# print result_a[:,0]
# result_a = result_a[:873,:]
# print result_a[:,0]
# print result_a[0,0:4]
# result_b = result_b[:873,:]
# result_a = result_a[result_a[:,0].argsort(),:]
# result_b = result_b[result_b[:,0].argsort(),:]
# print result_a[127,0:4]
# print result_a, result_b
# print np.where(result_a[:,0]==1)
# np.save('VIPeR_a', result_a)
# np.save('VIPeR_b', result_b)

P = 316

result_a = result_a[:P,:]
result_b = result_b[:P,:]

rank = np.zeros(P)

for i in xrange(P):
    af = result_a[i, 1:]
    dis = result_b[:, 1:] - af
    disn = np.linalg.norm(dis,ord=2,axis=1)
    ranki = np.where(disn.argsort()==i)[0][0]
    rank[ranki:] += 1

rank = rank/P
print rank

import matplotlib.pyplot as plt
plt.plot(rank[:P], 'o-')
# plt.show()
