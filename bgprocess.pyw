
def r():
    with open("data.csv", "r") as f:
        for a in f:
            return a

bb = r().split(",")
j=0
names=[]
numbers=[]

#Continuar usando essa função é bem mais facil, da pra corrigir o diaryhelper tbm usando ela...
#https://www.tutorialspoint.com/python/string_split.htm
