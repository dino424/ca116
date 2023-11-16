#!/usr/bin/env python3

s = input()
t = input()
if len(s) > len(t):
   print(s)
elif len(t) > len(s):
   print(t)
elif s > t:
   print(s)
else:
   print(t)
