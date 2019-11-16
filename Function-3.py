import string
convert = string.ascii_lowercase

def getAvailableLetters(lettersGuessed):
    lettersLeft = []
    for guess in convert:
        if guess not in lettersGuessed:
            lettersLeft.append(guess)
    return ''.join(lettersLeft)

