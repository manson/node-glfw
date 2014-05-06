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
        'VERSION=0.1.2'
      ],
      'sources': [
        'src/glfw.cc',
        'deps/glew-1.10.0/src/glew.c',
      ],
      'include_dirs': [
        './deps/glew-1.10.0/include',
        './deps/glfw-2.7.9/include',
      ],
      'conditions': [
        ['OS=="linux"', {
          'libraries': [
            '../deps/glfw-2.7.9/lib/x11/libglfw.so',
          ],
          'ldflags': [
            '-Wl,-rpath=./deps/glfw-2.7.9/lib/x11',
          ]
        }],
        ['OS=="mac"', {
          'libraries': [
            '../deps/glfw-2.7.9/lib/carbon/libglfw.so',
            '-framework OpenGL',
          ],
          'ldflags': [
            '-Wl,-rpath=./deps/glfw-2.7.9/lib/carbon',
          ]
        }],
        ['OS=="win"', {
          'library_dirs': [
            './deps/glfw-2.7.9/lib/win32',
          ],
          'libraries': [
            'glfw.lib',
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
