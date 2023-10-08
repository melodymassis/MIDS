# wordscore.py

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def score_word(word):
    """
    This function is super important yet straightforward
    provides necessary function for the scrabble.py file
    Handles wildcard '*' as a wildcard character 
    """
    score = 0
    for letter in word:
        letter_score = scores.get(letter.lower(), 0)
        if letter_score == 0:
            return 0  # Return 0 if any non-wildcard character is not found in the scores dictionary
        score += letter_score
    return score