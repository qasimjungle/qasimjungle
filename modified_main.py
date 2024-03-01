import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import re

SearchTypes = ['\t\033[0;31m   1.search return first  match if there is present',
               '\t\033[0;31m                2.Find all mathched search of string',
               '\033[0;31m                  3. split retrun a list where the string is split at each match where it is found',
               '\t\033[0;31m                4. sub replace string a string with match']

SearchOptions = ['\t\033[0;31m\t   A. Find matched string',
                 '\t\033[0;31m                   B. check if string start with entered character or not',
                 '\t\033[0;31m                    C. entere string starting and unknonw letter with .. and ending with speciifed letter',
                 '\t\033[0;31m                  D. Find any string']
UserSearchTypeMessage = "Enter the value of( int value) type of search from the above :"
UserInputMessage = "Enter yes to continue or no to exit"
UserSearchOptionMessage = "Enter Option A,B,C OR D to perform Operation"
StrinInputMessage = "Enter A STRING"
FileOpenMessage = "Enter the File name with .txt extension to open for search:"
string_start_with_message = 'Enter letter to find if string start with it ot not '
Unknown_start_letter_string = "Enter the starting letter"
Unknown_ending_letter_string = "Enter the Endsing letter"
Unknown_letter_message = "Enter the . instead of unknown letter please make sure . is use instead of unknown letter"
Replace_Input_Message = "Enter the String to be replaced"
Number_of_Replacement_String = "Enter How many times you want to replace the matched string"
First_Function_Object_Search_Type = {
    'a': "matched_string",
    'b': 'string_start_with',
    'c': 'find_unknown_letter_string',
    'd': 'find_any_string'
}


def open_file():
    a = open(str(a), 'r')
    a = a.read()
    a = str(a)
    return a


def matched_string():
    a = input(FileOpenMessage, '>')
    c = input(StrinInputMessage, '>')
    x = re.search(str(c), a)
    print(c)


def string_start_with():
    a = input(FileOpenMessage, '>')
    n = input(string_start_with_message, ">")
    x = re.search(n, a)
    print(x)


def find_unknown_letter_string():
    a = input(FileOpenMessage, ">")
    z = input(Unknown_start_letter_message, ">")
    b = input(Unknown_ending_letter_messade, ">")
    c = input(Unknown_letter_message, ">")
    x = re.search(z + c + b, a)
    print(x)


def find_any_string():
    a = input(FileOpenMessage, file_open())
    if x in a:
        print("\"" + x + "\"")
        print('yes it is present')
    else:
        print('No it is not present')


def uesr_search_type_input(UserSearchTypeMessage):
    x = int(input(UserSearchTypeMessage, "|>"))
    return x


def user_search_option_input(UserInputMessage):
    y = input(UserSearchOptionMessage)
    user_input = y.lower()
    return user_input


def replace_input():
    f = input(Replace_Input_Message, ">")
    k = int(input(Number_of_Repalcement_String, ">"))


def ask_user_continue_or_exit():
    user_i = take_user_input("Enter 'y' to continue or 'n' to exit the program")
    return True if user_i.lower() == "y" else False


User_Search_Type_Input = True
if __name__ == "__main__":

    while True:
        while True:
            user_input = user_search_option_input("\n".join(SearchOptions))
            ask_user_continue_or_exit()
    if x == 2:
        while True:
            if y == 'a':
                a = input(FileOpenMessage, '>')
                c = input(StrinInputMessage, '>')
                x = re.findall(str(v), a)
                print(x)
            elif y == 'b':
                a = input(FileOpenMessage, '>')
                n = input(string_start_with_message, ">")
                x = re.findall(n, a)
                print(x)
            elif y == 'c':
                a = input(FileOpenMessage, ">")
                z = input(Unknown_start_letter_message, ">")
                b = input(Unknown_ending_letter_messade, ">")
                c = input(Unknown_letter_message, ">")
                x = re.findall(z + c + b, a)
                print(x)
            elif y == 'd':
                find_any_string()
                ask_user_continue_or_exit()
    if x == 3:
        while True:
            if y == 'a':
                a = input(FileOpenMessage, '>')
                c = input(StrinInputMessage, '>')
                c = re.split(x, a)
                print(c)
            elif y == 'b':
                a = input(FileOpenMessage, '>')
                n = input(string_start_with_message, ">")
                x = re.split(n, a)
                print(x)
            elif y == 'c':
                a = input(FileOpenMessage, ">")
                z = input(Unknown_start_letter_message, ">")
                b = input(Unknown_ending_letter_messade, ">")
                c = input(Unknown_letter_
                message, ">")
                x = re.split(z + c + b, a)
                print(x)
            elif y == 'd':
                find_any_string()
                ask_user_continue_or_exit()
    if x == 4:
        while True:
            if y == 'a':
                a = input(FileOpenMessage, '>')
                c = input(StrinInputMessage, '>')
                replace_input()
                c = re.sub(str(x), str(f), a, k)
                print(c)
            elif y == 'b':
                a = input(FileOpenMessage, '>')
                n = input(string_start_with_message, ">")
                replace_input()
                c = re.sub(str(x), str(f), a, k)
                print(c)
        elif y == 'c':
        a = input(FileOpenMessage, ">")
        z = input(Unknown_start_letter_message, ">")
        b = input(Unknown_ending_letter_messade, ">")
        c = input(Unknown_letter_message, ">")
        replace_input()
        x = re.sub(z + c + b, str(f), a, k)
        print(x)
    elif y == 'd':
        find_any_string()
        replace_input()
        x = x.sub(str(z), str(f), a, k)
        print(x)
