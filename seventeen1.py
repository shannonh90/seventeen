#Seventeen Game
#The jar begins with seventeen marbles, and each player can remove one, 
#two, or three marbles during each turn. 

#human always goes first
#if human enters incorrect input(anthing other 1,2,3) or a number larger than how
#many marbles are left, display error
#prompt them to try again
#computer chooses random number (or always same as human)
#at the end of each turn, print number of marbles removed, # left in jar
#when no marbles left, computer delcares winner

#imports
import random

#check human input
def validate_human(guess, marble_count): 
	lst = ["1", "2", "3"]
	if (str(guess) not in lst) or (int(guess) > marble_count):
		print("Sorry, that is not a valid option. Try again!")
		print("Number of marbles left in jar: {}".format(marble_count))
		guess = input("\nYour turn: How many marbles will you remove (1-3)? ")
		guess = validate_human(guess, marble_count)
	else:
		return int(guess)

#check computer input is < marble_count
def validate_computer(number, marble_count):
	while number > marble_count:
		number = random.randint(1,3)
	return number

#run game
def seventeen():
	print("\nLet's play the game of Seventeen!")
	marble_count = 17
	print("Number of marbles left in jar: {}".format(marble_count))
	while marble_count > 0:
		guess = input("\nYour turn. How many marbles will you remove (1-3)? ")
		guess = validate_human(guess, marble_count)  #sending guess to check
		print("You removed {} marbles".format(guess))
		marble_count -= guess
		if marble_count > 0:
			print("Number of marbles left in jar: {}".format(marble_count))
			print("\nComputer's turn...")
			number = random.randint(1,3)
			number = validate_computer(number, marble_count) #sending guess to check
			print("Computer removed {} marbles.".format(number))
			marble_count -= number
			if marble_count > 0:
				print("Number of marbles left in jar: {}".format(marble_count))
		else:
			print("There are no marbles left. Computer wins!")
			exit()

	print("There are no marbles left. You win!")
	exit()


def main():
	seventeen()

if __name__ == "__main__":
	main()


