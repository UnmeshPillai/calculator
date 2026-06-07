while True:
    print("py calc ")

    num1 = int(input("enter the first number :" ))
    num2 = int(input("enter the second  number :" ))
    print("Fantastic! , Now choose an arithmatic operation :")
    print("M for multiplication")
    print("S for subtraction")
    print("D for division")
    print("A for addition")

    while True : 
        choice=input("")

        if choice == "m" or choice =="M":
            print("The result is :", num1*num2)
            break
        elif choice == "a" or choice =="A":
            print("The result is :", num1+num2)
            break
        elif choice == "d" or choice =="D":
            print("The result is :", num1/num2)
            break
        elif choice == "s" or choice =="S":
            print("The result is :", num1-num2)
            break
        else:
            print("please enter valid options")

          
    print("Would you like to continue again ?")
    opinion = input("Enter Y for yes and N for no:",   )
    if opinion.lower() == "y":

        print("Great!!, Let's start again!")
    else : 
        print("Thank You for your time ")
        break    

