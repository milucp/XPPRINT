import argparse
import sys

parser = argparse.ArgumentParser(description='html tree view pprint')
parser.add_argument('html', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='pipe html')
parser.add_argument('--omit', help='omit tag names (space sep)')


def main():
    if sys.stdin.isatty(): sys.exit(1)
    
    args = parser.parse_args()
    
    print(args.html.read())
    
    return 0
