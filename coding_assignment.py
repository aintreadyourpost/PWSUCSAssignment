#Import libs
from colorama import Fore, Style, Back
import sys
import turtle as tt

#Create global variables
rooml = ['101','102','103','104','201','202','203','204','301','302','303','304']
ava = [] 
occ = []
res = []
seperator = ', '

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

#Func changing the status of the roomc
def roomstatchange():
    avasort = sorted(str(x) for x in ava)   
    occsort = sorted(str(x) for x in occ)
    ressort = sorted(str(x) for x in res)
    prstat = f'''\n----------------------------------------------------------------------
        \n                         <LIST OF ROOMS>
        \n{Fore.GREEN}{Style.BRIGHT}Available room(s):{Style.RESET_ALL} {seperator.join(avasort)}
        \n{Fore.RED}{Style.BRIGHT}Occupied room(s):{Style.RESET_ALL}  {seperator.join(occsort)}
        \n{Fore.YELLOW}{Style.BRIGHT}Reserved room(s):{Style.RESET_ALL}  {seperator.join(ressort)}
        \n----------------------------------------------------------------------'''
    print(prstat)
    roomchoice = str(input('\nPlease enter the room that you want to change: '))
    while roomchoice not in rooml:    #Input validation
        print('\n----- INVALID INPUT -----')
        print('Please re-enter your choice.')
        roomchoice = str(input('\nPlease enter the room that you want to change: '))
    if roomchoice in ava:   #Changing room status if room is already availble
        print(f'\nRoom {roomchoice} is {Fore.GREEN}{Style.BRIGHT}AVAILABLE{Style.RESET_ALL}.')
        statchoice = str.lower(input(f'\nDo you want to make it {Fore.RED}{Style.BRIGHT}OCCUPIED (O){Style.RESET_ALL} or {Fore.YELLOW}{Style.BRIGHT}RESERVED (R){Style.RESET_ALL}?: '))
        while statchoice not in ['o','r']:  #Input validity check
            print('\n----- INVALID INPUT -----')
            print('Please re-enter your choice.')
            statchoice = str.lower(input(f'\nDo you want to make it {Fore.RED}{Style.BRIGHT}OCCUPIED (O){Style.RESET_ALL} or {Fore.YELLOW}{Style.BRIGHT}RESERVED (R){Style.RESET_ALL}?: '))
        if statchoice == 'o':
            ava.remove(roomchoice)              #
            occ.append(roomchoice)              #
            file_ava = open('ava.txt','w')      #
            file_occ = open('occ.txt','w')      #
            for x in ava:                       # Append and remove lists
                file_ava.write(x + '\n')        # Also, log the changes into external storage files
            for x in occ:                       # 
                file_occ.write(x + '\n')        # 
            file_ava.close()                    #
            file_occ.close()                    #
            print('\nRoom status changed successfully!')
            print(f'Room {roomchoice} is now {Fore.RED}{Style.BRIGHT}OCCUPIED{Style.RESET_ALL}.')
        elif statchoice == 'r':
            ava.remove(roomchoice)              
            res.append(roomchoice)
            file_ava = open('ava.txt','w')
            file_res = open('res.txt','w')   
            for x in ava:                       
                file_ava.write(x + '\n')        
            for x in res:
                file_res.write(x + '\n')
            file_ava.close()
            file_res.close()
            print('\nRoom status changed successfully!')
            print(f'\nRoom {roomchoice} is now {Fore.YELLOW}{Style.BRIGHT}RESERVED{Style.RESET_ALL}.')
        returnorend()
    elif roomchoice in occ:   #Changing room status if room is already occupied
        print(f'\nRoom {roomchoice} is {Fore.RED}{Style.BRIGHT}OCCUPIED{Style.RESET_ALL}.')
        statchoice = str.lower(input(f'Do you want to make it {Fore.GREEN}{Style.BRIGHT}AVAILABLE{Style.RESET_ALL}? Enter Y for {Fore.GREEN}{Style.BRIGHT}yes{Style.RESET_ALL} or N for {Fore.RED}{Style.BRIGHT}no{Style.RESET_ALL}: '))
        while statchoice not in ['y','n']:  #Input validation
            print('\n----- INVALID INPUT -----')
            print('Please re-enter your choice.\n')
            statchoice=str.lower(input(f'Do you want to make it {Fore.GREEN}{Style.BRIGHT}AVAILABLE{Style.RESET_ALL}? Enter Y for {Fore.GREEN}{Style.BRIGHT}yes{Style.RESET_ALL} or N for {Fore.RED}{Style.BRIGHT}no{Style.RESET_ALL}: '))
        if statchoice == 'y':
            occ.remove(roomchoice)
            ava.append(roomchoice)
            file_ava = open('ava.txt','w')
            file_occ = open('occ.txt','w')
            for x in ava:
                file_ava.write(x + '\n')
            for x in occ:
                file_occ.write(x + '\n')    
            file_ava.close()
            file_occ.close()
            print('\nRoom status changed successfully!')
            print(f'\nRoom {roomchoice} is now {Fore.GREEN}{Style.BRIGHT}AVAILABLE{Style.RESET_ALL}.')
        elif statchoice == 'n':
            print('\nRoom status remained.')
        returnorend()  
    elif roomchoice in res:   #Changing room status if room is already reserved
        print(f'\nRoom {roomchoice} is {Fore.YELLOW}{Style.BRIGHT}RESERVED{Style.RESET_ALL}.')
        statchoice = str.lower(input(f'Do you want to make it {Fore.RED}{Style.BRIGHT}OCCUPIED (O){Style.RESET_ALL} or {Fore.GREEN}{Style.BRIGHT}AVAILABLE (A){Style.RESET_ALL}?: '))
        while statchoice not in ['a','o']:  #Input validation
            print('\n----- INVALID INPUT -----')
            print('Please re-enter your choice.\n')
            statchoice = str.lower(input(f'Do you want to make it {Fore.RED}{Style.BRIGHT}OCCUPIED (O){Style.RESET_ALL} or {Fore.GREEN}{Style.BRIGHT}AVAILABLE (A){Style.RESET_ALL}?: '))
        if statchoice == 'o':
            res.remove(roomchoice)
            occ.append(roomchoice)
            file_occ = open('occ.txt','w')
            file_res = open('res.txt','w')
            for x in res:
                file_res.write(x + '\n')
            for x in occ:
                file_occ.write(x + '\n')
            file_occ.close()
            file_res.close()
            print('\nRoom status changed successfully!')
            print(f'\nRoom {roomchoice} is now {Fore.RED}{Style.BRIGHT}OCCUPIED{Style.RESET_ALL}.')
        elif statchoice == 'a':
            res.remove(roomchoice)
            ava.append(roomchoice)
            file_ava = open('ava.txt','w')
            file_res = open('res.txt','w')
            for x in ava:
                file_ava.write(x + '\n')
            for x in res:
                file_res.write(x + '\n')
            file_ava.close()
            file_res.close()
            print('\nRoom status changed successfully!')
            print(f'\nRoom {roomchoice} is now {Fore.GREEN}{Style.BRIGHT}AVAILABLE{Style.RESET_ALL}.')
        returnorend()
        
#Func showing list of rooms and their statuses
def roomlist():
    avasort = sorted(str(x) for x in ava)
    occsort = sorted(str(x) for x in occ)
    ressort = sorted(str(x) for x in res)
    prstat = f'''\n----------------------------------------------------------------------
        \n                         <LIST OF ROOMS>
        \n{Fore.GREEN}{Style.BRIGHT}Available room(s):{Style.RESET_ALL} {seperator.join(avasort)}
        \n{Fore.RED}{Style.BRIGHT}Occupied room(s):{Style.RESET_ALL}  {seperator.join(occsort)}
        \n{Fore.YELLOW}{Style.BRIGHT}Reserved room(s):{Style.RESET_ALL}  {seperator.join(ressort)}
        \n----------------------------------------------------------------------'''
    print(prstat)
    returnorend()
   
#Drawing hotel map:     
def hotelmap():
    
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
    
#Return to main menu or terminate program
def returnorend():
    print('\nDo you want to return to main menu or end your session?')
    menu = input('Enter 1 to return to main menu, or 2 to end your session: ')
    while menu not in ['1','2']:    #Input validation
        print('\n----- INVALID INPUT -----')
        menu = input('\nEnter 1 to return to main menu, or 2 to end your session: ')
    if menu == '1':
        mainmenu()
    elif menu == '2':
        print(f'\n{Fore.BLACK}{Back.WHITE}We hope to see you again! Good bye!{Style.RESET_ALL}')
        sys.exit()
      
#Menu mapping
def mainmenu():
    global menuchoice
    prmain = f'''\n----------------------------------------------------------------------
        \n                    {Style.BRIGHT}{Fore.RED}{Back.WHITE}WELCOME TO BUV SUNSHINE HOTEL{Style.RESET_ALL}
        \n                              MAIN MENU
        \n1. View list of rooms.
        \n2. Change room status.
        \n3. Show hotel map.
        \n4. Exit
        \n----------------------------------------------------------------------'''
    print(prmain)
    menuchoice = input('\nChoose your option: ')
    while menuchoice not in ['1','2','3','4']: #Input validation
        menuchoice = input('\nPlease enter a valid choice: ')
    if menuchoice == '1':
        roomlist()
    elif menuchoice == '2':
        roomstatchange()
    elif menuchoice == '3':
        hotelmap()
        mn = input('\nDo you want to return to main menu or end your session? \nEnter 1 to return to main menu, or 2 to end your session: ')
        while mn not in ['1','2']:    #Input validation
            print('\n----- INVALID INPUT -----')
            mn = input('\nDo you want to return to main menu or end your session? \nEnter 1 to return to main menu, or 2 to end your session: ')
        if mn == '1':
            tt.bye()
            mainmenu()
        elif mn == '2':
            print(f'\n{Fore.BLACK}{Back.WHITE}We hope to see you again! Good bye!{Style.RESET_ALL}')
            sys.exit()
    elif menuchoice == '4':
        print(f'\n----------------------------------------------------------------------\n{Fore.BLACK}{Back.WHITE}We hope to see you again! Good bye!{Style.RESET_ALL}')
        sys.exit()
        
#Program running              
mainmenu()
