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
        'src/glfw.cc'
      ],
      'conditions': [
        ['OS=="linux"', {'libraries': ['-lglfw', '-lGLEW']}],
        ['OS=="mac"', {'libraries': ['-lglfw', '-lGLEW', '-framework OpenGL']}],
        ['OS=="win"', {
          'libraries': [
            'glew64s.lib', 
            'glfw64dll.lib', 
            'opengl32.lib'
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
