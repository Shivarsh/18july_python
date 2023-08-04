print(".....................WELCOME TO THE ATM PROVIDE BY STATE BANK OF INDIA.....................\n")
print("::Please Set PIN Number::")



pin=int(input("Generate Your PIN:"))

print("press 1. to Diposit...\n")
print("press 2. to withdraw...\n")
print("press 3. to cheak a balance...\n")
print("press 4. to Exit...\n")

pin1=int(input("Enter Your PIN:"))

if pin==pin1:
        print("press 1. to Diposit...\n")
        print("press 2. to withdraw...\n")
        print("press 3. to cheak a balance...\n")
        print("press 4. to Exit...\n")
        choice=int(input("Enter Your choice:"))
        if choice==1:
            print("This is your  account balance :50000\n")
            # print("Enter your amount for diposit:\n")
            # print("your balance after diposit :\n")
            diposit=int(input("Enter Your Amount For Diposit:"))
            balance=50000+diposit
            print("Balance After Diposit:",balance)
        elif choice==2:
            print("This is your account balance :50000\n")
            withdraw=int(input("Enter Your Amount Of Withdraw:"))
            balance=50000-withdraw
            if balance>withdraw:
                    print("After Withdaw Your Balance Is:",balance)

            else:
                    print("Please Enter Valid Amount!!")
        elif choice==3:
            print("This Is  Your Account Balance: 50000\n")
        else:
            print("Thank You For Visit....")
else:
      print("Pin Does not match!")

        