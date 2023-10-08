# scrabble.py
from wordscore import score_word

def run_scrabble(rack):
    # Check for input errors
    if not (2 <= len(rack) <= 7):
        return "Invalid rack length. Please provide 2 to 7 characters."
    
    wildcard_count = rack.count('?') + rack.count('*')
    if wildcard_count > 2:
        return "Too many wildcards. You can use up to one '?' and one '*'."
    
    if wildcard_count == 2 and not ('*' in rack and '?' in rack):
        return "Invalid wildcard usage. You can use either '?' or '*' as wildcards."
    
    # read the list of valid Scrabble words from sowpods.txt
    with open("sowpods.txt", "r") as infile:
        valid_words = [word.strip() for word in infile.readlines()]

    # Initialize a list to store valid Scrable words along with their scores
    valid_word_scores = []

    # iterate through the valid words and check if they can be constructed from the rack
    for word in valid_words:
        if can_construct_word(word, rack):
            score = score_word(word)
            valid_word_scores.append((score, word.upper()))

    # sort the list by score (desc order) and then alphabetically ( ascending order)
    valid_word_scores.sort(key=lambda x: (-x[0], x[1]))

    # return the sorted list and the total number of valid words
    return valid_word_scores, len(valid_word_scores)


def can_construct_word(word, rack):
    # making a copy of the rack to avoid modifying the original rack
    remaining_rack = list(rack)
    
    for char in word:
        if char in ('?', '*'):
            # Handle wildcard character
            if '?' in remaining_rack:
                remaining_rack.remove('?')
            elif '*' in remaining_rack:
                remaining_rack.remove('*')
            else:
                return False
        elif char in remaining_rack:
            remaining_rack.remove(char)
        else:
            return False

    # Check if there are any remaining characters in the rack
    if remaining_rack:
        return False

    return True

