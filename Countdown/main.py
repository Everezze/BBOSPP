def main():
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
            user_time = int(user_time)
            hour= user_time// 3600
            minutes= user_time% 3600 //60
            seconds= user_time % 60
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

    print(hour,"hour",minutes,"minutes",seconds,"seconds")


main()
