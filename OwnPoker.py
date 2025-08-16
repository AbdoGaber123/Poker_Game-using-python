"""
===================================================
  📄 Poker Game System
===================================================

@description : Poker Game System using Python
@created     : 2025-08-01 03:30:00
@updated     : 2025-08-11 13:00:00
@author      : Abdallah Gaber
@version     : 1.0.0
@python      : 3.11+
===================================================
"""
import random

def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return allmax(hands , key= hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval  #if there is a new high power create a new result for it and remove the old
        elif xval == maxval:
            result.append(x)
    return result

# Build a standard deck of 52 cards
mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
def deal(numhands, n=5, deck=mydeck):
    deck = deck[:]            #  Make a copy of the deck to avoid modifying the original
    random.shuffle(deck)      #  Shuffle the deck randomly
    return [deck[i*n: (i+1)*n] for i in range(numhands) ]

    #hands = []                #  List to store all the hands
   # for i in range(numhands): #  Loop through the number of hands (players)
    #    hand = deck[i*n : (i+1)*n]  #  Slice the deck to get n cards for each hand
    #    hands.append(hand)          #  Add the hand to the hands list
    #return hands              #  Return all hands
    
def card_ranks(hand):
    "return a list of ranks of the hand"         #card = rank + suit
    ranks = [ '--23456789TJQKA'.index(rank) for rank,suit in hand]  
    #get each rank(first item in each card) and map it with its index in this string
    ranks.sort(reverse = True) #sort the ranks form high to low
    return [5,4,3,2,1] if ranks == [14,5,4,3,2] else  ranks
    #print card_ranks(['AC', '3D', '4S', 'KH']) #should output [14, 3, 4, 13]

def Straight(ranks):
    #if ranks == [5,4,3,2,1]:return False   # Ace stright hand in not actual hand
    #rank_sorted = sorted(ranks)
    #return rank_sorted == list(range(rank_sorted[0], rank_sorted[0] + 5))
    return (max(ranks) - min(ranks) == 4) and (len(set(ranks)) ==5)

def Flush(hand):
    #suits = {card[-1] for card in hand} #set comprehsension
    #return len(suits) == 1 
    return all(card[-1] == hand[0][-1] for card in hand) # Is each card type = the type of first card in hand?

def Kind(n,ranks): 
    for rank in ranks:
        if ranks.count(rank) == n:
            return rank   # return the rank that exist n of times in the ranks list
    return None

def two_pair(ranks):
    pairs = []
    for r in set(ranks):
        if ranks.count(r) == 2:
            pairs.append(r)
    if len(pairs) == 2:
        pairs.sort(reverse=True)
        return (pairs[0], pairs[1])
    return None

def hand_rank(hand):
    "the core function of all program"
    ranks = card_ranks(hand)
  
    if Straight(ranks) and Flush(hand):
        return (8,max(ranks)) # 6D 7D 8D 9D 10D => (8,10) 
        #max(ranks) breaks the tie(بتكسر حالة التعادل لو حصلت)
    
    elif Kind(4,ranks):
        return (7, Kind(4,ranks),Kind(1,ranks)) #get the rank that exist 4 times & 1 times.
        #ex: [6,6,6,6,4] => (7,6,4)
    
    elif Kind(3,ranks) and Kind(2,ranks):    
        return(6,Kind(3,ranks),Kind(2,ranks))   # full house power -> three of a type + one pair

    elif Flush(hand):
        return (5, ranks) #return the ranks sorted for the tiebreaker

    elif Straight(ranks):
        return(4,max(ranks))
    
    elif Kind(3,ranks):
        three =  Kind(3, ranks)
        return (3, three, [r for r in ranks if r != three])

    elif two_pair(ranks):
        tp = two_pair(ranks)
        if tp:
            return (2, tp,[r for r in ranks if r not in tp])
    
    elif Kind(2,ranks):
        two =  Kind(2, ranks)
        return (1, two,[r for r in ranks if r != two])
    
    else:
        return (0,ranks)




                #sf                               #4kind                       #fk                              

hands=[['8C', '8C', '8C', 'TC', 'TC'],['6C', '6C', '6C', '6C', 'TC'],['6C', '6C', '6C', '6C', 'TC'],['6C', '7C', '8C', '9C', 'TC'], ]     
hands2=deal(4)
#print(hands2)
#print(hand_rank(hands[2]))

import time 

start = time.time()
print(poker(hands2))
end = time.time()
print("Execution time:", end - start)

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # => ['6C', '7C', '8C', '9C', 'TC']
    fk = "9D 9H 9S 9C 7D".split() 
    fh = "TD TC TH 7C 7D".split()
    
    assert poker([sf, fk, fh]) == sf
    assert poker([fk,fh]) == fk
    assert poker([fh,fh]) == fh
    
    assert poker([sf]) == sf   #  A single hand.
    hands = [fh] * 99 + [sf]   #  99 full houses + 1 straight flush
    assert poker(hands) == sf  #  100 hands
    assert Straight([9, 8, 7, 6, 5]) == True
    assert Straight([9, 8, 8, 6, 5]) == False
    assert Flush(sf) == True
    assert Flush(fk) == False
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return "Test Passes"    
#print(test())