#!/usr/bin/env python3

s = input()
i = 0
total = 0
while i < len(s):
   if s[i] >= "a" and s[i] <= "z":
      total = total + 1
   i = i + 1
print(total)
