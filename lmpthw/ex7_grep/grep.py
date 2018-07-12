import argparse, re
import os

class Parser(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description = "Print lines matching a pattern")

    def get_parser(self):
        self.parser.add_argument('path',type=str, help="The place to start searching from")
        self.parser.add_argument('match', type=str, help='Pattern to match')
        self.parser.add_argument('-f', action='store_false', help='Obtain patterns strictly from file')
        return self.parser

    def run_parser(self):
        parser = self.get_parser()
        self.args = vars(parser.parse_args())
        return self.args


class GreppedFiles(object):

    def __init__(self, args):
        self.f = args['f']
        self.path = args['path']
        self.the_match = args['match']

    def check_line(self,fr):
        for line in fr:
            if re.search(self.the_match, line):
                subbed = re.sub(self.the_match, "\033[44;77m" + self.the_match + "\033[m", line)
                print(subbed)
            else:
                continue
        return



    def grep(self):
        if os.path.isdir(self.path):
            for dname, dirs, files in os.walk(self.path):
                files = [f for f in files if not f[0] == '.']
                dirs[:] = [d for d in dirs if not d[0] == '.']
                for fname in files:
                    fpath = os.path.join(dname, fname)
                   # print(f">>>>> File: {fpath}")
                    with open(fpath) as f:
                        try:
                            fr = f.readlines()
                        except UnicodeDecodeError:
                            print("Decode error")
                        self.check_line(fr)
        elif os.path.isfile(self.path):
            with open(self.path) as f:
                fr = f.readlines()
                self.check_line(fr)

        return


def main():
    parser = Parser()
    args = parser.run_parser()
    gf = GreppedFiles(args)
    gf.grep()

if __name__ == '__main__':
    main()

