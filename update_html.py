"""Utility to copy from compiled angular bundle, assumes common parent."""
from pathlib import Path
from shutil import copy

SRC = Path('../angmscada/dist/angmscada')
DST = Path('./src/pymscada_html/html')

for rm in ['main*js', 'runtime*js', 'styles*css', 'polyfills*js']:
    for f in DST.glob(rm):
        f.unlink()

for f in SRC.glob('*'):
    copy(f, DST)
