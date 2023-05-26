import random
def main():
    #NUMBER_OF_CARDS = 3
    GOAT_CARD = [
            "+------+  ",
            "|  ((  |  ",
            "|  oo  |  ",
            "| /_/|_|  ",
            "|    | |  ",
            "|GOAT|||  ",
            "+------+  ",
                ]
    CAR_CARD = [
            "+------+  ",
            "| CAR! |  ",
            "|    __|  ",
            "|  _/  |  ",
            "| /_ __|  ",
            "|   o  |  ",
            "+------+  ",
               ]

    FACE_DOWN_CARD = [
            "+------+  ",
            "|      |  ",
            "|   N  |  ",
            "|      |  ",
            "|      |  ",
            "|      |  ",
            "+------+  ",
                ]

    while True:
        CARDS_TRUTHINESS = [True,False,False]
        random.shuffle(CARDS_TRUTHINESS)
        CARDS_VALUES = {
                1:False,
                2:False,
                3:False
                }

        for card in CARDS_VALUES:
            #print(CARDS[card])
            CARDS_VALUES[card] = CARDS_TRUTHINESS.pop(0)
            if CARDS_VALUES[card]:
                card_index = card
            #draw_card(card)
        #print(CARDS)
        CARDS_VALUES["car_index"] = card_index
        draw_card(CARDS_VALUES,GOAT_CARD,CAR_CARD,FACE_DOWN_CARD,**{"pick":True,"hint":False,"reveal":False})

        chosen_card = False
        while True:
            chosen_card = input("Pick door 1,2 or 3 ?: ").strip()
            if chosen_card.isdecimal():
                if int(chosen_card) >= len(CARDS_VALUES):
                    print("Error: number is bigger than number of doors.")
                    continue
                elif int(chosen_card) <=0:
                    print("Error: number must be bigger than 0.")
                    continue
                else:
                    chosen_card = int(chosen_card)
                    break
            print("Only digits allowed.")

        if chosen_card == CARDS_VALUES["car_index"]:
            random_losing_card = draw_card(CARDS_VALUES,GOAT_CARD,CAR_CARD,FACE_DOWN_CARD, USER_CARD = chosen_card,**{"pick":False,"hint":True,"reveal":False})
            while True:
                swap_choice = input("Do you want to swap doors?(Y/N): ").strip()
                if swap_choice.isalpha():
                    if swap_choice in ("y","yes","YES"):
                        chosen_card,random_losing_card = random_losing_card,chosen_card
                        break
                    elif swap_choice in ("n","no","NO"):
                        break
                    else:
                        print("Answer by YES(yes,y)/NO(n,no).")
                else:
                    print("Only letters allowed, answer by yes or no.")
            draw_card(CARDS_VALUES,GOAT_CARD,CAR_CARD,FACE_DOWN_CARD,
                      USER_CARD = chosen_card,**{"pick":False,"hint":False,"reveal":True})
            if swap_choice in ("y","yes","YES"):
                print(f"You swapped door n°{random_losing_card} for door n°{chosen_card} and...")
                print("You lost! How unfortunate...:\\")
            else:
                print("You chose to not swap and...")
                print(f"You won! The car is in the door n°{chosen_card}, Congratulations!")
        else: 
            draw_card(CARDS_VALUES,GOAT_CARD,CAR_CARD,FACE_DOWN_CARD, USER_CARD = chosen_card,**{"pick":False,"hint":True,"reveal":False})
            while True:
                swap_choice = input("Do you want to swap doors?(Y/N): ").strip()
                if swap_choice.isalpha():
                    if swap_choice in ("y","yes","YES"):
                        chosen_card,CARDS_VALUES["car_index"] = CARDS_VALUES["car_index"],chosen_card
                        break
                    elif swap_choice in ("n","no","NO"):
                        break
                    else:
                        print("Answer by YES(yes,y)/NO(n,no).")
                else:
                    print("Only letters allowed, answer by yes or no.")
            draw_card(CARDS_VALUES,GOAT_CARD,CAR_CARD,FACE_DOWN_CARD,
                      USER_CARD = chosen_card,**{"pick":False,"hint":False,"reveal":True})
            if swap_choice in ("y","yes","YES"):
                print(f"You swapped door n°{CARDS_VALUES['car_index']} for door n°{chosen_card} and...")
                print(f"You won! The car is in the door n°{chosen_card}, Congratulations!")
            else:
                print("You chose to not swap and...")
                print("You lost! How unfortunate...:\\")

        while True:
            replay = input("Do you to play again?[Y/N]").strip()
            if replay.isalpha():
                if replay in ("y","yes","YES"):
                    break
                elif replay in ("n","no","NO"):
                    break
                else:
                    print("Please,answer only by Yes or No.")
            else:
                print("Only letters allowed.")
        if replay in ("n","no","NO"):
            break

def draw_card(CARDS_VALUES,GOAT_CARD,CAR_CARD,FACE_DOWN_CARD,
              USER_CARD = False,**STAGE_OF_GAME):
    #print(f"{0 if USER_CARD else 1}")
    #print(STAGE_OF_GAME)
    #print("pick stage",PICK_STAGE)
    CARD_HEIGHT = 7
    NUMBER_OF_CARDS = 3
    if STAGE_OF_GAME["pick"]:
        for line in range(CARD_HEIGHT):
            if line ==2:
                #this will be length of 4 with the "car_index" key so need to reduce to 1
                #maybe range(1,len(CARDS_VALUES)-1)
                for card in range(1,len(CARDS_VALUES)): 
                    print(f"|   {card}  |  ",end="")
                print()
                continue
            print(FACE_DOWN_CARD[line]*NUMBER_OF_CARDS)
    elif STAGE_OF_GAME["hint"]:
        #get a random card thats not the user card to make it hide and
        #display every other cards
        if USER_CARD == CARDS_VALUES["car_index"]:
            while True:
                random_losing_card = random.randint(1,len(CARDS_VALUES)-1)
                if random_losing_card != USER_CARD:
                    break
            for line in range(CARD_HEIGHT):
                for card in range(1,len(CARDS_VALUES)):
                    if card == USER_CARD or card == random_losing_card:
                        if line == 2:
                            print(f"|   {card}  |  ",end="")
                        else:
                            print(FACE_DOWN_CARD[line],end="")
                    else:
                        print(GOAT_CARD[line],end="")
                print()
            print(f"The car is either behind door n°{USER_CARD} or door n°{random_losing_card}")
        else:
            for line in range(CARD_HEIGHT):
                for card in range(1,len(CARDS_VALUES)):
                    if card == USER_CARD or card == CARDS_VALUES["car_index"]:
                        if line == 2:
                            print(f"|   {card}  |  ",end="")
                        else:
                            print(FACE_DOWN_CARD[line],end="")
                    else:
                        print(GOAT_CARD[line],end="")
                print()
            print(f"The car is either behind door n°{USER_CARD} or door n°{CARDS_VALUES['car_index']}")
    else:
        #display all cards and tell if the player won or lost
        for line in range(CARD_HEIGHT):
            for card in range(1,len(CARDS_VALUES)):
                if CARDS_VALUES[card]:
                    print(CAR_CARD[line],end="")
                else:
                    print(GOAT_CARD[line],end="")
            print()

main()
