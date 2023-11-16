#!/usr/bin/env python3


with open("irish-dobs.txt") as f1:
   idob = f1.readline()
   idob = idob.strip()
   with open("american-dobs.txt", "w") as f:
      while idob != "":
         i = 0
         while idob[i] != " ":
            i = i + 1
         idobn = idob[0:i].split("/")
         tmp = idobn[0]
         idobn[0] = idobn[1]
         idobn[1] = tmp
         idobn = "/".join(idobn)
         adob = idobn + " " + idob[(i + 1):] + "\n"
         f.write(adob)
         idob = f1.readline()
         idob = idob.strip()
