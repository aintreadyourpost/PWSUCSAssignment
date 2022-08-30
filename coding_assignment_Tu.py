#Import libs
from colorama import Fore, Style, Back
import sys

#Create global variables
ava = [] 
occ = []
res = []
seperator=', '

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

#Func changing the status of the room
def roomstatchange():
    rooml = ava + res + occ
    avasort = sorted(str(x) for x in ava)   
    occsort = sorted(str(x) for x in occ)
    ressort = sorted(str(x) for x in res)
    print('\n----------------------------------------------------------------------')
    print('\n                         <LIST OF ROOMS>')
    print(f'\n{Fore.GREEN}{Style.BRIGHT}Available room(s):{Style.RESET_ALL}',seperator.join(avasort))
    print(f'\n{Fore.RED}{Style.BRIGHT}Occupied room(s):{Style.RESET_ALL} ',seperator.join(occsort))
    print(f'\n{Fore.YELLOW}{Style.BRIGHT}Reserved room(s):{Style.RESET_ALL} ',seperator.join(ressort))
    print('\n----------------------------------------------------------------------')
    roomchoice = str.lower(input('\nPlease enter the room that you want to change: '))
    while roomchoice not in rooml:    #Input validation
        print('\n----- INVALID INPUT -----')
        print('Please re-enter your choice.')
        roomchoice = str.lower(input('\nPlease enter the room that you want to change: '))
    if roomchoice in ava:   #Changing room status if room is already availble
        print('\nRoom',roomchoice,f'is {Fore.GREEN}{Style.BRIGHT}AVAILABLE{Style.RESET_ALL}.')
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
                file_ava.write(x +'\n')         # Also, log the changes into external storage files
            for x in occ:                       # 
                file_occ.write(x +'\n')         # 
            file_ava.close()                    #
            file_occ.close()                    #
            print('\nRoom status changed successfully!')
            print('Room',roomchoice,f'is now {Fore.RED}{Style.BRIGHT}OCCUPIED{Style.RESET_ALL}.')
            returnorend()
        if statchoice == 'r':
            ava.remove(roomchoice)              
            res.append(roomchoice)
            file_ava = open('ava.txt','w')
            file_res = open('res.txt','w')   
            file_ava.write('')
            file_res.write('')
            for x in ava:                       
                file_ava.write(x + '\n')        
            for x in res:
                file_res.write(x + '\n')
            file_ava.close()
            file_res.close()
            print('\nRoom status changed successfully!')
            print('\nRoom',roomchoice,f'is now {Fore.YELLOW}{Style.BRIGHT}RESERVED{Style.RESET_ALL}.')
            returnorend()
    if roomchoice in occ:   #Changing room status if room is already occupied
        print('\nRoom',roomchoice,f'is {Fore.RED}{Style.BRIGHT}OCCUPIED{Style.RESET_ALL}.')
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
                file_occ.writelines(x +'\n')    
            file_ava.close()
            file_occ.close()
            print('\nRoom status changed successfully!')
            print('\nRoom',roomchoice,f'is now {Fore.GREEN}{Style.BRIGHT}AVAILABLE{Style.RESET_ALL}.')
            returnorend()
        if statchoice == 'n':
            print('\nRoom status remained.')
            returnorend()  
    if roomchoice in res:   #Changing room status if room is already reserved
        print('\nRoom',roomchoice,f'is {Fore.YELLOW}{Style.BRIGHT}RESERVED{Style.RESET_ALL}.')
        statchoice = str.lower(input(f'Do you want to make it {Fore.RED}{Style.BRIGHT}OCCUPIED (O){Style.RESET_ALL} or {Fore.GREEN}{Style.BRIGHT}AVAILABLE (A){Style.RESET_ALL}?: '))
        while statchoice not in ['a','o']:  #Input validation
            print('\n----- INVALID INPUT -----')
            print('Please re-enter your choice.\n')
            statchoice=str.lower(input(f'Do you want to make it {Fore.RED}{Style.BRIGHT}OCCUPIED (O){Style.RESET_ALL} or {Fore.GREEN}{Style.BRIGHT}AVAILABLE (A){Style.RESET_ALL}?: '))
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
            print('\nRoom',roomchoice,f'is now {Fore.RED}{Style.BRIGHT}OCCUPIED{Style.RESET_ALL}.')
            returnorend()
        if statchoice == 'a':
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
            print('\nRoom',roomchoice,f'is now {Fore.GREEN}{Style.BRIGHT}AVAILABLE{Style.RESET_ALL}.')
            returnorend()
    
#Func showing list of rooms and their statuses
def roomlist():
    avasort = sorted(str(x) for x in ava)
    occsort = sorted(str(x) for x in occ)
    ressort = sorted(str(x) for x in res)
    print('\n----------------------------------------------------------------------')
    print('\n                         <LIST OF ROOMS>')
    print(f'\n{Fore.GREEN}{Style.BRIGHT}Available room(s):{Style.RESET_ALL}',seperator.join(avasort))
    print(f'\n{Fore.RED}{Style.BRIGHT}Occupied room(s):{Style.RESET_ALL} ',seperator.join(occsort))
    print(f'\n{Fore.YELLOW}{Style.BRIGHT}Reserved room(s):{Style.RESET_ALL} ',seperator.join(ressort))
    print('\n----------------------------------------------------------------------')
    returnorend()
    
#Return to main menu or terminate program
def returnorend():
    print('\nDo you want to return to main menu or end your session?')
    menu = input('Enter 1 to return to main menu, or 2 to end your session: ')
    while menu not in ['1','2']:    #Input validation
        print('\n----- INVALID INPUT -----')
        menu = input('\nEnter 1 to return to main menu, or 2 to end your session: ')
    if menu == '1':
        mainmenu()
    if menu == '2':
        print(f'\n{Fore.BLACK}{Back.WHITE}We hope to see you again! Good bye!{Style.RESET_ALL}')
        sys.exit()
      
#Menu mapping
def mainmenu():
    global menuchoice
    print('\n----------------------------------------------------------------------')
    print(f'\n                    {Style.BRIGHT}{Fore.RED}{Back.WHITE}WELCOME TO BUV SUNSHINE HOTEL{Style.RESET_ALL}')
    print('\n                              MAIN MENU')
    print('\n1. View list of rooms.')
    print('\n2. Change room status.')
    print('\n3. Show hotel map.')
    print('\n4. Exit')
    print('\n----------------------------------------------------------------------')
    menuchoice=input('\nChoose your option: ')
    while menuchoice not in ('1','2','3','4'): #Input validation
        menuchoice=input('\nPlease enter a valid choice: ')
        break
    if menuchoice == '1':
        roomlist()
    if menuchoice == '2':
        roomstatchange()
    if menuchoice == '3': 
        pass
    if menuchoice == '4':
        print('\n----------------------------------------------------------------------')
        print(f'\n{Fore.BLACK}{Back.WHITE}We hope to see you again! Good bye!{Style.RESET_ALL}')
        sys.exit()
        
#Program running              
mainmenu()
