def isWordGuessed(secretWord, lettersGuessed):
    for guess in secretWord:
        if guess not in lettersGuessed:
            return False
    return True
