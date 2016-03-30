#!/usr/bin/env sh

CAFFE=/home/zhouyz14/caffe

$CAFFE/build/tools/caffe train \
	-solver solver_stage2.prototxt \
	-gpu 2 \
	-weights snapshots/stage1_alex_reid_iter_100000.caffemodel
