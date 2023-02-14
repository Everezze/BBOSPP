import random
def main():
    JAPANESE_NUMBERS = {
            1:"ICHI",
            2:"NI",
            3:"SAN",
            4:"SHI",
            5:"GO",
            6:"ROKU",
            }
    BINARY_OUTCOME = ("cho","han")
    BASE_MONEY = 5000
    FIRST_DICE_VALUE= random.randint(1,6)
    SECOND_DICE_VALUE= random.randint(1,6)
    DICE_TOTAL_VALUE= FIRST_DICE_VALUE + SECOND_DICE_VALUE
    HOUSE_FEE= 0.1

    PLAYER_BET= input(f"You have {BASE_MONEY}€, how much you want to bet?\n> ")
    while True:
        if not PLAYER_BET.isdecimal():
            PLAYER_BET = input("Please insert only digits.\n> ")
        elif int(PLAYER_BET)<1:
            PLAYER_BET = input("Your bet must be at least 1.\n> ")
        elif int(PLAYER_BET)>BASE_MONEY:
            PLAYER_BET = input("Your bet must be less than or equal to your fortune.\n> ")
        else:
            break
    PLAYER_BET = int(PLAYER_BET)

    print("The dealer threw the dice on the floor, hiding the outcome.\n")
    PLAYER_CHOICE = input("CHO(even) or HAN(odd)? ").strip().lower()
    while PLAYER_CHOICE not in ("cho","han"):
        PLAYER_CHOICE = input("Please choose one the two possibilities, CHO or HAN?")

    print(f"\nThe dice land on their feet, and you see:")
    print(f"{JAPANESE_NUMBERS[FIRST_DICE_VALUE]}({FIRST_DICE_VALUE}) - {JAPANESE_NUMBERS[SECOND_DICE_VALUE]}({SECOND_DICE_VALUE})")

    if BINARY_OUTCOME[DICE_TOTAL_VALUE % 2] == PLAYER_CHOICE:
        BASE_MONEY += PLAYER_BET*(1-HOUSE_FEE)
        print(f"Congratulations, You won! You have now {BASE_MONEY}(+{PLAYER_BET})")
        print(f"The house collects a {round(PLAYER_BET*HOUSE_FEE,2)} fee.")
    else:
        BASE_MONEY -= PLAYER_BET
        print(f"Oh no you lost...Your new balance is now {BASE_MONEY}(-PLAYER_BET)")

main()
