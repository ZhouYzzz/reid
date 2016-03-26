#!/usr/bin/env sh

DOC='train net'

BENCHMARK='prid_2011'

HOME='/home/zhouyz14'
CAFFE_ROOT=$HOME/caffe
TOOLS=$CAFFE_ROOT/build/tools
DATABASE=$HOME/proj/$BENCHMARK

$TOOLS/caffe train \
	-solver reid_net/reid_net_solver_train.prototxt \
	-weights VGG_ILSVRC_16_layers/VGG_ILSVRC_16_layers.caffemodel \
	-gpu 0

