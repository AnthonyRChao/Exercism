from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)

def is_pangram(sentence):
    """Checks if sentence uses every letter in the alphabet at least once"""
    return ALPHABET.issubset(sentence.lower())

