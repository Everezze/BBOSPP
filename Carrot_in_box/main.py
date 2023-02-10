import random
def main():

    BOX_STRUCTURES = {
            "opened":{
                "won": {
                    0:"   0VV0",
                    1:"  |2VV2|",
                    2:"  |2VV2|",
                    3:"  |0||0|",
                    4:" /2||2/|",
                    5:"+11+ |",
                    6:"|  3  | |",
                    7:"|242| /",
                    8:"+11+/",
                    },
                "lost": {
                    0:"   00",
                    1:"  |2  2|",
                    2:"  |2  2|",
                    3:"  |0__0|",
                    4:" /2  2/|",
                    5:"+11+ |",
                    6:"|  3  | |",
                    7:"|242| /",
                    8:"+11+/",
                    }
                },
            "closed": {
                    0:"  00",
                    1:" /2  2/|",
                    2:"+11+ |",
                    3:"|  3  | |",
                    4:"|242| /",
                    5:"+11+/",
                },
            "motifs": {
                0:"_",
                1:"-",
                2:" ",
                }
            }

    COLORS= ["BROWN","ORANGE"]
    PLAYERS={}

    for i in range(1,3):
        PLAYERS[i] = {}
        PLAYERS[i]["color"] = COLORS[i-1]
        PLAYERS[i]["box"] = {}
        get_name(PLAYERS,i)
    
    if random.randint(0,1):
        PLAYERS[1]["winning"]=True
        PLAYERS[2]["winning"]=False
    else:
        PLAYERS[1]["winning"]=False
        PLAYERS[2]["winning"]=True

    #print(players)
    #print(boxes["closed"])
    assign_boxes(PLAYERS,BOX_STRUCTURES)
    #print(*players[1]["box"], sep="\n")
    print(*PLAYERS[1]["box"]["opened"],sep="\n")
    print(*PLAYERS[1]["box"]["closed"],sep="\n")


def get_name(players, player_number):
    player_name= input(f"Player {player_number} give me your name: ").strip()
    while not player_name.isalpha():
        player_name= input(f"Please insert a valid option for your name: ").strip()
        
    players[player_number]["name"]= player_name

def assign_boxes(players,box_structures,opened_box=False):
    #get a list of components of the box and add the basic structure of the box and then readjust the strings with spaces needed
    for i in range(1,3):
        first_placeholder= True
        players[i]["box"]["opened"]=[]
        players[i]["box"]["closed"]=[]
        MAX_WIDTH = len(f"|  {players[i]['color']}  | |")

        #MAX_HEIGHT= 9
        if players[i]["winning"]:
            for component in box_structures["opened"]["won"].values():
                BASE_CHARS = len([x for x in component if not x.isnumeric()])
                if component == box_structures["opened"]["won"][0]:
                    BASE_CHARS +=1
                CHARS_TO_SUBSTITUTE = MAX_WIDTH - BASE_CHARS
                altered_component = component
                if "3" in component:
                    altered_component = component.replace("3",players[i]["color"])
                if "4" in component:
                    altered_component = component.replace("4","BOX")
                    CHARS_TO_SUBSTITUTE -=len("BOX")
                    #chars_to_substitute -= len(players[i]["color"])
                #elif "BOX" in component:
                    #chars_to_substitute -= len("BOX")
                    #pass
                if CHARS_TO_SUBSTITUTE % 2:
                    left_side_chars= CHARS_TO_SUBSTITUTE //2
                    right_side_chars= CHARS_TO_SUBSTITUTE //2 +1
                    if component == box_structures["opened"]["won"][4]:
                        left_side_chars,right_side_chars = right_side_chars,left_side_chars
                else:
                    left_side_chars = CHARS_TO_SUBSTITUTE//2
                    right_side_chars = CHARS_TO_SUBSTITUTE//2
                    if component == box_structures["opened"]["won"][4]:
                        left_side_chars +=1
                        right_side_chars-=1
                if component == box_structures["opened"]["won"][len(box_structures["opened"]["won"])-1]:
                    right_side_chars -=1
                #if players[i] == players[1]:
                    #print(f"max_width: {MAX_WIDTH}")
                    #print(f"base chars: {base_chars}")
                    #print(f"numbers of chars to replace: {chars_to_substitute}")
                    #print(f"left_side_chars: {left_side_chars}")
                    #print(f"right_side_chars: {right_side_chars}")
                while any(chrter.isdigit() for chrter in altered_component):
                    for digit in range(3):
                        if str(digit) in altered_component:
                            char_to_replace = altered_component[altered_component.find(str(digit))]
                            break
                    motif= box_structures["motifs"][int(char_to_replace)]
                    if first_placeholder:
                        altered_component = altered_component.replace(char_to_replace, motif*left_side_chars,1)
                        #print("half component replaced: ",*component,sep="")
                        first_placeholder= False
                    else:
                        altered_component = altered_component.replace(char_to_replace, motif*right_side_chars,1)
                        #print("other half component replaced: ",*component,sep="",end="\n")
                players[i]["box"]["opened"].append(altered_component)
                first_placeholder= True
        else:
            for component in box_structures["opened"]["lost"].values():
                BASE_CHARS = len([x for x in component if not x.isnumeric()])
                if component == box_structures["opened"]["lost"][0]:
                    BASE_CHARS +=1
                CHARS_TO_SUBSTITUTE = MAX_WIDTH - BASE_CHARS
                altered_component = component
                if "3" in component:
                    altered_component = component.replace("3",players[i]["color"])
                if "4" in component:
                    altered_component = component.replace("4","BOX")
                    CHARS_TO_SUBSTITUTE -=len("BOX")
                    #chars_to_substitute -= len(players[i]["color"])
                #elif "BOX" in component:
                    #chars_to_substitute -= len("BOX")
                    #pass
                if CHARS_TO_SUBSTITUTE % 2:
                    left_side_chars= CHARS_TO_SUBSTITUTE //2
                    right_side_chars= CHARS_TO_SUBSTITUTE //2 +1
                else:
                    left_side_chars = CHARS_TO_SUBSTITUTE//2
                    right_side_chars = CHARS_TO_SUBSTITUTE//2
                if component == box_structures["opened"]["won"][len(box_structures["opened"]["won"])-1]:
                    right_side_chars -=1
                #if players[i] == players[1]:
                    #print(f"max_width: {MAX_WIDTH}")
                    #print(f"base chars: {BASE_CHARS}")
                    #print(f"numbers of chars to replace: {CHARS_TO_SUBSTITUTE}")
                    #print(f"left_side_chars: {left_side_chars}")
                    #print(f"right_side_chars: {right_side_chars}\n")
                while any(chrter.isdigit() for chrter in altered_component):
                    for digit in range(3):
                        if str(digit) in altered_component:
                            char_to_replace = altered_component[altered_component.find(str(digit))]
                            break
                    motif= box_structures["motifs"][int(char_to_replace)]
                    if first_placeholder:
                        altered_component = altered_component.replace(char_to_replace, motif*left_side_chars,1)
                        #print("half component replaced: ",*component,sep="")
                        first_placeholder= False
                    else:
                        altered_component = altered_component.replace(char_to_replace, motif*right_side_chars,1)
                        #print("other half component replaced: ",*component,sep="",end="\n")
                players[i]["box"]["opened"].append(altered_component)
                first_placeholder= True

        for component in box_structures["closed"].values():
            BASE_CHARS = len([x for x in component if not x.isnumeric()])
            if component == box_structures["closed"][0]:
                BASE_CHARS +=1
            CHARS_TO_SUBSTITUTE = MAX_WIDTH - BASE_CHARS
            altered_component = component
            if "3" in component:
                altered_component = component.replace("3",players[i]["color"])
            if "4" in component:
                altered_component = component.replace("4","BOX")
                CHARS_TO_SUBSTITUTE -=len("BOX")
                #chars_to_substitute -= len(players[i]["color"])
            #elif "BOX" in component:
                #chars_to_substitute -= len("BOX")
                #pass
            if CHARS_TO_SUBSTITUTE % 2:
                left_side_chars= CHARS_TO_SUBSTITUTE //2
                right_side_chars= CHARS_TO_SUBSTITUTE //2 +1
            else:
                left_side_chars = CHARS_TO_SUBSTITUTE//2
                right_side_chars = CHARS_TO_SUBSTITUTE//2
            if component == box_structures["opened"]["won"][len(box_structures["opened"]["won"])-1]:
                right_side_chars -=1
            #if players[i] == players[1]:
                #print(f"max_width: {MAX_WIDTH}")
                #print(f"base chars: {base_chars}")
                #print(f"numbers of chars to replace: {chars_to_substitute}")
                #print(f"left_side_chars: {left_side_chars}")
                #print(f"right_side_chars: {right_side_chars}")
            while any(chrter.isdigit() for chrter in altered_component):
                for digit in range(3):
                    if str(digit) in altered_component:
                        char_to_replace = altered_component[altered_component.find(str(digit))]
                        break
                motif= box_structures["motifs"][int(char_to_replace)]
                if first_placeholder:
                    altered_component = altered_component.replace(char_to_replace, motif*left_side_chars,1)
                    #print("half component replaced: ",*component,sep="")
                    first_placeholder= False
                else:
                    altered_component = altered_component.replace(char_to_replace, motif*right_side_chars,1)
                    #print("other half component replaced: ",*component,sep="",end="\n")
            players[i]["box"]["closed"].append(altered_component)
            first_placeholder= True

main()

