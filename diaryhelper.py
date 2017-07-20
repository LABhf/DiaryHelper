# diaryhelper asks questions about your day in a regular interval so that you don't forget about writing your diary

        #MENU
            #ALTER QUESTIONS
                #ADD QUESTIONS
                #REMOVE QUESTIONS
def mainbody():
                #READ DIARY FILE
    print("     MENU")
    print("---")
    print("[1] ADD QUESTIONS")
    print("[2] REMOVE QUESTIONS")
    print("[3] READ DIARY FILE")
    print("---")


    #dict = {'Almoço': '15' , 'janta': '21' }
    #print(dict)
    #print(dict["janta"])
    #for a in dict:
    #    print(a)

    q={}
    #for debug >
    #q={'janta': '21', 'almoco': 14, 'geral': '22'}      
    x=55


    def answer(a):
        a = int(input("Choose: "))

        if a == 1:
            print("#1")

            def addq():
                print('CURRENT QUESTIONS')


                print("")
                print("ADD NEW")

                qname = input("QUESTION NAME: ")
                print(qname)
                trigger= input("TRIGGER TIME: ")
                print(trigger)

                q.update({qname: trigger})

                print(q)
                print("MORE QUESTIONS?   YES=1,   NO =0 ")
                more = input(": ")
                more = int(more)

                if more == 1:
                    print("## MORE 1")
                    addq()
                elif more == 0:
                    mainbody()

            addq()

            if more == 1:
                addq()
        elif a == 2:

            def rmq():
                print("WICH QUESTIONS YOU WANT TO REMOVE?")
                i = 0
                ll=[]
                for a in q:
                    i=i+1
                    print(i,".", a)
                    ll.append(a)
                    ####

                rname = input(": ")
                rname = int(rname)
                rname = rname - 1
                ff=str(ll[rname])
                del q[ff]
                del ll[rname]
                print(ll)

                mainbody()
            rmq()
        elif a == 3:
            print("#3")
            #read doc

        else:
            print("Choose a number between 1 and 3")
            #repeat
            answer(a)

    answer(x)

if __name__ == '__main__':
    print("#T")      #isso só vai rodar se for executado diretamente o arquivo mymath
    mainbody()

print("#EXIT")
