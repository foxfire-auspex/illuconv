# IlluConv - An Illustrative Number System Converter

## Quickstart
```
usage: illuconv.py [-h] [--verbose] [--input INPUT] [--output OUTPUT] [-id] [-ib] [-ix] [-ih] [-od] [-ob] [-ox] [-oh] input_number

positional arguments:
  input_number     User-provided number to convert

options:
  -h, --help       show this help message and exit
  --verbose, -v    Enable verbose output

  --input INPUT    Specify input format [ decimal | binary | hex ]
  --output OUTPUT  Specify output format [ decimal | binary | hex ]

  -id              User input is decimal
  -ib              User input is binary
  -ix              User input is hexadecimal
  -ih              User input is hexadecimal

  -od              Convert input to decimal
  -ob              Convert input to binary
  -ox              Convert input to hexadecimal
  -oh              Convert input to hexadecimal
```