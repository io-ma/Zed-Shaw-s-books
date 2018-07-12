import argparse
import codecs
import os


def write_result(args, encoded):
    """ Write result to the output file """
    result = args['text'][:-4] + '_1.txt'
    with open(result, 'w') as target:
        target.write(encoded)
        target.close()
        print("Success! Your file is encoded.")


def encode(args):
    """ Read the input file and encode it"""

    with open(args['text']) as text:
        txt= text.read()
        encoded = codecs.encode(txt, 'rot_13')

    write_result(args, encoded)

def get_parser():

    parser= argparse.ArgumentParser(description="""
                                            This is a program that encodes any text using the ROT13 cipher.
                                            """)
    parser.add_argument('text', type=str, help='name of the input file')
    return parser

def run_parser():
    parser= get_parser()
    args= vars(parser.parse_args())

    if not os.path.exists(args['text']):
        print("You need a text file, try again.")
        return

    encode(args)

if __name__ == "__main__":
    run_parser()
