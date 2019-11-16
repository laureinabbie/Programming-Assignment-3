def Hangman(secretWord):
    print('Welcome to Hangman!')
    print('The Secret Word is consists of',len(secretWord), "letters.")
    mistakesMade = 0
    lettersGuessed = []

    while 30 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('------------')
            print('You got it! Congratulations!')
            break
        else:
        	print('------------')
        	guess = str(input('Please guess a letter:')).lower()
        	if guess in secretWord and guess not in lettersGuessed:
        		lettersGuessed.append(guess)
        		print('Nice!:', getGuessedWord(secretWord, lettersGuessed))
        	elif guess in lettersGuessed:
        		print("Oops! You've already guessed that:", getGuessedWord(secretWord, lettersGuessed))
        	elif guess not in secretWord:
        		print("Uh-oh! Try again.", getGuessedWord(secretWord, lettersGuessed))
        		lettersGuessed.append(guess)
        		mistakesMade += 1
        if 30 - mistakesMade == 0:
        	print('------------')
        	print('Game Over. The Secret Word is: ', secretWord)
        	break
        else:
        	continue

