{
  'variables': {
    'platform': '<(OS)',
  },
  'conditions': [
    # Replace gyp platform with node platform, blech
    ['platform == "mac"', {'variables': {'platform': 'darwin'}}],
    ['platform == "win"', {'variables': {'platform': 'win32'}}],
  ],
  'targets': [
    {
      #'target_name': 'glfw-<(platform)-<(target_arch)',
      'target_name': 'glfw',
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
          'libraries': [
            'opengl32.lib',
          ],
          'defines' : [
            'WIN32_LEAN_AND_MEAN',
            'VC_EXTRALEAN'
          ]
          },
        ],
      ],
    }
  ]
}
