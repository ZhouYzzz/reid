TOOLS=/home/zhouyz14/caffe/build/tools

$TOOLS/caffe train \
	-solver solver.prototxt \
	-gpu 0,1
