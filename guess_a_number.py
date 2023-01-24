import random

cpu_number = random.randint(1, 100)

# Read Player's Move
while True:
	player_input = input("Guess a n umber between 1 and 100: ")

	if not player_input.isdigit():
		print("Invalid input. Try again..... ")
		continue
	player_input = int(player_input)
	if player_input == cpu_number:
		print("You guess it !")
		break
	elif player_input < cpu_number:
		print("Too Low")
	else:
		print("Too High")