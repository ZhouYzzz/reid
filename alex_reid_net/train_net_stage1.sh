#!/usr/bin/env sh

CAFFE=/home/zhouyz14/caffe

$CAFFE/build/tools/caffe train \
	-solver solver_stage1.prototxt \
	-gpu 2 \
	-weights $CAFFE/models/bvlc_alexnet/bvlc_alexnet.caffemodel
