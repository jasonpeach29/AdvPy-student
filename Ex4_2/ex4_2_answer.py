"""

"""
import re
import argparse

from collections import defaultdict
from ex4_2_build import validate_ssn, validate_ipv4, validate_phone


def main(file):
    print("SSNs present are for demonstration only")
    result = defaultdict(int)
    vals = [validate_ssn, validate_ipv4, validate_phone]
    with open(file) as fin:
        for line in fin.readlines():
            for validator in vals:
                if validator(line.strip()):
                    result[validator.__name__] += 1
    for k in result:
        print("{}: {}".format(k, result[k]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find SSN in text of file')
    parser.add_argument('file', type=str, help='file to search')
    args = parser.parse_args()
    main(args.file)