{
  'variables': {
    'conditions': [
      ['OS=="win" and target_arch=="ia32"', {
        'angle_out': [
          '../angle/gyp/Release_Win32',
        ],
      }],
      ['OS=="win" and target_arch=="x64"', {
        'angle_out': [
          '../angle/out/Release',
        ],
      }],
    ],
  },

  'targets': [
    {
      'target_name': 'node_angle',
      'sources': [
        'src/node_angle.cc',
        'src/EGLWindowObject.cc',
      ],

      'include_dirs': [
        '<!(node -e "require(\'nan\')")',
        'angle/include',
        'angle/src',
        'angle/util',
      ],

      'libraries': [
        '<(angle_out)/libEGL.dll.lib',
        '<(angle_out)/libGLESv2.dll.lib',
        '<(angle_out)/angle_util.dll.lib',
      ],

      'defines': [
        'GL_GLEXT_PROTOTYPES',
        'EGL_EGLEXT_PROTOTYPES',
      ],

      # Fails due to variables defined in angle/gyp/common_defines.gypi not being set,
      # despite everything I've tried, so hand-write the options above.
     #  'dependencies': [
     #     'angle/util/util.gyp:angle_util',
     #  ],
    },
  ],
}
