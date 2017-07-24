#this should run on background after GUI passed de info to data.csv file

import os
ll=[]
def r():
    with open("data.csv", "r") as f:
        # f.write(str(print(a, localq[a])))
        for a in f:
            global rr
            rr = a
r()
strings=""

ll=[]
for item in rr:
    if item != ",":
        strings=strings+item

    else:
        ll.append(strings)
        strings=""

print(ll)

i=-1
j=-1
numbers=[]
names=[]
for a in ll:

    for i in a:
        j=j+1


    """print("#number")
    print(a[j-1::])"""
    numbers.append(a[j-1::])

    """print("#part not used in the string part")
    print(a[j-2::1])
    print("@!")
    print(a[0:j-2])"""
    names.append(a[0:j-2])

    j=-1

finaldict=dict(zip(names,numbers))
print(finaldict)


