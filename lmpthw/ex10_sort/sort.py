import argparse, itertools

class Parser(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description = "Print elements in order.")

    def get_parser(self):
        self.parser.add_argument('input',type=str, nargs='+', help="File or files to sort.")
        self.parser.add_argument('-r', action="store_true", help="Print sorted elements in reversed order.")
        self.parser.add_argument('-o', type=str, action="store", help="Write sorted elements to a file.")
        return self.parser

    def run_parser(self):
        parser = self.get_parser()
        self.args = vars(parser.parse_args())
        return self.args

def main():
    parser = Parser()
    args = parser.run_parser()
    print("Args are:", args)
    input_files = args['input']
    string_list = []
    total = []
    file_out = args['o']

    for f in input_files:
        with open(f) as f:
            rl = f.readlines()
            string_list.append(rl)
    for i in string_list:
        total += i
    srted = (sorted(total))
    result = ''.join(srted)
    if args['r']:
        rev = reversed(srted)
        res = ''.join(rev)
        print(res)
    elif args['o']:
        with open(file_out, 'w') as target:
            target.write(result)
        print("Success! Your file is written.")
    else:
        print(result)


main()
