# -*- coding: utf-8 -*-
"""
Seeing the World
"""
loc = ["Japan", "Finland", "Britain", "Ireland", "New Zealand"]

print("Original")
print(loc)
print("\n")

print("Sorted Alphabetical + Original")
s_loc = sorted(loc)
print (s_loc)
print (loc)

print("\n")

print("Sorted Reverse alphabetical + Original")
r_loc = sorted(loc, reverse=True)
print (r_loc)
print (loc)

print("\n")

print("Reverse Original")
loc.reverse()
print (loc)

print("\n")

print("Back to Original")
loc.reverse()
print (loc)

print("\n")

print("Alphabetical")
loc.sort()
print(loc)

print("\n")

print("Reverse Alphabetical")
loc.sort(reverse=True)
print(loc)