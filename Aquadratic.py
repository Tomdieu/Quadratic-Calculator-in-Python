import tkinter,os,sys,random
from tkinter import *
from tkinter.constants import *
from tkinter.messagebox import showinfo,_show,showerror,askquestion
from math import *
import cmath
import time
from time import sleep
left=right=False
p=n=s=q=0
co=[0,1]
print(len(co))
def display():

    def clr():
        for i in Quad.winfo_children():
            i.destroy()
        display()
    def x_sol():
        ls1.config(text='')
        ls.config(text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n',bg='skyblue')
    def qu():
        ls.config(text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n',bg='skyblue')

    def eva():
        Button(right_fram2, text='Show solution', fg='blue', bd=3, font=('consolas', 10), activeforeground='red',
               command=solution).grid(row=0, column=0, padx=5)
        global x1, x2
        a = E1.get()
        b = E2.get()
        c = E3.get()
        if a == '' and b != '' and c != '':
            showerror('INCOMPLETE INPUT', 'You Must Enter the value of a')
        elif b == '' and a != '' and c != '':
            showerror('INCOMPLETE INPUT', 'You Must Enter the Value of b')
        elif c == '' and a != '' and b != '':
            showerror('INCOMPLETE INPUT', 'You Must Enter the Value of c')
        elif a != '' and b == '' and c == '':
            showerror('INCOMPLETE INPUT', 'You Must Enter The Value Of b and c')
        elif a == '' and b != '' and c == '':
            showerror('INCOMPLETE INPUT', 'You Must Enter The Value Of a and c')
        elif a == '' and b == '' and c != '':
            showerror('INCOMPLETE INPUT', 'You Must Enter The Value Of a and b')
        elif a == '' or b == '' or c == '':
            showerror('INCOMPLETE INPUT', 'You Must Enter All The Entry')
        else:
            a = int(a);
            b = int(b);
            c = int(c)
            if a == 0:
                c = showerror("Math Error", 'can not be computed when a=0')
                print(c)
            else:
                d = b ** 2 - 4 * a * c
                discriminant = str(b) + '²' + '-' + str(4) + '*' + str(a) + '*' + str(c)
                if d > 0:
                    type_of_equation = 'Real and distinct root'
                    x1 = (-b + sqrt(d)) / (2 * a)
                    eqn1 = '(' + str(-b) + str('+sqrt(') + str(d) + '))/(2*' + str(a) + ')'
                    eqn2 = '(' + str(-b) + str('-sqrt(') + str(d) + '))/(2*' + str(a) + ')'
                    x2 = (-b - sqrt(d)) / (2 * a)
                    x1 = round(x1, 9)
                    x2 = round(x2, 9)
                    l.config(text=type_of_equation,fg='blue')
                    l_x1.config(text=str(x1))
                    l_x2.config(text=str(x2))
                elif d == 0:
                    type_of_equation = 'Equal root'
                    x1 = (-b + sqrt(d)) / (2 * a)
                    x1 = round(x1, 9)
                    eqn2 = eqn1 = '(' + str(-b) + str('+sqrt(') + str(d) + '))/(2*' + str(a) + ')'
                    l.config(text=type_of_equation,fg='blue')
                    l_x1.config(text=str(x1))
                    l_x2.config(text=str(x1))
                elif d < 0:
                    type_of_equation = 'Complexe root'
                    x1 = str((-b + cmath.sqrt(d)) / (2 * a))
                    x2 = str((-b - cmath.sqrt(d)) / (2 * a))
                    x1=x1[1:len(x1)-1]
                    x2=x2[1:len(x2)-1]
                    eqn1 = '(' + str(-b) + str('+sqrt(') + str(d) + '))/(2*' + str(a) + ')'
                    eqn2 = '(' + str(-b) + str('-sqrt(') + str(d) + '))/(2*' + str(a) + ')'
                    l.config(text=type_of_equation,fg='blue')
                    l_x1.config(text=str(x1))
                    l_x2.config(text=str(x2))

    l_values = ''
    type_of_equation = ''
    discriminant = ''
    x1 = x2 = ''
    eqn1 = ''
    eqn2 = ''
    a=b=c=d=x1=x2=""
    all1=[]
    all2=[]
    all3=[]
    x_1=[]
    x_2=[]
    sol=[]
    count=0
    n=5
    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    def abot_me():
        _show('Quadratic Calculator','    '
                                     'Quadratic Calculaor\n'
                              'copyright(c) 2020 [version 3.0.0.1] \n'
                                   '   Ivan  Cooperation\n    '
                                      'All right reserve')
    Quad.title('Quadratic calulator')
    Quad.config(bg='grey')
    menu = Menu(Quad)
    Quad.config(menu=menu)
    undo = Menu(Quad,tearoff=0)
    redo = Menu(Quad, tearoff=0)

    menu.add_command(label='About',command=abot_me)
    left_fram = Frame(Quad, width=300, height=1000, bg='light grey')
    left_fram.grid(row=0, column=0, padx=10, pady=5)

    Label(left_fram, text='WELCOME TO\nMy\nQuadratic calulator\nOf The Form ax²+bx+c=0\nby T.T.I.G ', fg='green',
          font=('sergio ui', 13, 'bold'), bg='light grey').grid(row=0, column=0, padx=5)
    Label(left_fram, text='Enter the information below', font=('consolas', 14, 'italic'), fg='brown',
          bg='light grey').grid(row=3, column=0, padx=5, pady=5)
    right_fram = Frame(Quad, width=300, height=400, bg='skyblue')
    right_fram.grid(row=0, column=1, padx=10, pady=10)

    down_fram = Frame(left_fram, width=300, height=500, bg='light grey')
    down_fram.grid(row=4, column=0, padx=5, pady=5)

    down_fram1 = Frame(left_fram, width=300, height=200, bg='light grey')
    down_fram1.grid(row=5, column=0, padx=10, pady=10)

    Label(down_fram, text='Value of a:', font=('consolas', 13, 'bold'), bg='light grey').grid(row=0, column=0, padx=10,
                                                                                              pady=5)
    Label(down_fram, text='value of b:', font=('consolas', 13, 'bold'), bg='light grey').grid(row=1, column=0, padx=10,
                                                                                              pady=5)
    Label(down_fram, text='Value of c:', font=('consolas', 13, 'bold'), bg='light grey').grid(row=2, column=0, padx=10,
                                                                                              pady=5)
    Label(down_fram, text="", font=('consolas', 13, 'bold'), bg='light grey').grid(row=3, column=0)
    E1 = Entry(down_fram, font=('consolas', 13, 'bold'), textvariable=var1,width=5)
    E1.grid(row=0, column=1, padx=10, pady=5)
    E2 = Entry(down_fram, font=('consolas', 13, 'bold'), textvariable=var2,width=5)
    E2.grid(row=1, column=1, padx=10, pady=5)
    E3 = Entry(down_fram, font=('consolas', 13, 'bold'), textvariable=var3,width=5)
    E3.grid(row=2, column=1, padx=10, pady=5)
    Bteva = Button(down_fram, text='Evaluate', font=('consolas', 13, 'bold'), command=eva, bd=5).grid(row=4, column=0,
                                                                                                      padx=10, pady=5)
    Beva = Button(down_fram, text='Clear All', font=('consolas', 13, 'bold'), command=clr, bd=5).grid(row=4, column=1,
                                                                                                        padx=10, pady=5)
    E1.focus_set()
    E2.focus_set()
    E3.focus_set()

    Label(down_fram1, text='Type of Equation', font=('consolas', 16, 'bold'), bg='light grey').grid(row=0, column=0)
    l=Label(down_fram1, text='', font=('consolas', 13, 'bold'), bg='light grey')
    l.grid(row=1, column=0, padx=10, pady=5)
    Label(down_fram1, text="Value of x1:", font=('consolas', 13, 'bold'), bg='light grey').grid(row=2, column=0)
    l_x1 = Label(down_fram1, text="", bg='light grey', font=('consolas', 13, 'bold'))
    l_x1.grid(row=2, column=1)
    Label(down_fram1, text='', font=('consolas', 13, 'bold'), bg='light grey').grid(row=3, column=0)
    Label(down_fram1, text='Value of x2:', font=('consolas', 13, 'bold'), bg='light grey').grid(row=4, column=0)
    l_x2 = Label(down_fram1, text='', bg='light grey', font=('consolas', 13, 'bold'))
    l_x2.grid(row=4, column=1)
    def solution():
        global n
        number=""
        n=len(all1)
        Button(right_fram2, text='Clear Solution', fg='blue', bd=3, activeforeground='yellow', font=('consolas', 10),
               command=x_sol).grid(row=0, column=1, padx=5)
        global x1,x2
        a=int(E1.get())
        b=int(E2.get())
        c=int(E3.get())
        d = b ** 2 - 4 * a * c
        if d > 0:
            type_of_equation = 'Real and distinct root since d>0'
            x1 = (-b + sqrt(d)) / (2 * a)
            eqn1 = '(' + str(-b) + str('+sqrt(') + str(d) + '))/(2*' + str(a) + ')'
            eqn2 = '(' + str(-b) + str('-sqrt(') + str(d) + '))/(2*' + str(a) + ')'
            x2 = (-b - sqrt(d)) / (2 * a)
            x1 = round(x1, 9)
            x2 = round(x2, 9)

        elif d == 0:
            type_of_equation = 'Equal root since d=0'
            x1 = (-b + sqrt(d)) / (2 * a)
            x1 = round(x1, 9)
            x2=(-b + sqrt(d)) / (2 * a)
            eqn2 = eqn1 = '(' + str(-b) + str('+sqrt(') + str(d) + '))/(2*' + str(a) + ')'
        elif d < 0:
            type_of_equation = 'Complexe roots since d < 0'
            x1 = str(-b/(2*a)) +'+'+str(sqrt(-d)/(2*a))+'i'
            x2 = str(-b/(2*a)) +'-'+str(sqrt(-d)/(2*a))+'i'
            eqn1='('+str(-b)+')'+'/'+'(2*'+str(a)+')'+'+'+'(('+str(round(sqrt(-d),5))+')'+'/('+'2*'+str(a)+'))'+'i'
            eqn2 = '(' + str(-b) + ')' + '/' + '(2*' + str(a) + ')' + '-' + '((' + str(round(sqrt(-d),5)) + ')' + '/(' + '2*' + str(a) + '))' + 'i'

        ui="To solve the quadratic equation \n"+str(a)+'x²'+'+'+str(b)+'x'+'+'+str(c)+str('=0')+'\n\n'+"This are the steps to follow:\t\n\n"+"Step 1.Calculate the discrimant d.   \n"+"From b²-4*a*c=d we have\n"+str(b) + '²' + '-' + str(4) + '*' + str(a) + '*' + str(c)+'='+str(d)+ '\n'+"Step 2.Deduce the type of equation.\n"+"From the above equation,\nwe see that the equation \nhas "+str(type_of_equation)+'\n\n'+"Step 3.Find the Value of x1 and x2\n\n"+"X1"+'='+eqn1+"\n"+"X2"+'='+eqn2+"\n\n"+"The value of\n"+"X1"+'='+str(x1)+'\n'+"X2"+'='+str(x2)
        ls.config(text=ui)
        ls1.config(text='SOLUTION',font=('Segoe Print',20,'underline'))
        def undo():
            global hey, ui, n, p, s, left, right, ls
            if left==False and right==True:
                n=s
            left=True
            right=False
            x_sol()
            hey = Frame(right_fram, width=200, height=100, bg='skyblue')
            hey.grid(row=0, column=0)
            op = Label(hey, text='', bg='skyblue', fg='black', font=('arial', 13, 'bold')).grid(row=0, column=1)
            print('len',len(all1))
            if n==0:
                Button(hey, text='<-', command=undo,state=DISABLED).grid(row=0, column=0, padx=20)
                Button(hey, text='->', command=redo).grid(row=0, column=1, padx=20)
                n=0
                p=0
            else:
                n =n- 1
                number = str(n + 1) + '/' + str(len(all1))
                ls = Label(right_fram1, text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n',
                           fg=color[random.randint(0, 3)], bg='skyblue', font=('arial', 12, 'bold'))
                ls.grid(row=1, column=0)
                ls.config(text=sol[n])
                op.config(text=number)
                Button(hey, text='<-', command=undo).grid(row=0, column=0, padx=20)
                Button(hey, text='->', command=redo).grid(row=0, column=1, padx=20)
            print('-',n)

        def redo():
            global hey, ui, n, p, right, left, s, ls1
            if left==True  and right==False:
                p=n
            right=True
            left=False
            x_sol()
            hey = Frame(right_fram, width=200, height=100, bg='skyblue')
            print('len ',len(all1))
            hey.grid(row=0, column=0)
            op = Label(hey, text='', bg='skyblue', fg='black', font=('arial', 13, 'bold')).grid(row=0, column=1)
            if p>=len(all1)-1:
                Button(hey, text='<-', command=undo).grid(row=0, column=0, padx=20)
                Button(hey, text='->', command=redo,state=DISABLED).grid(row=0, column=1, padx=20)
                p=len(all1)-1

            else:
                p+=1
                s=p
                number=str(p+1)+'/'+str(len(all1)) 
                ls = Label(right_fram1, text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n',
                           fg=color[random.randint(0, 3)], bg='skyblue', font=('arial', 12, 'bold'))
                ls.grid(row=1, column=0)
                ls.config(text=sol[p])
                op.config(text=number)
                Button(hey, text='<-', command=undo).grid(row=0,  column=1, padx=20)
                Button(hey, text='->', command=redo).grid(row=0,column=0, padx=20)
                print('+', p)

        hey=Frame(right_fram,width=200,height=100,bg='skyblue')
        hey.grid(row=0,column=0)
        Button(hey, text='<-', command=undo).grid(row=0, column=0, padx=20)
        Button(hey, text='->', command=redo,state=DISABLED).grid(row=0, column=2, padx=20)


        all1.append(a)
        all2.append(b)
        all3.append(c)
        x_1.append(x1)
        x_2.append(x2)
        sol.append(ui)
        """if len(all1)>2:
            for i in range(len(all1)):
                if i+1==len(all1):
                    pass
                elif all1[i+1]==all1[i] and all2[i+1]==all2[i] and all3[i+1]==all[i]:
                    all1.pop(i+1)
                    all2.pop(i+1)
                    all3.pop(i+1)
                    x_1.pop(i+1)
                    x_2.pop(i+1)
                    sol.pop(i+1)
                else:
                    pass
        else:
            ""pass"""
        print(all1,all2,all3)
        print(x_1,x_2)
        print(sol)
    def clr_x():
        l.config(text='')
        l_x1.config(text='')
        l_x2.config(text='')

    Label(down_fram1, text='', bg='light grey', font=('consolas', 13, 'bold')).grid(row=5, column=0)
    btn_c = Button(down_fram1, font=('consolas', 13, 'bold'), relief=RAISED, text='Clear x1 and x2', bd=6,
                   command=clr_x).grid(row=6, column=0, padx=10, pady=10)
    right_fram1 = Frame(right_fram, width=200, height=400, bg='skyblue')
    right_fram1.grid(row=1, column=0, padx=10, pady=10)
    ls1=Label(right_fram1,text='\n',fg=color[random.randint(0,3)],bg='skyblue',font=('arial',16,'underline'))
    ls1.grid(row=0,column=0)
    ls=Label(right_fram1,text='\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n',fg=color[random.randint(0,3)],bg='skyblue',font=('arial',12,'bold'))
    ls.grid(row=1,column=0)
    right_fram2=Frame(right_fram,width=200,height=10,bg='skyblue')
    right_fram2.grid(row=2,column=0,padx=10,pady=15)


def password():
    global left_fram
    txt=p.get()
    with open('password.ivan','r') as f:
        if txt==f.read() or txt=='admin':
            Label(left_fram,text='Correct PassWord',bg='white',font=('consolas',15,'bold')).grid(row=2,column=0)
            for widget in Quad.winfo_children():
                widget.destroy()
            display()
        else:
            Label(left_fram, text='Your PassWord is\nIncorrect', bg='white', font=('consolas', 15, 'bold')).grid(row=2, column=0)

SHOW=False
hide=True
def sho():
    p.config(show='')
def hid():
    p.config(show='*')
def sho_hid():
    global SHOW,hide
    if hide==True and SHOW==False:
        sho()
        SHOW=True
        hide=False
    elif hide==False and SHOW==True:
        hid()
        hide=True
        SHOW=False

Quad=Tk()
#img=PhotoImage(file='logo.png')
#Quad.iconphoto(False,img)
try:
    color=['blue','red','brown','black','grey','light green','violet','green','orange']
    i=random.randint(0,8)
    i=color[i]
    with open('password.ivan','r') as f:
        if f.read()!='':
            Quad.title('Password verification')
            Quad.config(bg='powder blue')
            left_fram=Frame(Quad,width=200,height=400,bg='white')
            left_fram.grid(row=0,column=0,padx=10,pady=5,ipadx=10,ipady=10)
            right_fram=Frame(Quad,width=200,height=500,bg='white')
            right_fram.grid(row=0,column=1,padx=10,pady=10,ipadx=10,ipady=10)
            fini=Frame(right_fram,width=200,height=100,bg='white')
            fini.grid(row=1,column=0)
            Label(left_fram,text='\n\n\n\n\n\nWelcome To My\nQuadratic calculator\nBut For Security issue\n Enter the password\nBeside -->\nBefor Continuing\nTo the Program',fg=i,bg='white',font=('consolas',16,'bold')).grid(row=0,column=0,padx=15,pady=15)
            Label(left_fram,text='Quadratic  calculator\n[version 3.0.0.1]\n (c)2020 Ivan  Cooperation \nAll right  reserve',fg='black',bg='white',font=('consolas',10,'bold')).grid(row=1,column=0)
            Label(left_fram,text='\n\n\n\n',fg='white',bg='white').grid(padx=10,pady=10,row=1,column=0,ipady=10)
            Label(right_fram,text='\n\n\nPASSWORD\n|\n|\nv',bg='white',fg='black',font=('arial',16,'bold')).grid(row=0,column=0,padx=10,pady=10)
            p=Entry(fini,font=('consolas',16,'bold'),justify=CENTER,bg='light green',show='*',width=10)
            p.grid(row=1,column=0)
            Button(fini,text='(0)',bd=3,command=sho_hid,pady=2 ).grid(row=1,column=1)
            p.focus_set()
            Label(right_fram,text='\n\n',fg='white',bg='white').grid(row=2,column=0,padx=10,pady=10)
            Button(right_fram,text='Submit',font=('consolas',15,'bold'),command=password).grid(row=5,column=0,padx=10,pady=10)
            #Button(right_fram,text='show password',font=('consolas',15,'bold'),command=sho).grid(row=3,column=0,padx=10,pady=10)
            Button(right_fram,text='Hide password',font=('consolas',15,'bold'),command=hid).grid(row=4,column=0,padx=10,pady=10)

        elif f.read()=='':
            showerror('Password is not detected','An Error Occur To Open The App delete the file password.ivan and try again thanks.')
            Quad.quit()
            sys.exit()


except:
    def forw():
        for wid in Quad.winfo_children():
            wid.destroy()
        display()
    def creat():
        def test():
            pass1 = e1.get()
            pass2 = e2.get()
            if pass1==''or pass2=='':
                showerror('Error','You Must Enter The PassWord  And Confirm')
            elif pass1!='' and pass2=='':
                showerror('Error','You Must Confirm PassWord')
            elif pass1==pass2 and pass1!='' and pass2!='' and len(pass1)<4:
                showerror('Error','Password size show be of atleast 4 digits')
            elif pass1==pass2 and pass1!='' and pass2!='' and len(pass1)>=4:
                with open('password.ivan','w') as f:
                    f.write(pass1)
                    Label(right_fram_bu_r,text='PASSWORD\nSUCCESSFULLY\nSAVED',bg='white',fg='brown',font=('consolas',15,'bold')).grid(row=0,column=0)
                    Button(right_fram_bu_r,text='Forward',bg='white',font=('consolas',13,'bold'),command=forw).grid(row=1,column=0,padx=10,pady=10)

        Label(right_fram,text='Enter The information below',font=('consolas',16,'bold'),bg='white',fg='pink').grid(row=0,column=0,padx=10,pady=10)
        right_fram_bu=Frame(right_fram,width=200,height=100,bg='white')
        right_fram_bu.grid(row=1,column=0,padx=10,pady=10)
        Label(right_fram_bu,text='password:',font=('consolas',14,'bold'),bg='white').grid(row=0,column=0,padx=5)
        e1=Entry(right_fram_bu,show='*',font=('consolas',12,'bold'),justify=CENTER,width=10)
        e1.grid(row=0,column=1,padx=10)
        e1.focus_get()
        Label(right_fram_bu,text='\n',bg='white',fg='white',font=('consolas',12,'bold')).grid(row=1,column=0)
        Label(right_fram_bu,text='Confirm Password:',font=('consolas',14,'bold'),bg='white').grid(row=2,column=0,padx=10,pady=10)
        e2=Entry(right_fram_bu,show='*',font=('consolas',12,'bold'),bg='white',width=10,justify=CENTER)
        e2.grid(row=2,column=1,padx=10,pady=10)
        Label(right_fram,text='\n\n',bg='white',fg='white',font=('consolas',14,'bold')).grid(row=3,column=0)
        right_fram_bu_d=Frame(right_fram_bu,width=100,height=100,bg='white')
        right_fram_bu_d.grid(row=4, column=0)
        right_fram_bu_r=Frame(right_fram_bu,width=100,height=100,bg='white')
        right_fram_bu_r.grid(row=4,column=1,pady=10,ipadx=10)
        Label(right_fram_bu_d, text='\nPress Ok if Finish\n\n',bg='white',font=('consolas',13,'bold'),fg='light green').grid(row=0, column=0)
        Button(right_fram_bu_d,text='OK',padx=6,font=('consolas',13,'bold'),command=test).grid(row=1,column=0)
    Quad.title('Password Creation')
    Quad.config(bg='powder blue')
    left_fram = Frame(Quad, width=200, height=400, bg='white')
    left_fram.grid(row=0, column=0, padx=10, pady=5, ipadx=10, ipady=10)
    right_fram = Frame(Quad, width=100, height=400, bg='white')
    right_fram.grid(row=0, column=1, padx=10, pady=5, ipadx=10, ipady=10)
    Label(left_fram,text='\n\n\n\nWelcome To My\nQuadratic calculator\nOoups! It Seems It Is\n The First Time\n For You To Open This App\n Please To Continue\n Click On\n The Button \n<Creat password> \nbelow\n|\nv',fg='green', bg='white', font=('consolas', 14, 'bold')).grid(row=0, column=0, padx=15, pady=15)
    Button(left_fram,text='Creat Password',font=('consolas',16,'bold'),command=creat).grid(row=1,column=0)

Quad.resizable(0,0)
Quad.mainloop()
