import argparse, re
import os

class Parser(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description = "Print lines matching a pattern")

    def get_parser(self):
        self.parser.add_argument('search', type=str, help='Pattern to search for')
        self.parser.add_argument('replace', type=str, help='String to replace with')
        self.parser.add_argument('path',type=str, help="The place to start searching from")
        self.parser.add_argument('file_out', type=str, help='File out')
        return self.parser

    def run_parser(self):
        parser = self.get_parser()
        self.args = vars(parser.parse_args())
        return self.args


class SedFiles(object):

    def __init__(self, args):
        self.search = args['search']
        self.replace = args['replace']
        self.path = args['path']
        self.file_out = args['file_out']

    def check_line(self,fi):
        results_list = []
        for line in fi:
            if re.search(self.search, line):
                subbed = re.sub(self.search, self.replace, line)
                results_list.append(subbed)
            else:
                continue
        result = ''.join(results_list)
        print("result is:", result)
        return result

    def sed(self):
        fi = None
        if os.path.isfile(self.path):
            with open(self.path) as f:
                fi = f.readlines()
        else:
            print("Feed me a file, I am not that fancy yet.")

        return self.check_line(fi)


def main():
    parser = Parser()
    args = parser.run_parser()
    sf = SedFiles(args)
    sd = sf.sed()
    fo = sf.file_out

    print(">>>>> SD is:", sd)
    with open(fo, 'w') as target:
        target.write("\n")
        target.write(sd)
        target.write("\n")
    print("\033[44;77m>>>>> Success! Your file is written.\033[m")


if __name__ == '__main__':
    main()

