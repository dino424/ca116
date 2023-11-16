#!/usr/bin/env python3

n = int(input())
running = True
while running:
   m = int(input())
   if n % 2 == 0 and m == n // 2:
      print(n, m)
      running = False
   elif n % 2 != 0 and m == (n * 3) + 1:
      print(n, m)
      running = False
   n = m
