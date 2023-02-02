import random

def main():
    boxes={
            "closed": """
  __________
 /         /|
+---------+ |
|   GOLD  | |
|   BOX   | /
+---------+/""",
            "winning": """
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|
 /    ||   /|
+---------+ |
|   RED   | |
|   BOX   | /
+---------+/
""",
            "losing":"",
            }

    COLORS= ["BROWN","ORANGE"]

    players={}

    for i in range(1,3):
        players[i] = {}
        players[i]["color"] = COLORS[i-1]
        get_name(players,i)
    
    if random.randint(0,1):
        players[1]["winning"]=True
        players[2]["winning"]=False
    else:
        players[1]["winning"]=False
        players[2]["winning"]=True

    #print(players)
    print(boxes["closed"])
    assign_boxes(players)
    print(*players[1]["box"], sep="\n")


def get_name(players, player_number):
    player_name= input(f"Player {player_number} give me your name: ").strip()
    while not player_name.isalpha():
        player_name= input(f"Please insert a valid option for your name: ").strip()
        
    players[player_number]["name"]= player_name

def assign_boxes(players,opened_box=False):
    #get a list of components of the box and add the basic structure of the box and then readjust the strings with spaces needed
    for i in range(1,3):
        MAX_WIDTH = len(f"|  {players[i]['color']}  | |")
        if MAX_WIDTH % 2:
            left_side_chars= MAX_WIDTH//2
            right_side_chars= MAX_WIDTH//2 + 1
        else:
            left_side_chars = MAX_WIDTH//2
            right_side_chars = MAX_WIDTH//2

        if opened_box:
            MAX_HEIGHT= 9
            if players[i]["winning"]:
                BOX_COMPONENTS = [f"   {'-'*left_side_chars}VV{'-'*right_side_chars}",
                                  f"  |{' '*left_side_chars}VV{' '*right_side_chars}|",
                                  f"  {' '*left_side_chars}|VV|{' '*right_side_chars}",
                                  f"  |{'_'*left_side_chars}||{'_'*right_side_chars}|",
                                  f" /{' '*left_side_chars}||{' '*right_side_chars}/|",
                                  f"+{'-'*(left_side_chars+right_side_chars)}+ |",
                                  f"|  {players[i]['color']}  | |",
                                  f"|{' '*left_side_chars}BOX{' '*right_side_chars}| /",
                                  f"+{'-'*(left_side_chars+right_side_chars)}+/"]
                #here draw the box to display
                players[i]["box"]= BOX_COMPONENTS
            else:
                BOX_COMPONENTS = [f"   {'-'*left_side_chars}{'-'*right_side_chars}",
                                  f"  |{' '*left_side_chars}{' '*right_side_chars}|",
                                  f"  {' '*left_side_chars}{' '*right_side_chars}",
                                  f"  |{'_'*left_side_chars}{'_'*right_side_chars}|",
                                  f" /{' '*left_side_chars}{' '*right_side_chars}/|",
                                  f"+{'-'*(left_side_chars+right_side_chars)}+ |",
                                  f"|  {players[i]['color']}  | |",
                                  f"|{' '*left_side_chars}BOX{' '*right_side_chars}| /",
                                  f"+{'-'*(left_side_chars+right_side_chars)}+/"]
                players[i]["box"]=BOX_COMPONENTS
        else:
            MAX_HEIGHT= 6
            BOX_COMPONENTS = [f"  {'_'*left_side_chars}{'_'*right_side_chars}",
                                  f" /{' '*left_side_chars}{' '*right_side_chars}/|",
                                  f"+{'-'*(left_side_chars+right_side_chars)}+ |",
                                  f"|  {players[i]['color']}  | |",
                                  f"|{' '*left_side_chars}BOX{' '*right_side_chars}| /",
                                  f"+{'-'*(left_side_chars+right_side_chars)}+/"]
            players[i]["box"]= BOX_COMPONENTS

def readjust_box_size(box_components,max_height):
    max_width= len(box_components[6]) if max_height == 9 else len(box_components[3])
    for i in range(max_height):
        ...

main()

