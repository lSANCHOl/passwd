#!/bin/python3

import sys
import secrets


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
print("9: custom_set")

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
if choice == "9":
    characters = input("input characters you want to use: ")

length = len(characters)
pass_len = int(input("how long for the password?: "))
multiple = int(input("how many passwords should be created?: "))
passwords = [ ]
mylist = []
while len(mylist) < multiple:
    for j in range(multiple):
        password = ''.join(secrets.choice(characters) for i in range(pass_len-1))
        passwords.append(password)
        #password = ""
        mylist = passwords
        mylist = list(dict.fromkeys(mylist))
	

output = input("print resuts or store in text file? [p/s]: ")
appearance = input("show numbers on side? [y/n]: ")

if output == "p":
    if appearance == "y":
        for i in range(len(mylist)):
            print(i+1,".",mylist[i-1])
    if appearance == "n":
        for i in range(len(mylist)):
            print(mylist[i-1])

if output == "s":
    f = open("passwd.txt","w+")
    if appearance == "y":
        print("[+]Passwords are stored as \'passwd.txt\' in current dirctory[+]")
        for i in range(len(mylist)):
            i_str = i+1
            f.write(str(i+1))
            f.write(".")
            f.write(mylist[i-1])
            f.write('\n')
            f.close
        if appearance == "n":
            print("[+]Passwords are stored as \'passwd.txt\' in current dirctory[+]")
            for i in range(len(mylist)):
                f.write(mylist[i-1])
                f.write('\n')
                f.close

