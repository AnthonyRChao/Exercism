from re import findall

def abbreviate(words):
    return ''.join(c[0].upper() for c in findall('[a-zA-Z\']+', words))

