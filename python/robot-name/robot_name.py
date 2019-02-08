from random import randint, choice
from string import ascii_uppercase


class Robot(object):
    def __init__(self):
        name = []
        for _ in range(2):
            name.append(choice(ascii_uppercase))
        for _ in range(3):
            name.append(str(randint(0, 9)))
        self.name = ''.join(name)

    def reset(self):
        self.name = 'AB123'



