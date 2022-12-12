#!/usr/bin/env python3

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("input_number", help="User-provided number to convert", type=str)
parser.add_argument("--verbose", "-v", help="Enable verbose output", action="store_true")

# specifiers for input/output formats are both required,
# but their respective variants need to be mutually exclusive
input_group = parser.add_mutually_exclusive_group(required=False)
output_group = parser.add_mutually_exclusive_group(required=True)

# just have --input and --output accept a string; one of decimal, binary, hex; check against string content later
# complain on unexpected input string, but validate against as many as you can think of [h, hex ,hexadecimal, 0x, etc.]
input_group.add_argument("--input", help="Specify input format [ decimal | binary | hex ]", type=str, action="store")
output_group.add_argument("--output", help="Specify output format [ decimal | binary | hex ]", type=str, action="store")

# implement pseudo-BSD-esque short options that combine input and output specification
# e.g. "-dx" or "-dh" for decimal input and hex output
input_group.add_argument("-id", help="User input is decimal", action="store_true")
input_group.add_argument("-ib", help="User input is binary", action="store_true")
input_group.add_argument("-ix", help="User input is hexadecimal", action="store_true")
input_group.add_argument("-ih", help="User input is hexadecimal", action="store_true")

output_group.add_argument("-od", help="Convert input to decimal", action="store_true")
output_group.add_argument("-ob", help="Convert input to binary", action="store_true")
output_group.add_argument("-ox", help="Convert input to hexadecimal", action="store_true")
output_group.add_argument("-oh", help="Convert input to hexadecimal", action="store_true")

args       = parser.parse_args()


# now perform aforementioned input checking
def check_user_input():
    global input_format
    global output_format
    global user_input

    user_input = args.input_number
    decimal_matches = ["d", "dec", "decimal", "0d", "0D"]
    binary_matches = ["b", "bin", "binary", "0b", "0B"]
    hex_matches = ["h", "hex", "hexadecimal", "x", "0x", "0X"]
    format_error = "Please provide any of: \n \"dec\", \"decimal\" | \"bin\", \"binary\" | \"hex\", \"hexadecimal\""

    # you might recognize this as a fake match/case statement
    # yeah, Python versions prior to 3.10 didn't provide those
    if args.input is not None:
        if args.input in decimal_matches:
            input_format = "decimal"
        elif args.input in binary_matches:
            input_format = "binary"
        elif args.input in hex_matches:
            input_format = "hex"
        else:
            input_format = "invalid"
    elif args.id:
        input_format = "decimal"
    elif args.ib:
        input_format = "binary"
    elif args.ix or args.ih:
        input_format = "hex"
    else:
        # it is a reasonable assumption most users might mean decimal input when they don't instinctively specify
        input_format = "decimal"

    # handle output separately, because pertaining options may very well drift over time
    # also, since this script is written for illustrative purposes, this solution yields a lot of quasi-duplicate code,
    # but also avoids a set of loops with compound conditions, lists of variables and the like - it's just simpler
    if args.output is not None:
        if args.output in decimal_matches:
            output_format = "decimal"
        elif args.output in binary_matches:
            output_format = "binary"
        elif args.output in hex_matches:
            output_format = "hex"
        else:
            output_format = "invalid"
    elif args.od:
        output_format = "decimal"
    elif args.ob:
        output_format = "binary"
    elif args.ox or args.oh:
        output_format = "hex"
    else:
        output_format = "invalid"

    # yell at the user if they fail to provide usable format specs
    if input_format == "invalid":
        print("Input:", format_error)
    elif output_format == "invalid":
        print("Output:", format_error)

    # check whether we were lied to all along
    if input_format == "decimal":
        try:
            user_input = int(user_input, 10)
        except:
             print("You filthy scoundrel!")
    elif input_format == "binary":
        try:
            user_input = int(user_input, 2)
        except:
             print("You filthy scoundrel!")
    elif input_format == "hex":
        try:
            user_input = int(user_input, 16)
        except:
             print("You filthy scoundrel!")


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


def hex_convert(number_to_convert: int) -> str:
    hex_table = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    hex_store = ""
    while number_to_convert > 0:
        remainder = number_to_convert % 16
        hex_store = hex_table[remainder] + hex_store
        number_to_convert = number_to_convert // 16
    return hex_store


