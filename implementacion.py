import sys

from impementacion_lexer import *

def usage():
    sys.stderr.write('Usage: implementacion filename\n')
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
    filename = sys.argv[1]
    text = open(filename).read()
    tokens = implementacion_lexer(text)
    for t in tokens:
        print t
