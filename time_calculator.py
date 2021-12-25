def add_time(start, duration, day=False): 

    list_am_pm = ["AM", "PM"]
    list_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    n_wd=''
    d_later=''
    f=0

    s_time, s_ampm = start.split()
#Get the value of the starting hour and minute
    s_hour, s_minute = (int(i) for i in s_time.split(":"))
#Get the value of the duration hour and minute
    d_hours, d_minutes = (int(i) for i in duration.split(":"))
#Calculate, make the minutes string and fill with zeros
    n_minute = (s_minute + d_minutes) % 60
    n_minute = str(n_minute).zfill(2)
#Sum the total hours
    sum_hours = s_hour + d_hours
#check the integer value of hours and minutes > 59 add 1 hour
    n_hour = (sum_hours % 12) 
    if (s_minute + d_minutes) > 59:
        a = 1                       #temporal flag
        n_hour += a
    n_hour = str(n_hour)
#Calculate the half days in order to know how many days after and if am or pm
    h_days = sum_hours 
    if (s_minute + d_minutes) > 59:
        b = 1                       #temporal flag
        h_days += b
    h_days //= 12
#Check if we started in AM or PM
    s_ampm = list_am_pm.index(s_ampm)
#Calculate the new AM, PM
    c = h_days % 2                  #temporal calculation of the halfdays
    d = (s_ampm + (c)) % 2          #temporal calculation starting value AM PM and new calculated with halfdays
    new_ampm = list_am_pm[d]   
#Calculate the days later
    if h_days > (3 - s_ampm):
        e = h_days + s_ampm         #temporal calculation add to total halfdays the value of the starting AM or PM
        f = e // 2                  #temporal calculation get the integer of the division 
        d_later = f'({f} days later)'
    elif h_days > (1 - s_ampm): 
        f = 1
        d_later = "(next day)"
#If no day selected
    new_time = f'{n_hour}:{n_minute} {new_ampm}'
#Calculate day of the week if day is added
    if (day):
        o_ind = list_days.index(day.lower().capitalize())
        g = ((o_ind + f) % 7)
        new_time += f', {list_days[g]} {d_later}'
    else :
        new_time = " ".join((new_time,d_later))

    new_time= new_time.strip()
    return new_time