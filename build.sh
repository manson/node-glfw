#!/bin/bash -e

pushd deps/glfw-2.7.9

bash compile.sh
case "$(uname)" in
Linux) make x11 ;;
Darwin) make cocoa ;;
*) echo "This platform is not yet supported. Pull requests welcome."; exit 1 ;;
esac


popd

node-gyp rebuild
