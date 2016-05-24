#!/usr/bin/python

import sys


def atoi(str):
   isNegative = False;
   pointer = 0;
   solution = 0;
   while pointer<len(str) and str[pointer] == ' ':
       pointer = pointer+1;
   if pointer == len(str):
       return 0;
   if str[pointer] == '-':
       isNegative == 1;
       pointer +=1;
   while pointer < len(str):
       if not str[pointer].isdigit():
           break;
       solution = solution*10;
       solution = solution + int(str[pointer])
       pointer = pointer+1;
   print solution;


def itoa(num,base):
    isNegative = False;
    strlist = [];
    if (num == 0):
        return 0;
    if(num < 0):
        IsNegative = 1;
        num  = -num
    while(num is not 0):
        rem = num%base;
        if(rem>9):            
          strlist.append(chr(rem-10+ord('a')));
        else:
          strlist.append(chr(rem + ord('0')));
        num = num/base;
    if(isNegative):
        strlist.reverse();
    return ''.join(strlist);



if __name__ == "__main__":
       atoi('1')
       print itoa(30,16)
