import datetime

def main():

    A_DAY= datetime.timedelta(1)
    DAYS_IN_WEEK = 7
    NUMBER_OF_ROWS = 6
    TOTAL_OF_DAYS = DAYS_IN_WEEK * NUMBER_OF_ROWS
    TOP_SIDE= []
    MIDDLE_SIDE= []
    BOTTOM_SIDE= []
    LAST_LINE= ["+","-----+"*DAYS_IN_WEEK]
    DAYS_LIST=[]

    user_year= input("What year you want to display?: ").lower().strip()
    while not user_year.isdecimal():
        user_year= input("Please insert a valid year: ").lower().strip()
    user_year= int(user_year)

    months_dict= {}
    months_dict.update(dict.fromkeys(("january","jan"),1))
    months_dict.update(dict.fromkeys(("february","feb"),2))
    months_dict.update(dict.fromkeys(("march","mar"),3))
    months_dict.update(dict.fromkeys(("april","apr"),4))
    months_dict.update(dict.fromkeys(("may"),5))
    months_dict.update(dict.fromkeys(("june","jun"),6))
    months_dict.update(dict.fromkeys(("july","jul"),7))
    months_dict.update(dict.fromkeys(("august","aug"),8))
    months_dict.update(dict.fromkeys(("september","sep"),9))
    months_dict.update(dict.fromkeys(("october","oct"),10))
    months_dict.update(dict.fromkeys(("november","nov"),11))
    months_dict.update(dict.fromkeys(("december","dec"),12))

    user_month= input(f"What month of {user_year} you're interested in?: ").lower().strip()
    
    while not months_dict.get(user_month):
        user_month= input("Please insert a valid month: ").lower().strip()

    current_date= datetime.date(user_year,months_dict[user_month],1)
    CHOSEN_MONTH = current_date.strftime("%B")
    CHOSEN_YEAR = current_date.strftime("%Y")
    while current_date.weekday() != 0:
        current_date = current_date - A_DAY

    print(TOTAL_OF_DAYS)
    print(current_date)

    for i in range(TOTAL_OF_DAYS):
        TOP_SIDE.append("-----+")
        MIDDLE_SIDE.append(f"  {current_date.day}  |" if len(str(current_date.day))==1 else f"  {current_date.day} |" )
        BOTTOM_SIDE.append("     |")

        if len(DAYS_LIST)==0:
            DAYS_LIST.append(current_date.strftime("  %a"))
        elif len(DAYS_LIST)<7:
            DAYS_LIST.append(current_date.strftime("   %a"))
        current_date += A_DAY

    print(current_date)
    #print(current_date - datetime.timedelta(TOTAL_OF_DAYS))
    #print(TOP_SIDE,len(TOP_SIDE))
    #print(MIDDLE_SIDE,len(MIDDLE_SIDE))
    #print(BOTTOM_SIDE,len(BOTTOM_SIDE))
    #print(*TOP_SIDE[0:7],TOP_SIDE[7:14])

    print((CHOSEN_MONTH + " " + CHOSEN_YEAR).rjust(28))
    print("\n",*DAYS_LIST,sep="")
    for index in range(0,TOTAL_OF_DAYS,DAYS_IN_WEEK):
        print("+",*TOP_SIDE[index:index+DAYS_IN_WEEK],sep="",end="\n")
        print("|",*MIDDLE_SIDE[index:index+DAYS_IN_WEEK],sep="",end="\n")
        print("|",*BOTTOM_SIDE[index:index+DAYS_IN_WEEK],sep="",end="\n")
    print(*LAST_LINE,sep="",end="\n")

main()
