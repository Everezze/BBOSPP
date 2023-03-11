def main():
    user_number= input("Choose a number to start the Collatz sequence: ").strip()
    while not user_number.isdecimal() or int(user_number)<=0:
        user_number= input("Please insert a valid number greater than 0, it should only contain integers\n> ")
    user_number= int(user_number)

    collatz_sequence= []
    collatz_sequence.append(user_number)
    while user_number != 1:
        if user_number % 2:
            user_number = user_number * 3 +1
        else:
            user_number //=2
        collatz_sequence.append(user_number)
    print(*collatz_sequence)

main()
