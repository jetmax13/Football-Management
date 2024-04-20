import turtle
from tkinter import *
from PIL import ImageTk, Image
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="pes")
mycursor=mydb.cursor()
import os



#LOGIN SYSTEM



def main_screen():                                 
    global screen
    global login_button
    global register_button
    screen=Tk()
    screen.title("Login/Register")
    screen.geometry("550x550")
    Label(screen,text="Login Page").pack()
    Label(screen,text="").pack()
    login_button=Button(screen,text="Login",width=20,height=2,command=login).pack()
    Label(screen,text="").pack()

    register_button=Button(screen,text="Register",width=20,height=2,command=register).pack()

    
def login():                                     
    global screen1
    global loginusername
    global loginpassword
    global submit_login
    global usernameentryl
    global passwordentryl
    loginusername=StringVar()
    loginpassword=StringVar()
    
    
    screen1=Toplevel(screen)
    screen1.title("Login")
    screen1.geometry("550x550")
    

    Label(screen1,text="Enter the details").pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Username").pack()
    usernameentryl=Entry(screen1,textvariable=loginusername)
    usernameentryl.pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Password").pack()
    passwordentryl=Entry(screen1,textvariable=loginpassword,show="*")
    passwordentryl.pack()
    
    Label(screen1,text="").pack()
    submit_login=Button(screen1,text="Submit",command=loginsubmit).pack()

        
def register():
    global screen2
    global registerusername
    global registerpassword
    global usernameentryr
    global passwordentryr
    global submit_register
    registerusername=StringVar()
    registerpassword=StringVar()
    
       
    screen2=Toplevel(screen)
    screen2.title("Register")
    screen2.geometry("550x550")
    
    Label(screen2,text="Enter the details").pack()
    Label(screen2,text="").pack()
    Label(screen2,text="Username").pack()
    usernameentryr=Entry(screen2,textvariable=registerusername)
    usernameentryr.pack()
    Label(screen2,text="").pack()
    Label(screen2,text="Password").pack()
    passwordentryr=Entry(screen2,textvariable=registerpassword,show="*")
    passwordentryr.pack()
    Label(screen2,text="").pack()
    submit_register=Button(screen2,text="Submit",command=registersubmit).pack()
    
def loginsubmit():
    usernamel=loginusername.get()
    passwordl=loginpassword.get()
    usernameentryl.delete(0,END)
    passwordentryl.delete(0,END)
    
    
    path = os.getcwd()
    f = os.listdir(path)
    corrected=usernamel+".txt"
    if corrected in f:
        filel=open(corrected,"r")
        verify=filel.read().splitlines()
        if passwordl in verify:
            Label(screen1,text="Login successful",fg="green").pack()
            mainscreen()
        else:
            Label(screen1,text="Incorrect password",fg="red").pack()
    else:
        Label(screen1,text="Incorrect username",fg="red").pack()
        
    
    
def registersubmit():
    usernamer=registerusername.get()
    passwordr=registerpassword.get()
    file=open(usernamer+".txt","w")
    file.write(usernamer+"\n")
    file.write(passwordr)
    file.close()
    usernameentryr.delete(0,END)
    passwordentryr.delete(0,END)
    Label(screen2,text="Registration successful",fg="green").pack()


#MAIN PROGRAM

    
def mainscreen():
    global screenp
    global pes
    global squad
    global manager
    global logo
    global tactics
    global statistics
    
    
    screenp=Toplevel(screen)
    screenp.title("Pes Team")
    screenp.geometry("550x550")
    Label(screenp,text="").pack()
    Label(screenp,text="Jetmax FC").pack()
    Label(screenp,text="").pack()
    
    logo = Image.open("jetmax.png")
    logo = logo.resize((250, 335), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logo)
    Label(screenp, image=logo).pack()
    

    
    pes=Menu(screenp)
    screenp.config(menu=pes)
    
    squad=Menu(pes)
    pes.add_cascade(label="Squad",menu=squad)
    
    squad.add_command(label="Create",command=addsquad)
    squad.add_command(label="View",command=viewsquad)
    squad.add_command(label="Update",command=updatesquad)
    squad.add_command(label="Delete",command=deletesquad)

    manager=Menu(pes)
    pes.add_cascade(label="Manager",menu=manager)

    manager.add_command(label="Add",command=addmanager)
    manager.add_command(label="View",command=viewmanager)
    manager.add_command(label="Update",command=updatemanager)
    manager.add_command(label="Delete",command=deletemanager)


    tactics=Menu(pes)
    pes.add_cascade(label="Tactics",menu=tactics)

    tactics.add_command(label="View",command=viewtactics)

    statistics=Menu(pes)
    pes.add_cascade(label="Statistics",menu=statistics)

    statistics.add_command(label="Update",command=updatestats)
    statistics.add_command(label="View",command=viewstats)


    
    
    
    
    
def addsquad():
    global a
    global jerseynop
    global namep
    global jerseyentry
    global nameentry
    a=Toplevel(screenp)
    a.geometry("550x550")
    a.title("Create Squad")
    jerseynop=StringVar()
    namep=StringVar()
    Label(a,text="").pack()
    Label(a,text="Jersey No").pack()
    Label(a,text="").pack()
    jerseyentry=Entry(a,textvariable=jerseynop)
    jerseyentry.pack()
    Label(a,text="").pack()
    Label(a,text="Name").pack()
    Label(a,text="").pack()
    nameentry=Entry(a,textvariable=namep)
    nameentry.pack()
    Label(a,text="").pack()
    Button(a,text="Add Player",command=cs).pack()
    
    
def cs():
    global jerseynopp
    global namepp
    global sqlformula1
    global players
    jerseynopp=jerseynop.get()
    namepp=namep.get()
    sqlformula1=("insert into squad values(%s, %s,0,0,0)")
    players=[(jerseynopp,namepp)]
    mycursor.executemany(sqlformula1,players)
    mydb.commit()
    jerseynopp=jerseynop.set("")
    namepp=namep.set("")
    Label(a,text="").pack()
    Label(a,text="Player Added",fg="green").pack()
            
    
def viewsquad():
    global b
    global sqlview
    global sqlview1
    b=Toplevel(screenp)
    b.geometry("550x550")
    b.title("Squad")
    Label(b,text="").pack()
    sqlview=("select jerseyno,name from squad")
    mycursor.execute(sqlview)
    sqlview1=mycursor.fetchall()
    for i in sqlview1:
        Label(b,text=i).pack()



        
def updatesquad():
    global c
    global oldjersey
    global newjersey
    global newname
    global oldjerseyentry
    global newjerseyentry
    global newnameentry
    c=Toplevel(screenp)
    c.geometry("550x550")
    c.title("Update Squad")
    oldjersey=StringVar()
    newjersey=StringVar()
    newname=StringVar()
    Label(c,text="").pack()
    Label(c,text="Old Jersey No").pack()
    Label(c,text="").pack()
    oldjerseyentry=Entry(c,textvariable=oldjersey)
    oldjerseyentry.pack()
    Label(c,text="").pack()
    Label(c,text="New Jersey No").pack()
    Label(c,text="").pack()
    newjerseyentry=Entry(c,textvariable=newjersey)
    newjerseyentry.pack()
    Label(c,text="").pack()
    Label(c,text="New Player Name").pack()
    Label(c,text="").pack()
    newnameentry=Entry(c,textvariable=newname)
    newnameentry.pack()
    Label(c,text="").pack()
    Button(c,text="Save Changes",command=us).pack()




def us():
    global oldjersey1
    global newjersey1
    global newname1
    global sqlformula2
    global sqlformula3
    global u1
    global u2
    oldjersey1=oldjersey.get()
    newjersey1=newjersey.get()
    newname1=newname.get()
    sqlformula2=("update squad set name=%s where jerseyno=%s")
    u1=[(newname1,oldjersey1)]
    mycursor.executemany(sqlformula2,u1)
    mydb.commit()
    sqlformula3=("update squad set jerseyno=%s where name=%s")
    u2=[(newjersey1,newname1)]
    mycursor.executemany(sqlformula3,u2)
    mydb.commit()
    oldjersey1=oldjersey.set("")
    newjersey1=newjersey.set("")
    newname1=newname.set("")
    Label(c,text="").pack()
    Label(c,text="Changes Saved",fg="green").pack()
    
    
    
def deletesquad():
    global d
    d=Toplevel(screenp)
    d.geometry("550x550")
    d.title("Delete Squad")
    Label(d,text="").pack()
    Label(d,text="Pressing 'Delete' will delete the name and jersey numbers of all the players").pack()
    Label(d,text="").pack()
    Button(d,text="Delete",command=ds).pack()



    
def ds():
    mycursor.execute("truncate table squad")
    mydb.commit()
    Label(d,text="").pack()
    Label(d,text="Squad Deleted",fg="green").pack()


def addmanager():
    global e
    global formationp
    global mnamep
    global formationentry
    global mnameentry
    e=Toplevel(screenp)
    e.geometry("550x550")
    e.title("Manager Details")
    formationp=StringVar()
    mnamep=StringVar()
    Label(e,text="").pack()
    Label(e,text="Name").pack()
    Label(e,text="").pack()
    mnameentry=Entry(e,textvariable=mnamep)
    mnameentry.pack()
    Label(e,text="").pack()
    Label(e,text="Formation").pack()
    Label(e,text="").pack()
    formationentry=Entry(e,textvariable=formationp)
    formationentry.pack()
    Label(e,text="").pack()
    Button(e,text="Add Manager",command=am).pack()

def am():
    global formationpp
    global mnamepp
    global sqlformula4
    global managers
    formationpp=formationp.get()
    mnamepp=mnamep.get()
    sqlformula4=("insert into manager values(%s, %s)")
    managers=[(mnamepp,formationpp)]
    mycursor.executemany(sqlformula4,managers)
    mydb.commit()
    formationpp=formationp.set("")
    mnamepp=mnamep.set("")
    Label(e,text="").pack()
    Label(e,text="Manager Added",fg="green").pack()
    
def viewmanager():
    global f
    global sqlviewm
    global sqlviewm1
    f=Toplevel(screenp)
    f.geometry("550x550")
    f.title("Managers")
    Label(f,text="").pack()
    sqlviewm=("select * from manager")
    mycursor.execute(sqlviewm)
    sqlviewm1=mycursor.fetchall()
    for i in sqlviewm1:
        Label(f,text=i).pack()



        
def updatemanager():
    global g
    global oldmname
    global newformation
    global newmname
    global oldmnameentry
    global newformationentry
    global newmnameentry
    g=Toplevel(screenp)
    g.geometry("550x550")
    g.title("Update Managers")
    oldmname=StringVar()
    newformation=StringVar()
    newmname=StringVar()
    Label(g,text="").pack()
    Label(g,text="Old Name").pack()
    Label(g,text="").pack()
    oldmnameentry=Entry(g,textvariable=oldmname)
    oldmnameentry.pack()
    Label(g,text="").pack()
    Label(g,text="New Name").pack()
    Label(g,text="").pack()
    newmnameentry=Entry(g,textvariable=newmname)
    newmnameentry.pack()
    Label(g,text="").pack()
    Label(g,text="New Formation").pack()
    Label(g,text="").pack()
    newformationentry=Entry(g,textvariable=newformation)
    newformationentry.pack()
    Label(g,text="").pack()
    Button(g,text="Save Changes",command=um).pack()




def um():
    global oldmname1
    global newmname1
    global newformation1
    global sqlformula5
    global sqlformula6
    global um1
    global um2
    oldmname1=oldmname.get()
    newmname1=newmname.get()
    newformation1=newformation.get()
    sqlformula5=("update manager set formation=%s where name=%s")
    um1=[(newformation1,oldmname1)]
    mycursor.executemany(sqlformula5,um1)
    mydb.commit()
    sqlformula6=("update manager set name=%s where formation=%s")
    um2=[(newmname1,newformation1)]
    mycursor.executemany(sqlformula6,um2)
    mydb.commit()
    oldmname1=oldmname.set("")
    newmname1=newmname.set("")
    newformation1=newformation.set("")
    Label(g,text="").pack()
    Label(g,text="Changes Saved",fg="green").pack()
    
    

def deletemanager():
    global h
    h=Toplevel(screenp)
    h.geometry("550x550")
    h.title("Delete Manager")
    Label(h,text="").pack()
    Label(h,text="Pressing 'Delete' will delete the name and formations of all managers").pack()
    Label(h,text="").pack()
    Button(h,text="Delete",command=dm).pack()
    


def dm():
    mycursor.execute("truncate table manager")
    mydb.commit()
    Label(h,text="").pack()
    Label(h,text="Managers Deleted",fg="green").pack()



    

def viewtactics():
    global i
    global nodef_var
    global nodmf_var
    global nocmf_var
    global nowmf_var
    global noamf_var
    global noss_var
    global noatt_var
    nodef_var=IntVar()
    nodmf_var=IntVar()
    nocmf_var=IntVar()
    nowmf_var=IntVar()
    noamf_var=IntVar()
    noss_var=IntVar()
    noatt_var=IntVar()
    i=Toplevel(screenp)
    i.geometry("800x800")
    i.title("Tactics")
    Label(i,text="").pack()
    Label(i,text="Select total 10 players").pack()
    Label(i,text="Enter below the number of players for each position").pack()
    Label(i,text="Valid number of players for each position shown in brackets").pack()
    Label(i,text="").pack()
    Label(i,text="Defenders(3/4/5)").pack()
    Entry(i,textvariable=nodef_var).pack()
    Label(i,text="").pack()
    Label(i,text="Defensive Midfielders(0/1/2/3)").pack()
    Entry(i,textvariable=nodmf_var).pack()
    Label(i,text="").pack()
    Label(i,text="Central Midfielders(0/1/2/3)").pack()
    Entry(i,textvariable=nocmf_var).pack()
    Label(i,text="").pack()
    Label(i,text="Wide Midfielders(0/2)").pack()
    Entry(i,textvariable=nowmf_var).pack()
    Label(i,text="").pack()
    Label(i,text="Attacking Midfielders(0/1/2/3)").pack()
    Entry(i,textvariable=noamf_var).pack()
    Label(i,text="").pack()
    Label(i,text="Supporting Strikers(0/1/2/3)").pack()
    Entry(i,textvariable=noss_var).pack()
    Label(i,text="").pack()
    Label(i,text="Attackers(0/1/2/3)").pack()
    Entry(i,textvariable=noatt_var).pack()
    Label(i,text="").pack()
    Button(i,text="Submit",command=vt).pack()



    
def vt():
    global nodef
    global nodmf
    global nocmf
    global nowmf
    global noamf
    global noss
    global noatt
    
    nodef=nodef_var.get()
    nodmf=nodmf_var.get()
    nocmf=nocmf_var.get()
    nowmf=nowmf_var.get()
    noamf=noamf_var.get()
    noss=noss_var.get()
    noatt=noatt_var.get()
    mainpitch()
    nodef_var.set(0)
    nodmf_var.set(0)
    nocmf_var.set(0)
    nowmf_var.set(0)
    noamf_var.set(0)
    noss_var.set(0)
    noatt_var.set(0)


def updatestats():
    
    global ii
    global sname
    global snamenetry
    global goals
    global goalsentry
    global assists
    global assistsentry
    global saves
    global savesentry
    
    ii=Toplevel(screenp)
    ii.geometry("550x550")
    ii.title("Update Statistics")
    sname=StringVar()
    goals=StringVar()
    assists=StringVar()
    saves=StringVar()
    Label(ii,text="").pack()
    Label(ii,text="Name").pack()
    Label(ii,text="").pack()
    snameentry=Entry(ii,textvariable=sname)
    snameentry.pack()
    Label(ii,text="").pack()
    Label(ii,text="Goals").pack()
    Label(ii,text="").pack()
    goalsentry=Entry(ii,textvariable=goals)
    goalsentry.pack()
    Label(ii,text="").pack()
    Label(ii,text="Assists").pack()
    Label(ii,text="").pack()
    assistsentry=Entry(ii,textvariable=assists)
    assistsentry.pack()
    Label(ii,text="").pack()
    Label(ii,text="Saves").pack()
    Label(ii,text="").pack()
    savesentry=Entry(ii,textvariable=saves)
    savesentry.pack()
    Label(ii,text="").pack()
    Button(ii,text="Save Changes",command=ust).pack()




def ust():
    
    sname1=sname.get()
    goals1=goals.get()
    assists1=assists.get()
    saves1=saves.get()
    sqlformulas1=("update squad set goals=%s where name=%s")
    us1=[(goals1,sname1)]
    mycursor.executemany(sqlformulas1,us1)
    mydb.commit()
    sqlformulas2=("update squad set assists=%s where name=%s")
    us2=[(assists1,sname1)]
    mycursor.executemany(sqlformulas2,us2)
    mydb.commit()
    sqlformulas3=("update squad set saves=%s where name=%s")
    us3=[(saves1,sname1)]
    mycursor.executemany(sqlformulas3,us3)
    mydb.commit()
    sname1=sname.set("")
    goals1=goals.set("")
    assists1=assists.set("")
    saves1=saves.set("")
    Label(ii,text="").pack()
    Label(ii,text="Changes Saved",fg="green").pack()
    
def viewstats():
    global j
    global sqlviews
    global sqlviews1
    j=Toplevel(screenp)
    j.geometry("550x550")
    j.title("Squad")
    Label(j,text="").pack()
    Label(j,text="Name Goals Assists Saves").pack()
    sqlviews=("select name,goals,assists,saves from squad")
    mycursor.execute(sqlviews)
    sqlviews1=mycursor.fetchall()
    for i in sqlviews1:
        Label(j,text=i).pack()   
    
            
    
    







#TACTICS COMMANDS

    

    
def mainpitch():
  
  
  
  noplayer=nodef+nodmf+nocmf+noamf+noss+noatt+nowmf


  if noplayer==10:

      drawpitch()
      drawplayer("blue",0,-194)
    
    
      if nodef==4:
          drawplayer("yellow",-35,-120) 
          drawplayer("yellow",35,-120) 
          drawplayer("yellow",-100,-105)
          drawplayer("yellow",100,-105)
      elif nodef==3:
          drawplayer("yellow",0,-120)
          drawplayer("yellow",-50,-120)
          drawplayer("yellow",50,-120)
      elif nodef==5:
          drawplayer("yellow",0,-120)
          drawplayer("yellow",-50,-120)
          drawplayer("yellow",50,-120)
          drawplayer("yellow",-100,-105)
          drawplayer("yellow",100,-105)
      else:
        Label(i,text="").pack()
        Label(i,text="Enter values according to the instructions",fg="red").pack()

        
      if nodmf==0:
          pass
      elif nodmf==1:
          drawplayer("orange",0,-60)
      elif nodmf==2:
          drawplayer("orange",-25,-60)
          drawplayer("orange",25,-60)
      elif nodmf==3:
          drawplayer("orange",0,-60)
          drawplayer("orange",-90,-60)
          drawplayer("orange",90,-60)
      else:
        Label(i,text="").pack()
        Label(i,text="Enter values according to the instructions",fg="red").pack()
        
      if nocmf==0:
          pass
      elif nocmf==1:
          drawplayer("orange",0,-5)
      elif nocmf==2:
          drawplayer("orange",-25,-5)
          drawplayer("orange",25,-5)
      elif nocmf==3:
          drawplayer("orange",0,-5)
          drawplayer("orange",-25,-5)
          drawplayer("orange",25,-5)
      else:
        Label(i,text="").pack()
        Label(i,text="Enter values according to the instructions",fg="red").pack()
        
      if nowmf==0:
          pass
      elif nowmf==2:
          drawplayer("orange",115,10)
          drawplayer("orange",-115,10)
      else:
        Label(i,text="").pack()
        Label(i,text="Enter values according to the instructions",fg="red").pack()

        
      if noamf==0:
          pass
      elif noamf==1:
          drawplayer("orange",0,50)
      elif noamf==2:
          drawplayer("orange",-25,50)
          drawplayer("orange",25,50)
      elif noamf==3:
          drawplayer("orange",0,50)
          drawplayer("orange",-25,50)
          drawplayer("orange",25,50)
      else:
        Label(i,text="").pack()
        Label(i,text="Enter values according to the instructions",fg="red").pack()
        
      if noss==0:
          pass
      elif noss==1:
          drawplayer("red",0,90)
      elif noss==2:
          drawplayer("red",-25,90)
          drawplayer("red",25,90)
      elif noss==3:
          drawplayer("red",0,90)
          drawplayer("red",-90,75)
          drawplayer("red",90,75)
      else:
        Label(i,text="").pack()
        Label(i,text="Enter values according to the instructions",fg="red").pack()

        
      if noatt==0:
          pass
      elif noatt==1:
          drawplayer("red",0,130)
      elif noatt==2:
          drawplayer("red",-25,130)
          drawplayer("red",25,130)
      elif noatt==3:
          drawplayer("red",0,130)
          drawplayer("red",-90,115)
          drawplayer("red",90,115)
      else:
        Label(i,text="").pack()
        Label(i,text="Enter values according to the instructions",fg="red").pack()    
          
  else:
        Label(i,text="").pack()
        Label(i,text="Enter values according to the instructions",fg="red").pack()


        

#DRAWING THE PITCH


      
def drawpitch():
  global screent
  
  screent=turtle.Screen()
  screent.tracer(0)
  screent.bgcolor("green")
  
  myBrush = turtle.Turtle()
  myBrush.width(1)
  myBrush.hideturtle()
  
  myBrush.speed(0)
  myBrush.color("white")
  
  #Outer lines
  myBrush.penup()
  myBrush.goto(-140,195)
  myBrush.pendown()
  myBrush.goto(140,195)
  myBrush.goto(140,-195)
  myBrush.goto(-140,-195)
  myBrush.goto(-140,195)
  
  #Penalty Box - Top
  myBrush.penup()
  myBrush.goto(0,115)
  myBrush.pendown()
  myBrush.circle(40)
  myBrush.penup()
  myBrush.goto(-80,195)
  myBrush.pendown()
  myBrush.fillcolor("green")
  myBrush.begin_fill()
  myBrush.goto(80,195)
  myBrush.goto(80,140)
  myBrush.goto(-80,140)
  myBrush.goto(-80,195)  
  myBrush.end_fill()
 
  #Penalty Box - Bottom 
  myBrush.penup()
  myBrush.goto(0,-195)
  myBrush.pendown()
  myBrush.circle(40)
  myBrush.penup()
  myBrush.goto(-80,-195)
  myBrush.pendown()
  myBrush.fillcolor("green")
  myBrush.begin_fill()
  myBrush.goto(80,-195)
  myBrush.goto(80,-140)
  myBrush.goto(-80,-140)
  myBrush.goto(-80,-195)  
  myBrush.end_fill()

  # Goal Box - Bottom
  myBrush.penup()
  myBrush.goto(40,-195)
  myBrush.pendown()
  myBrush.goto(40,-170)
  myBrush.goto(-40,-170)
  myBrush.goto(-40,-195)  

  # Goal Box - Top
  myBrush.penup()
  myBrush.goto(40,195)
  myBrush.pendown()
  myBrush.goto(40,170)
  myBrush.goto(-40,170)
  myBrush.goto(-40,195)     
  
  #Halfway Line
  myBrush.penup()
  myBrush.goto(-140,0)
  myBrush.pendown()
  myBrush.goto(140,0)
  
  #Central Circle
  myBrush.penup()
  myBrush.goto(0,-40)
  myBrush.pendown()
  myBrush.circle(40)
  myBrush.penup()
  #screent.tracer(1)





#DRAWING A PLAYER





  
def drawplayer(color,x,y):
  
  screent=turtle.Screen()
  screent.tracer(0)
  myPen = turtle.Turtle()
  myPen.hideturtle()
  myPen.penup()
  myPen.goto(x,y)
  myPen.fillcolor(color)
  myPen.begin_fill()
  myPen.circle(10)
  myPen.end_fill()
  #screent.tracer(1)  
  myPen.penup()
  myPen.goto(x+10,y)
  myPen.color(color)

main_screen()
screen.mainloop()
        
    
    
