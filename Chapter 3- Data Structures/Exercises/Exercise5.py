# -*- coding: utf-8 -*-
"""
Exercise 5: Change Guest List
"""
#Guest list of people invited from previous exercise
guest = ["Elon Musk", "God", "Vincent Van Gogh"]
#Just to notify which person in the list cannot make it.
print(guest[0], "cannot make it due to being too egotistic.")
#guest 0 has been replaced
guest = ["Carl Sagan", "God", "Vincent Van Gogh"]
#new invitation for the replacing guest, as well as the previous statements
print("Salutations, Mr." ,guest[0], "I would like to have a talk about the mysteries of the universe over dinner.")
print("Hello!", guest[1], ", you are invited to share a night of dining and drinking with a very curious atheist.")
print("Mr.", guest[2], ", you are hereby invited to a celebration of your artistry and lifetime work over dinner.")