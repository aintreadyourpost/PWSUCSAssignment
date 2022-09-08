#Import libs
import turtle as tt

#List of rooms
rooml = ['101','102','103','104','201','202','203','204','301','302','303','304']
ava = [] 
occ = []
res = []

#Reading data from script booting
file_ava = open('ava.txt','r')
ava = [line.rstrip('\n') for line in file_ava]
file_ava.close()
file_occ = open('occ.txt','r')
occ = [line.rstrip('\n') for line in file_occ]
file_occ.close()
file_res = open('res.txt','r')
res = [line.rstrip('\n') for line in file_res]
file_res.close()

#Title of the map
tt.title('BUV Sunshine Hotel Map')

#Set turtle, clear screen, speed and initial coordination
t = tt.Turtle()
t.speed(999)
tt.clearscreen()
t.goto(-200,300)
t.pendown()

#Draw a room: 
def drawroom(room):
    room = str(room)
    if room in ava:
        t.fillcolor('green')
    elif room in occ:
        t.fillcolor('red')
    elif room in res:
        t.fillcolor('yellow')
    t.begin_fill()
    for i in range(4):
      t.fd(100)
      t.rt(90)
    t.end_fill()

#Name box: 
def nbox(x,y,z): #x is x-coor, y is y-coor and z is the left-most room of the floor
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fd(400)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(400)
    t.rt(90)
    t.fd(100)
    t.rt(180)
    t.fd(100)
    t.lt(90)
    t.penup()
    t.goto(x+55,y-30)
    for i in range(4):
        t.write('Room '+str(z), align = 'center')
        z+=1
        t.fd(100)
    t.goto(0,y-90)
    t.write('Floor '+str(round(z/100)),align = 'center')     
    t.goto(x,y-100)
    t.pendown()
#Legends:
def legends():
    t.penup()
    t.goto(300,100)
    t.pendown()
    t.fd(220)
    t.rt(90)
    t.fd(150)
    t.rt(90)
    t.fd(220)
    t.rt(90)
    t.fd(150)
    t.back(150)
    t.rt(90)
    t.penup()
    t.goto(330,15)
    t.write('Legends:',align = 'center')
    t.goto(375,80)
    t.fillcolor('green')
    t.begin_fill()
    for n in range(4):
        t.fd(20)
        t.rt(90)
    t.end_fill()
    t.rt(90)
    t.fd(45)
    t.lt(90)
    t.fillcolor('yellow')
    t.begin_fill()
    for n in range(4):
        t.fd(20)
        t.rt(90)
    t.end_fill()
    t.rt(90)
    t.fd(45)
    t.lt(90)
    t.fillcolor('red')
    t.begin_fill()
    for n in range(4):
        t.fd(20)
        t.rt(90)
    t.end_fill()
    t.goto(440,63)
    t.write('Available room', align = 'center')
    t.rt(90)
    t.fd(46)
    t.lt(90)
    t.write('Reserved room', align = 'center')
    t.rt(90)
    t.fd(46)
    t.lt(90)
    t.write('Occupied room', align = 'center')
    t.pendown()
    
#Hotel map drawing
for i in range(101,105):
    drawroom(i)
    t.fd(100)
nbox(-200,200,101)
for i in range(201,205):
    drawroom(i)
    t.fd(100)
nbox(-200,0,201)
for i in range(301,305):
    drawroom(i)
    t.fd(100)
nbox(-200,-200,301)
legends()

# tt.bye()