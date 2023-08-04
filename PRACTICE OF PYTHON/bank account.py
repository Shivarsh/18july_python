print("\t \t \t|| WELCOME TO VAGHELA'S BANK ||")

print("Create Your Account! Please Fill The Details...")

name=input("Enter Your Name:")
address=input("Enter your Address:")


print("What Kind Of Account Do You Want To Open || Savings or Current")

account_type=input("Enter Your Account Type:")

print("Your Account Number is 123456789.")
print("Create Your Password Like This: name@123")

password=input(" ")

diposit=int(input("How Much Money Do You Want To Add *Minimum Amount For Diposit is 3000\n"))
if diposit>=3000:
    print("Do You Want To Use Our Service?")
    choice=int(input("|| Yes=Press 1 OR No=Press 2||\n"))
    if choice==1:
            password1=input("Enter Your Password:\n")
            if password==password1:
                print("******What Did You Want To?******")
                print("Press.1. To Diposit A Amount")
                print("Press.2. To Withdraw A Amount")
                print("Press.3. To Exit")
                print("*********************************")
                choice1=int(input("Enter Your Choice:"))
                if choice1==1:
                    print("You Chooses To Diposit A Amount")
                    amount=int(input("Enter Your Amount:"))
                    print("After Diposit Your Balance is:",diposit+amount+0.01)
                elif choice1==2:
                    print("You Chooses To Withdraw A Amount")
                    amount1=int(input("Enter Your Amount:"))
                    if amount1<=diposit:
                        print("After Withdraw Your Balance is:",diposit-amount1+0.01)
                    else:
                        print("::Invalid Input::")
                else:
                    print("You Chooses Exit!")
            else:
                print("Your Password Does Not Match !!!")
    elif choice==2:
                print("\n Thank You For Visit!!")
    else:
                print("Invalid Option!!")     
else:
    print("Invalid input")   