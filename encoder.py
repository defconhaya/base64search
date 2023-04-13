import base64
import sys

# https://www.leeholmes.com/searching-for-content-in-base-64-strings/

def display(line, nth):    
    res =  [line[i:i+nth] for i in range(0, len(line), nth)]
    for x in res:
        print("{} ".format(x),end =" ")
    print()

def enc(input):
    return base64.b64encode(input.encode('ascii')).decode('ascii')

def print_bin(input):
     return ''.join(format(ord(x), 'b') for x in input)

def pr_mut(input):    
    print("{}\t{}\t{} ".format(input, enc(input), print_bin(enc(input))))
    for x in range(0, 10):
        v = "{}{}".format(x , input)
        print("{}\t{}\t{} ".format(v,enc(v), print_bin(enc(v))))



input = sys.argv[1]
pr_mut(input)
v1 = "0" + input
v2 = input + "0"


b64 = base64.b64encode(input.encode('ascii')).decode('ascii')
b64_1 = base64.b64encode(v1.encode('ascii')).decode('ascii')
b64_2 = base64.b64encode(v2.encode('ascii')).decode('ascii')

print (" ".join("{:02x}".format(ord(c)) for c in b64))
bin1 = ''.join(format(ord(x), 'b') for x in b64)
bin2 = ''.join(format(ord(x), 'b') for x in input)
bv1 = ''.join(format(ord(x), 'b') for x in b64_1)
bv2 = ''.join(format(ord(x), 'b') for x in b64_2)

print(bin1)
print (bv1)
print (bv2)
# print ("{}:\t\t".format(input), end=' ')
# display(bin2,7)
# print ("{}:\t".format(b64), end=' ')
# display(bin1,6)
# print("\t{}".format(bin1))

