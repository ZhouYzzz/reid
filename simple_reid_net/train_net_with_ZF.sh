#!/usr/bin/env sh

DOC='train net'

BENCHMARK='prid_2011'

HOME='/home/zhouyz14'
CAFFE_ROOT=$HOME/proj/Deep-Metric-Learning-CVPR16/Caffe-Deep-Metric-Learning-CVPR16
TOOLS=$CAFFE_ROOT/build/tools

DATABASE=$HOME/proj/$BENCHMARK

$TOOLS/caffe train \
	-solver solver_simple.prototxt \
	-weights $HOME/py-faster-rcnn/data/faster_rcnn_models/ZF_faster_rcnn_final.caffemodel \
	-gpu 0


	# -weights $HOME/py-faster-rcnn/data/faster_rcnn_models/ZF_faster_rcnn_final.caffemodel \
	# -snapshot ZF_reid_iter_3511.solverstate \
