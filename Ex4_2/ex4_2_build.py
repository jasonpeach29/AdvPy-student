import re
import argparse
import random
import loremipsum

from string import ascii_letters
from collections import defaultdict


def gen_line(tracker):
    gen_types = [gen_good_ipv4, gen_bad_ipv4, gen_good_phone, gen_bad_phone, gen_good_ssn, gen_bad_ssn, gen_lorem]
    next_fun = random.choice(gen_types)
    tracker[next_fun.__name__] += 1
    return next_fun()


def gen_lorem():
    return loremipsum.get_sentence()


def gen_good_ipv4():
    result = []
    for i in xrange(3):
        result.append(random.randint(0,255))
        result.append('.')
    result.append(random.randint(0,255))
    ip = ''.join([str(i) for i in result])
    if not validate_ipv4(ip):
        raise ValueError('Something in the IP builder broke, {}'.format(ip))
    return ip


def gen_bad_ipv4():
    ip = gen_good_ipv4()
    octets = ip.split('.')
    separators = ['.', '.', '.']
    changes = random.randint(1,3)
    while changes:
        action = random.randint(0,2)
        if action == 0:
            separators[random.randint(0,len(separators)-1)] = random.choice('-+*_!')
        if action == 1:
            octet = random.randint(0, len(octets)-1)
            octets[octet] = str(int(octets[octet]) + random.randint(255,900))
        if action == 2:
            random.choice([octets, separators]).pop()
        changes -= 1

    result = ['' for i in xrange(len(octets) + len(separators))]
    for i in xrange(max([len(octets), len(separators)])):
        try:
            result.append(octets[i])
        except IndexError:
            pass
        try:
            result.append(separators[i])
        except IndexError:
            pass
    new_ip = ''.join(result)

    if not bad_validator(new_ip):
        raise ValueError('SOB that failed hard, {}'.format(new_ip))
    return new_ip


def gen_good_phone():
    result = []
    result.append(str(random.randint(200,999)))
    result.append("{:03d}".format(random.randint(000,999)))
    result.append("{:04d}".format(random.randint(0000,9999)))
    sep = random.choice(['-', '/', '.', ' ', ''])
    if random.choice([True, False]):
        result[0] = '({})'.format(result[0])
    phone = sep.join(result)
    if not validate_phone(phone):
        raise ValueError('Something in the Phone builder broke, {}'.format(phone))
    return phone


def gen_bad_phone():
    phone = gen_good_phone()
    changes = random.randint(1, 3)
    pattern = re.compile(r'\(?(\d{3})\)?[-/ .]?(\d{3})[-/ .]?(\d{4})')
    phone_match = pattern.search(phone)
    result = [phone_match.group(1), phone_match.group(2), phone_match.group(3)]
    while changes:
        action = random.randint(0, 1)
        index = random.randint(0, len(result)-1)
        if action == 0:  #Delete number
            result[index] = result[index][0:-1]
        if action == 1:  #Change number to other character
            result[index] = result[index].replace(random.choice(result[index]), random.choice(ascii_letters))
        changes -= 1
    sep = random.choice(['-', '/', '.', ' ', ''])
    if random.choice([True, False]):
        result[0] = '({})'.format(result[0])
    phone = sep.join(result)
    if not bad_validator(phone):
        raise ValueError('Bad Phone builder broke, {}'.format(phone))
    return phone


def gen_good_ssn():
    result = []
    result.append(str(random.randint(100, 899)))
    result.append("{:02d}".format(random.randint(01, 99)))
    result.append("{:04d}".format(random.randint(0001, 9999)))
    while result[0] == '666':
        result[0] = str(random.randint(100,899))
    sep = random.choice(['-', ' ', ''])
    ssn = sep.join(result)
    if not validate_ssn(ssn):
        raise ValueError('SSN Builder broke, {}'.format(ssn))
    return ssn


def gen_bad_ssn():
    ssn = gen_good_ssn()
    changes = random.randint(1, 3)
    pattern = re.compile(r'(\d{3}).?(\d{2}).?(\d{4})')
    ssn_match = pattern.search(ssn)
    result = [ssn_match.group(1), ssn_match.group(2), ssn_match.group(3)]
    while changes:
        action = random.randint(0, 1)
        index = random.randint(0, len(result) - 1)
        if action == 0:  # Delete number
            result[index] = result[index][0:-1]
        if action == 1:  # Change number to other character
            if len(result[index]):
                result[index] = result[index].replace(random.choice(result[index]), random.choice(ascii_letters))
        changes -= 1
    sep = random.choice(['-', ' ', ''])
    new_ssn = sep.join(result)
    if not bad_validator(new_ssn):
        raise ValueError('Bad SSN builder broke, {}'.format(new_ssn))
    return new_ssn


def bad_validator(check):
    vals = [validate_phone, validate_ssn, validate_ipv4]
    for val in vals:
        if val(check):
            return False
    return True

def validate_ipv4(ip):
    pattern = re.compile('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    return pattern.match(ip)


def validate_phone(phone):
    pattern = re.compile(r'''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    $           # end of string
    ''', re.VERBOSE)
    return pattern.search(phone)


def validate_ssn(ssn):
    pattern = re.compile(r'^(?!219[\s-]?09[\s-]?9999|078[\s-]?05[\s-]?1120)(?!666|000|9\d{2})\d{3}[\s-]?(?!00)\d{2}[\s-]?(?!0{4})\d{4}$')
    return pattern.match(ssn)


def main(file, size):
    tracker = defaultdict(int)
    with open(file, 'w') as fout:
        for i in xrange(size):
            try:
                fout.write(gen_line(tracker))
                fout.write('\n')
            except ValueError as e:
                print(e)
                continue

    for k in tracker:
        print('{}: {}'.format(k, tracker[k]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Build Regex list file')
    parser.add_argument('file', type=str, help='file to write to')
    parser.add_argument('size', type=int, help='size of file to build')
    args = parser.parse_args()
    main(args.file, args.size)