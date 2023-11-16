#!/usr/bin/env python3

mark = int(input())
print("first:", 70 <= mark)
print("second:", 50 <= mark <= 69)
print("third:", 40 <= mark <= 49)
print("fail:", 0 < mark < 40)
