import random
def main():
    NUMBER_OF_DICE = 2
    NUMBER_OF_FACE = 6
    OUTCOMES = {}
    SAMPLE = 1_000_000
    for possibilities in range(NUMBER_OF_DICE, NUMBER_OF_DICE*NUMBER_OF_FACE+1):
        OUTCOMES[possibilities] = 0
    print(OUTCOMES)

    for roll in range(SAMPLE):
        total = 0
        for number in range(NUMBER_OF_DICE):
            total += random.randint(1,NUMBER_OF_FACE)
        OUTCOMES[total] += 1
    print(OUTCOMES)

    print("TOTAL - ROLLS - PERCENTAGE")
    for key in OUTCOMES:
        rounded_frequency= round(OUTCOMES[key]/SAMPLE*100,1)
        print(f"  {key} - {OUTCOMES[key]} - {rounded_frequency}%")

main()
