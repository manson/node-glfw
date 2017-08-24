cd deps/glfw-3.0.4
cmake -DBUILD_SHARED_LIBS=1 -G "Visual Studio 14 2015 Win64" .
msbuild GLFW.sln
cd ../..
node-gyp rebuild
