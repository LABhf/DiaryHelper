
import datetime
import time
import os
import threading
now=""
snow=""
timev=""
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


def main2():

    def delay(a):
        time.sleep(a)

    def timef():
        #  Always rechecks time ...
        while True:
            global now, snow
            now = datetime.datetime.now()
            snow = now.strftime("%S")
            snow = int(snow)
            delay(0.2)
            print(snow)


    def trigger():

        # if the timev, timev format, variable is equal to the trigger variable then
        # it will check -r in the triggers list to see if timev == triggers
        global now, snow, timev
        print(snow)
        timev = snow+3
        print("init snow is ", snow)
        print("timev is ", timev)

        # Main2 loop
        while True:

            for names in finaldict:
                triggers = finaldict[names]
                triggers = int(triggers)

                if int(triggers) == int(timev):
                    print("start warn.py")
        #             exec warn.py


    s_thread = threading.Thread(target=timef, name="Second Thread / ##")
    # START TRIGGER()
    s_thread.start()
    trigger()

main2()
