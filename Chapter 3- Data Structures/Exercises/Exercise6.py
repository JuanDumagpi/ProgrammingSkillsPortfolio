"""
Shrinking Guest List
"""

#Guest List
guest = ["Carl Sagan", "God", "Vincent Van Gogh"]
print("It has come to my attention that my new dinner table will not arrive today. As such there will be a change in guests.")

#space to make it look clean
print("\n") 

#removing guest, and showing updated list
print("Removed guests:", guest.pop(1))
print("Updated guest list:", guest)

print("\n")

#showing guests with unchanged status
print(guest[0], "your status as a guest has not changed and we welcome you to dinner.")
print(guest[1], "your status as a guest has not changed and we welcome you to dinner.")

#deleting guest from list
del guest[1]
del guest[0]
#printing empty list, and showing that the list is empty
print(guest)

print("\n")

if guest==[]:
    print("You have no people left in the guest list.")