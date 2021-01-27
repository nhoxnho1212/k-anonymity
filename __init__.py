import sys
import os
from dotenv import load_dotenv

sys.path.append(os.getcwd() + '/')
load_dotenv()

from help.argument_handler import get_argument
from config.configs import *


custom_argv = get_argument()

try:
    K = int(os.getenv("K")) if os.getenv("K") else K
    K = int(custom_argv.k_value) if custom_argv.k_value else K

    print(f'k={K}')
except NameError:
    raise Exception('k is none')

try:
    FILE_DATA = f'{os.getcwd()}/data/{os.getenv("DATA_SOURCE")}' if os.getenv("DATA_SOURCE") else FILE_DATA
    FILE_DATA = f'{os.getcwd()}/data/{custom_argv.data_source_value}' if custom_argv.data_source_value else FILE_DATA

    if os.path.exists(FILE_DATA):
        print(f'Data source:"{FILE_DATA}"')
    else:
        raise Exception(f'ERROR: data source "{FILE_DATA}" not exist!')


except NameError:
    raise Exception('FILE_DATA is none')

FILE_RESULT_PREFIX = os.getcwd() + '/result'

if not os.path.exists(FILE_RESULT_PREFIX):
    os.makedirs(FILE_RESULT_PREFIX)

FILE_RESULT = FILE_RESULT_PREFIX + f'/adult_{K}.csv'

try:
    FILE_RESULT = f'{FILE_RESULT_PREFIX}/{os.getenv("RETURN_SOURCE")}' if os.getenv("RETURN_SOURCE") else FILE_RESULT
    FILE_RESULT = f'{FILE_RESULT_PREFIX}/{custom_argv.return_source_value}' if custom_argv.return_source_value else FILE_RESULT

    print(f'file result:"{FILE_RESULT}"')
except NameError:
    raise Exception('file result is none')