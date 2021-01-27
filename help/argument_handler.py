import argparse

def get_argument():
    parser = argparse.ArgumentParser()


    parser.add_argument('-k', dest='k_value',
                        default = None,
                        help='k-anonimity')
    
    parser.add_argument('-d', dest='data_source_value',
                        default = None,
                        help='data source')

    parser.add_argument('-r', dest='return_source_value',
                        default = None,
                        help='return source')

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    return parser.parse_args()

