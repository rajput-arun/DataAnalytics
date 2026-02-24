"""
Event Planning


We're organizing a large tech and fashion expo and have separate lists of attendees for each department.
Your task is to use set methods to analyze this information.

union() - to get the list of all unique visitors to the expo.
intersection() — to find attendees interested in both tech and fashion.
difference() — to identify attendees who are interested in only tech, but not in fashion.
Write a function event_planning() that should return a tuple of two sets:
    those who prefer both directions, and those who prefer only one direction.
"""

def event_planning(electronics_attendees: set, clothing_attendees: set) -> tuple[set, set]:

    both = electronics_attendees & clothing_attendees
    only_one  = electronics_attendees ^ clothing_attendees



    print(f"Both : {both}")
    print(f"Only One : {only_one}")

    return(both, only_one)


electronics_attendees = {"Alex", "Maria", "John"}
clothing_attendees = {"John", "Sophia", "Maria", "Mike"}

event_planning(electronics_attendees, clothing_attendees) == ({"John", "Maria"}, {"Alex", "Sophia", "Mike"})

#event_planning(electronics_attendees, clothing_attendees) == ({"John", "Maria"}, {"Alex", "Sophia", "Mike"})
