Hangman game programmed with a few weeks' worth of Python knowledge

(I've... known this amount of knowledge for a long time, though)

Game includes a lot of hard-coded words, of which one is randomly chosen per play. I'm nice enough to give the player the category of the word before they start guessing.

The player can guess a letter or the entire word, case-insensitive.

Duplicate letter guesses do not count against the player, but they can see which letters they've guessed anyway. The game will ask for a guess again if the player enters a guess with non-alphabetical characters, so I suppose you can say that they also do not count against the player.

Duplicate word guesses _do_ count against the player, because shame on you if you guess the same wrong word again.

Players get 6 incorrect guesses before they see a fully hanged man (well, more like just a full ASCII stick figure).

To play: Run hangman.py as you would any other Python script (e.g. from the command line).