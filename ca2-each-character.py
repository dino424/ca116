#!/usr/bin/env python3

with open("characters.txt") as f:
   text = f.read()
   i = 0
   while i < len(text):
      if text[i] == "\n":
         print()
      else:
         print(text[i])
      i = i + 1
