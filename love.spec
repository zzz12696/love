# -*- mode: python -*-

block_cipher = None

add_filed = (("1.png", "."), ("1.mp3", "."), ("msyhl.ttc", "."))
a = Analysis(['love.py'],
             pathex=['C:\\Users\\12696\\PycharmProjects\\love'],
             binaries=[],
             datas=add_filed,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='love',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
