import build_test
from os.path import join, dirname
import sys


print('=' * 30)
print(f'sys.path = {sys.path}')
GLOBAL_CONFIG = join(dirname(build_test.__file__), '../config.txt')


with open(GLOBAL_CONFIG, 'r') as f:
    config = f.read()
