#!/usr/bin/env python3

import os

file = os.listdir(".")
i = 0
while i < len(file):
   t = len(file[i])
   if file[i][t - 4:] != ".bak":
      j = 0
      with open(file[i]) as f:
         with open(file[i] + ".bak", "w") as f1:
            f1.write(f.read())
   i = i + 1
