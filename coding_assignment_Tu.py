#Import libs
from colorama import Fore, Style, Back
import sys

#Create global variables
ava=['101','102','103','104'] 
occ=['201','202','203','204']
res=['301','302','303','304']

seperator=', '

#Func changing the status of the room
def roomstatchange():
    avasort=sorted(str(x) for x in ava)
    occsort=sorted(str(x) for x in occ)
    ressort=sorted(str(x) for x in res)
    print('\n----------------------------------------------------------------------')
    print('\n                         <LIST OF ROOMS>')
    print(f'\n{Fore.GREEN}{Style.BRIGHT}Available room(s):{Style.RESET_ALL}',seperator.join(avasort))
    print(f'\n{Fore.RED}{Style.BRIGHT}Occupied room(s):{Style.RESET_ALL} ',seperator.join(occsort))
    print(f'\n{Fore.YELLOW}{Style.BRIGHT}Reserved room(s):{Style.RESET_ALL} ',seperator.join(ressort))
    print('\n----------------------------------------------------------------------')
    roomchoice=str.lower(input('\nPlease enter the room that you want to change: '))
    if roomchoice in ava:
        print('\nRoom',roomchoice,f'is {Fore.GREEN}{Style.BRIGHT}AVAILABLE{Style.RESET_ALL}.')
        statchoice=str.lower(input(f'\nDo you want to make it {Fore.RED}{Style.BRIGHT}OCCUPIED (O){Style.RESET_ALL} or {Fore.YELLOW}{Style.BRIGHT}RESERVED (R){Style.RESET_ALL}?: '))
        while statchoice not in ['o','r']:
            print('\n----- INVALID INPUT -----')
            print('Please re-enter your choice.')
            statchoice=str.lower(input(f'\nDo you want to make it {Fore.RED}{Style.BRIGHT}OCCUPIED (O){Style.RESET_ALL} or {Fore.YELLOW}{Style.BRIGHT}RESERVED (R){Style.RESET_ALL}?: '))
        if statchoice=='o':
            ava.remove(roomchoice)           
            occ.append(roomchoice)
            print('\nRoom status changed successfully!')
            print('Room',roomchoice,f'is now {Fore.RED}{Style.BRIGHT}OCCUPIED{Style.RESET_ALL}.')
            returnorend()
        if statchoice=='r':
            ava.remove(roomchoice)
            res.append(roomchoice)
            print('\nRoom status changed successfully!')
            print('\nRoom',roomchoice,f'is now {Fore.YELLOW}{Style.BRIGHT}RESERVED{Style.RESET_ALL}.')
            returnorend()
    if roomchoice in occ:
        print('\nRoom',roomchoice,f'is {Fore.RED}{Style.BRIGHT}OCCUPIED{Style.RESET_ALL}.')
        statchoice=str.lower(input(f'\nDo you want to make it {Fore.GREEN}{Style.BRIGHT}AVAILABLE{Style.RESET_ALL}? Enter Y for {Fore.GREEN}{Style.BRIGHT}yes{Style.RESET_ALL} or N for {Fore.RED}{Style.BRIGHT}no{Style.RESET_ALL}: '))
        while statchoice not in ['y','n']:
            print('\n----- INVALID INPUT -----')
            print('Please re-enter your choice.')
            statchoice=str.lower(input(f'\nDo you want to make it {Fore.GREEN}{Style.BRIGHT}AVAILABLE{Style.RESET_ALL}? Enter Y for {Fore.GREEN}{Style.BRIGHT}yes{Style.RESET_ALL} or N for {Fore.RED}{Style.BRIGHT}no{Style.RESET_ALL}: '))
        if statchoice=='y':
            occ.remove(roomchoice)
            ava.append(roomchoice)
            print('\nRoom status changed successfully!')
            print('\nRoom',roomchoice,f'is now {Fore.GREEN}{Style.BRIGHT}AVAILABLE{Style.RESET_ALL}.')
            returnorend()
        if statchoice=='n':
            print('\nRoom status remained.')
            returnorend()  
    if roomchoice in res:
        print('\nRoom',roomchoice,f'is {Fore.YELLOW}{Style.BRIGHT}RESERVED{Style.RESET_ALL}.')
        statchoice=str.lower(input(f'\nDo you want to make it {Fore.RED}{Style.BRIGHT}OCCUPIED (O){Style.RESET_ALL} or {Fore.GREEN}{Style.BRIGHT}AVAILABLE (A){Style.RESET_ALL}?: '))
        while statchoice not in ['r','a']:
            print('\n----- INVALID INPUT -----')
            print('Please re-enter your choice.')
            statchoice=str.lower(input(f'\nDo you want to make it {Fore.RED}{Style.BRIGHT}OCCUPIED (O){Style.RESET_ALL} or {Fore.GREEN}{Style.BRIGHT}AVAILABLE (A){Style.RESET_ALL}?: '))
        if statchoice=='o':
            res.remove(roomchoice)
            occ.append(roomchoice)
            print('\nRoom status changed successfully!')
            print('\nRoom',roomchoice,f'is now {Fore.RED}{Style.BRIGHT}OCCUPIED{Style.RESET_ALL}.')
            returnorend()
        if statchoice=='a':
            res.remove(roomchoice)
            ava.append(roomchoice)
            print('\nRoom status changed successfully!')
            print('\nRoom',roomchoice,f'is now {Fore.GREEN}{Style.BRIGHT}AVAILABLE{Style.RESET_ALL}.')
            returnorend()
        
#Func showing list of rooms and their statuses
def roomlist():
    avasort=sorted(str(x) for x in ava)
    occsort=sorted(str(x) for x in occ)
    ressort=sorted(str(x) for x in res)
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
    menu=input('Enter 1 to return to main menu, or 2 to end your session: ')
    while menu not in ['1','2']:
        print('\n----- INVALID INPUT -----')
        menu=input('\nEnter 1 to return to main menu, or 2 to end your session: ')
    if menu=='1':
        mainmenu()
    if menu=='2':
        print(f'\n{Fore.BLACK}{Back.WHITE}We hope to see you again! Good bye!{Style.RESET_ALL}')
        sys.exit()
      
#Menu mapping
def mainmenu():
    global menuchoice
    print('\n----------------------------------------------------------------------')
    print(f'\n                    {Style.BRIGHT}{Fore.RED}{Back.WHITE}WELCOME TO BUV SUNSHINE HOTEL{Style.RESET_ALL}') #Main menu
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
    if menuchoice=='1':
        roomlist()
    if menuchoice=='2':
        roomstatchange()
    if menuchoice=='3': 
        pass
    if menuchoice=='4':
        print('\n----------------------------------------------------------------------')
        print(f'\n{Fore.BLACK}{Back.WHITE}We hope to see you again! Good bye!{Style.RESET_ALL}')
        sys.exit()
        
#Program running              
mainmenu()