#!/bin/bash -e

pushd deps/glfw-3.0.4

cmake -DBUILD_SHARED_LIBS=1 -DGLFW_BUILD_EXAMPLES=0 -DGLFW_BUILD_TESTS=0 -DGLFW_BUILD_DOCS=0 .
make -j 4

popd

node-gyp rebuild -j 4
