#!/usr/bin/env python3

import sys
n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]
a = {}

i = 0
while i < len(src):
   a[src[i]] = dst[i]
   i = i + 1

s = sys.stdin.read()
j = 0
while j < len(s):
   if s[j] in a:
      sys.stdout.write(a[s[j]])
   else:
      sys.stdout.write(s[j])
   j = j + 1
