import random

def main():

    
    DIAMOND = chr(9830)
    SPADE = chr(9824)
    CLUB = chr(9827)
    HEART = chr(9829)

    PLAYERS_TURN = 1
    PLAYERS_NUMBER = [[],[]]
    PLAYERS_MONEY = {}
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
    PLAYER_BET =get_bet(PLAYERS_TURN,PLAYERS_MONEY)

    while PLAYERS_TURN:

        if len(PLAYERS_NUMBER[PLAYERS_TURN]) == 2:
            for option in PLAYER_ADDITIONAL_OPTIONS:
                if option == '(Sp)lit' and len(set(list(zip(*PLAYERS_NUMBER[PLAYERS_TURN]))[0])) !=1:
                    continue
                PLAYER_OPTIONS.append(option)
        else:
            PLAYER_OPTIONS = [x for x in PLAYER_OPTIONS if x not in PLAYER_ADDITIONAL_OPTIONS]

        #check player cards for double, split and surrender option
        print(f"Player {PLAYERS_TURN} turn. {', '.join(PLAYER_OPTIONS)}.")
        player_move= input("> ")

        if player_move.lower() in ('h','hit') and player_move in PLAYER_OPTIONS:
            PLAYERS_NUMBER[PLAYERS_TURN].append(deck.pop(0))
        elif player_move.lower() in ('st','stand') and player_move in PLAYER_OPTIONS:
            continue
        elif player_move.lower() in ('do','double') and player_move in PLAYER_OPTIONS:
            if PLAYERS_MONEY[PLAYERS_TURN] >= PLAYER_BET * 2:
                PLAYER_BET *=2
                PLAYERS_NUMBER[PLAYERS_TURN].append(deck.pop(0))
        elif player_move.lower() in ('sur','surrender') and player_move in PLAYER_OPTIONS:
            PLAYERS_MONEY[PLAYERS_TURN] = PLAYER_BET / 2
        elif player_move.lower() in ('sp','split') and player_move in PLAYER_OPTIONS:
            if len(set(list(zip(*PLAYERS_NUMBER[PLAYERS_TURN]))[0])) ==1:
                # add another hand to the player, either separately or in the
                # same hand
                ...

        card_sum = get_cards_value(PLAYERS_NUMBER[PLAYERS_TURN])
        if card_sum >21:
            print("Bust! You lost your bet,try another time")
            PLAYERS_MONEY[PLAYERS_TURN] = PLAYERS_MONEY[PLAYERS_TURN] - PLAYER_BET
            if PLAYERS_NUMBER[PLAYERS_TURN] == PLAYERS_NUMBER[-1]:
                break
            else:
                PLAYERS_TURN +=1
                PLAYER_BET =get_bet(PLAYERS_TURN,PLAYERS_MONEY)


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
        PLAYER_BET =input(f"Player {player_turn},Amount you're betting: ")
        if PLAYER_BET.isnumeric() and int(PLAYER_BET) <= player_money[player_turn]:
            return int(PLAYER_BET)
        elif PLAYER_BET.isnumeric() and int(PLAYER_BET) > player_money[player_turn]:
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


main()
