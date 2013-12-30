#!/bin/bash -e

pushd deps/glfw-3.0.4

cmake .
make

popd

node-gyp rebuild
