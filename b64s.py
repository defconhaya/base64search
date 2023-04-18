#!/usr/bin/python3
import argparse
import base64
import sys
import os
import re


def enc(input):
    return base64.b64encode(input.encode('utf-8')).decode('utf-8')

def trim_padding(input):
    reobj = re.compile("=+?")
    match = reobj.search(input)
    if match:
        return input[:match.start()-1] 
    else:
        return input

def search_pattern_in_files(dir_path, ext, pattern):
    """
    Searches for a regular expression pattern in all files with a specified extension in a directory and its subdirectories.
    """
    regex = re.compile(pattern)
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(ext):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    for line_number, line in enumerate(f):
                        if regex.search(line):
                            print(f"Found pattern in file: {file_path} (line {line_number+1}): {line.strip()}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search for a regular expression pattern in all files with a specified extension in a directory and its subdirectories.')
    parser.add_argument('dir_path', type=str, help='The directory to search in')
    parser.add_argument('ext', type=str, help='The file extension to search for')
    parser.add_argument('pattern', type=str, help='The pattern to search for')
    args = parser.parse_args()

    input = args.pattern
    regex2 = "({}|{}|{}|{})".format(trim_padding(enc(input)), trim_padding(enc("0"+ input)), trim_padding(enc("00" + input)),re.escape( input ))
    print(f"RegEx:{regex2}")   
    search_pattern_in_files(args.dir_path, args.ext, regex2 )