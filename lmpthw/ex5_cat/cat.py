import argparse
import fileinput

parser = argparse.ArgumentParser(description = "Prints the content of a file or concatenates more files")
parser.add_argument('files', type=str, help='name of input files', nargs='+')
args = parser.parse_args()

for f in args.files:
    output = open(f)
    print(output.read())



