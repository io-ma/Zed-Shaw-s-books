import argparse
import os
import sys
import fileinput

class Parser(object):

    def __init__(self):
        self.parser = argparse.ArgumentParser(description = "Remove sections from each line of files and print them")

    def get_parser(self):
        self.parser.add_argument('-d', type=str, help="Delimiter")
        self.parser.add_argument('-f', type=int, help='Select only these fields')
        self.parser.add_argument('-file_in',type=str, help="The file to cut from. If not specified will cut from stdin")

        return self.parser

    def run_parser(self):
        parser = self.get_parser()
        self.args = vars(parser.parse_args())
        return self.args

class StuffToCut(object):

    def __init__(self, args):
        self.file_in = args['file_in']
        self.d = args['d']
        self.f = args['f']


    def cut_strings(self):
        if self.file_in:
            with fileinput.input(self.file_in) as f:
                for line in f:
                    splitted = line.rstrip('\n').split(self.d)
                    if self.f:
                        raw = splitted[self.f - 1]
                        result = ''.join(raw)
                    else:
                        raw = splitted[1:]
                        result = ''.join(raw)
                    print(result)
        else:
            for line in sys.stdin:
                splitted = line.split(self.d)
                if self.f:
                    raw = splitted[self.f]
                    result = ''.join(raw)
                else:
                    raw = splitted[1:]
                    result = ''.join(raw)
                print(result)
        return


def main():
    parser = Parser()
    args = parser.run_parser()
    stc = StuffToCut(args)
    stc.cut_strings()

if __name__ == '__main__':
    main()


