from gtts import gTTS
from pyttsx3 import *
from tkinter import *
from random import *
import playsound
import mysql.connector as my



def new_questions(password):
    if password=='bhavans':
        a=my.connect(host='localhost',user='root',passwd='Aryan@123',database='csproject_bhavans')
        c=a.cursor()
        for i in range(int(input('NUMBER OF QUESTIONS : '))):
            q=input('QUESTION '+str(i+1)+" : ")
            o1='A : '+input('OPTION A : ')
            o2='B : '+input('OPTION B : ')
            o3='C : '+input('OPTION C : ')
            o4='D : '+input('OPTION D : ')
            l=input('LEVEL : ')
            an=input('ANSWER : ')
            que=q+'\n\n\n'+o1+'\n\n\n'+o2+'\n\n\n'+o3+'\n\n\n'+o4
            query='insert into questions values("'+que+'",'+l+',"'+an+'")'
            c.execute(query)
            a.commit()
    else:
        print('UNAUTHORISED USER')
v1=input('DO YOU WANT TO INPUT NEW QUESTIONS ? : ')
if v1.lower()=='no':
    pass
else:
    v2=input('ENTER PASSWORD : ')
    new_questions(v2)
questions=[]
a=my.connect(host='localhost',user='root',passwd='Aryan@123',database='csproject_bhavans')
c=a.cursor()
c.execute('select * from questions')
for i in c:
    questions.append(i)
questions_attempted=[]
random_elist=[]
random_mlist=[]
random_hlist=[]
esy=[]
med=[]
hrd=[]
user_score_e=[]
user_score_m=[]
user_score_h=[]

# This is the dictonay for hindi
Questions_Dictonary = {"A mother is twice as old as her son. If 20 years ago, the age of the mother was 10 times the age of the son, what is the present age of the mother?" : "Q1", "A train moving at speed of 80 km/hr crosses a pole in 7 seconds. Find the length of the train." : "Q2", "If Suresh borrows Rs. 36000 from Mahesh at rate of interest 6% S.I, at the end of four years how much interest Suresh has to pay along with principal amount?":"Q3","A shopkeeper sold an article for Rs. 2500. If the cost price of the article is 2000, find the profit percent?": "Q4", "A running man crosses a bridge of length 500 meters in 4 minutes. At what speed he is running?":"Q5","The speed of a boat in still water is 5km/hr. If the speed of the boat against the stream is 3 km/hr, what is the speed of the stream?": "Q6","How many times the hands of a clock coincide in a day?":"Q7","Two ships are sailing in the sea on the two sides of a lighthouse. The angles of elevation of the top of the lighthouse observed from the ships are 30° and 45° respectively. If the lighthouse is 100m high, find the distance between the two ships?":"Q8","Worker A completes a task in 8 days and worker B completes the same task in 10 days. If both A and B work together, in how many days they will complete the task?":"Q9","If(A×B)means A is to south of B ; (A+B) means A is to the north of B ;(A%B) means A is to the east of B ; (A – B) means A is to west of B, then in (P % Q + R – S), S is in which direction with respect to Q ?":"Q10","In a code, CORNER is written as GSVRIV. How can CENTRAL be written in that code?":"Q11","Amir was born on Feb 29th of 2012 which was a Wednesday. If he lives to be 101 years old, how many birthdays would he celebrate on a Wednesday?":"Q12","Introducing a man, a woman said, He is the only son of my mother's mother. How is the woman related to the man ?":"Q13","Introducing a man, Neeraj said, His wife is the only daughter of my wife. How is Neeraj related to that man?":"Q14","What should come in the place of question mark (?) in the following alpha-numeric series? C-3, E-5, G-7, I-9, ?, ?":"Q15","A clock which gains 10 minutes in 24 hours, is set right at 12 AM. What will be the true time when the clock indicates 5 AM on the following day?":"Q16","A clock is started at noon. By 10 min past 5, the hour hand has turned through :":"Q17","The year next to 1896 that will have the same calendar as that of the year 1896 : ":"Q18","Some equal cubes are arranged in the form of a solid block. All the visible surfaces of the block (except bottom) are then painted.How many cubes do not have any of the faces painted?":"Q19","If REASON is coded as 5 and BELIEVED as 7, then what is the code for GOVERNMENT":"Q20","If the English letters A to Z are written in a reverse order then what is the fourth letter to the right of 12th letter from the left ?":"Q21","A train running at a speed of 40 m/s crosses a pole in 21 sec less than the time it requires to cross a bridge 3.5 times its length at the same speed. What is the length of the bridge?":"Q22","Insert the missing number in the sequence 8, 24, 12, 36, 18, 54, …":"Q23","Which word is opposite in meaning to SIGNIFICANT ?":"Q24","Total area of 64 small squares of a chess board is 400cm. There is 3 cm wide border around the chess board. What is the length of the side of the chess board?":"Q25","A man ate 100 bananas in five days, each day eating 6 more than the previous day. How many bananas did he eat on the first day?":"Q26","Six roads lead to a country. They may be indicated by letters X, Y, Z and digits 1, 2, 3. When there is storm, Y is blocked. When there are floods, X, 1 and 2 will be affected. When road 1 is blocked, Z also is blocked. At a time when there are floods and a storm also blows, which road(s) can be used?":"Q27","From 5 different green balls, four different blue balls and three different red balls, how many combinations of balls can be chosen taking at least one green and one blue ball?":"Q28","Kailash remembers that his brother Deepak’s birthday falls after 20th May but before 28th May, while Geeta remembers that Deepak’s birthday falls before 22nd May but after 12th May. On what date Deepak’s birthday falls?":"Q29","If 2x – y = 4 then 6x – 3y = ?":"Q30"}


for i in questions:
    if i[1]==1:
        i=list(i)
        esyi=list(i[0])
        ind=esyi.index('\n')
        esyinew=esyi[:ind]
        esyinew2=esyi[ind:]
        esyi=esyinew+esyinew2
        que=''
        for j in esyi:
            j=str(j)
            que+=j
        i[0]=que
        esy.append([i[0]]+[i[2]])
    elif i[1]==2:
        i=list(i)
        medi = list(i[0])
        ind = medi.index('\n')
        medinew = esyi[:ind]
        medinew2 = esyi[ind:]
        medi = medinew + medinew2
        que = ''
        for j in medi:
            j = str(j)
            que += j
        i[0] = que
        med.append([i[0]] + [i[2]])
    else:
        i=list(i)
        hrdi = list(i[0])
        ind = hrdi.index('\n')
        hrdinew = hrdi[:ind]
        hrdinew2 = hrdi[ind:]
        hrdi = hrdinew + hrdinew2
        que = ''
        for j in hrdi:
            j = str(j)
            que += j
        i[0] = que
        hrd.append([i[0]] + [i[2]])
def easy(number):
    def speaking():
        a = que[0]
        for i in Questions_Dictonary.keys():
            if i in a:
                x = Questions_Dictonary[i]
                x += ".mp3"
                print(x)
                playsound.playsound(x, True)

    def submite():
        ans=easyv.get().upper()
        questions_attempted[-1]+=[ans]
        if ans==que[1]:
            user_score_e.append(1)
            n.append(1)
        else:
            user_score_e.append(0)
        win.destroy()
    n=[0]
    win=Tk()





    win.title('QUIZ')
    win.configure(background="#45B39D")
    win.attributes('-fullscreen',True)
    index=randint(0,len(esy)-1)
    while index in random_elist:
        index=randint(0,len(esy)-1)
    que=esy[index]
    random_elist.append(index)
    questions_attempted.append(esy[index])

    Label(win,text='QUESTION '+str(number),font=("Arial",30)).pack(pady=20)
    Label(win,text=que[0],font=("Arial",20)).pack(pady=20)
    easyv=StringVar()
    Entry(win,textvariable=easyv, font=("Arial",35), borderwidth=4,highlightcolor="black",highlightthickness=4,highlightbackground="black").pack(pady=20,side="bottom")
    #Button(win,text = "SUBMIT", font=("Arial",40),command=submite,cursor="hand").pack(pady=20,side="bottom")
    #Button(win, text="Speak Question", font=("Arial", 40), command=speaking, cursor="hand").pack(pady=20, side="left")

    question_submit = PhotoImage(file="question submit.png")
    Button(win, image=question_submit, command=submite, cursor="hand").pack(pady=10, side="bottom")

    speak_image = PhotoImage(file="speaker.png")
    Button(win, image=speak_image, command=speaking, cursor="hand").pack(pady=10, side="left")




    win.mainloop()
    return n[-1]
def medium(number):
    def speaking():
        a = que[0]
        for i in Questions_Dictonary.keys():
            if i in a:
                x = Questions_Dictonary[i]
                x += ".mp3"
                print(x)
                playsound.playsound(x, True)
    def submitm():
        ans=mediumv.get().upper()
        questions_attempted[-1]+=[ans]
        if ans==que[1]:
            user_score_m.append(1)
            n.append(1)
        else:
            user_score_m.append(0)
        win.destroy()
    n=[0]
    win=Tk()
    win.title('QUIZ')
    win.configure(background="#45B39D")
    win.attributes('-fullscreen',True)
    index=randint(0,len(med)-1)
    while index in random_mlist:
        index=randint(0,len(med)-1)
    que=med[index]
    random_mlist.append(index)
    questions_attempted.append(med[index])
    Label(win,text='QUESTION '+str(number),font=("Arial",30)).pack(pady=20)
    Label(win,text=que[0],font=("Arial",20)).pack(pady=20)
    mediumv=StringVar()

    Entry(win,textvariable=mediumv, font=("Arial",35), borderwidth=4,highlightcolor="black",highlightthickness=4,highlightbackground="black").pack(pady=20,side="bottom")
    #Button(win,text='SUBMIT',font=("Arial", 40),command=submitm).pack(pady=20,side="bottom")
    question_submit = PhotoImage(file="question submit.png")
    Button(win, image=question_submit, command=submitm,cursor = "hand" ).pack(pady=10,side="bottom")
    #Button(win, text="🔊" + "Speak Question", font=("Arial", 40), command=speaking, cursor="hand").pack(pady=20, side="left")
    speak_image = PhotoImage(file="speaker.png")
    Button(win, image=speak_image, command=speaking,cursor = "hand" ).pack(pady=10, side = "left")
    win.mainloop()
    return n[-1]
def hard(number):
    def speaking():
        a = que[0]
        for i in Questions_Dictonary.keys():
            if i in a:
                x = Questions_Dictonary[i]
                x += ".mp3"
                print(x)
                playsound.playsound(x, True)
    def submith():
        ans=hardv.get().upper()
        questions_attempted[-1]+=[ans]
        if ans==que[1]:
            user_score_h.append(1)
            n.append(1)
        else:
            user_score_h.append(0)
        win.destroy()
    n=[0]
    win=Tk()
    win.title('QUIZ')
    win.attributes('-fullscreen',True)
    index=randint(0,len(hrd)-1)
    while index in random_hlist:
        index=randint(0,len(hrd)-1)
    que=hrd[index]
    random_hlist.append(index)
    questions_attempted.append(hrd[index])
    Label(win,text='QUESTION '+str(number)+".",font=("Arial",30)).pack(pady=20)
    Label(win,text=que[0],font=("Arial",20)).pack(pady=20)
    hardv=StringVar()
    Entry(win,textvariable=hardv, font=("Arial",35), borderwidth=4,highlightcolor="black",highlightthickness=4,highlightbackground="black").pack(pady=20,side="bottom")
    #Button(win,text='SUBMIT',font=("Arial", 40),command=submith).pack(pady=20,side="bottom")
    #Button(win, text="Speak Question", font=("Arial", 40), command=speaking, cursor="hand").pack(pady=20, side="left")

    question_submit = PhotoImage(file="question submit.png")
    Button(win, image=question_submit, command=submith, cursor="hand" ).pack(pady=10, side="bottom")

    speak_image = PhotoImage(file="speaker.png")
    Button(win, image=speak_image, command=speaking, cursor="hand" ).pack(pady=10, side="left")


    win.mainloop()
    return n[-1]
def begin():
    check.append(1)
    win.destroy()
check=[0]
win=Tk()
win.title('QUIZ')
win.attributes('-fullscreen',True)
win.attributes('-fullscreen',True)
Label(win,text='QUIZ CANNOT BE EXITED ONCE STARTED',font=("Arial", 65),fg = "#FF0000").pack(pady=25)
Label(win,text='YOU CAN EXIT NOW IF YOU WANT TO\n\n',font=("Arial", 45)).pack(pady=20)
#Button(win,text='BEGIN',font=("Arial", 50),command=begin).pack(pady=20)

start_image = PhotoImage(file="start button.png")
Button(win,image=start_image,command=begin,).pack(pady=10)

Label(win,text='\n\n',font=("Arial", 45)).pack(pady=20)

quit_image = PhotoImage(file="exit red and white.png")
Label(win,text='\n\n\n\n\n\n\n\nDeveloped By: Aryan Patel & Aryan Vasvaria',font=("Arial", 15)).pack(side="right")
Label(win,text='''


                                                                           ''',font=("Arial", 15)).pack(side="left")

Button(win,image=quit_image,command=win.destroy).pack(pady=10,side="right")

win.mainloop()
if check[-1]:
    one=medium(1)
    two=medium(2)
    if one and two:
        three=hard(3)
        four=hard(4)
        if three and four:
            five=hard(5)
            six=hard(6)
            if five and six:
                seven=hard(7)
                eight=hard(8)
                if seven and eight:
                    nine=hard(9)
                    ten=hard(10)
                elif seven or eight:
                    nine=hard(9)
                    ten=hard(10)
                else:
                    nine=medium(9)
                    ten=medium(10)
            elif five or six:
                seven=hard(7)
                eight=hard(8)
                if seven and eight:
                    nine=hard(9)
                    ten=hard(10)
                elif seven or eight:
                    nine=hard(9)
                    ten=hard(10)
                else:
                    nine=medium(9)
                    ten=medium(10)
            else:
                seven=medium(7)
                eight=medium(8)
                if seven and eight:
                    nine=hard(9)
                    ten=hard(10)
                elif seven or eight:
                    nine=medium(9)
                    ten=medium(10)
                else:
                    nine=easy(9)
                    ten=easy(10)
        elif three or four:
            five=hard(5)
            six=hard(6)
            if five and six:
                seven=hard(7)
                eight=hard(8)
                if seven and eight:
                    nine=hard(9)
                    ten=hard(10)
                elif seven or eight:
                    nine=hard(9)
                    ten=hard(10)
                else:
                    nine=medium(9)
                    ten=medium(10)
            elif five or six:
                seven=hard(7)
                eight=hard(8)
                if seven and eight:
                    nine=hard(9)
                    ten=hard(10)
                elif seven or eight:
                    nine=hard(9)
                    ten=hard(10)
                else:
                    nine=medium(9)
                    ten=medium(10)
            else:
                seven=medium(7)
                eight=medium(8)
                if seven and eight:
                    nine=hard(9)
                    ten=hard(10)
                elif seven or eight:
                    nine=medium(9)
                    ten=medium(10)
                else:
                    nine=easy(9)
                    ten=easy(10)
        else:
            five=medium(5)
            six=medium(6)
            if five and six:
                seven=hard(7)
                eight=hard(8)
                if seven and eight:
                    nine=hard(9)
                    ten=hard(10)
                elif seven or eight:
                    nine=hard(9)
                    ten=hard(10)
                else:
                    nine=medium(9)
                    ten=medium(10)
            elif five or six:
                seven=medium(7)
                eight=medium(8)
                if seven and eight:
                    nine=hard(9)
                    ten=hard(10)
                elif seven or eight:
                    nine=medium(9)
                    ten=medium(10)
                else:
                    nine=easy(9)
                    ten=easy(10)
            else:
                seven=easy(7)
                eight=easy(8)
                if seven and eight:
                    nine=medium(9)
                    ten=medium(10)
                elif seven or eight:
                    nine=easy(9)
                    ten=easy(10)
                else:
                    nine=easy(9)
                    ten=easy(10)
    elif one or two:
        three=medium(3)
        four=medium(4)
        if three and four:
            five=hard(5)
            six=hard(6)
            if five and six:
                seven=hard(7)
                eight=hard(8)
                if seven and eight:
                    nine=hard(9)
                    ten=hard(10)
                elif seven or eight:
                    nine=hard(9)
                    ten=hard(10)
                else:
                    nine=medium(9)
                    ten=medium(10)
            elif five or six:
                seven=hard(7)
                eight=hard(8)
                if seven and eight:
                    nine=hard(9)
                    ten=hard(10)
                elif seven or eight:
                    nine=hard(9)
                    ten=hard(10)
                else:
                    nine=medium(9)
                    ten=medium(10)
            else:
                seven=medium(7)
                eight=medium(8)
                if seven and eight:
                    nine=hard(9)
                    ten=hard(10)
                elif seven or eight:
                    nine=medium(9)
                    ten=medium(10)
                else:
                    nine=easy(9)
                    ten=easy(10)
        elif three or four:
            five=medium(5)
            six=medium(6)
            if five and six:
                seven=hard(7)
                eight=hard(8)
                if seven and eight:
                    nine=hard(9)
                    ten=hard(10)
                elif seven or eight:
                    nine=hard(9)
                    ten=hard(10)
                else:
                    nine=medium(9)
                    ten=medium(10)
            elif five or six:
                seven=medium(7)
                eight=medium(8)
                if seven and eight:
                    nine=hard(9)
                    ten=hard(10)
                elif seven or eight:
                    nine=medium(9)
                    ten=medium(10)
                else:
                    nine=easy(9)
                    ten=easy(10)
            else:
                seven=easy(7)
                eight=easy(8)
                if seven and eight:
                    nine=medium(9)
                    ten=medium(10)
                elif seven or eight:
                    nine=easy(9)
                    ten=easy(10)
                else:
                    nine=easy(9)
                    ten=easy(10)
        else:
            five=easy(5)
            six=easy(6)
            if five and six:
                seven=medium(7)
                eight=medium(8)
                if seven and eight:
                    nine=hard(9)
                    ten=hard(10)
                elif seven or eight:
                    nine=medium(9)
                    ten=medium(10)
                else:
                    nine=easy(9)
                    ten=easy(10)
            elif five or six:
                seven=easy(7)
                eight=easy(8)
                if seven and eight:
                    nine=medium(9)
                    ten=medium(10)
                else:
                    nine=easy(9)
                    ten=easy(10)
            else:
                seven=easy(7)
                eight=easy(8)
                if seven and eight:
                    nine=medium(9)
                    ten=medium(10)
                else:
                    nine=easy(9)
                    ten=easy(10)
    else:
        three=easy(3)
        four=easy(4)
        if three and four:
            five=medium(5)
            six=medium(6)
            if five and six:
                seven=hard(7)
                eight=hard(8)
                if seven and eight:
                    nine=hard(9)
                    ten=hard(10)
                elif seven or eight:
                    nine=hard(9)
                    ten=hard(10)
                else:
                    nine=medium(9)
                    ten=medium(10)
            elif five or six:
                seven=medium(7)
                eight=medium(8)
                if seven and eight:
                    nine=hard(9)
                    ten=hard(10)
                elif seven or eight:
                    nine=medium(9)
                    ten=medium(10)
                else:
                    nine=easy(9)
                    ten=easy(10)
            else:
                seven=easy(7)
                eight=easy(8)
                if seven and eight:
                    nine=medium(9)
                    ten=medium(10)
                else:
                    nine=easy(9)
                    ten=easy(10)
        elif three or four:
            five=easy(5)
            six=easy(6)
            if five and six:
                seven=medium(7)
                eight=medium(8)
                if seven and eight:
                    nine=hard(9)
                    ten=hard(10)
                elif seven or eight:
                    nine=medium(9)
                    ten=medium(10)
                else:
                    nine=easy(9)
                    ten=easy(10)
            elif five or six:
                seven=easy(7)
                eight=easy(8)
                if seven and eight:
                    nine=medium(9)
                    ten=medium(10)
                else:
                    nine=easy(9)
                    ten=easy(10)
            else:
                seven=easy(7)
                eight=easy(8)
                if seven and eight:
                    nine=medium(9)
                    ten=medium(10)
                else:
                    nine=easy(9)
                    ten=easy(10)
        else:
            five=easy(5)
            six=easy(6)
            if five and six:
                seven=medium(7)
                eight=medium(8)
                if seven and eight:
                    nine=hard(9)
                    ten=hard(10)
                elif seven or eight:
                    nine=medium(9)
                    ten=medium(10)
                else:
                    nine=easy(9)
                    ten=easy(10)
            elif five or six:
                seven=easy(7)
                eight=easy(8)
                if seven and eight:
                    nine=medium(9)
                    ten=medium(10)
                else:
                    nine=easy(9)
                    ten=easy(10)
            else:
                seven=easy(7)
                eight=easy(8)
                if seven and eight:
                    nine=medium(9)
                    ten=medium(10)
                else:
                    nine=easy(9)
                    ten=easy(10)
    win2=Tk()
    win2.title('RESULT')
    win2.attributes('-fullscreen',True)
    Label(win2,text='THANK YOU FOR TAKING THIS QUIZ.',font=("Arial", 60)).pack(pady=20)
    Label(win2,text=' YOUR RESULTS ARE AS FOLLOWS : ',font=("Arial", 35)).pack(pady=5)
    esyatt=0
    medatt=0
    hrdatt=0
    esyc=0
    medc=0
    hrdc=0
    esyi=0
    medi=0
    hrdi=0
    for i in user_score_e:
        esyatt+=1
        if i:
            esyc+=1
        else:
            esyi+=1
    for i in user_score_m:
        medatt+=1
        if i:
            medc+=1
        else:
            medi+=1
    for i in user_score_h:
        hrdatt+=1
        if i:
            hrdc+=1
        else:
            hrdi+=1
    def analyse():
        try:
            win2.destroy()
        except:
            pass
        lst_helper=[1]
        win4=Tk()
        win4.attributes('-fullscreen',True)
        Label(win4,text='    EASY ATTEMPTED           :     '+str(esyatt),font=("Arial", 20)).pack(pady=20)
        Label(win4,text='    EASY CORRECT               :     '+str(esyc),font=("Arial", 20)).pack(pady=20)
        Label(win4,text='    EASY INCORRECT            :     '+str(esyi),font=("Arial", 20)).pack(pady=20)
        Label(win4,text='   MEDIUM ATTEMPTED       :     '+str(medatt),font=("Arial", 20)).pack(pady=20)
        Label(win4,text='   MEDIUM CORRECT           :     '+str(medc),font=("Arial", 20)).pack(pady=20)
        Label(win4,text='  MEDIUM INCORRECT        :     '+str(medi),font=("Arial", 20)).pack(pady=20)
        Label(win4,text='  HARD ATTEMPTED           :     '+str(hrdatt),font=("Arial", 20)).pack(pady=20)
        Label(win4,text='   HARD CORRECT              :     '+str(hrdc),font=("Arial", 20)).pack(pady=20)
        Label(win4,text='  HARD INCORRECT           :     '+str(hrdi),font=("Arial", 20)).pack(pady=20)
        Button(win4,text='QUESTIONWISE ANALYSIS',font=("Arial", 30),command=win4.destroy).pack(pady=15)
        def analysemainquit():
            win4.destroy()
            lst_helper.append(0)
        #Button(win4,text='QUIT',font=("Arial", 55),command=analysemainquit).pack(pady=60)

        quit_image = PhotoImage(file="exit red and white.png")
        Button(win4, image=quit_image, command=analysemainquit, ).pack(pady=10)

        win4.mainloop()
        if lst_helper[-1]:
            toquit=[1]
            j=0
            while j<len(questions_attempted) and toquit[-1]:
                i=questions_attempted[j]
                win=Tk()
                win.title('PAPER ANALYSIS')
                toquitl=[0]
                win.attributes('-fullscreen',True)
                num=j+1
                Label(win,text='QUESTION '+str(num)+'.',font=("Arial", 30)).pack(pady=20)
                Label(win,text=i[0],font=("Arial", 20)).pack(pady=20)
                Label(win,text='CORRECT ANSWER : ',font=("Arial", 20)).pack(pady=20)
                Label(win,text=i[1],font=("Arial", 20)).pack(pady=20)
                Label(win,text='YOUR ANSWER : ',font=("Arial", 20)).pack(pady=20)
                Label(win,text=i[2]+"\n\n",font=("Arial", 20)).pack(pady=20)
                #Button(win,text='NEXT',font=("Arial", 30),command=win.destroy).pack(pady=0)
                next_image = PhotoImage(file="next.png")
                Button(win, image=next_image, command=win.destroy, ).pack()
                def toquitf():
                    win.destroy()
                    toquit.append(0)
                #Button(win,text='QUIT',font=("Arial", 50),command=toquitf).pack(pady=150)
                quit_image = PhotoImage(file="exit red and white.png")
                Button(win, image=quit_image, command=toquitf).pack(pady=10,side = "right")

                win.mainloop()
                j+=1
        try:
            if toquit[-1]:
                analyse()
        except:
            None
    score=(1*esyc)+(2*medc)+(3*hrdc)
    def paper_score():
        playsound.playsound("final_score.mp3")
    Button(win2, text='Speak Score', font=("Arial", 65), command=paper_score, cursor = "hand").pack(pady=0,side = "left")

    Label(win2,text='TOTAL SCORE : '+str(score)+"                       ",font=("Arial", 45)).pack(pady=150)

    Label(win2, text="                       ", font=("Arial", 45)).pack(pady=150,side = "right")

    #Button(win2,text='OK',font=("Arial", 30),command=win2.destroy).pack(pady=10)


    ok_exit_image = PhotoImage(file="ok.png")
    Button(win2, image=ok_exit_image, command=win2.destroy, ).pack(pady=10)

    Button(win2,text='PAPER ANALYSIS',font=("Arial", 30),command=analyse).pack(pady=10)
    final_score = 'कुल स्कोर: ' + str(score) + "है"
    obj = gTTS(text=final_score, slow=False, lang='hi')
    obj.save('final_score.mp3')



    win2.mainloop()
else:
    pass