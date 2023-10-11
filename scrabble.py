# scrabble.py
from wordscore import score_word


def run_scrabble(rack):
    """
    This function checks if valid Scrabble words can be constructed from the rack
    and returns the valid words sorted by score and alphabetically.
    """
    # Check for input errors
    if not isinstance(rack, str):
        return "Invalid input. Please provide a string as the rack."

    if not (2 <= len(rack) <= 7):
        return "Invalid rack length. Please input 2 to 7 characters."
    
    wildcard_count = rack.count('?') + rack.count('*')
    if wildcard_count > 2:
        return "Too many wildcards. You can use up to one '?' and one '*'."
    
    if wildcard_count == 2 and not ('*' in rack and '?' in rack):
        return "Invalid wildcard usage. You can use either '?' or '*' as wildcards."
    
    # Check for numeric characters in the rack
    if any(char.isdigit() for char in rack):
        return "Invalid characters in the rack. Please remove numbers."

    # read the list of valid Scrabble words from sowpods.txt
    with open("sowpods.txt", "r") as infile:
        valid_words = [word.strip() for word in infile.readlines()]

    # Initialize a list to store valid Scrabble words along with their scores
    valid_word_scores = []


    # iterate through the valid words and check if they can be constructed from the rack
    for word in valid_words:
        if len(word) <= len(rack) and can_construct_word(word, rack):
            score = score_word(word)
            valid_word_scores.append((score, word.upper()))

    # sort the list by score (desc order) and then alphabetically (ascending order)
    valid_word_scores.sort(key=lambda x: (-x[0], x[1]))
    
    # return the sorted list and the total number of valid words
    return valid_word_scores, len(valid_word_scores)



def can_construct_word(word, rack):
    """
    This function checks if a given word can be constructed from a rack
    with wildcard characters represented by '?' and '*' characters.
    """
    # Convert both word and rack to lowercase
    word = word.lower()
    rack = rack.lower()

    # Count the number of wildcard characters in the rack
    wildcard_count = rack.count('?') + rack.count('*')

    # If there are no wildcard characters, use the original function
    if wildcard_count == 0:
        remaining_rack = list(rack)
        for char in word:
            if char in remaining_rack:
                remaining_rack.remove(char)
            else:
                return False
        return True

    # Generate word combos with wildcsrds
    
    def generate_combinations(prefix, remaining_word):
        combinations = []
        if not remaining_word:
            combinations.append(prefix)
        else:
            char = remaining_word[0]
            if char in rack:
                generate_combinations(prefix + char, remaining_word[1:])
            if '?' in rack:
                for wildcard_char in 'abcdefghijklmnopqrstuvwxyz':
                    generate_combinations(prefix + wildcard_char, remaining_word[1:])
                    
        generate_combinations('',word)
    
    