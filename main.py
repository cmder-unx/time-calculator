def add_time(start_time, duration, starting_day=""):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    #INPUTS TREATMENT
    start_time, duration, starting_day = str(start_time), str(duration), str(starting_day.lower())
    
    #START TIME TREATMENT
    start_time_split = start_time.split(":")
    start_time_split2 = start_time_split[1].split(" ")
    hour, minutes, ending = int(start_time_split[0]), int(start_time_split2[0]), start_time_split2[1]
    
    #DURATION TREATMENT
    duration_split = duration.split(":")
    dHours, dMinutes = int(duration_split[0]), int(duration_split[1])
    
    rsltH = hour+dHours
    if minutes < 60 and dMinutes < 60:
        rsltM = minutes+dMinutes
    else:
        return "Error, minutes must be less than 60"
    
    nbDays = 0
    if ending.lower() == "am":
        if rsltM < 60:
            if rsltH < 12:
                ending = "am"
            elif rsltH == 12:
                ending = "pm"
            elif rsltH > 12:
                if rsltH > 24:
                    nbDays = int(round(float(rsltH)/24.0))
                while rsltH > 24:
                    rsltH-=24
                if rsltH <= 12:
                    ending = "am"
                elif rsltH > 12:
                    rsltH-=12
                    ending = "pm"
        if rsltM > 59:
            rsltM-=60
            rsltH+=1
            if rsltH < 12:
                ending = "am"
            elif rsltH == 12:
                ending = "pm"
            elif rsltH > 12:
                if rsltH > 24:
                    nbDays = int(round(float(rsltH)/24.0))
                while rsltH > 24:
                    rsltH-=24
                if rsltH <= 12:
                    ending = "am"
                elif rsltH > 12:
                    rsltH-=12
                    ending = "pm"
        rsltM = "0"+str(rsltM) if len(str(rsltM)) < 2 else str(rsltM)
        new_time = str(rsltH)+":"+str(rsltM)+" "+ending.upper()
    elif ending.lower() == "pm":
        if rsltM < 60:
            if rsltH < 12:
                ending = "pm"
            elif rsltH == 12:
                ending = "am"
            elif rsltH > 12:
                if rsltH > 24:
                    nbDays = int(round(float(rsltH)/24.0))
                while rsltH > 24:
                    rsltH-=24
                if rsltH < 12:
                    ending = "pm"
                elif rsltH == 12:
                    ending = "am"
                elif rsltH > 12:
                    rsltH-=12
                    ending = "am"
                    if nbDays == 0:
                        nbDays = 1
        elif rsltM > 59:
            rsltM-=60
            rsltH+=1
            if rsltH < 12:
                ending = "pm"
            elif rsltH == 12:
                ending = "am"
            elif rsltH > 12:
                if rsltH > 24:
                    nbDays = int(round(float(rsltH)/24.0))
                while rsltH > 24:
                    rsltH-=24
                if rsltH < 12:
                    ending = "pm"
                elif rsltH == 12:
                    ending = "am"
                elif rsltH > 12:
                    rsltH-=12
                    ending = "am"
                    if nbDays == 0:
                        nbDays = 1
        rsltM = "0"+str(rsltM) if len(str(rsltM)) < 2 else str(rsltM)
        new_time = str(rsltH)+":"+str(rsltM)+" "+ending.upper()
    else:
        return "Error, ending must be AM or PM."
    
    if starting_day:
        starting_day = starting_day.lower().capitalize()
        if starting_day in days:
            if nbDays == 0:
                starting_day = ", "+starting_day
                new_time+=starting_day
            elif nbDays == 1:
                strtD_index = days.index(starting_day)
                nD_index = nbDays+strtD_index
                if nD_index > 6:
                    nD_index-=7
                nxtDay = ", "+days[nD_index]+" (next day)"
                new_time+=nxtDay
            elif nbDays == 2:
                strtD_index = days.index(starting_day)
                nD_index = nbDays+strtD_index
                if nD_index > 6:
                    nD_index-=7
                tD_later = ", "+days[nD_index]+" "+"(2 days later)"
                new_time+=tD_later
            elif nbDays > 2:
                strtD_index = days.index(starting_day)
                nD_index = nbDays+strtD_index
                while nD_index > 6:
                    nD_index-=7
                xD_later = ", "+days[nD_index]+" ("+str(nbDays)+" days later)"
                new_time+=xD_later
        else:
            return "Error, your starting day isn't a valid day."
    elif not starting_day:
        if nbDays == 1:
            new_time+=" (next day)"
        elif nbDays == 2:
            new_time+=" (2 days later)"
        elif nbDays > 2:
            xD_later = " ("+str(nbDays)+" days later)"
            new_time+=xD_later
    
    return new_time

print(add_time("11:59 PM", "24:05"))