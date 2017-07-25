
# Pulls data out of data.csv
def r():
    with open("data.csv", "r") as data:
        # f.write(str(print(a, localq[a])))
        for i in data:
            global strv
            strv = i

r()

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
print(finaldict)

# Pulls data out of data.csv
def r():
    with open("data.csv", "r") as data:
        # f.write(str(print(a, localq[a])))
        for i in data:
            global strv
            strv = i

r()

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
print(finaldict)

#########################
#define the trigger while/function to open the warn.py file
