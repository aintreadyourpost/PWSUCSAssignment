#Import libs
import turtle as tt
import sys

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

#Data integrity check
L = ava + occ + res
list.sort(L)
if rooml != L:
    print('----- DATA IS INCORRECT -----')
    print('\nPlease check and correct the data from text files.')
    sys.exit()

#Title of the map
tt.title('BUV Sunshine Hotel Map')
#Set speed
t = tt.Turtle()

t.speed(200)
t.penup()
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
    t.goto(x+50,y-30)
    t.pendown()
    for i in range(4):
        t.write('Room '+str(z), align = 'center')
        z+=1
        t.penup()
        t.fd(100)
    t.penup()
    t.goto(0,y-80)
    t.pendown()
    t.write('Floor '+str(round(z/100)),align = 'center')     
    t.penup()
    t.goto(x,y-100)
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
for i in range(401,405):
    drawroom(i)
    t.fd(100)
nbox(-200,-400,401)