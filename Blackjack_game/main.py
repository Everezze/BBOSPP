import random

def main():

    DIAMOND = chr(9830)
    SPADE = chr(9824)
    CLUB = chr(9827)
    HEART = chr(9829)

    numbr_of_players= False
    while not numbr_of_players:
        z= input('how many players do you want in the game?(1-7): ')
        if z.isnumeric and int(z) > 0 and int(z) < 8:
            numbr_of_players = int(z)

    PLAYERS_TURN = 1
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

    #print(PLAYERS)
    display_hands(PLAYERS,display_all=True)

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
    for symbol in forms:
        for value in range(2,11):
            deck.append((value,symbol))
        for prestige in ('J','Q','K','A'):
            deck.append((prestige, symbol))
    random.shuffle(deck)
    return deck

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
    #can go bust when not if cards not re-arranged, add all cards but ace and add ace at the end with either 1 or 11 as a value
    regular_cards=[]
    ace_cards=[]
    for x in hand:
        if x[0] not in ('J','Q','K','A'):
            regular_cards.append(x[0])
        elif x[0] in ('J','Q','K'):
            regular_cards.append(10)
        else:
            ace_cards.append(x[0])

    total = sum(regular_cards)
    for ace in ace_cards:
        if total + 11 <= 21:
            total += 11
        else:
            total += 1
    return total

def check_and_process_move(players_turn,players,current_bet,deck,player_additional_options):
    hand_still_inplay= True
    split_still_inplay= True if players[players_turn].get('split') else False

    while True:
        if get_cards_value(players[players_turn]['hand'])>21 :
            if hand_still_inplay and not players[players_turn].get('split'):
                players[players_turn]['base_money'] -= current_bet
                display_hands(players, players_turn)
                print("Bust! You lost your bet,try another time")
                break
            elif hand_still_inplay and split_still_inplay:
                players[players_turn]['base_money'] -= current_bet/2
                hand_still_inplay= False
            elif hand_still_inplay and not split_still_inplay:
                players[players_turn]['base_money'] -= current_bet/2
                break
        if players[players_turn].get('split'):
            if get_cards_value(players[players_turn]['split'])>21 :
                if split_still_inplay and not hand_still_inplay:
                    players[players_turn]['base_money'] -= current_bet/2
                    break
                elif split_still_inplay and hand_still_inplay:
                    players[players_turn]['base_money'] -= current_bet/2
                    split_still_inplay=False

        # add player options and change accordingly
        #check player cards for double, split and surrender option
        if len(players[players_turn]['hand']) == 2:
            for option in player_additional_options:
                if option == 'split' and len(set(list(zip(*players[players_turn]['hand']))[0])) !=1 and current_bet*2 > players[players_turn]['base_money']:
                    continue
                if option== 'double' and current_bet*2 > players[players_turn]['base_money']:
                    continue
                players[players_turn]['options'].append(option)
        else:
            players[players_turn]['options'] = [x for x in players[players_turn]['options'] if x not in player_additional_options]

        print(f"Player {players_turn} turn. {', '.join([f'{x[0].upper()}{x[1:]}' for x in players[players_turn]['options']])}:")
        #{(x[0] for x in players[players_turn]['options'])}
        player_move= input("> ")

        if player_move.lower() in ('h','hit') and 'hit' in players[players_turn]['options']:
            if hand_still_inplay:
                players[players_turn]['hand'].append(deck.pop(0))
            if split_still_inplay:
                players[players_turn]['split'].append(deck.pop(0))
            display_hands(players, players_turn)

            #print(f"Player\'s hand: {display_cards()}")
        elif player_move.lower() in ('st','stand','s') and 'stand' in players[players_turn]['options']:
            break
        elif player_move.lower() in ('do','double','d') and 'double' in players[players_turn]['options']:
            #print(f"Player\'s hand: {display_cards()}")
            current_bet *=2
            players[players_turn]['bet']= current_bet
            players[players_turn]['hand'].append(deck.pop(0))
            display_hands(players, players_turn)
            break
        elif player_move.lower() in ('sur','surrender') and 'surrender' in players[players_turn]['options']:
            players[players_turn]['base_money'] -= current_bet / 2
            players[players_turn]['bet']= current_bet #keep track of the bet to display how much he lost at the end
            players[players_turn]['outcome']= 'lost'
            print(f"Player {players_turn}, you lost half of your bet by surrendering.")
            break
        elif player_move.lower() in ('sp','split') and 'split' in players[players_turn]['options']:
            # add another hand to the player, either separately or in the  same hand
            #draw cards until len() ==2 for both hands
            # display hands with print(f"Player\'s hand: {display_cards()}")
            current_bet *=2
            players[players_turn]['bet']= current_bet
            players[players_turn]['split']= []
            players[players_turn]['split'].append(players[players_turn]['hand'].pop())
            players[players_turn]['hand'].append(deck.pop())
            players[players_turn]['split'].append(deck.pop())
            display_hands(players, players_turn)
                #...
        else:
            print('Please insert a valid option.')

def display_hands(players,players_turn=False,display_all=False):
    #draw the cards with horizontal and vertical lines and add the motif and value of each card of the player's hand and split eventually
    top_line= []
    top_side_card= [[],[]]
    middle_side_card= [[],[]]
    bottom_side_card= [[],[]]

    if display_all:
        for i in range(0,len(players)):
            top_line =[]
            top_side_card= [[],[]]
            middle_side_card= [[],[]]
            bottom_side_card= [[],[]]
            current_hand= players[i]['hand']
            current_split= players[i].get('split')

#a,b,c,d corresponds to the different level of cards : respectively top line of card, top side, middle side, bottom side of a card
#having this condition will allow to correctly display cards with 10 as a value
            for z in range(0,len(current_hand)):
                if len(str(current_hand[z][0])) > 1 and i!= 0 and z!=0:
                    a= " ____ "
                    c=f"| {current_hand[z][1]}  |"
                else:
                    a= " ___ "
                    c=f"| {current_hand[z][1]} |"

                if not players[i].get('hidden_card') or players[i].get('hidden_card') and z!=0:
                    top_line.append(a)
                    top_side_card[0].append(f"|{current_hand[z][0]}  |")
                    middle_side_card[0].append(c)
                    bottom_side_card[0].append(f"|__{current_hand[z][0]}|")
                else:
                    top_line.append(a)
                    top_side_card[0].append(f"|#  |")
                    middle_side_card[0].append(f"| # |")
                    bottom_side_card[0].append(f"|__#|")

            for z in range(0,len(current_split) if current_split else 0):
                if len(str(current_split[z][0])) > 1:
                    a= " ____ "
                    c=f"| {current_split[z][1]}  |"
                else:
                    a= " ___ "
                    c=f"| {current_split[z][1]} |"

                top_line.append(a)
                top_side_card[1].append(f"|{current_split[z][0]}  |")
                middle_side_card[1].append(c)
                bottom_side_card[1].append(f"|__{current_split[z][0]}|")

#print topside cards and their split if any, and do with middle and bottom also
            print("".rjust(15), ' '.join(top_line))
            print("".rjust(15) , ' '.join(top_side_card[0]),
                  "".rjust(15) , ' '.join(top_side_card[1]) )

            print("".rjust(15) , ' '.join(middle_side_card[0]),
                  "".rjust(15) , ' '.join(middle_side_card[1]) )

            print(f"Player {i} hand: " if i else "Dealer's hand: ", ' '.join(bottom_side_card[0]),
                  f"Player {i} split: " if players[i].get('split') else '' , ' '.join(bottom_side_card[1]) )
    else:
            current_hand= players[players_turn]['hand']
            current_split= players[players_turn].get('split')

            for z in range(0,len(current_hand)):
                if len(str(current_hand[z][0])) > 1 and players_turn!=0 and z!=0:
                    a= " ____ "
                    c=f"| {current_hand[z][1]}  |"
                else:
                    a= " ___ "
                    c=f"| {current_hand[z][1]} |"

                if not players[players_turn].get('hidden_card') or players[players_turn].get('hidden_card') and z!=0:
                    top_line.append(a)
                    top_side_card[0].append(f"|{current_hand[z][0]}  |")
                    middle_side_card[0].append(c)
                    bottom_side_card[0].append(f"|__{current_hand[z][0]}|")
                else:
                    top_line.append(a)
                    top_side_card[0].append(f"|#  |")
                    middle_side_card[0].append(f"| # |")
                    bottom_side_card[0].append(f"|__#|")

            for z in range(0,len(current_split) if current_split else 0):
                if len(str(current_split[z][0])) > 1:
                    a= " ____ "
                    c=f"| {current_split[z][1]}  |"
                else:
                    a= " ___ "
                    c=f"| {current_split[z][1]} |"
                top_line.append(a)
                top_side_card[1].append(f"|{current_split[z][0]}  |")
                middle_side_card[1].append(c)
                bottom_side_card[1].append(f"|__{current_split[z][0]}|")

            print("".rjust(15), ' '.join(top_line))
            print("".rjust(15) , ' '.join(top_side_card[0]),
                  "".rjust(15) , ' '.join(top_side_card[1]) )

            print("".rjust(15) , ' '.join(middle_side_card[0]),
                  "".rjust(15) , ' '.join(middle_side_card[1]) )

            print(f"Player {players_turn} hand: " if players_turn else "Dealer's hand: ", ' '.join(bottom_side_card[0]),
                  f"Player {players_turn} split: " if players[players_turn].get('split') else '' , ''.join(bottom_side_card[1]) )

main()
