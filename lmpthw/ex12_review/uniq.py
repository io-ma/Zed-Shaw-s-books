#!/usr/bin/env python3.6

import sys, argparse, collections

class Parser(object):
    """ Parse CLI arguments """
    def __init__(self):
        """ Initializes class Parser"""
        self.parser = argparse.ArgumentParser(description = "Print elements after excluding the duplicates.")

    def get_parser(self):
        """ Adds the arguments """
        self.parser.add_argument('-d', action="store_true", help="Report only elements that have duplicates")
        self.parser.add_argument('-c', action="store_true", help="Prefix lines by the number of occurences")
        self.parser.add_argument('-i', action="store_true", help="Ignore case")
        self.parser.add_argument('-D', action="store_true", help="Print all duplicate lines")
        self.parser.add_argument('-u', action="store_true", help="Print unique lines, exclude all duplicates")
        self.parser.add_argument('-input',type=str, help="File to remove duplicates from.")

        return self.parser

    def run_parser(self):
        """ Parse the CLI arguments """
        parser = self.get_parser()
        self.args = vars(parser.parse_args())
        return self.args


class Unique(object):
    """ Finds the unique elements """
    def __init__(self):
        """ Initializes Unique class """
        self.stuff_in = []
        self.uniques = set()
        self.duplicates = []
        self.count = 0

    # check if the elements
    # appear only once or not
    def unique(self, stuff_in):
        """ Finds uniques"""
        for line in stuff_in:
            self.stuff_in.append(line)
            self.uniques.add(line)
        return

    # isolate the duplicates
    def get_duplicates(self):
        """ Finds duplicates"""
        for i in self.uniques:
            count = self.stuff_in.count(i)
            if count > 1:
                for x in range(count):
                    self.duplicates.append(i)
        return self.duplicates

    def check_options(self, args, stuff):
        """ Checks CLI flags"""
        self.unique(stuff)
        self.get_duplicates()

        if args['D']:
            d = ''.join(self.duplicates)
            print(d)

        elif args['d']:
            dupes = set()
            for line in self.duplicates:
                dupes.add(line)
            print(''.join(dupes))

        elif args['i']:
            for line in stuff:
                if line in self.uniques and line.lower() in self.duplicates:
                    self.uniques.remove(line)
                    self.uniques.add(line.lower())
            print(''.join(self.uniques))


        elif args['u']:
            for line in self.stuff_in:
                if line not in self.duplicates:
                    print(line)
                else:
                    continue

        elif args['c']:

            for line in self.uniques:
                self.count = self.stuff_in.count(line)
                print(f"{self.count} {line}")

    def process_input(self, s):
        """Prints uniques"""
        self.unique(s)
        print(''.join(self.uniques))

    def check_input_type(self, args, in_file):
        """Checks if there is an input file or just stdin"""
        if in_file:
            with open(in_file) as f:
                rl = f.readlines()
            if len(sys.argv) == 3:
                self.process_input(rl)
            else:
                self.check_options(args, rl)
        else:
            if len(sys.argv) == 1:
                self.process_input(sys.stdin)
            else:
                self.check_options(args, sys.stdin)


def main():
    parser = Parser()
    args = parser.run_parser()
    input_file = args['input']
    string_list = []
    unique = Unique()
    unique.check_input_type(args, input_file)



if __name__ == "__main__":
    main()

