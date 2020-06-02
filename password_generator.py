#!/bin/python3

import sys
import random

char_set1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!\"£$%^&*()-_=+[{]};:'@#~\|,<.>/?"
char_set2 = "abcdefghijklmnopqrstuvwxyz"
char_set3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
char_set4 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
char_set5 = "1234567890"
char_set6 = "abcdefghijklmnopqrstuvwxyz1234567890"
char_set7 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
char_set8 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

print("OPTION: characters")
print("1: ", char_set1)
print("2: ", char_set2)
print("3: ", char_set3)
print("4: ", char_set4)
print("5: ", char_set5)
print("6: ", char_set6)
print("7: ", char_set7)
print("8: ", char_set8)

choice = input("which option of characters do you want to include?: ")
characters = ""

if choice == "1":
	characters = char_set1
if choice == "2":
	characters = char_set2
if choice == "3":
	characters = char_set3
if choice == "4":
	characters = char_set4
if choice == "5":
	characters = char_set5
if choice == "6":
	characters = char_set6
if choice == "7":
	characters = char_set7
if choice == "8":
	characters = char_set8

length = len(characters)
pass_len = int(input("how long for the password?: "))
multiple = int(input("how many passwords should be created?: "))
password = ""

for j in range(multiple):
	for i in range(pass_len):
		ran_num = random.randint(0,length - 1)
		ran_char = characters[ran_num]
		password += ran_char
	print("[PASSWORD][+] ",password," [+]")
	password = ""
