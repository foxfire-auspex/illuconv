#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_number", help="User-provided integer to convert", type=int)
parser.add_argument("-b", "--to_binary", help="Convert input to binary", action="store_true", default=False)
parser.add_argument("-d", "--to_decimal", help="Convert input to decimal", action="store_true", default=False)
args = parser.parse_args()

# TODO: Only accept integers (and binary numbers)


def binary_convert(number_to_convert: int) -> list:
    binary_store = []
    while number_to_convert >= 1:
        if number_to_convert ==1:
            binary_store.append(1)
            break
        else:
            if number_to_convert % 2 != 0:
                number_to_convert = int(number_to_convert / 2)
                binary_store.append(1)
            else:
                number_to_convert = int(number_to_convert / 2)
                binary_store.append(0)
    return(binary_store[::-1]) # fancy slicing syntax that reverses our list


def decimal_convert(number_to_convert: int) -> int:
    store = [int(x) for x in str(number_to_convert)] # list comprehension that puts every digit of the input integer in a list
    store = store[::-1]
    loopvar = 0
    metastore = 0
    for digit in store:
        if digit == 1:
            metastore += 2**loopvar
            loopvar += 1
        elif digit == 0:
            loopvar += 1
    return metastore

if args.to_binary:
    print(binary_convert(args.input_number))
elif args.to_decimal:
    print(decimal_convert(args.input_number))
