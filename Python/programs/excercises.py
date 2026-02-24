"""
while True:
    user_input = input("Enter \"exit\" to stop the program: ")
    if user_input.lower() == "exit":
        break
    print(f"You entered: {user_input}")


import random
import time

while True:
    server_command = random.choice(["running", "stop"])
    if server_command == "stop":
        print("Server is shutting down.")
        break
    else:
        print("Server is running smoothly.")
    time.sleep(1)
"""
"""
finding Prime Numbers 
"""

x=[1,2,3]
def change(lst):
    lst = lst + [4]
    print(lst)
    return lst

change(x)
print(x)

players_height = [171, 190, 182, 176, 169, 188, 180, 181, 188, 175]
number_of_tall_players = 0
for height in players_height:
    if height > 185:
        number_of_tall_players += 1
print(f"Number of tall players: {number_of_tall_players}")

