# diaryhelper asks questions about your day in a regular interval so that you don't forget about writing your diary

# debuging q
# q={'what did you eat today?': '21', 'what time did you get up?': '15', 'what did you do today?': '22'}

# normal q
q={}
localq = q
def mainbody():
                #READ DIARY FILE
    print("     MENU")
    print("---")
    print("[1] ADD QUESTIONS")
    print("[2] REMOVE QUESTIONS")
    print("[3] UPDATE AND EXIT")
    print("---")

    # this is a trigger for the answer() since it falls in else:
    x=55

    def answer(a):
        a = int(input("Choose: "))

        if a == 1:
            # print("#1")

            def addq():
                print('CURRENT QUESTIONS')


                print("")
                print("ADD NEW")

                qname = input("QUESTION NAME: ")
                print(qname)

                trigger= input("TRIGGER TIME: ")
                print(trigger)

                if trigger.isdigit() == False:
                    print("TRIGGER NOT AN INTEGER")
                    print("")
                    addq()

                else:
                    if int(trigger) < 1 or int(trigger) > 24:
                        print("TRIGGER SHOULD BE 1 TO 24")
                        addq()
                    else:
                        pass

                q.update({qname: trigger})

                print(q)
                print("MORE QUESTIONS?   YES=1,   NO =0 ")

                more = input(": ")

                if more.isdigit() == False:
                    print("NOT AN INTEGER SHOULD BE 1 OR 0")
                    print("")
                    more=""
                    addq()
                else:
                    pass

                more = int(more)

                # Essa solução não parece ser boa, mas é um jeito de acessar a q local do addq
                # e usar ela em uma var global localq, a sintaze tbm ta confusa...
                 
                # o problema aqui é que eu tenho que citar localq =q aqui e 
                # no inicio do programa, pra poder executar o elif == 3 
                
                global localq
                localq = q

                if more == 1:
                    print("## MORE 1")
                    addq()
                elif more == 0:
                    mainbody()

            addq()

        elif a == 2:

            def rmq():
                if localq=={}:
                    print("NO QUESTIONS ... ")
                    mainbody()
                else:
                    pass

                print("WICH QUESTIONS YOU WANT TO REMOVE?")
                i = 0
                ll=[]
                # print(localq)
                for a in localq:
                    i=i+1
                    print(i,".", a, ":", localq[a], "HOURS")
                    ll.append(a)
                    ####
                print("")
                rname = input("CHOSE A NUMBER:  ")
                rname = int(rname)
                rname = rname - 1
                ff=str(ll[rname])
                del localq[ff]
                del ll[rname]
                print(ll)

                mainbody()
            rmq()
        elif a == 3:

            def w(val):
                with open("data.csv", "w") as f:
                    #f.write(str(print(a, localq[a])))
                    print("CURRENT CONFIG FILE:")
                    print(localq)
                    print("")
                    for a in localq:
                        f.write(str(a))
                        f.write(":")
                        f.write(str(localq[a]))
                        f.write(",")

            w(localq)



        # This is answer filter...
        else:
            print("Choose a number between 1 and 3")
            #repeat
            answer(a)


    answer(x)

if __name__ == '__main__':

    mainbody()

print("EXIT")
