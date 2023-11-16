#!/usr/bin/env python3

n = input()
i = 0
total = 0
while i < len(n):
   t = n[len(n) - i - 1]
   new_t = int(t) * 2 ** i
   total = total + new_t
   i = i + 1
print(total)
