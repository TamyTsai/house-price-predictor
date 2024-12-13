# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\陳銘泓\\Desktop\\GitHub\\NOU_python_zzz002_work\\main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['mysql.connector.plugins.mysql_native_password'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='房價預測器 Windows v0.X',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
