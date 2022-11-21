import random

def main():

    
    DIAMOND = chr(9830)
    SPADE = chr(9824)
    CLUB = chr(9827)
    HEART = chr(9829)

    numbr_of_players= int(input('how many players do you want in the game?: '))

    PLAYERS_TURN = 1
    #PLAYERS_NUMBER = [[],[]]
    #PLAYERS_MONEY = {}
    #PLAYERS_BET = [0]
    #PLAYER_OPTIONS = ['(H)it','(S)tand']
    PLAYER_ADDITIONAL_OPTIONS = ['double','split','surrender']
    PLAYERS = {}
    deck = make_deck(DIAMOND,SPADE,CLUB,HEART)

    for i in range(0,numbr_of_players+1):
        PLAYERS[i]= {}
        if i:
            PLAYERS[i]['base_money'] = 1_000
            PLAYERS[i]['options'] = ['hit','stand']

        PLAYERS[i]['hand'] = []
        cards_to_distribute = 2
        while cards_to_distribute:
            PLAYERS[i]['hand'].append(deck.pop())
            cards_to_distribute -=1
    PLAYERS[0]['hidden_card'] = True
        #else:
            #PLAYERS[i]['hand'] = []
            #cards_to_distribute = 2
            #while cards_to_distribute:
                #PLAYERS[i]['hand'].append(deck.pop())
                #cards_to_distribute -=1


    #while len(PLAYER_HAND) < 2 :
    #while len(PLAYERS_NUMBER[-1]) < 2:
        #for player_hand in PLAYERS_NUMBER:
            #player_hand.append(deck.pop(0))
    #for i in range(0,numbr_of_players+1):
        #if i:
            #PLAYERS[i]['hand'] = []
        #cards_to_distribute = 2
        #while cards_to_distribute:
            #PLAYERS[i]['hand'].append(deck.pop())
            #cards_to_distribute -=1

    #print(PLAYERS)

    while PLAYERS_TURN:
        CURRENT_BET =get_bet(PLAYERS_TURN,PLAYERS)
        PLAYERS[PLAYERS_TURN]['bet'] = CURRENT_BET


        check_and_process_move(PLAYERS_TURN,PLAYERS,CURRENT_BET,deck,PLAYER_ADDITIONAL_OPTIONS)
        #print(f"Player\'s hand: {display_cards()}")

        #try to get the key if None is returned then there's no more players so break the loop, use the get method of the dict construct
        if PLAYERS.get(PLAYERS_TURN+1):
            PLAYERS_TURN +=1
        else:
            PLAYERS_TURN=0
            #break

    PLAYERS[PLAYERS_TURN]['hidden_card'] = False
    #now make the dealer draw cards until he's above 17
    while get_cards_value(PLAYERS[PLAYERS_TURN]['hand']) < 17:
        PLAYERS[PLAYERS_TURN]['hand'].append(deck.pop(0))

    #print(f"Dealer\'s hand: {display_cards()}")

    if get_cards_value(PLAYERS[PLAYERS_TURN]['hand']) > 21:
        #display dealer's cards
        #print(f'dealer busted!')
        for player in range(1,numbr_of_players+1):
            if get_cards_value(PLAYERS[player]['hand']) <=21:
                #display player hand and tell how much he earned
                PLAYERS[player]['base_money'] += PLAYERS[player]['bet']
                PLAYERS[player]['outcome'] = 'won'
    else:
        for player in range(1,numbr_of_players+1):
            if get_cards_value(PLAYERS[player]['hand']) <= 21 :
                if get_cards_value(PLAYERS[player]['hand']) > get_cards_value(PLAYERS[PLAYERS_TURN]['hand']):
                    # pay the player bet 
                    PLAYERS[player]['base_money'] += PLAYERS[player]['bet']
                    PLAYERS[player]['outcome'] = 'won'
                    #...
                elif get_cards_value(PLAYERS[player]['hand']) < get_cards_value(PLAYERS[PLAYERS_TURN]['hand']):
                    #get player money
                    PLAYERS[player]['base_money'] -= PLAYERS[player]['bet']
                    PLAYERS[player]['outcome'] = 'lost'
                    #...

def make_deck(*forms):

    deck= []
    #print(deck)

    for symbol in forms:
        for value in range(2,11):
            deck.append((value,symbol))
        for prestige in ('J','Q','K','A'):
            deck.append((prestige, symbol))
    random.shuffle(deck)

    return deck
    #print(deck)

def get_bet(player_turn, players):
    while True:
        CURRENT_BET =input(f"Player {player_turn},Amount you're betting: ")
        if CURRENT_BET.isnumeric() and int(CURRENT_BET) <= players[player_turn]['base_money']:
            return int(CURRENT_BET)
        elif CURRENT_BET.isnumeric() and int(CURRENT_BET) > players[player_turn]:
            print("You\'re betting money you don't have in your treasury")
        else:
            print("Please insert a valid amount")

def get_cards_value(hand):
    total=0
    for card in hand:
        value = card[0]
        if value in ('J','Q','K'):
            total+=10
        elif value == 'A':
            if total + 11 > 21:
                total +=1
            else:
                total+=11
        else:
            total +=value

    return total


def check_and_process_move(players_turn,players,current_bet,deck,player_additional_options):

    while True:

        if get_cards_value(players[players_turn]['hand'])>21:
            print("Bust! You lost your bet,try another time")
            players[players_turn]['base_money'] -=  current_bet
            break
        
        # add player options and change accordingly
        #check player cards for double, split and surrender option
        if len(players[players_turn]['hand']) == 2:
            for option in player_additional_options:
                if option == 'split' and len(set(list(zip(*players[players_turn]['hand']))[0])) !=1:
                    continue
                players[players_turn]['options'].append(option)
        else:
            players[players_turn]['options'] = [x for x in players[players_turn]['options'] if x not in player_additional_options]

        print(f"Player {players_turn} turn. {', '.join([f'({x[0].upper()}){x[1:]}' for x in players[players_turn]['options']])}")
        #{(x[0] for x in players[players_turn]['options'])}
        player_move= input("> ")

        if player_move.lower() in ('h','hit') and 'hit' in players[players_turn]['options']:
            players[players_turn]['hand'].append(deck.pop(0))
            #print(f"Player\'s hand: {display_cards()}")
        elif player_move.lower() in ('st','stand','s') and 'stand' in players[players_turn]['options']:
            break
        elif player_move.lower() in ('do','double','d') and 'double' in players[players_turn]['options']:
            #print(f"Player\'s hand: {display_cards()}")
            if players[players_turn]['base_money'] >= current_bet * 2:
                current_bet *=2
                players[players_turn]['bet']= current_bet
                players[players_turn]['hand'].append(deck.pop(0))
            break
        elif player_move.lower() in ('sur','surrender') and 'surrender' in players[players_turn]['options']:
            players[players_turn]['base_money'] -= current_bet / 2
            players[players_turn]['bet']= current_bet/2 #keep track of the bet to display how much he lost at the end
            players[players_turn]['outcome']= 'lost'
            print(f"Player {players_turn}, you lost half of your bet by surrendering.")
            break
        elif player_move.lower() in ('sp','split') and 'split' in players[players_turn]['options']:
            # add another hand to the player, either separately or in the  same hand
            #draw cards until len() ==2 for both hands
            # display hands with print(f"Player\'s hand: {display_cards()}")
            if players[players_turn]['base_money'] >= current_bet * 2:
                current_bet *=2
                players[players_turn]['bet']= current_bet
                players[players_turn]['split']= []
                players[players_turn]['split'].append(players[players_turn]['hand'].pop())
                players[players_turn]['hand'].append(deck.pop())
                players[players_turn]['split'].append(deck.pop())
            else:
                players[players_turn]['options'].remove('split')
                print('Unfortunate! You could have split your hand if you had enough money to double your bet.')
                print('Choose other option(s).')
                #...
                
        else:
            print('Please insert a valid option.')

def display_hands(players,players_turn=False,display_all=False):
    #draw the cards with horizontal and vertical lines and add the motif and value of each card of the player's hand and split eventually
    top_side_card=True
    middle_side_card=False
    bottom_side_card=False
    if display_all:
        for i in range(0,len(players)+1):
            current_hand= players[i]['hand']
            current_split= players[i].get('split')

            #no card drawing for split since there's none
            #if not current_split:
                #current_split =0

            total_cards= len(current_hand) + (0 if not current_split else len(current_split))

            #loop through each value and symbol (a card) and use these value for printing the card
            #for value,symbol in current_hand:
            #...
            #if i ==0 and len(current_hand == 2):
            print(" ___ " + "  ___"*total_cards )

            while top_side_card or middle_side_card or bottom_side_card:
                #print("|"+ f"{current_hand[drawing_component][0]  }")
                if top_side_card:
                    #print("|".rjust(7) + "{current_hand[drawing_component][0]}")
                    #print("|".rjust(7) , ["{current_hand[z][0]}" for z in range(0,total_cards)])
                    #print("".rjust(7) , "  ".join(["{current_hand[z][0]}  |" for z in range(0,total_cards)]))
                    print("".rjust(15) , "  ".join([f"|{current_hand[z][0]}  |"
                          if not players.get('hidden_card') else '|#  |' for z in range(0,len(current_hand))]),
                          "".rjust(15) , "  ".join([f"|{current_split[z][0]} |" for z in range(0,len(current_split)) if current_split]))
                    #if current_split:
                        #print("".rjust(6) , "  ".join([f"|{current_split[z][0]} |" for z in range(0,len(current_split))]))
                    top_side_card = False
                    middle_side_card=True
                elif middle_side_card:
                    print("".rjust(15) , "  ".join([f"| {current_hand[z][1]} |"
                          if not players.get('hidden_card') else '| # |'for z in range(0,len(current_hand))]),
                          "".rjust(15) , "  ".join([f"| {current_split[z][1]} |" for z in range(0,len(current_split)) if current_split]))
                    #if current_split:
                        #print("".rjust(6) , "  ".join([f"| {current_split[z][1]} |" for z in range(0,len(current_split))]))
                    middle_side_card=False
                    bottom_side_card=True
                else:
                    print(f"PLAYER {i} HAND: " , " ".join([f"|__{current_hand[z][0]}|" 
                          if not players.get('hidden_card') else '| # |' for z in range(0,len(current_hand))]),
                          f"PLAYER {i} SPLIT: " , " ".join([f"|__{current_split[z][0]}|" if current_split else "x" for z in range(0,len(current_split)) ]))
                    #if current_split:
                        #print("SPLIT: " , " ".join([f"|__{current_split[z][0]}|" for z in range(0,len(current_split))]))
                    bottom_side_card=False
                    top_side_card = True
                    break

    else:
            current_hand= players[players_turn]['hand']
            current_split= players[players_turn].get('split')
            total_cards= len(current_hand) + (0 if not current_split else len(current_split))

            print(" ___ " + "  ___"*total_cards )

            while top_side_card or middle_side_card or bottom_side_card:
                if top_side_card:
                    print("".rjust(15) , "  ".join([f"|{current_hand[z][0]}  |" 
                          if not players.get('hidden_card') else '|#  |' for z in range(0,len(current_hand))]),
                          "".rjust(15) , "  ".join([f"|{current_split[z][0]} |" for z in range(0,len(current_split)) if current_split]))
                    top_side_card = False
                    middle_side_card=True
                elif middle_side_card:
                    print("".rjust(15) , "  ".join([f"| {current_hand[z][1]} |"
                          if not players.get('hidden_card') else '| # |'for z in range(0,len(current_hand))]),
                          "".rjust(15) , "  ".join([f"| {current_split[z][1]} |" for z in range(0,len(current_split)) if current_split]))
                    middle_side_card=False
                    bottom_side_card=True
                else:
                    print(f"PLAYER {players_turn} HAND: " , "  ".join([f"|__{current_hand[z][0]}|" 
                          if not players.get('hidden_card') else '| # |' for z in range(0,len(current_hand))]),
                          f"PLAYER {players_turn} SPLIT: " , " ".join([f"|__{current_split[z][0]}|" if current_split else "x" for z in range(0,len(current_split)) ]))
                    bottom_side_card=False



main()
