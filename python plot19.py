# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
import os 
import re
while True:
 print("\t1.search return first  match if there is present\t2.Find all mathched search of string\t3. split retrun a list where the string is split at each match where it is found\t4. sub replace string a string with match")
 x=int(input('Enter the value of( int value) type of search from the above :'))
 if x==1:
  while True:
   print("\tA. Find matched string\tB.check if string start with entered character or not\tC.entere string starting and unknonw letter with .. and ending with speciifed letter\tD.Find any string")
   y=str(input('Entere  a choce form the above'))
   if y=='a':     
      a=str(input('Enter the File name with.txt extention to open for search: '))
      print("Enter the string to find in file")
      c=str(input('Enter the string :'))
      x=re.search(str(c),a)
      print(c)
      u=str(input('Do you want to continue( yes or no)')).lower()
   elif y=='b':
      a=input('enter file name')
      a=open(str(a),'r')
      a=a.read()
      a=str(a)
      print("Find if Entered  string starting with some special letters")
      n=str(input('Enter   characters to find whether a string is starting in file is present or not'))
      x = re.search(n, a)
      print(x)
   elif y=='c':
      print("Find the word with specified starting letter and followed by any letter and ending with specified letter")
      a=str(input('Enter the File name with.txt extention to open for search: '))
      z=str(input('Enter the starting letters'))
      b=str(input('Enter the ending letters'))
      c=str(input('Enter Dots to to repsent how many character should be place between enentered alphabets'))
      x = re.search(z+c+b, a)
      print(x)
   elif y=='d':
      a=input('enter file name')
      a=open(str(a),'r')
      a=a.read()
      a=str(a)
      x=str(input('Enter string'))
      if x in a:
       print("\""+x+"\"")
       print('yes it is present')
      else:
       print('No it is not present')
   else:
      print("Please enter right option")
   h=str(input('Do you want to continue enter yes or no to quit')).lower()
   if h=='yes':
    continue
   else:
    break




 if x==2:
  while True:
    print("\tA. Find matched string\tB.check if string start with entered character or not\tC.entere string starting and unknonw letter with .. and ending with speciifed letter\tD.Find any string") 
    y=str(input('Enter the choice from above only:'))
    if y=='a':     
  
           a=str(input('Enter the File name with.txt extention to open for search: '))
           print("Enter the string to find in file")
           v=str(input('Enter the string :'))
           x=re.findall(str(v),a)
           print(x)
    elif y=='b':
          a=input('enter file name')
          a=open(str(a),'r')
          a=a.read()
          a=str(a)
          print("Find if Entered  string starting with some special letters")
          n=str(input('Enter   characters to find whether a string is starting in file is present or not'))
          x = re.findall(n, a)
          print(x)
    elif y=='c':      
          print("Find the word with specified starting letter and followed by any two letter and ending with specified letter")
          a=str(input('Enter the File name with.txt extention to open for search: '))
          z=str(input('Enter the starting letters'))
          b=str(input('Enter the ending letters'))
          c=str(input('Enter Dots to to repsent how many character should be place between enentered alphabets'))
          x = re.findall(z+c+b, a) 
          print(x)
    elif y=='d':    
          a=input('enter file name')
          a=open(str(a),'r')
          a=a.read()
          a=str(a)
          z=str(input('Enter string'))
          if z in a:
           print("\""+z+"\"")
           print('yes it is present')
          else:
           print('No it is not present')
    h=str(input('Do you want to continue enter yes or no to quit')).lower()
    if h=='yes':
     continue
    else:
     break





 if x==3:
  while True:
    print("\tA. Find matched string\tB.check if string start with entered character or not\tC.entere string starting and unknonw letter with .. and ending with speciifed letter\tD.Find any string") 
    y=str(input('Enter the choice from above only:'))
    if y=='a':     
              a=str(input('Enter the File name with.txt extention to open for search: '))
              print("Enter the string to find in file")
              x=str(input('Enter the string :'))
              c=re.split(x,a)
              print(c)
    elif y=='b':
              a=input('enter file name')
              a=open(str(a),'r')
              a=a.read()
              a=str(a)
              print("Find if Entered  string starting with some special letters")
              n=str(input('Enter   characters to find whether a string is starting in file is present or not'))
              x = re.split(n, a)
              print(x)
    elif y=='c':
              print("Find the word with specified starting letter and followed by any two letter and ending with specified letter")
              a=str(input('Enter the File name with.txt extention to open for search: '))
              z=str(input('Enter the starting letters'))
              b=str(input('Enter the ending letters'))
              c=str(input('Enter Dots to to repsent how many character should be place between enentered alphabets'))
              x = re.split(z+c+b, a)
              print(x)
    elif y=='d':
              a=input('enter file name')
              a=open(str(a),'r')
              a=a.read()
              a=str(a)
              z=str(input('Enter string'))
              if z in a:
                print("\""+z+"\"")
                print('yes it is present')
              else:
                print('No it is not present')  
    h=str(input('Do you want to continue enter yes or no to quit')).lower()
    if h=='yes':
     continue
    else:
     break


    
  
 if x==4:
  while True:
    print("\tA. Find matched string\tB.check if string start with entered character or not\tC.entere string starting and unknonw letter with .. and ending with speciifed letter\tD.Find any string") 
    y=str(input('Enter the choice from above only:'))
    if y=='a':     
              a=str(input('Enter the File name with.txt extention to open for search: '))
              print("Enter the string to find in file")
              x=str(input('Enter the string :'))
              f=str(input('Entered the string ro replace with match strings'))
              k=int(input('Enter how many times you will want to replace the string:'))
              c=re.sub(str(x),str(f), a,k)
              print(c)
    elif y=='b':
              a=input('enter file name')
              a=open(str(a),'r')
              a=a.read()
              a=str(a)
              print("Find if Entered  string starting with some special letters")
              x=str(input('Enter   characters to find whether a string is starting in file is present or not'))
              f=str(input('Entered the string ro replace with match strings'))
              k=int(input('Enter how many times you will want to replace the string:'))
              c=re.sub(str(x),str(f), a,k)
              print(c)
    elif y=='c':
              print("Find the word with specified starting letter and followed by any two letter and ending with specified letter")
              a=str(input('Enter the File name with.txt extention to open for search: '))
              z=str(input('Enter the starting letters'))
              b=str(input('Enter the ending letters'))
              c=str(input('Enter Dots to to repsent how many character should be place between enentered alphabets'))
              f=str(input('Entered the string ro replace with match strings'))
              k=int(input('Enter how many times you will want to replace the string:'))
              
              x = re.sub(z+c+b,str(f), a,k)
              print(x)
    elif y=='d':          
              a=input('enter file name')
              a=open(str(a),'r')
              a=a.read()
              a=str(a)
              z=str(input('Enter string'))
              if z in a:
                   print("\""+z+"\"")
                   print('yes it is present')
                   f=str(input('Entered the string ro replace with match strings'))
                   k=int(input('Enter how many times you will want to replace the string:'))
                   x=x.sub(str(z),str(f),a,k)
       
              else: 
                   print('No it is not present')
    h=str(input('Do you want to continue enter yes or no to quit this method ')).lower()
    if h=='yes':
     continue
    else:
     break
                   