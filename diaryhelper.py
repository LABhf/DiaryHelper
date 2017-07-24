import os           #operating system dependent functionality
import csv


# diaryhelper asks questions about your day in a regular interval so that you don't forget about writing your diary

        #MENU
            #ALTER QUESTIONS
                #ADD QUESTIONS
                #REMOVE QUESTIONS

q={'janta': '21', 'almoco': 14, 'geral': '22'}
#q={}
localq=q


def mainbody():
                #READ DIARY FILE
    print("     MENU")
    print("---")
    print("[1] ADD QUESTIONS")
    print("[2] REMOVE QUESTIONS")
    print("[3] UPDATE CONF. FILE")

    print("---")


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

                # Essa solução não parece ser boa, mas é um jeito de acessar a q local do addq
                # e usar ela em uma var global localq, a sintaze tbm ta confusa...

                global localq
                localq = q
                print(localq, q)

                if more == 1:
                    print("## MORE 1")
                    addq()
                elif more == 0:
                    mainbody()

            addq()

        elif a == 2:

            def rmq():
                print("WICH QUESTIONS YOU WANT TO REMOVE?")
                i = 0
                ll=[]
                for a in localq:
                    i=i+1
                    print(i,".", a)
                    ll.append(a)
                    ####

                rname = input(": ")
                rname = int(rname)
                rname = rname - 1
                ff=str(ll[rname])
                del localq[ff]
                del ll[rname]
                print(ll)

                mainbody()
            rmq()
        elif a == 3:
            print("#3 UPDATE")
            #UPDATE



            def w(q):
                with open("data.csv", "w") as f:
                    #f.write(str(print(a, localq[a])))
                    print(localq)
                    for a in localq:
                        f.write(str(a))
                        f.write(":")
                        f.write(str(localq[a]))
                        f.write(",")

            w(localq)

            print("#3 FINAL")


        else:           # This is answer filter...
            print("Choose a number between 1 and 3")
            #repeat
            answer(a)

    answer(x)

if __name__ == '__main__':
    print("#T")      #isso só vai rodar se for executado diretamente o arquivo mymath
    mainbody()

print("#EXIT")
