# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pgzero/data/icon.png', 'pgzero/data'),
        ('images', 'images'),
    ],
    hiddenimports=[],
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
    name='main',
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
app = BUNDLE(
    exe,
    name='main.app',
    icon=None,
    bundle_identifier=None,
)
