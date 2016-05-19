#!/usr/local/bin/python3

from collections import namedtuple
numStudents = int(input())
Student = namedtuple('Student', input())
print(sum(list(float(x.MARKS) for x in [Student(*input().split()) for _ in range(numStudents)]))/numStudents)
