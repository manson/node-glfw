cd deps/glfw-3.0.4
cmake -DBUILD_SHARED_LIBS=1 -DGLFW_BUILD_EXAMPLES=0 -DGLFW_BUILD_TESTS=0 -DGLFW_BUILD_DOCS=0 -DCMAKE_GENERATOR_PLATFORM=x64 .
REM cmake -DBUILD_SHARED_LIBS=1 -G "Visual Studio 14 2015 Win64" .
msbuild GLFW.sln /p:Configuration=Release
cd ../..
node-gyp rebuild -j 4
