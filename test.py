
'''
def parse_hand(cards):
    rank_map = {
        '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7','8': '8',
        '9': '9', 'T': '10','J': '11', 'Q': '12', 'K': '13', 'A': '14'
    }
    parsed = []
    for card in cards:
        rank = rank_map[card[:-1]] 
        suit = card[-1]
        parsed.append(rank+ suit)
    return parsed

print(parse_hand(['6C', 'KC', '8C', 'QC', 'TC']))
'''

'''
def Stright(hand)
rank = [int(card[:-1]) for card in hand]
rank_sorted = sorted(rank)

is_straight = rank_sorted == list(range(rank_sorted[0], rank_sorted[0] + 5))
return (is_straight)   # ✅ True
'''
'''
def Flush(hand):
    suits = {card[-1] for card in hand}
    hand_suit = suits[0]
    is_flush= len(suits) == 1
    return(is_flush,hand_suit)
'''

'''
hand=['6C', '7C', '8C', '9C', '10C']
def Stright(hand):

    rank = [int(card[:-1]) for card in hand]
    rank_sorted = sorted(rank)
    high = rank_sorted[-1]
    is_straight = rank_sorted == list(range(rank_sorted[0], rank_sorted[0] + 5))
    return (is_straight,high)
'''

'''
def Flush(hand):
    suits = {card[-1] for card in hand}
    is_flush= len(suits) == 1
    return(is_flush)
print(Flush(hand))

'''

#----------------------------

'''
hands=[['6C', '7C', '8C', '9C', 'TC'],['6C', '6C', '6C', '6C', 'TC'],['8C', '8C', '8C', 'TC', 'TC']]     

def allmax(iterable, hand_rank):
    max_lst=[(0,0,0)]
    for item in iterable:
        power = hand_rank(item)
        if power > max_lst[0]:max[0] = power
        elif power == max_lst[0]: max_lst.append(power)
    return max_lst
allmax()
'''

# -----------
# User Instructions
# 
# Write a function, deal(numhands, n=5, deck), that 
# deals numhands hands with n cards each.
#

import random # this will be a useful library for shuffling

# Build a standard deck of 52 cards
mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
def deal(numhands, n=5, deck=mydeck):
    deck = deck[:]            #  Make a copy of the deck to avoid modifying the original
    random.shuffle(deck)      #  Shuffle the deck randomly
    return [deck[i*n: (i+1)*n] for i in range(numhands) ]
print(deal(4))