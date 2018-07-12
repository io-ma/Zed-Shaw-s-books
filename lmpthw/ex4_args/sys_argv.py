"""
This is a program that encodes any text using the ROT13 cipher.
You need 2 files in the same dir with this script: text.txt and result.txt. Write your text in text.txt, run the script and you will get the  encoded version in result.txt.

Usage:
    sys_argv.py -i <text.txt> -o <result.txt>
"""


import sys, codecs

for arg in sys.argv[1:]:
    arg_pos = sys.argv[1:].index(arg) + 1
    if arg in ["-h", "--help", "-i", "--input", "-o", "--output"]:
        if arg == "-h" or arg == "--help":
            v = __doc__
            print(v)
        elif arg == "-i" or arg == "--input":
            ifile = sys.argv[arg_pos + 1]
            text = ifile
        elif arg == "-o" or arg == "--output":
            ofile = sys.argv[arg_pos +1]
            result = ofile
        else:
            print("""You need an input and an output file. Type -h for more info.""")



class Encode(object):


    def encode_txt(self):
        """ This function encodes the text """
        txt = open(text)
        read = txt.read()
        encoded = codecs.encode(read, 'rot_13')
        target = open(result, 'w')
        target.write(encoded)
        target.close()

def main():
    encode = Encode()
    encode.encode_txt()
    print("Succes! Your file is encoded.")

if __name__ == "__main__":
    main()



