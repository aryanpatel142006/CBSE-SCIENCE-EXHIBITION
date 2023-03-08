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


for i in questions:
    if i[1]==1:
        esy.append([i[0]]+[i[2]])
    elif i[1]==2:
        med.append([i[0]]+[i[2]])
    else:
        hrd.append([i[0]]+[i[2]])
from tkinter import *
from random import *
def easy(number):
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
    win.configure(background="#FFC300")
    win.attributes('-fullscreen',True)
    index=randint(0,len(esy)-1)
    while index in random_elist:
        index=randint(0,len(esy)-1)
    que=esy[index]
    random_elist.append(index)
    questions_attempted.append(esy[index])
    Label(win,text='QUESTION '+str(number)+".",font=("Arial",30)).pack(pady=20)
    Label(win,text=que[0],font=("Arial",20)).pack(pady=20)
    easyv=StringVar()
    Entry(win,textvariable=easyv, font=("Arial",30), borderwidth=4,highlightcolor="black",highlightthickness=4,highlightbackground="black").pack(pady=20,side="bottom")
    Button(win,text = "SUBMIT", font=("Arial",30),command=submite,cursor="hand").pack(pady=20,side="bottom")
    win.mainloop()
    return n[-1]
def medium(number):
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
    win.configure(background="#FFC300")
    win.attributes('-fullscreen',True)
    index=randint(0,len(med)-1)
    while index in random_mlist:
        index=randint(0,len(med)-1)
    que=med[index]
    random_mlist.append(index)
    questions_attempted.append(med[index])
    Label(win,text='QUESTION '+str(number)+".",font=("Arial",30)).pack(pady=20)
    Label(win,text=que[0],font=("Arial",20)).pack(pady=20)
    mediumv=StringVar()

    Entry(win,textvariable=mediumv, font=("Arial",30), borderwidth=4,highlightcolor="black",highlightthickness=4,highlightbackground="black").pack(pady=20,side="bottom")
    Button(win,text='SUBMIT',font=("Arial", 30),command=submitm).pack(pady=20,side="bottom")
    win.mainloop()
    return n[-1]
def hard(number):
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
    Entry(win,textvariable=hardv, font=("Arial",30), borderwidth=4,highlightcolor="black",highlightthickness=4,highlightbackground="black").pack(pady=20,side="bottom")
    Button(win,text='SUBMIT',font=("Arial", 30),command=submith).pack(pady=20,side="bottom")
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
Label(win,text='QUIZ CANNOT BE EXITED ONCE STARTED.',font=("Arial", 65)).pack(pady=25)
Label(win,text='YOU CAN EXIT NOW IF YOU WANT TO.\n\n',font=("Arial", 45)).pack(pady=20)
Button(win,text='BEGIN',font=("Arial", 50),command=begin).pack(pady=20)
quit_image = PhotoImage(file="123.png")
Button(win,image=quit_image,command=win.destroy,).pack(pady=10)
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
    Label(win2,text='THANKYOU FOR TAKING THIS QUIZ.',font=("Arial", 60)).pack(pady=20)
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
        Label(win4,text='EASY ATTEMPTED : '+str(esyatt)).pack(pady=20)
        Label(win4,text='EASY CORRECT : '+str(esyc)).pack(pady=20)
        Label(win4,text='EASY INCORRECT : '+str(esyi)).pack(pady=20)
        Label(win4,text='MEDIUM ATTEMPTED : '+str(medatt)).pack(pady=20)
        Label(win4,text='MEDIUM CORRECT : '+str(medc)).pack(pady=20)
        Label(win4,text='MEDIUM INCORRECT : '+str(medi)).pack(pady=20)
        Label(win4,text='HARD ATTEMPTED : '+str(hrdatt)).pack(pady=20)
        Label(win4,text='HARD CORRECT : '+str(hrdc)).pack(pady=20)
        Label(win4,text='HARD INCORRECT : '+str(hrdi)).pack(pady=20)
        Button(win4,text='QUESTIONWISE ANALYSIS',font=("Arial", 30),command=win4.destroy).pack(pady=40)
        def analysemainquit():
            win4.destroy()
            lst_helper.append(0)
        Button(win4,text='QUIT',font=("Arial", 55),command=analysemainquit).pack(pady=60)
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
                Label(win,text='QUESTION '+str(num)+'.',font=("Arial",30)).pack(pady=20)
                Label(win,text='QUESTION : ').pack(pady=20)
                Label(win,text=i[0]).pack(pady=20)
                Label(win,text='CORRECT ANSWER : ').pack(pady=20)
                Label(win,text=i[1]).pack(pady=20)
                Label(win,text='YOUR ANSWER : ').pack(pady=20)
                Label(win,text=i[2]+"\n\n").pack(pady=20)
                Button(win,text='NEXT',font=("Arial", 30),command=win.destroy).pack(pady=0)
                def toquitf():
                    win.destroy()
                    toquit.append(0)
                Button(win,text='QUIT',font=("Arial", 50),command=toquitf).pack(pady=150)
                win.mainloop()
                j+=1
        try:
            if toquit[-1]:
                analyse()
        except:
            None
    score=(1*esyc)+(2*medc)+(3*hrdc)
    Label(win2,text='TOTAL SCORE : '+str(score),font=("Arial", 45)).pack(pady=150)
    Button(win2,text='OK',font=("Arial", 30),command=win2.destroy).pack(pady=10)
    Button(win2,text='PAPER ANALYSIS',font=("Arial", 30),command=analyse).pack(pady=10)
    win2.mainloop()
else:
    pass
