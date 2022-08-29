#Import libs
from colorama import Fore, Style, Back

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
    print('\n\t\t\t<LIST OF ROOMS>\n')
    print(f'{Fore.GREEN}{Style.BRIGHT}Available room(s):{Style.RESET_ALL}',seperator.join(avasort))
    print(f'\n{Fore.RED}{Style.BRIGHT}Occupied room(s):{Style.RESET_ALL} ',seperator.join(occsort))
    print(f'\n{Fore.YELLOW}{Style.BRIGHT}Reserved room(s):{Style.RESET_ALL} ',seperator.join(ressort))
    print('\n----------------------------------------------------------------------')
    a=str.lower(input('\nPlease enter the room that you want to change: '))
    while a in ava:
        print('\nRoom',a,f'is {Fore.GREEN}{Style.BRIGHT}AVAILABLE{Style.RESET_ALL}.')
        b=str.lower(input(f'Do you want to make it {Fore.RED}{Style.BRIGHT}OCCUPIED (O){Style.RESET_ALL} or {Fore.YELLOW}{Style.BRIGHT}RESERVED (R){Style.RESET_ALL}?: '))
        if b=='o':
            ava.remove(a)           
            occ.append(a)
            print('\nRoom status changed successfully!')
            print('Room',a,f'is now {Fore.RED}{Style.BRIGHT}OCCUPIED{Style.RESET_ALL}.')
            returnorend()
            break
        if b=='r':
            ava.remove(a)
            res.append(a)
            print('\nRoom status changed successfully!')
            print('\nRoom',a,f'is now {Fore.YELLOW}{Style.BRIGHT}RESERVED{Style.RESET_ALL}.')
            returnorend()
            break
    while a in occ:
        print('\nRoom',a,f'is {Fore.RED}{Style.BRIGHT}OCCUPIED{Style.RESET_ALL}.')
        b=str.lower(input(f'Do you want to make it {Fore.GREEN}{Style.BRIGHT}AVAILABLE{Style.RESET_ALL}? Enter Y for {Fore.GREEN}{Style.BRIGHT}yes{Style.RESET_ALL} or N for {Fore.RED}{Style.BRIGHT}no{Style.RESET_ALL}: '))
        if b=='y':
            occ.remove(a)
            ava.append(a)
            print('\nRoom status changed successfully!')
            print('\nRoom',a,f'is now {Fore.GREEN}{Style.BRIGHT}AVAILABLE{Style.RESET_ALL}.')
            returnorend()
            break
        if b=='n':
            print('Room status remained.')
            returnorend()
            break
    while a in res:
        print('\nRoom',a,f'is {Fore.YELLOW}{Style.BRIGHT}RESERVED{Style.RESET_ALL}.')
        b=str.lower(input(f'Do you want to make it {Fore.RED}{Style.BRIGHT}OCCUPIED (O){Style.RESET_ALL} or {Fore.GREEN}{Style.BRIGHT}AVAILABLE (A){Style.RESET_ALL}?: '))
        if b=='o':
            res.remove(a)
            occ.append(a)
            print('\nRoom status changed successfully!')
            print('\nRoom',a,f'is now {Fore.RED}{Style.BRIGHT}OCCUPIED{Style.RESET_ALL}.')
            returnorend()
            break
        if b=='a':
            res.remove(a)
            ava.append(a)
            print('\nRoom status changed successfully!')
            print('\nRoom',a,f'is now {Fore.GREEN}{Style.BRIGHT}AVAILABLE{Style.RESET_ALL}.')
            returnorend()
            break
    if (a not in ava or a not in occ or a not in res):
        print('\n----- INVALID INPUT -----')
        roomstatchange()
        
#Func showing list of rooms and their statuses
def roomlist():
    avasort=sorted(str(x) for x in ava)
    occsort=sorted(str(x) for x in occ)
    ressort=sorted(str(x) for x in res)
    print('\n----------------------------------------------------------------------')
    print('\n\t\t\t<LIST OF ROOMS>\n')
    print(f'{Fore.GREEN}{Style.BRIGHT}Available room(s):{Style.RESET_ALL}',seperator.join(avasort))
    print(f'\n{Fore.RED}{Style.BRIGHT}Occupied room(s):{Style.RESET_ALL}',seperator.join(occsort))
    print(f'\n{Fore.YELLOW}{Style.BRIGHT}Reserved room(s):{Style.RESET_ALL}',seperator.join(ressort))
    print('\n----------------------------------------------------------------------')
    returnorend()
    
#Return to main menu or terminate program
def returnorend():
      while True:
          print('\nDo you want to return to main menu or end your session?')
          menu=input('Enter 1 to return to main menu, or 2 to end your session: ')
          if menu=='1':
              mainmenu()
              break
          elif menu=='2':
              print(f'\n{Fore.BLACK}{Back.WHITE}We hope to see you again! Good bye!{Style.RESET_ALL}')
              quit
              break
          else:
              print('\n----- INVALID INPUT -----')
          
#Menu mapping
def mainmenu():
    global menuchoice
    print('\n----------------------------------------------------------------------')
    print(f'\n\t\t\t\t{Style.BRIGHT}{Fore.RED}{Back.WHITE}WELCOME TO BUV SUNSHINE HOTEL{Style.RESET_ALL}\n') #Main menu
    print('\t\t\t\t\t\t MAIN MENU\n')
    print('1. View list of rooms.\n')
    print('2. Change room status.\n')
    print('3. Show hotel map.\n')
    print('4. Exit')
    print('\n----------------------------------------------------------------------')
    menuchoice=input('\nChoose your option: ')
    print('')
    while menuchoice not in ('1','2','3','4'): #Input validation
        menuchoice=input('Please enter a valid choice: ')
    if menuchoice=='1':
        roomlist()
    if menuchoice=='2':
        roomstatchange()
    if menuchoice=='3': 
        pass
    if menuchoice=='4':
        print(f'{Fore.BLACK}{Back.WHITE}We hope to see you again! Good bye!{Style.RESET_ALL}')
        quit
        
#Program running              
mainmenu()