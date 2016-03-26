#!/usr/bin/env sh

DOC="This script convert re-id images and data to caffe database."

BENCHMARK='prid_2011'

HOME='/home/zhouyz14'
CAFFE_ROOT=$HOME/caffe
TOOLS=$CAFFE_ROOT/build/tools
DATABASE=$HOME/proj/$BENCHMARK

TARIN="train"
VAL="val"

#if [ "$1"=$TARIN ]; then
#$TOOLS/convert_imageset \
#	--shuffle \
#	''  \
#	train.txt \
#	'lmdb'
#fi

#if [ "$1"=$VAL ]; then
$TOOLS/convert_imageset \
	--shuffle \
	'' \
	val.txt \
	'lmdb_val'

#fi
