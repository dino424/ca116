#!/usr/bin/env python3

import sys
check = []
s = sys.stdin.readline().strip()
p = s.split()
while s != "":
   names = p[0] + " " + p[1]
   if int(p[2]) >= 40:
      check.append(names)
   s = sys.stdin.readline().strip()
   p = s.split()
i = 0
while i < len(check):
   print(check[i])
   i = i + 1
