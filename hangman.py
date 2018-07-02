# Hangman game
# by Sarah Meng
# 2018-07-02

import random

def draw_man(progress):
	#  O
	# /|\
	# / \
    if progress == 0:
        print("No hanged parts yet! :)")
        return
    for i in range(0, progress)): # I don't like how this reads... not intuitive
        if i == 0:
            print(" O")
        elif i == 1 and progress == 2:
		    print(" |")
        elif i == 2 and progress == 3:
		    print("/|")
		elif i == 3 and progress <= 4:
		    print("/|\")
		elif i == 4 and progress == 5:
		    print("/")
			print("Yikes.")
		else: # i == 5 and progress == 6
		    print("/ \")
			print("Uh oh...")
	return

# hardcoded word bank
# pick one word randomly
# be nice and print category of word
category = random.choice(["Color", "Language", "Animal"])
print("Category: " + category)
if category == "Color":
    word = random.choice(["crimson", "tangerine", "lemon", "grass", "teal", "cerulean", "indigo", "lavender", "magenta"])
elif category == "Language":
    word = random.choice(["Python", "Spanish", "Java", "English", "HTML", "Chinese", "Swift", "Indonesian"])
else: # category == "Animal"
    word = random.choice(["tiger", "beaver", "falcon", "bass", "kangaroo", "thylacine"])

# keep track of which letters have already been guessed
guessed = []

# user can have 6 wrong guesses
incorrect = 0

while incorrect < 6:
    # ask user for guess
	guess = 0
	if not guess.isalpha():
	    guess = input("Guess a letter or the word: ")
	
	if guess == word:
		print("You guessed the word! You win!")
		draw_man(incorrect)
		# update word progress to be complete
		# show word progress
    

# while guess does not contain only letters, keep re-prompting

# if guess is multiple letters and is the answer, YOU WIN
# else decrement wrong guesses

# if guess is single letter:
#     if dupe guess of letter, do nothing

#     elif wrong guess, decrement wrong guesses remaining and add to person

#     elif correct guess, record it

# show word progress and man progress