#!/usr/bin/env python3

total = 0
while total != 1000:
   total = 0
   s = input()
   start = 0
   p = start
   while p < len(s) and s[p] != "+":
      p = p + 1
   total = int(s[start:p]) + int(s[p + 1:])
   print(total)
   start = p + 1
