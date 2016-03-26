#!/usr/bin/env sh

CAFFE=/home/zhouyz14/caffe

$CAFFE/build/tools/caffe train \
	-solver \
	-gpu 0
