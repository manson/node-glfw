{
  'variables': {
    'platform': '<(OS)',
    'build_arch': '<!(node -p "process.arch")',
    'build_win_platform': '<!(node -e "if(process.arch==\'ia32\') {console.log(\'Win32\');} else {console.log(process.arch);}")',
  },
  'conditions': [
    # Replace gyp platform with node platform, blech
    ['platform == "mac"', {'variables': {'platform': 'darwin'}}],
    ['platform == "win"', {'variables': {'platform': 'win32'}}],
  ],
  'targets': [
    {
      'target_name': 'native_glfw_build',
      "variables": {
      },
      'conditions': [
        ['OS=="win"', {
          "variables": {
            "call_build_script": "cmd /c <!(<(module_root_dir)/build.bat <(build_arch) <(module_root_dir) <(build_win_platform))",
          },
          'actions': [
            {
              'action_name': 'action_build_native_glfw',
              'inputs': [],
              'outputs': [
                '<(module_root_dir)/deps/glfw-3.0.4/src/Release/glfw3dll.lib',
                '<(module_root_dir)/deps/glfw-3.0.4/src/Release/glfw3.dll',
              ],
              'action': [
                'cmd /c echo', 'build script result: <(build_win_platform)',
              ],
            },
          ],
        },
        ],
        ['OS=="linux"', {
          'actions': [
            {
              'action_name': 'action_build_native_glfw',
              'inputs': [],
              'outputs': [
                '<(module_root_dir)/deps/glfw-3.0.4/src/libglfw.so',
              ],
              'action': [
                './build.sh',
              ],
            },
          ],
        }],
      ],
    },
    {
      #'target_name': 'glfw-<(platform)-<(target_arch)',
      'target_name': 'glfw',
      "dependencies" : [ "native_glfw_build" ],
      'defines': [
        'VERSION=0.2.0'
      ],
      'sources': [
        'src/glfw.cc',
        'deps/glew-1.10.0/src/glew.c',
      ],
      'include_dirs': [
        '<(module_root_dir)/deps/glew-1.10.0/include',
        '<(module_root_dir)/deps/glfw-3.0.4/include',
        "<!(node -e \"require('nan')\")",
      ],
      'conditions': [
        ['OS=="linux"', {
          'libraries': [
            '<(module_root_dir)/deps/glfw-3.0.4/src/libglfw.so',
            '-lGLU'
          ],
          'ldflags': [
            '-Wl,-rpath,\$$ORIGIN/../../deps/glfw-3.0.4/src',
          ]
        }],
        ['OS=="mac"', {
          'libraries': [
            '<(module_root_dir)/deps/glfw-3.0.4/src/libglfw.so',
            '-framework OpenGL',
          ],
          'ldflags': [
            '-Wl,-rpath,@loader_path/../../deps/glfw-3.0.4/src',
          ]
        }],
        ['OS=="win"', {
          'msvs_settings': {
            'VCCLCompilerTool': {
              'WarnAsError': 'false',
              'DisableSpecificWarnings': ['4273', '4244', '4005'],
              'SuppressStartupBanner': 'true',
            }
          },
          'libraries': [
            '<(module_root_dir)/deps/glfw-3.0.4/src/Release/glfw3dll.lib',
            '-lGlu32.lib',
            'opengl32.lib',
          ],
          'defines' : [
            'WIN32_LEAN_AND_MEAN',
            'VC_EXTRALEAN'
          ]
          },
        ],
      ],
    },
    {
      "target_name": "copy_dll",
      "type":"none",
      "dependencies" : [ "glfw" ],
      "conditions": [
        ['OS=="win"', {
           "copies":
            [
              {
                'destination': '<(module_root_dir)/build/Release',
                'files': ['<(module_root_dir)/deps/glfw-3.0.4/src/Release/glfw3.dll']
              }
            ]
        }]
      ]
    }
  ]
}
