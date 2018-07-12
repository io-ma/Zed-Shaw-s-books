import argparse, glob, os
from pathlib import Path

class Parser(object):
    """ Parse CLI arguments"""

    def __init__(self):
        self.parser = argparse.ArgumentParser(description = "Finds a file")

    def get_parser(self):
        self.parser.add_argument('path', type=str, help='name of the dir to start the search from')
        self.parser.add_argument('name', help='Pattern to match')
        return self.parser

    def run_parser(self):
        parser = self.get_parser()
        self.args = vars(parser.parse_args())
        return self.args

class Finder(object):

    def __init__(self, args):
        self.args = args
        self.path = self.args['path']
        self.name = self.args['name']


    def find_file(self):
            p = Path(self.path)
            for f in p.glob(self.name):
                files = set()
                files.add(f)
                for f in files:
                    print(f)
            # file_list = list(p.rglob(self.name))
            # print(">>>>file_list is:", file_list)
            #files = set()
            #for f in file_list:
            #files.add(f)
            #for f in files:
            #print(f)

def main():
    parser = Parser()
    args = parser.run_parser()
    finder = Finder(args)
    finder.find_file()

if __name__ == '__main__':
    main()
