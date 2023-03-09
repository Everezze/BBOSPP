import random
def main():
    nbr = random.randint(2,20)
    VERBS = {
            "action": {
                "transitive":["give","raise","lay","borrow","address","bring",
                              "read","admit","break","lead","love","tweak","spread"],
                "intransitive":["rise","lie","go","remain","vanish","stand",
                                "emerge","depend","stay","fall","become","occur","wait"]
                },
            "linking":["become","be","seem","feel","smell","go","keep","enjoy"],
            "helping":["could","must","might","should","shall","will",
                       "would","may","do","do not"],
            "progressive":["giving","raising","laying","borrowing","addressing","bringing",
                           "reading","admitting","breaking","leading","loving","tweaking","spreading"]}

    COUNTRIES = ["Cambodia","Indonesia","Lesotho","Nepal","France","Germany","USA","UK","Brazil",
               "South Africa","China","Japan","India","Serbia","Portugal","Spain"]

    CONJUNCTIONS_OF_TIME = ["after","before","while","when","whenever","until"]

    NOUNS= {
            "pronouns":["him","her"],
            "collective":["Herd","Pack","Flock","Swarm","Gang","Choir","Orchestra","Panel","Crowd","Troupe","Celebrities"],
            "abstract":{"feelings":["Anxiety","Pain","Pleasure","Stress","Sympathy"],
                        "states":["Chaos","Freedom","Luxury","Peace","Pessimism","Stability"],
                        "emotions":["Anger","Happiness","Love","Sadness","Indifference"],
                        "qualities":["Brilliance","Courage","Determination","Generosity","Patience"],
                        "concepts":["Comfort","Energy","Failure","Success","Motivation","Opportunity","Faith"],
                        #"ideas":["Chaos","Freedom","Luxury","Peace","Pessimism"],
                        "events":["Birthday","Career","Childhood","Death","Holiday","Marriage"],
                        },
            "countable":["book","table","restaurant","cat","giraffe","photograph","candle","painting",
                         "birthday cake","painting","neighborhood","car","skate","house"],
            "uncountable":["water","fire","garbage","salt","cheese","information","equipment","bread","furniture","butter","milk","clay"],
            "concrete":["rocks","butterflies","music","air","animals","plants","trees","noises","painter",
                        "prime minister","chair","social media","tango","yoga"],
            }
    #store all clickbaits function into dict with int key and use random to chose one
    CLICKBAITS = {
            0: {"function":XreasonsWhy,"param":[nbr,NOUNS["collective"],VERBS["linking"],NOUNS["concrete"]]},
            1:
            {"function":XthingsYou,"param":[nbr,CONJUNCTIONS_OF_TIME,VERBS["progressive"],NOUNS["countable"]]},#not finished yet
            2: {"function":WhatHappensIf,"param":[VERBS["action"]["transitive"],NOUNS["concrete"]]},
            3: {"function":XBest,"param":[nbr,NOUNS["countable"],VERBS["action"]["transitive"]]},
            4: {"function":WontBelieve,"param":[COUNTRIES,NOUNS["abstract"]["events"]]},
            5: {"function":XWays,"param":[nbr,VERBS["linking"],NOUNS["abstract"]["feelings"]]},
            6: {"function":BigCompaniesHate,"param":[NOUNS["pronouns"],COUNTRIES,NOUNS["countable"]]},
            7: {"function":MillenialsKilling,"param":[NOUNS["concrete"]]},
            }

    number_of_headlines = input("How much random headlines do you want to generate?: ")
    while not number_of_headlines.isnumeric():
        number_of_headlines = input("Insert a valid amount of headlines you want: ")
    number_of_headlines= int(number_of_headlines)

    for headline in range(number_of_headlines):
        clickbait_index = random.randint(0,7)
        args = []
        for el in CLICKBAITS[clickbait_index]["param"]:
            if type(el) is int:
                args.append(random.randint(2,20))
            else:
                args.append(el[random.randint(0,len(el)-1)])
        CLICKBAITS[clickbait_index]["function"](*args)
        #loop through the array arguments and if not int then give a random key and add it as argument to the function


def XreasonsWhy(nbr, collective_noun, linking_verb,concrete_noun):
    print(f"{nbr} Reasons why {collective_noun} {linking_verb} {concrete_noun}")

def XthingsYou(nbr,conjunctions_of_time,progressive_verb,countable_noun):
    sentences = [
            f"{nbr} Things You need to do {conjunctions_of_time} {progressive_verb} a {countable_noun}",
            f"{nbr} Things You don't know about your {countable_noun}"
            ]
    print(sentences[random.randint(0,1)])

def WhatHappensIf(transitive_verb,concrete_noun):
    print(f"This is what happens if You {transitive_verb} {concrete_noun}")

def XBest(nbr,countable_noun,transitive_verb):
    print(f"{nbr} Best {countable_noun} to {transitive_verb}")

def WontBelieve(country,event):
    print(f"You Won't believe what {country} population do before {event}")

def XWays(nbr,linking_verb,feeling_noun):
    print(f"{nbr} Ways to {linking_verb} {feeling_noun}")

def BigCompaniesHate(pronoun,country,countable_noun):
    gender = "girl" if pronoun == "she" else "boy"
    print(f"Big companies hate {pronoun}! See how this {country} {gender} Invented a cheaper {countable_noun}")

def MillenialsKilling(concrete_noun):
    print(f"Are Millenials killing the {concrete_noun} industry?")


main()
