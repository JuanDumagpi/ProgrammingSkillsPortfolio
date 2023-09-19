# -*- coding: utf-8 -*-
"""
Exercise 7: Seeing the World
"""
#variable for the list of locations
loc = ["Japan", "Finland", "Britain", "Ireland", "New Zealand"]

#prints original list
print("Original")
print(loc)

#extra space to clean up
print("\n")

#prints the list in alphabetical order and original for comparison WIHOUT changing the original list
print("Sorted Alphabetical + Original")
s_loc = sorted(loc)
print (s_loc)
print (loc)

print("\n")


#prints the list in reverse alphabetical order and original for comparison WIHOUT changing the original list
print("Sorted Reverse alphabetical + Original")
r_loc = sorted(loc, reverse=True)
print (r_loc)
print (loc)

print("\n")

#prints the original list in reverse order
print("Reverse Original")
loc.reverse()
print (loc)

print("\n")

#reversed again, back to original order
print("Back to Original")
loc.reverse()
print (loc)

print("\n")

#original list now sorted to alphabetical order
print("Alphabetical")
loc.sort()
print(loc)

print("\n")

#original list now sorted to reverse alphabetical order
print("Reverse Alphabetical")
loc.sort(reverse=True)
print(loc)