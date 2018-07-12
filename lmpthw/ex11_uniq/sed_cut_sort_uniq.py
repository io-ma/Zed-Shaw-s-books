#!/usr/bin/env python3.6

import sys, argparse, re

class Parser(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description = "Search and replace elements from stdin, cut the ones needed, sort them and remove duplicates.")
        self.parser.add_argument('search' , type=str, help="sequence to search for")
        self.parser.add_argument('replace', type=str, help="sequence to replace with")
        self.parser.add_argument('-d', type=str, help="Delimiter")
        self.parser.add_argument('-f', type=int, help='Select only these fields')

    def get_parser(self):
        return self.parser

    def run_parser(self):
        parser = self.get_parser()
        self.args = vars(parser.parse_args())
        return self.args

class Sedder(object):

    def __init__(self, args):
        self.search = args['search']
        self.replace = args['replace']

    def check_line(self, fi):
        results_list = []
        for line in fi:
            if re.search(self.search, line):
                pat = re.compile(r"{self.search}")

                subbed = re.sub(pat, r"{self.replace}", line)
                results_list.append(subbed)
            else:
                continue
        return results_list

class Cutter(object):

    def __init__(self, args):
        self.d = args['d']
        self.f = args['f']
        self.splitted = []
        self.res = []


    def cut_strings(self, stin):
        for line in stin:
            self.splitted = line.split(self.d)
            raw = self.splitted[self.f]
            result = ''.join(raw)
            self.res.append(result)
        return self.res


class Sorter(object):
    def __init__(self):
        self.total = []

    def sort(self, stin):
        for l in stin:
            self.total.append(l)
        srted = (sorted(self.total))
        print("sorted is:", srted)
        return srted


class Uniquer(object):

    def __init__(self):
        pass

    def unique(self, stuff_in):
        uniques = set()
        for line in stuff_in:
            uniques.add(line)
        for i in uniques:
            print(i)

def main():
    parser = Parser()
    args = parser.run_parser()
    print(">>> ARGS are:", args)
    sedder = Sedder(args)
    cutter = Cutter(args)
    sorter = Sorter()
    uniquer = Uniquer()

    s = sedder.check_line(sys.stdin)
    for line in s:
        print(f">>>{line}<<<")
    c = cutter.cut_strings(s)
    sor = sorter.sort(c)
    u = uniquer.unique(sor)

    u



main()
