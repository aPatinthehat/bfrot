#!/usr/bin/env python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", action='store_true', help="file containing ROT data")
parser.add_argument("-s", action='store_true', help="ROT encoded string")
parser.add_argument("data", help="data")
args = parser.parse_args()

if args.s:
	encoded = args.data

else:
	stuff = ''
	with open(args.data) as file:
		for line in file:
			stuff += line
	encoded = stuff.strip()

def code_char(string,shift):
	decoded=''

	for l in string:
		letter = ord(l)

		if letter>=65 and letter <=90:
			letter=letter+shift

			while letter>90:
				letter=letter-26

		elif letter>=97 and letter <=122:
			letter=letter+shift

			while letter>122:
				letter=letter-26

		letter = chr(letter)
		decoded += letter

	print(decoded + '\n')

count=0

while count < 27:
	count += 1
	code_char(encoded,count)
