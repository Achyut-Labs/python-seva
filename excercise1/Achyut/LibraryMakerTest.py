import myMaths

def main():
    x = True
    while x:
       print('The Calculator.')
       c = int(input('enter you number for maths: '))
       d = int(input('enter you second number for maths: '))
    
       print('Addition: ',myMaths.myAddition(c,d) )
       print( 'Multiplication:', myMaths.myMultiplication(c,d))
       print('Division:', myMaths.myDivision(c,d))
       print('Sunbtraction:', myMaths.mySubtraction(c,d))
       a = input('Do you want to use the calculator again (Enter [y]es [n]o): ')
       if a == 'y' or 'Y':
           continue
       elif a == 'n' or 'N':
           x= False
       else:
           print('please inserst a valid value y or n')
        
           
           


    

    

if __name__ == '__main__':
    main()
    


