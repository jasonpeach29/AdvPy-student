"""
:::Author:  Derrick Beckman
:::File:    ex4_1.py
:::Desc:    This program will decode a caesar ciphered document through the use of
            statistical lookup to determine the proper cipher setting.
"""
import argparse
import string
import base64


from Crypto.Cipher import DES, AES
from hashlib import md5


def main(file):
    data = ""
    with open(file) as f:
        data = f.readlines()
    evalCaesarCipher(data)


def caesarEncode(data, shift):
    """
    Takes a text string input and encodes it into caesar ciphered text
    :param data: string text
    :param shift: integer to shift by
    :return: encoded string
    """

    result = ''
    for letter in data:
        if letter.isupper():
            base_position = string.ascii_uppercase.find(letter)
            encoded_position = (base_position + shift) % 26
            result += string.ascii_uppercase[encoded_position]
        elif letter.islower():
            base_position = string.ascii_lowercase.find(letter)
            encoded_position = (base_position + shift) % 26
            result += string.ascii_lowercase[encoded_position]
        else:
            result += letter
    return result


def caesarDecode(data, shift):
    """
    Takes encoded text and decodes it based on the shift
    :param data: encoded string
    :param shift: integer to shift by
    :return: decoded text
    """

    return caesarEncode(data, shift * -1)

def atbashConvert(data):
    """
    Encodes and Decodes atbash cipher text
    :param data: text string to encode or decode
    :return: encoded or decoded string
    """

    result = ''
    for letter in data:
        if letter.isupper():
            base_position = string.ascii_uppercase.find(letter)
            encoded_position = ((base_position + 1) * -1) #This seems wrong
            result += string.ascii_uppercase[encoded_position]
        elif letter.islower():
            base_position = string.ascii_lowercase.find(letter)
            encoded_position = ((base_position + 1) * -1) #This seems wrong
            result += string.ascii_lowercase[encoded_position]
        else:
            result += letter
    return result


def base64Encode(data):
    return base64.b64encode(data)


def base64Decode(data):
    return base64.b64decode(data)


def DESEncode(data, key):
    des = DES.new(key, DES.MODE_ECB)
    return des.encrypt(data)


def DESDecode(data, key):
    des = DES.new(key, DES.MODE_ECB)
    return des.decrypt(data)


def AESEncode(data, key):
    aes = AES.new(key)
    return aes.encrypt(data)


def AESDecode(data, key):
    aes = AES.new(key)
    return aes.decrypt(data)


def MD5Hash(data):
    return md5(data).hexdigest()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Decode caesar ciphered file')
    parser.add_argument('file', type=str, help='file to decode', required=True)
    args = parser.parse_args()
    main(args.file)