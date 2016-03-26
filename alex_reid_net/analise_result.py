#!/usr/bin/python
import numpy as np

'''

'''

r = np.loadtxt('result.txt')

print 'RESULT LOAD, shape:', r.shape

# feat = r[:,1:]

# norm = np.linalg.norm(feat, ord=2, axis=1)

# CALCULATE THE mean FEAT for each label

cls_mean = np.zeros([935, r.shape[1]-1])

for LABEL in xrange(1,936):
    feat = r[r[:,0]==LABEL,1:]
    # np.linalg.norm(feat, ord=2, axis=1)
    mean = np.mean(feat, axis=0)
    # print LABEL, mean
    cls_mean[LABEL-1, :] = mean


print cls_mean

dist = []
sort = dist.argsort() + 1
rank = np.where(sort==LABEL)[0][0] + 1
