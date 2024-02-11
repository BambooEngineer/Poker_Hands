poker_card_file = open('MyPoker.txt')   
poker_cards = poker_card_file.readline()


hearts = {'2H' : 2, '3H' : 3, '4H' : 4, '5H' : 5, '6H' : 6, '7H' : 7, '8H' : 8, '9H' : 9,
          'TH' : 10, 'JH' : 11, 'QH' : 12, 'KH' : 13, 'AH' : 14}

diamonds = {'2D' : 2, '3D' : 3, '4D' : 4, '5D' : 5, '6D' : 6, '7D' : 7, '8D' : 8, '9D' : 9,
          'TD' : 10, 'JD' : 11, 'QD' : 12, 'KD' : 13, 'AD' : 14}

spades = {'2S' : 2, '3S' : 3, '4S' : 4, '5S' : 5, '6S' : 6, '7S' : 7, '8S' : 8, '9S' : 9,
          'TS' : 10, 'JS' : 11, 'QS' : 12, 'KS' : 13, 'AS' : 14}

clubs = {'2C' : 2, '3C' : 3, '4C' : 4, '5C' : 5, '6C' : 6, '7C' : 7, '8C' : 8, '9C' : 9,
          'TC' : 10, 'JC' : 11, 'QC' : 12, 'KC' : 13, 'AC' : 14}

hand_type = {2 : 'One_pair', 3: 'Two_pairs', 4:'three_of_a_kind', 5:'Straight',6: 'flush',
             7:'full_house', 8:'four_of_a_kind', 9:'straight_flush',
             10:'royal_flush'}

player_1_wins = 0
player_2_wins = 0

p1_ranks = []   # player_1 ranks
p1_distinct_ranks = [] # For detecting highest, 1 pair, 2 pair, three kind, four kind, full house
p1_number_on_hand = {}

p1_Player_Hand = 1
three_of_a_kind = False 
A_Pair = False
royal  = False
p1_pair_rnk = 0    # comparison variables
p1_pair_rnk_2 = 0
p1_three_kind_rnk = 0
p1_four_kind_rnk = 0


p2_ranks = []   # player_2 ranks
p2_distinct_ranks = []
p2_number_on_hand = {}

p2_Player_Hand = 1
three_of_a_kind = False 
A_Pair = False
royal  = False
p2_pair_rnk = 0       
p2_pair_rnk_2 = 0
p2_three_kind_rnk = 0
p2_four_kind_rnk = 0

def player_1_Hand():

    global p1_Player_Hand
    global three_of_a_kind 
    global A_Pair
    global royal
    global p1_pair_rnk
    global p1_pair_rnk_2
    global p1_three_kind_rnk
    global p1_four_kind_rnk

    p1_ranks.clear()                                # player_1 ranks

    h, d, s, c = 0,0,0,0            # hearts, diamonds, spades, clubs
        
    for i in range(0, 5):           # Count each suit for detecting flushes later      
        if(hands[i][1] == 'H'): 
            h = h + 1
            p1_ranks.append(hearts[hands[i]]) 
        if(hands[i][1] == 'D'):
            d = d + 1
            p1_ranks.append(diamonds[hands[i]]) 
        if(hands[i][1] == 'S'):
            s = s + 1
            p1_ranks.append(spades[hands[i]])
        if(hands[i][1] == 'C'):
            c = c + 1
            p1_ranks.append(clubs[hands[i]])

                            
    p1_distinct_ranks.clear() # For detecting highest card, 1 pair, 2 pair, three kind, four kind, full house
    p1_number_on_hand.clear()
    
    for x in p1_ranks:   # only use distinct values to scan hand for pairs/3_kind/4_kind/full house              
        if x not in p1_distinct_ranks:
            p1_distinct_ranks.append(x)
            
    p1_ranks.sort(reverse=True) # Sort hand in decreasing order to easily compare highest cards

    p1_Player_Hand = 1
    three_of_a_kind = False 
    A_Pair = False
    royal  = False
    p1_pair_rnk = 0    # comparison variables
    p1_pair_rnk_2 = 0
    p1_three_kind_rnk = 0
    p1_four_kind_rnk = 0
    
    for x in range(len(p1_distinct_ranks)):   # distinct values are to avoid double counting cards
        
        if(p1_ranks.count(p1_distinct_ranks[x]) == 2):  # pair
            p1_Player_Hand = p1_Player_Hand + 1
            p1_number_on_hand[p1_distinct_ranks[x]] = 2
            if(p1_pair_rnk == 0): p1_pair_rnk = p1_distinct_ranks[x] # save the ranking 
            if(p1_pair_rnk > 0): p1_pair_rnk_2 = p1_distinct_ranks[x]
            A_Pair = True
            
        if(p1_ranks.count(p1_distinct_ranks[x]) == 3):  # three of a kind
            p1_Player_Hand = 4
            p1_number_on_hand[p1_distinct_ranks[x]] = 3
            p1_three_kind_rnk = p1_distinct_ranks[x]
            three_of_a_kind = True
            
        if(p1_ranks.count(p1_distinct_ranks[x]) == 4):  # four of a kind
            p1_Player_Hand = 8
            p1_number_on_hand[p1_distinct_ranks[x]] = 4
            p1_four_kind_rnk = p1_distinct_ranks[x]
            
    if(three_of_a_kind and A_Pair): # full_house boolean triggers
        p1_Player_Hand = 7

   
    max_c = max(p1_ranks)                                        # For detecting straights
    lowest_c = max_c - 4
    for i in range(1,5):
        if(p1_ranks[i] == (max_c - 1)):
            max_c = p1_ranks[i]
    if((max_c == lowest_c and not(max_c == 10)) and (p1_Player_Hand<7)): # if not a royal
        p1_Player_Hand = 5
    if((max_c == lowest_c and max_c == 10) and (p1_Player_Hand<7)): # if all royal ranks
        royal = True
        p1_Player_Hand = 5
            
    if((h == 5 or d == 5 or s == 5 or c == 5) and (p1_Player_Hand<7)): # For detecting flushes
        if(not(p1_Player_Hand == 5)):           # flush
           p1_Player_Hand = 6
        if(p1_Player_Hand == 5 and not(royal)): # straight flush 
            p1_Player_Hand = 9                         
        if(p1_Player_Hand == 5 and royal):      # royal flush
            p1_Player_Hand = 10


def player_2_Hand():

    global p2_Player_Hand
    global three_of_a_kind
    global A_Pair
    global royal
    global p2_pair_rnk      
    global p2_pair_rnk_2
    global p2_three_kind_rnk
    global p2_four_kind_rnk
    
    h, d, s, c = 0,0,0,0

    p2_ranks.clear() # player_2 ranks                    
        
    for i in range(5, 10):           # Count each suit for detecting flushes later      
        if(hands[i][1] == 'H'): 
            h = h + 1
            p2_ranks.append(hearts[hands[i]]) 
        if(hands[i][1] == 'D'):
            d = d + 1
            p2_ranks.append(diamonds[hands[i]]) 
        if(hands[i][1] == 'S'):
            s = s + 1
            p2_ranks.append(spades[hands[i]])
        if(hands[i][1] == 'C'):
            c = c + 1
            p2_ranks.append(clubs[hands[i]])

                        
    p2_distinct_ranks.clear()
    p2_number_on_hand.clear()
    
    for x in p2_ranks:               
        if x not in p2_distinct_ranks:
            p2_distinct_ranks.append(x)
            
    p2_ranks.sort(reverse=True) 

    p2_Player_Hand = 1
    three_of_a_kind = False 
    A_Pair = False
    royal  = False
    p2_pair_rnk = 0       
    p2_pair_rnk_2 = 0
    p2_three_kind_rnk = 0
    p2_four_kind_rnk = 0
    
    for x in range(len(p2_distinct_ranks)):   
        
        if(p2_ranks.count(p2_distinct_ranks[x]) == 2):  # pairs
            p2_Player_Hand = p2_Player_Hand + 1
            p2_number_on_hand[p2_distinct_ranks[x]] = 2
            if(p2_pair_rnk == 0): p2_pair_rnk = p2_distinct_ranks[x] 
            if(p2_pair_rnk > 0): p2_pair_rnk_2 = p2_distinct_ranks[x]
            A_Pair = True
            
        if(p2_ranks.count(p2_distinct_ranks[x]) == 3):   # 3 of a kind
            p2_Player_Hand = 4
            p2_number_on_hand[p2_distinct_ranks[x]] = 3
            p2_three_kind_rnk = p2_distinct_ranks[x]
            three_of_a_kind = True
            
        if(p2_ranks.count(p2_distinct_ranks[x]) == 4):  # four of a kind
            p2_Player_Hand = 8
            p2_number_on_hand[p2_distinct_ranks[x]] = 4
            p2_four_kind_rnk = p2_distinct_ranks[x]
            
    if(three_of_a_kind and A_Pair):  # full house
        p2_Player_Hand = 7

   
    max_c = max(p2_ranks)            # straight                             
    lowest_c = max_c - 4
    for i in range(1,5):
        if(p2_ranks[i] == (max_c - 1)):
            max_c = p2_ranks[i]
    if((max_c == lowest_c and not(max_c == 10)) and (p2_Player_Hand<7)): 
        p2_Player_Hand = 5
    if((max_c == lowest_c and max_c == 10) and (p2_Player_Hand<7)): 
        royal = True
        p2_Player_Hand = 5 
            
    if((h == 5 or d == 5 or s == 5 or c == 5) and (p2_Player_Hand<7)): 
        if(not(p2_Player_Hand == 5)):           # flush
           p2_Player_Hand = 6
        if(p2_Player_Hand == 5 and not(royal)): # straight flush 
            p2_Player_Hand = 9                         
        if(p2_Player_Hand == 5 and royal):      # royal flush
            p2_Player_Hand = 10


def compare_cards():

    global p1_Player_Hand
    global p2_Player_Hand
    global player_1_wins
    global player_2_wins
    global p1_pair_rnk
    global p1_pair_rnk_2
    global p2_pair_rnk
    global p2_pair_rnk_2
    global p2_ranks
    global p1_ranks

    global p1_three_kind_rnk
    global p2_three_kind_rnk
    
    if(p1_Player_Hand > p2_Player_Hand): player_1_wins = player_1_wins + 1        # compare hand types
    if(p1_Player_Hand < p2_Player_Hand): player_2_wins = player_2_wins + 1         # if same then compare ranks of hands
                                                                        # if same then compare rest of card ranks
                                                                        
    if(p1_Player_Hand == p2_Player_Hand and (p1_Player_Hand == 2)): #   1 pair compare
        if(p1_pair_rnk > p2_pair_rnk): player_1_wins = player_1_wins + 1           # compare ranks in pairs
        if(p1_pair_rnk < p2_pair_rnk): player_2_wins = player_2_wins + 1
        if(p1_pair_rnk == p2_pair_rnk):
           for i in range(0, 5):                    # compare highest cards
               if(p2_ranks[i] > p1_ranks[i]):     # value lists are already sorted greatest to least
                   player_2_wins = player_2_wins + 1
                   break
               if(p2_ranks[i] < p1_ranks[i]):
                   player_1_wins = player_1_wins + 1
                   break

    if(p1_Player_Hand == p2_Player_Hand and (p1_Player_Hand == 3)): #   2 pair compare - (person with larger top pair wins)
        if(p1_pair_rnk > p1_pair_rnk_2 and p1_pair_rnk > p2_pair_rnk and p1_pair_rnk > p2_pair_rnk_2):
            player_1_wins = player_1_wins + 1           
        if(p1_pair_rnk < p1_pair_rnk_2 and p1_pair_rnk_2 > p2_pair_rnk and p1_pair_rnk_2 > p2_pair_rnk_2):
            player_1_wins = player_1_wins + 1
        if(p2_pair_rnk > p2_pair_rnk_2 and p2_pair_rnk > p1_pair_rnk and p2_pair_rnk > p1_pair_rnk_2):
            player_2_wins = player_2_wins + 1           
        if(p2_pair_rnk < p2_pair_rnk_2 and p2_pair_rnk_2 > p1_pair_rnk and p2_pair_rnk_2 > p1_pair_rnk_2):
            player_2_wins = player_2_wins + 1
        if(p1_pair_rnk == p2_pair_rnk and p1_pair_rnk_2 == p2_pair_rnk_2):
           for i in range(0, 5):                   
               if(p2_ranks[i] > p1_ranks[i]):   
                   player_2_wins = player_2_wins + 1
                   break
               if(p2_ranks[i] < p1_ranks[i]):
                   player_1_wins = player_1_wins + 1
                   break

    if(p1_Player_Hand == p2_Player_Hand and (p1_Player_Hand == 4)): # 3 of a kind compare
        if(p1_three_kind_rnk > p2_three_kind_rnk):
            player_1_wins = player_1_wins + 1
        if(p1_three_kind_rnk < p2_three_kind_rnk):
            player_2_wins = player_2_wins + 1 
        if(p1_three_kind_rnk == p2_three_kind_rnk):
           for i in range(0, 5):                   
               if(p2_ranks[i] > p1_ranks[i]):   
                   player_2_wins = player_2_wins + 1
                   break
               if(p2_ranks[i] < p1_ranks[i]):
                   player_1_wins = player_1_wins + 1
                   break

    if(p1_Player_Hand == p2_Player_Hand and (p1_Player_Hand == 8)): # 4 of a kind compare
        if(p1_four_kind_rnk > p2_four_kind_rnk):
            player_1_wins = player_1_wins + 1
        if(p1_four_kind_rnk < p2_four_kind_rnk):
            player_2_wins = player_2_wins + 1  
        if(p1_four_kind_rnk == p2_four_kind_rnk):
           for i in range(0, 5):                   
               if(p2_ranks[i] > p1_ranks[i]):   
                   player_2_wins = player_2_wins + 1
                   break
               if(p2_ranks[i] < p1_ranks[i]):
                   player_1_wins = player_1_wins + 1
                   break

    if(p1_Player_Hand == p2_Player_Hand and (p1_Player_Hand == 7)): # full house - compare looks at highest 3 of a kind
        if(p1_three_kind_rnk > p2_three_kind_rnk):                  # then the pair if they have same 3 of a kind
            player_1_wins = player_1_wins + 1
        if(p1_three_kind_rnk < p2_three_kind_rnk):
            player_2_wins = player_2_wins + 1  
        if(p1_three_kind_rnk == p2_three_kind_rnk):     # look at the pairs if they have the same three of a kinds rnks
           if(p1_pair_rnk > p2_pair_rnk): player_1_wins = player_1_wins + 1           
           if(p1_pair_rnk < p2_pair_rnk): player_2_wins = player_2_wins + 1

    if(p1_Player_Hand == p2_Player_Hand and (p1_Player_Hand == 5)): # straight 
        for i in range(0, 5):                   
           if(p2_ranks[i] > p1_ranks[i]):   
               player_2_wins = player_2_wins + 1
               break
           if(p2_ranks[i] < p1_ranks[i]):
               player_1_wins = player_1_wins + 1
               break

    if(p1_Player_Hand == p2_Player_Hand and (p1_Player_Hand == 6)): # flush 
        for i in range(0, 5):                   
           if(p2_ranks[i] > p1_ranks[i]):   
               player_2_wins = player_2_wins + 1
               break
           if(p2_ranks[i] < p1_ranks[i]):
               player_1_wins = player_1_wins + 1
               break

    if(p1_Player_Hand == p2_Player_Hand and (p1_Player_Hand == 9)): # straight flush 
        for i in range(0, 5):                   
           if(p2_ranks[i] > p1_ranks[i]):   
               player_2_wins = player_2_wins + 1
               break
           if(p2_ranks[i] < p1_ranks[i]):
               player_1_wins = player_1_wins + 1               
               break
            
    if(p1_Player_Hand == p2_Player_Hand and (p1_Player_Hand == 1)): # High Card Compare
        for i in range(0, 5):                   
           if(p2_ranks[i] > p1_ranks[i]):   
               player_2_wins = player_2_wins + 1
               break
           if(p2_ranks[i] < p1_ranks[i]):
               player_1_wins = player_1_wins + 1               
               break
    
    

while(poker_cards):                                                 # MAIN LOOP

    poker_cards = poker_cards.rstrip()
    hands = poker_cards.split()                 # this being defined after function definitions seems to not affect anything

    player_1_Hand()     # read player hands                             
    player_2_Hand() 
                             
    compare_cards()     # Decides which has the better hand

    poker_cards = poker_card_file.readline()


print("player 1 wins : "+ str(player_1_wins))   

