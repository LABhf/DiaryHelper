
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

def delay(a):
    time.sleep(a)

def main2():
     #  Always rechecks time ...
     while True:
         for names in finaldict:
             triggers = finaldict[names]
             print(names, finaldict[names])

             global now, snow
             now = datetime.datetime.now()
             snow = now.strftime("%S")
             snow = int(snow)
             delay(0.2)
             print(snow)

             if int(triggers) == snow:
                 print(triggers)
main2()
