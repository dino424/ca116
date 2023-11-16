#!/usr/bin/env python3

kg = int(input())
cm = int(input())
bmi = kg / (cm * cm) * 10000
if bmi >= 30.0:
   print("obese")
elif bmi >= 25.0:
   print("overweight")
elif bmi >= 18.5:
   print("normal")
else:
   print("underweight")
