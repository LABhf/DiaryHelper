import datetime
import time
import os
import threading

strv=""
# Pulls data out of data.csv
def r():
    with open("data.csv", "r") as data:
        # f.write(str(print(a, localq[a])))
        for i in data:
            global strv
            strv = i

r()
# print(strv)

# filters the string from r() to a dict
def strfilter(a):
    names = []
    trigger = []
    a = a.split(",")
    for i in a:
        i = i.split(":")
        for index, z in enumerate(i):
            # print(index, z)
            if index == 0:
                names.append(z)
            elif index == 1:
                trigger.append(z)
            else:
                pass
    global finaldict
    finaldict = dict(zip(names, trigger))

strfilter(strv)

# ################################################

def delay(a):
    time.sleep(a)

def warnf(a, b):
        # 'a' is a_trigger and 'b' is a_name
        print("warnf was exectd")
        print(finaldict)
        print("trigger is ", a, "its name is ", b, "time of warnf, eq = snow +1 ", snow)



#     compare the timev with the trigger list from finaldict
# after that it couldse if thw timev is changed if it is exec warn.py


#     marks a second data.csv file execs the warn.py and
def time_update():
    global now, snow
    now = datetime.datetime.now()
    snow = now.strftime("%S")
    snow = int(snow)

def main2():

     #  Always rechecks time ...
     while True:
         for a_name in finaldict:
             a_trigger = finaldict[a_name]
             a_trigger = int(a_trigger)
             # triggers separation

             # time variables statements of time_update function
             time_update()


             # faster delay to see repetition of if == warn loop
             delay(0.02)
             # time debug

             print(snow)

             # a_trigger and time verification
             if (int(a_trigger)-1) == snow:
                 time_update()

                 while (int(a_trigger)-1) == snow:
                     time_update()
                     # print("first block, ==", snow)

                     if (int(a_trigger)-1) !=snow:
                         time_update()
                         print("Second block !=", "START WARNF()")
                         warnf(a_trigger, a_name)
                         print("close != loop")

main2()
