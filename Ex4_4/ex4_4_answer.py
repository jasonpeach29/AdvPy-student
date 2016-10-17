from __future__ import print_function
"""

"""
import itertools
import string
import zipfile
import time
import argparse


def main(file):
    zfile = zipfile.ZipFile(file, 'r')
    start = time.time()
    print('Starting crack at {}'.format(time.strftime('%j: %H:%M:%S', time.localtime(start))))
    print('.', end='')
    for i, p in enumerate(gen_pass(maxval=4)):
        if not i % 1000: print('.', end='')
        if not i % 100000: print('\n{}'.format(i / 100000), end='')
        if p == 's@f3': print('found s@f3')
        try:
            #print('{}: trying password: {}'.format(i, p))
            zfile.extractall(pwd=p)
            print('\nThe password is {}'.format(p))
            print('That took {} seconds'.format(time.time()-start))
            exit(0)
        except RuntimeError:
            pass
        except Exception as e:
            #print('{}: {}'.format(p, e))
            pass


def gen_pass(minval=3, maxval=4):
    letters = string.ascii_lowercase
    numbers = '0123456789'
    symbols = '!@#'
    characters = list(letters) + list(numbers) + list(symbols)
    while maxval >= minval:
        for p in itertools.product(characters, repeat=maxval):
            yield ''.join(p)
        maxval -= 1


def pass_test(length=3):
    a = 0
    for p in gen_pass(maxval=length):
        a+=1
    return a


def gen_file(minval, maxval, out_file):
    with open(out_file, 'w') as fout:
        for p in gen_pass(minval, maxval):
            fout.write('{}\n'.format(p))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Brute force a password protected zip file')
    parser.add_argument('file', type=str, help='zip file to crack')
    args = parser.parse_args()
    main(args.file)