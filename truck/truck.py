import sys

from environ import Environ
from source import Source
from lexer import Lexer
from parser import Parser

def run_prompt():
    environ = Environ()
    print('Truck v0.1')
    while True:
        string = input('>>> ')
        source = Source(string)
        lexer = Lexer(source)
        parser = Parser(lexer)
        parser.parse()
        parser.root.eval(environ)


def run_file(filename):
    string = ''
    with open(filename, 'r') as f:
        string = f.read()
    source = Source(string)
    lexer = Lexer(source)
    parser = Parser(lexer)
    parser.parse()
    environ = Environ()
    parser.root.eval(environ)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[-1]
        run_file(filename)
    elif len(sys.argv) == 1:
        run_prompt()
    else:
        print("see help")
