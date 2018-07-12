import sys, argparse

class Parser(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description = "Print elements in order, after removing the duplicates.")

    def get_parser(self):
        self.parser.add_argument('-input',type=str, nargs='+', help="File or files to remove duplicates from.")
        return self.parser

    def run_parser(self):
        parser = self.get_parser()
        self.args = vars(parser.parse_args())
        return self.args

def unique(stuff_in):
    uniques = set()
    for line in stuff_in:
        uniques.add(line)
    for i in uniques:
        sys.stdout.write(i)

def main():
    parser = Parser()
    args = parser.run_parser()
    input_files = args['input']
    string_list = []

    if input_files:
        for f in input_files:
            with open(f) as f:
                rl = f.readlines()
                unique(rl)
    else:
        unique(sys.stdin)

main()

