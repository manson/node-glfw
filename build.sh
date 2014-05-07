#!/bin/bash -e

pushd deps/glfw-3.0.4

cmake -DBUILD_SHARED_LIBS=1 .
make

popd

node-gyp rebuild
