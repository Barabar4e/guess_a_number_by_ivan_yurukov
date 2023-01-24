import random

# Read Player's Move
cpu_number = random.randint(1, 100)
counter_of_guesses = 0
# Setting the body of Game
while True:
	# initialising player's input and changing the color of text for better vision
	player_input = input("\33[2;34;2m Guess a number between 1 and 100: ")
	# Checking for a proper input data from player
	if not player_input.isdigit():
		print("\33[2;31;2mInvalid input. Try again..... ")
		continue
	player_input = int(player_input)
	counter_of_guesses += 1
	# checking if the first guess is in bullseye
	if player_input == cpu_number and counter_of_guesses == 1:
		print("\33[1;32;2m !!! B U L L S E Y E !!! \n ")
		break
	# checking if the guess is correct or lower or higher than the random computer number
	if player_input == cpu_number:
		print("\33[1;32;2m You guess it !")
		break
	elif player_input < cpu_number:
		print("\33[1;35;20m Too Low")
	else:
		print("\33[1;35;20mToo High")