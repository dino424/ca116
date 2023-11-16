#!/usr/bin/env python3

import sys

s = sys.argv[1]
s = int(s)
n = s
i = 0
a = []
while i < 9:
   if n % 2 == 0:
      n = n // 2
      a.append(n)
   else:
      n = (n * 3) + 1
      a.append(n)
   i = i + 1
j = 0
while j < len(a):
   print(a[len(a) - j - 1])
   j = j + 1
print(s)
