import sys
import os
sys.path.append(os.getcwd() + '/')

from help.argument_handler import get_argument

custom_argv = get_argument()

from config.configs import *

try:
    K = int(custom_argv.k_value) if custom_argv.k_value else K
    print(f'k={K}')
except NameError:
    raise Exception('k is none')

FILE_RESULT_PREFIX = os.getcwd() + '/result'

if not os.path.exists(FILE_RESULT_PREFIX):
    os.makedirs(FILE_RESULT_PREFIX)

FILE_RESULT = FILE_RESULT_PREFIX + f'/adult_{K}.csv'