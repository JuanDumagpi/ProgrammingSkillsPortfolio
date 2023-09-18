# -*- coding: utf-8 -*-
"""
Shrinking Guest List
"""
guest = ["Carl Sagan", "God", "Vincent Van Gogh"]
print("It has come to my attention that my new dinner table will not arrive today. As such there will be a change in guests.")

print("Removed guests:", guest.pop(1))
print("Updated guest list:", guest)
print(guest[0], "your status as a guest has not changed and we welcome you to dinner.")
print(guest[1], "your status as a guest has not changed and we welcome you to dinner.")

del guest
#error, list is empty
print(guest)