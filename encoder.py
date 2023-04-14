import base64
import sys
import re

# https://www.leeholmes.com/searching-for-content-in-base-64-strings/


def enc(input):
    return base64.b64encode(input.encode('utf-8')).decode('utf-8')

def trim_padding(input):
    reobj = re.compile("=+?")
    match = reobj.search(input)
    if match:
        return input[:match.start()-1] 
    else:
        return input

input = sys.argv[1]
print(input)
regex2 = "({}|{}|{})".format(trim_padding(enc(input)), trim_padding(enc("0"+ input)), trim_padding(enc("00" + input)))


print(regex2)
