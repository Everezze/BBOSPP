import time
def main():
    DIGIT_COMPONENTS= {
            0:{
                "top":" __ ",
                "mid":"|  |",
                "bot":"|__|"},
            1:{
                "top":" ",
                "mid":"|",
                "bot":"|"},
            2:{
                "top":" __ ",
                "mid":" __|",
                "bot":"|__ "},
            3:{
                "top":"__ ",
                "mid":"__|",
                "bot":"__|"},
            4:{
                "top":"   ",
                "mid":"|_|",
                "bot":"  |"},
            5:{
                "top":" __ ",
                "mid":"|__ ",
                "bot":" __|"},
            6:{
                "top":" __ ",
                "mid":"|__ ",
                "bot":"|__|"},
            7:{
                "top":"__ ",
                "mid":"  |",
                "bot":"  |"},
            8:{
                "top":" __ ",
                "mid":"|__|",
                "bot":"|__|"},
            9:{
                "top":" __ ",
                "mid":"|__|",
                "bot":" __|"},
            }

    DIGITAL_CLOCK={
            "top": [],
            "mid": [],
            "bot": [],
            }

    while True:
        user_time= input("Choose a timer(default=sec):\n> ").strip().lower()
        if user_time[-1] == "h":
            if 2<=len(user_time) <=3:
                time_value= user_time[:-2]
                if time_value.isdecimal():
                    if int(time_value)==0:
                        print("Hour need to be greater than 0")
                    if int(time_value)<=24:
                        timer_in_seconds= int(time_value)*3600
                        hour = timer_in_seconds//3600
                        minutes= timer_in_seconds%3600 //60
                        seconds= timer_in_seconds%60
                        break
                    else:
                        print("Hour need to be less than 24")
                else:
                    print("Only digits can precede the hour specified!")
            else:
                print("You can't go over 2-digits hour, stay within 24 hour range")

        if user_time[-1] == "m":
            time_value= user_time[:-1]
            if time_value.isdecimal():
                if int(time_value)==0:
                    print("Minutes need to be greater than 0")
                print("time value: ",time_value)
                timer_in_seconds= int(time_value)*60
                print("total seconds: ",timer_in_seconds)
                hour = timer_in_seconds//3600
                minutes= timer_in_seconds%3600 //60
                seconds= timer_in_seconds%60
                if hour>24:
                    print("Minutes given translates to more than 24hours, Choose lower value")
                    continue
                if hour == 24:
                    if minutes !=0:
                        print("Minutes given translates to more than 24hours, Choose lower value")
                        continue
                    if seconds !=0:
                        print("Minutes given translates to more than 24hours, Choose lower value")
                        continue
                print(user_time)
                break
            else:
                print("Only digits can precede the minutes specified!")

        if user_time.isdecimal():
            timer_in_seconds = int(user_time)
            hour= timer_in_seconds// 3600
            minutes= timer_in_seconds% 3600 //60
            seconds= timer_in_seconds % 60
            if hour>24:
                print("Seconds given translates to more than 24hours, Choose lower value")
                continue
            if hour == 24:
                if minutes !=0:
                    print("Seconds given translates to more than 24hours, Choose lower value")
                    continue
                if seconds !=0:
                    print("Seconds given translates to more than 24hours, Choose lower value")
                    continue
            break
        else:
            print("It must only contain digits(Remove space within if any)")

    print(hour,"hour",minutes,"minutes",seconds,"seconds")

    while timer_in_seconds >= 0:
        time_component = [hour,minutes,seconds]
        create_ascii_clock(time_component,DIGIT_COMPONENTS,DIGITAL_CLOCK)
        timer_in_seconds -=1
        hour= timer_in_seconds// 3600
        minutes= timer_in_seconds% 3600 //60
        seconds= timer_in_seconds % 60
        for value in DIGITAL_CLOCK.values():
            print(*value)
        time.sleep(1)

def create_ascii_clock(time_component,digit_components,digital_clock):
    for key in digital_clock.keys():
        if digital_clock[key]:
            digital_clock[key] = []

    for component_index,clock_component in enumerate(time_component):
        if len(str(clock_component)) ==1:
            clock_component = "0"+str(clock_component)
        else:
            clock_component = str(clock_component)
        for number_index,number in enumerate(clock_component):
            for side in digit_components[int(number)]:
                #print("side",side)
                #print("digit-components",DIGIT_COMPONENTS[int(number)])
                #print("single component",DIGIT_COMPONENTS[int(number)][side])
                digital_clock[side].append(digit_components[int(number)][side])
            if number_index == len(clock_component)-1 and component_index != len(time_component)-1:
                digital_clock["top"].append("   ")
                digital_clock["mid"].append(" * ")
                digital_clock["bot"].append(" * ")
    

main()
