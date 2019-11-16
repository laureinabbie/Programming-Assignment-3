def getGuessedWord(secretWord, lettersGuessed):
    output = []
    for guess in secretWord:
        if guess in lettersGuessed:
            output.append(guess)
        else:
            output.append('_')
    return ' '.join(output)

