import re
import argparse

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('word', help='specify word to search for')
    parser.add_argument('fname', help='specify file to search')
    args = parser.parse_args()

    with open (args.fname) as searchFile:
        lineNum = 0
        for line in searchFile.readlines():
            line = line.rstrip()
            lineNum += 1
            searchResult = re.search (args.word, line, re.M | re.I)
            if searchResult:
                print(f'{lineNum}: {line}')

if __name__ == '__main__':
    Main()
