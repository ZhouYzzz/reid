#!/usr/bin/env sh

DOC='train net'

BENCHMARK='prid_2011'

HOME='/home/zhouyz14'
CAFFE_ROOT=$HOME/proj/Deep-Metric-Learning-CVPR16/Caffe-Deep-Metric-Learning-CVPR16
TOOLS=$CAFFE_ROOT/build/tools

DATABASE=$HOME/proj/$BENCHMARK

$TOOLS/caffe train \
	-solver solver_simple.prototxt \
	-gpu 0

