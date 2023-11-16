#!/usr/bin/env python3

import os

files = os.listdir(".")
i = 0

while i < len(files):
   t = len(files[i])
   if os.path.isfile(files[i]) and files[i][t - 4:] != ".bak":
         with open(files[i]) as f:
            with open(files[i] + ".bak", "w") as f1:
               f1.write(f.read())
   i = i + 1
