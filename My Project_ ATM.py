#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('Welcome to Mayur Bank ATM')
restart='y' 
chances=3
balance=1010.10
while chances >= 0:
    pin=int(input('Please Enter You 4 Digit Pin: '))
    if pin == 1234:
        print('You Entered Your Pin Correctly\n')
        while restart not in ('n', 'NO', 'no', 'N'):
            print('Please Press 1 For Your Balance\n')
            print('Please Press 2 To Make a Withdrawl\n')
            print('Please Press 3 To Diposite\n')
            print('Please Press 4 To Get Return Your Card\n')
            option = int(input('What Would you like to choose?'))
            if option==1:
                print('Your Balance is Rs', balance, '\n')
                restart=input('Would You you like to do any other Transaction? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                break
            elif option == 2:
                option2 = 'y'
                withdrawl=float( input('How Much Would you like to withdraw? \nRs10/Rs20/Rs40/Rs60/Rs80/Rs100 for other enter 1: '))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance=balance-withdrawl
                    print("\nYour Balance is now Rs", balance)
                    restart=input('Would You you like to do any other Transaction?') 
                    if restart in ('n', 'NO', 'no', 'N'):
                        print('Thank You')
                    break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print('Invalid Amount, Please Re-try\n')
                    restart = 'y'
                elif withdrawl == 1:
                    withdrawl=float(input('Please Enter Desired amount:'))
            elif option == 3:
                Pay_in=float(input('How Much Would You Like To Diposite?'))
                balance = balance + Pay_in
                print("\nYour Balance is now Rs", balance)
                restart=input('Would You you like to do any other Transaction? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                break
            elif option == 4:
                print('Please wait while your card is Returned... \n')
                print('Thank you for your service')
                break
            else:
                print('Please Enter a correct number. \n')
                restart="y" 
    elif pin!= '1234':
        print('Incorrect Password')
        chances=chances - 1
        if chances == 0:
            print("\nNo more tries")
            break                


# In[ ]:




