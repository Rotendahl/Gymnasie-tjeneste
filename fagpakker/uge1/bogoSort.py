from random import *

cards = sample(range(0, 13), 10)


def shuffle(cards):
    return sample(range(len(cards)), len(cards))


def isSorted(cards):
    for i in range(1, len(cards)):
        if not (cards[i-1] <= cards[i]):
            return False
    return True


def bogoSort(cards):
    cards = cards
    while(not isSorted(cards)):
        cards = shuffle(cards)
    return cards


print bogoSort(cards)
