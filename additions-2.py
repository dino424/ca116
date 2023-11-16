#!/usr/bin/env python3

t = input()
i = 0
s = 0
total = 0
while i < 5:
   p = s
   while p < len(t) and t[p] != "+":
      p = p + 1
   total = total + int(t[s:p])
   s = p + 1
   i = i + 1
print(total)
