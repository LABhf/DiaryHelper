#this file should come after the bgprocess to show the questions in the time defined in trigger from the tempdata.csv temporary file
#it should not open more than once for the same question
#it should open a prompt ask the question, retrieve info and add it to the major diary.txt file.
#And then clean the datatemp file
import os
strv=""
# debug strv
strv= "almoco"
def mainbody():
    # print("test")

    def r():
        with open("tempdata.csv", "r") as data:
            # f.write(str(print(a, localq[a])))
            for i in data:
                global strv
                strv = i



    r()
    # remove file and recreat it, to delete all data for next bgprocess
    # strv variable is already stored in warn.py
    os.remove("tempdata.csv")
    open('tempdata.csv', 'w+')
   
    print("")
    print("DIARYHELPER MENU")
    print("     QUESTION IS:", strv)
    print("[1] ANSWER QUESTION:")
    print("[2] EXIT WITHOUT ANSWERING")
    # a() is the answer
    def a():
        try:
            # ma = menu answer
            ma = input(":")
            ma = int(ma)
            b = ma - 1
        except:
            print("numbers only")
            a()

        if ma == 1:
                print("#1")
        #        -w to diary file


        elif ma == 2:
                print("#2")
                pass
        else:
            print("SHOULD BE 1 OR 2")
            a()
    a()



if __name__ == '__main__':
    mainbody()
