import random

def main():

    
    DIAMOND = chr(9830)
    SPADE = chr(9824)
    CLUB = chr(9827)
    HEART = chr(9829)

    PLAYERS_TURN = 1
    PLAYERS_NUMBER = [[],[]]
    PLAYERS_MONEY = {}
    PLAYERS_BET = [0]
    PLAYER_OPTIONS = ['(H)it','(S)tand']
    PLAYER_ADDITIONAL_OPTIONS = ['(Do)uble','(Sp)lit','(Sur)render']

    for i in range(1,len(PLAYERS_NUMBER)):
        PLAYERS_MONEY[i] = 1_000

    deck = make_deck(DIAMOND,SPADE,CLUB,HEART)

    #while len(PLAYER_HAND) < 2 :
    while len(PLAYERS_NUMBER[-1]) < 2:
        for player_hand in PLAYERS_NUMBER:
            player_hand.append(deck.pop(0))

    #print(PLAYERS)

    while PLAYERS_TURN:
        CURRENT_BET =get_bet(PLAYERS_TURN,PLAYERS_MONEY)
        PLAYERS_BET.append(CURRENT_BET)


        check_and_process_move(PLAYERS_NUMBER,PLAYERS_TURN,PLAYER_OPTIONS,PLAYERS_MONEY,CURRENT_BET,deck,PLAYERS_BET,PLAYER_ADDITIONAL_OPTIONS)
        #print(f"Player\'s hand: {display_cards()}")


        if PLAYERS_NUMBER[PLAYERS_TURN] == PLAYERS_NUMBER[-1]:
            PLAYERS_TURN=0
            break
        else:
            PLAYERS_TURN +=1

    #now make the dealer draw cards until he's above 17
    while get_cards_value(PLAYERS_NUMBER[PLAYERS_TURN]) < 17:
        PLAYERS_NUMBER[PLAYERS_TURN].append(deck.pop(0))

    #print(f"Dealer\'s hand: {display_cards()}")

    if get_cards_value(PLAYERS_NUMBER[PLAYERS_TURN]) > 21:
        #display dealer's cards
        #print(f'dealer busted!')
        for player in range(1,len(PLAYERS_NUMBER)):
            if get_cards_value(PLAYERS_NUMBER[player]) <=21:
                #display player hand and tell how much he earned
                PLAYERS_MONEY[player] += PLAYERS_BET[player]
    else:
        for player in range(1,len(PLAYERS_NUMBER)):
            if get_cards_value(PLAYERS_NUMBER[player]) <= 21 :
                if get_cards_value(PLAYERS_NUMBER[player]) > get_cards_value(PLAYERS_NUMBER[PLAYERS_TURN]):
                    # pay the player bet 
                    ...
                elif get_cards_value(PLAYERS_NUMBER[player]) < get_cards_value(PLAYERS_NUMBER[PLAYERS_TURN]):
                    #get player money
                    ...



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

def get_bet(player_turn, player_money):
    while True:
        CURRENT_BET =input(f"Player {player_turn},Amount you're betting: ")
        if CURRENT_BET.isnumeric() and int(CURRENT_BET) <= player_money[player_turn]:
            return int(CURRENT_BET)
        elif CURRENT_BET.isnumeric() and int(CURRENT_BET) > player_money[player_turn]:
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


def check_and_process_move(players_number,players_turn,player_options,players_money,player_bet,deck,players_bet,player_additional_options):


    while True:

        if get_cards_value(players_number[players_turn])>21:
            print("Bust! You lost your bet,try another time")
            players_money[players_turn] -=  player_bet
            break
        
        # add player options and change accordingly
        #check player cards for double, split and surrender option
        if len(players_number[players_turn]) == 2:
            for option in player_additional_options:
                if option == '(Sp)lit' and len(set(list(zip(*players_number[players_turn]))[0])) !=1:
                    continue
                player_options.append(option)
        else:
            player_options = [x for x in player_options if x not in player_additional_options]

        print(f"Player {players_turn} turn. {', '.join(player_options)}.")
        player_move= input("> ")

        if player_move.lower() in ('h','hit') and player_move in player_options:
            players_number[players_turn].append(deck.pop(0))
            #print(f"Player\'s hand: {display_cards()}")
        elif player_move.lower() in ('st','stand','s') and player_move in player_options:
            break
        elif player_move.lower() in ('do','double','d') and player_move in player_options:
            #print(f"Player\'s hand: {display_cards()}")
            if players_money[players_turn] >= player_bet * 2:
                player_bet *=2
                players_bet[players_turn]= player_bet
                players_number[players_turn].append(deck.pop(0))
            break
        elif player_move.lower() in ('sur','surrender') and player_move in player_options:
            players_money[players_turn] -= player_bet / 2
            players_bet[players_turn]= player_bet/2
            print(f"Player {players_turn}, you lost half of your bet by surrendering")
            break
        elif player_move.lower() in ('sp','split') and player_move in player_options:
            # add another hand to the player, either separately or in the  same hand
            #draw cards until len() ==2 for both hands
            # display hands with print(f"Player\'s hand: {display_cards()}")
            ...
            
        else:
            print('Please insert a valid option.')


main()
