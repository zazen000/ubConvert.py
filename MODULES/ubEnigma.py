import sys, random
import cryptomath as cr_math
from struct import Struct



SYMBOLS = """ !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]
^_`abcdefghijklmnopqrstuvwxyz{|}~"""


def main(myMode, myKey, myMessage):

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    return translated


def getKeyParts(key):

    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)


def checkKeys(keyA, keyB, mode):

    if keyA == 1 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key A is set to 1. Choose a different key.')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))


def encryptMessage(key, message):

    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''

    for symbol in message:
        if symbol in SYMBOLS:

            # encrypt this symbol
            symIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol # just append this symbol unencrypted
    return ciphertext


def decryptMessage(key, message):

    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInverseOfKeyA = cr_math.findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            # decrypt this symbol

            symIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol # just append this symbol undecrypted
    return plaintext


def getRandomKey():

    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cr_math.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB


##  Function that writes the value of *args, **kwargs to a binary file
##  fmt = '' is for the data types being packed, ie: "ffi" denotes three
##  parameters of a float, a float, and an integer. List of data types below.

def write_binary_file(fmt='', filename='',*args, **kwargs):
    from struct import Struct
    mystruct = Struct(fmt)
    data = mystruct.pack(*args, **kwargs)
    with open(filename, "wb") as out:
        out.write(data)

## Reads the binary file and upacks the data

def read_binary_file(fmt='', filename=''):
    from struct import Struct
    fp = open(filename, "rb").read()
    mystruck = Struct(fmt)
    data = mystruck.unpack(fp)
    return data


def write_json_file(filename, data):
    import json
    with open(filename, "a") as file:
        json.dump(data, file)


def write_txt_file(filename='', txt='', option="a"):
    with open(filename, option) as file:
        file.write('\n')
        file.write(txt)


def read_txt_file(filename=''):
    with open(filename, 'r') as file:
        data = file.read()
    return data


def write_csv_file(filename='', option="w"):
    with open(filename, option) as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(rows)


def write_key(fmt='', filename='', *args):
    write_binary_file(fmt, filename, *args) 


## Clandestine pass of key used to decrypt encoded API_ID to user file

def read_key(fmt='', filename=''):
    key = read_binary_file(fmt, filename)
    mykey = int((key)[0])
    return mykey


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap


def generate_key_and_code(bin_name, txt_name, text='api'):  ## 'api' to be encrypted
    write_key('i', bin_name, getRandomKey())                ## encrypt - binary file

    myKey = read_key('i', bin_name)
    myMode = 'encrypt'
    myMessage = text

    coded = main(myMode, myKey, myMessage)
    write_txt_file(txt_name, coded)



if __name__ == "__main__":
    main()

'''
x   pad byte            no value        c   char                bytes of length 1
b   signed char         integer         B   unsigned char       integer
?   _Bool               bool            h   short               integer
H   unsigned short      integer         i   int                 integer
I   unsigned int        integer         l   long                integer
L   unsigned long       integer         q   long long           integer
Q   unsigned long long  integer         n   ssize_t             integer
N   size_t              integer         f   float               float
d   double              float           s   char[]              bytes
p   char[]              bytes
'''