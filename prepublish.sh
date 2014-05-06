#!/bin/bash -e

GLEW_VERSION=1.10.0
GLFW_VERSION=2.7.9

cd "$(dirname $0)"
rm -rf deps

GLEW_FILE="glew-${GLEW_VERSION}.tar.gz"
if ! [ -e "$GLEW_FILE" ]
then
	curl -L -o "$GLEW_FILE" "https://sourceforge.net/projects/glew/files/glew/${GLEW_VERSION}/glew-${GLEW_VERSION}.tgz/download"
fi

GLFW_FILE="glfw-${GLFW_VERSION}.zip"
if ! [ -e "$GLFW_FILE" ]
then
	curl -L -o "$GLFW_FILE" "http://sourceforge.net/projects/glfw/files/glfw/${GLFW_VERSION}/glfw-${GLFW_VERSION}.zip/download"
fi


mkdir -p deps
cd deps

rm -rf "glew-${GLEW_VERSION}"
tar zxf "../$GLEW_FILE"

rm -rf "glfw-${GLFW_VERSION}"
unzip "../$GLFW_FILE"
