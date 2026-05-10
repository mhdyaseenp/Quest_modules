# import datetime
# datetime.datetime.now



from datetime import *

# print("Current date and time :",datetime.now())             #print current time and date

# print(date.today())                                         #current date
# print(datetime.now().year)                                  #curren year
# print(datetime.now().month)                                 #curren month
# print(datetime.now().day)                                   #curren day

# print(datetime.now().time())                                #curren time
# print(datetime.now().hour)                                  #curren hour
# print(datetime.now().minute)                                #curren minuts
# print(datetime.now().second)                                #curren second
# print(datetime.now().microsecond)                           #curren microsecond


# dt=datetime.now()
# print(dt)
# print()

# print("%Y    ->",dt.strftime("%Y"))                          #year full ,           Eg 2026
# print("%y    ->",dt.strftime("%y"))                          #year sort ,           Eg 26
# print("%m    ->",dt.strftime("m"))                           #month number ,        Eg 5
# print("%B    ->",dt.strftime("%B"))                          #Month name Full ,     Eg May
# print("%b    ->",dt.strftime("%b"))                          #Month name sort ,     Eg May       
# print("%d    ->",dt.strftime("%d"))                          #Day of month  ,       Eg 07#
# print("%A    ->",dt.strftime("%A"))                          #Week Day (full ),     Eg Thursday 
# print("%a    ->",dt.strftime("%a"))                          #Week day (sort)  ,    Eg 2026
# print("%H    ->",dt.strftime("%H"))                          #Hour (24-hr)
# print("%I    ->",dt.strftime("%I"))                          #Hour (12-hr).    
# print("%p    ->",dt.strftime("%p"))                          #Hour (am/pm)          Eg: am
# print("%M    ->",dt.strftime("%M"))                          #Minuts                Eg: 54
# print("%S    ->",dt.strftime("%S"))                          #Second                Eg: 34
# print("%f    ->",dt.strftime("%f"))                          #Micro second.         Eg:768344
# print("%z    ->",dt.strftime("%z"))                          #UTF offset
# print("%Z    ->",dt.strftime("%Z"))                          #Time zone name
# print("%j    ->",dt.strftime("%j"))                          #Day of year.                  Eg:127
# print("%U    ->",dt.strftime("%U"))                          #Week of number(sunday first)  Eg:18
# print("%W    ->",dt.strftime("%W"))                          #Week of number(monday first)  Eg:18
# print("%c    ->",dt.strftime("%c"))                          #Local date and time      Eg:Thu May  7 11:59:38 2026
# print("%x    ->",dt.strftime("%x"))                          #Local date               Eg:05/07/26
# print("%X    ->",dt.strftime("%X"))                          #Local Time               Eg:11:59:38


# data=datetime(2002,8,25)
# print(data)


# after & days
# today=datetime.today()
# print(today)
# after_7=today + timedelta(days=7)
# # after_7=today + timedelta(days=7,hours=21,minutes=23,weeks=3)
# print(after_7)

# before & days
# today=datetime.today()
# print(today)
# before_7=today - timedelta(days=7)
# after_7=today + timedelta(days=7,hours=21,minutes=23,weeks=3)
# print(before_7)


# print your age p 
# data=datetime(2005,5,13)
# print(data)
# now=datetime.today()
# cur=now - data
# age=cur/365
# print(age.days)