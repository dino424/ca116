#!/usr/bin/env python3

i = 0
j = 0
while i < 10:
   s = input()
   j = 0
   while j < len(s) and s[j] != "+":
      j = j + 1
   a = int(s[0:j]) + int(s[j + 1:])
   print(a)
   i = i + 1
