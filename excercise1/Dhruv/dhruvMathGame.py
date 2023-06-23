import myMaths
<<<<<<< Updated upstream

def main():
    print("hello we are playing a math game")
    play=True

    while play:
        print("would you like play the game?")
        start=input("yes or no:")
        if start.lower() == "yes":
            a=int(input("Enter 1 number for maths:"))
            b=int(input("Enter another number for maths:"))
            print("sum of both numbers =")
            print( myMaths.myAddittion(a,b))
            print("product of both numbers=")
            print(myMaths.mymultipilycation(a,b))
            print("difference of both numbers=")
            print(myMaths.mySubtraction(a,b))
            print("Both numbers divided =")
            print(myMaths.myDivision(a,b))
         
        if start.lower() == "no":
            play=False
            
=======
def main():
    print("hello we are playing a math game")
play=True

while play:
    print("would you like play the game?")
    start=input("yes or no:")
    if start.lower=="yes":
        continue
    if start.lower=="no":
        set;play;False
        break
    a=int(input("Enter 1 number for maths:"))
    b=int(input("Enter another number for maths:"))
    print("sum of both numbers =")
    print( myMaths.myAddittion(a,b))
    print("product of both numbers=")
    print(myMaths.mymultipilycation(a,b))
    print("difference of both numbers=")
    print(myMaths.mySubtraction(a,b))
    print("Both numbers divided =")
    print(myMaths.myDivision(a,b))

>>>>>>> Stashed changes
if __name__=='__main__':
    main()
    
