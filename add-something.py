#!/usr/bin/env python3

a = []
n = input()
while n != "end":
   n = int(n)
   a.append(n)
   n = input()
m = int(input())
i = 0
while i < len(a):
   a[i] = a[i] + m
   print(a[i])
   i = i + 1
