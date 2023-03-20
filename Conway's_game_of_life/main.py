import random
def main():
    previous_grid = []
    WIDTH= 50
    HEIGHT= 10
    PREVIOUS_CYCLE_TITLE = "Latest Life Cycle"
    CURRENT_CYCLE_TITLE = "Current Life Cycle"

    for i in range(HEIGHT):
        previous_grid.append([])
    for row in previous_grid:
        while len(row)<WIDTH:
            row.append("O" if random.randint(0,1) else " ")
    #print(*previous_grid,sep="\n")
    print(PREVIOUS_CYCLE_TITLE.rjust(((WIDTH-len(PREVIOUS_CYCLE_TITLE))//2 ) + len(PREVIOUS_CYCLE_TITLE)))
    print(" ","_"*WIDTH,sep="")
    for row in previous_grid:
        print("|",*row,"|",sep="")
    print(" ","-"*WIDTH,sep="")
    #print("\n"*2)
    editable_grid = [x[:] for x in previous_grid]

    while True:
        cycles_to_generate= input("How many cycles do you want to simulate?(max=10) or q(quit): ").strip().lower()
        if cycles_to_generate in ("q","quit"):
            break
        while not cycles_to_generate.isdecimal():
            cycles_to_generate= input("Please insert only digits: ")
        if int(cycles_to_generate)>10:
            print("!Warning: Exceeded Limit of cycles.")
            continue
        else:
            cycles_to_generate = int(cycles_to_generate)
        for cycle in range(1,cycles_to_generate+1):
            previous_grid = generate_life_cycle(previous_grid,editable_grid)
            CURRENT_CYCLE_TITLE = f"Cycle n{cycle}"
            print("\n",CURRENT_CYCLE_TITLE.rjust(((WIDTH-len(CURRENT_CYCLE_TITLE))//2 ) + len(CURRENT_CYCLE_TITLE)))
            print(" ","_"*WIDTH,sep="")
            for row in previous_grid:
                print("|",*row,"|",sep="")
            print(" ","-"*WIDTH,sep="")


def count_neighbors(current_row,top_row,bottom_row,cell_index,first_cell=False,last_cell=False):
    number_of_neighbors = 0
    if first_cell:
        if current_row[cell_index+1] == "O":
            number_of_neighbors +=1
        if current_row[-1] == "O":
            number_of_neighbors +=1
        if top_row[cell_index+1] == "O":
            number_of_neighbors +=1
        if top_row[cell_index] == "O":
            number_of_neighbors +=1
        if top_row[-1] == "O":
            number_of_neighbors +=1
        if bottom_row[cell_index+1] == "O":
            number_of_neighbors +=1
        if bottom_row[cell_index] == "O":
            number_of_neighbors +=1
        if bottom_row[-1] == "O":
            number_of_neighbors +=1
    elif last_cell:
        if current_row[cell_index-1] == "O":
            number_of_neighbors +=1
        if current_row[0] == "O":
            number_of_neighbors +=1
        if top_row[cell_index] == "O":
            number_of_neighbors +=1
        if top_row[cell_index-1] == "O":
            number_of_neighbors +=1
        if top_row[0] == "O":
            number_of_neighbors +=1
        if bottom_row[cell_index] == "O":
            number_of_neighbors +=1
        if bottom_row[cell_index-1] == "O":
            number_of_neighbors +=1
        if bottom_row[0] == "O":
            number_of_neighbors +=1
    else:
        if current_row[cell_index-1] == "O":
            number_of_neighbors +=1
        if current_row[cell_index+1] == "O":
            number_of_neighbors +=1
        if top_row[cell_index] == "O":
            number_of_neighbors +=1
        if top_row[cell_index-1] == "O":
            number_of_neighbors +=1
        if top_row[cell_index+1] == "O":
            number_of_neighbors +=1
        if bottom_row[cell_index] == "O":
            number_of_neighbors +=1
        if bottom_row[cell_index-1] == "O":
            number_of_neighbors +=1
        if bottom_row[cell_index+1] == "O":
            number_of_neighbors +=1

    return number_of_neighbors

def generate_life_cycle(previous_grid,editable_grid):
    for row_index in range(len(previous_grid)):
        row= previous_grid[row_index]
        if row_index == 0:
            top_row = previous_grid[-1]
            bottom_row = previous_grid[row_index+1]
        elif row_index == len(previous_grid)-1:
            top_row = previous_grid[row_index-1]
            bottom_row = previous_grid[0]
        else:
            top_row = previous_grid[row_index-1]
            bottom_row = previous_grid[row_index+1]
        #print(top_row,bottom_row)
        for cell_index in range(len(row)):
            #!! here index function of list will sometimes return same index as
            #previous elements because its the first found so the code is broken
            #by this !!!!!!
            cell= row[cell_index]
            #print("cell index:",cell_index)
            if cell_index == 0:
                number_of_neighbors = count_neighbors(row,top_row,bottom_row,cell_index,first_cell= True)
            elif cell_index == len(row)-1:
                number_of_neighbors = count_neighbors(row,top_row,bottom_row,cell_index,last_cell= True)
            else:
                number_of_neighbors = count_neighbors(row,top_row,bottom_row,cell_index)
            #print("number_of_neighbors",number_of_neighbors)
            if cell == " ":
                if number_of_neighbors ==3:
                    editable_grid[row_index][cell_index] = "O"
            else:
                if 2>number_of_neighbors or number_of_neighbors >3:
                    editable_grid[row_index][cell_index] = " "
    previous_grid = [x[:] for x in editable_grid]
    return previous_grid


main()
