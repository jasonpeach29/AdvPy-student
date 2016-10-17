from __future__ import print_function
"""

"""

import argparse

from passlib.hash import md5_crypt, sha256_crypt, sha512_crypt


def main(shadow, wordlist):
    with open(shadow, 'r') as fin:
        for p_hash in fin.readlines():
            evaluate_hash(p_hash, wordlist)


def evaluate_hash(p_hash, wordlist):
    hash_algos = {'1': md5_crypt, '5': sha256_crypt, '6': sha512_crypt}
    hash_list = p_hash.split(':')
    pass_list = hash_list[1][1::].split('$')
    if len(pass_list) != 3:
        print('User {} has no password'.format(hash_list[0]))
        return
    with open(wordlist, 'r') as wordlist_in:
        print('Evaluating {}'.format(hash_list[0]), end='')
        for i, word in enumerate(wordlist_in.readlines()):
            if i % 1000 == 0: print('.', end='')
            if hash_algos[pass_list[0]].verify(word.strip(), hash_list[1]):
                print('User {} has password {}'.format(hash_list[0], word))
                return
    print('User {} password not found'.format(hash_list[0]))
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Crack shodow file passwords')
    parser.add_argument('shadow', type=str, help='shadow file to crack')
    parser.add_argument('wordlist', type=str, help='wordlist to try against shadow file')
    args = parser.parse_args()
    main(args.shadow, args.wordlist)