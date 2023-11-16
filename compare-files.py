#!/usr/bin/env python3

import sys
f1 = sys.argv[1]
f2 = sys.argv[2]

with open(f1) as f1:
   with open(f2) as f2:
      i = 0
      l1 = f1.readline()
      l2 = f2.readline()
      while i < len(l1) and i < len(l2):
         j = 0
         while j < len(l1) and j < len(l2):
            if l1[j] != l2[j]:
               print(i, j)
            j = j + 1
         l1 = f1.readline()
         l2 = f2.readline()
         i = i + 1
