#!/usr/bin/python3
""" Script prints a calendar from the year provided in interactive mode """

from calendar import *
year = int(input("Enter year: "))
print(calendar(year))
