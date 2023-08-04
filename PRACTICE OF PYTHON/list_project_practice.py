account=[]

account_holder_name=[]

account_number=[]

account_balance=[]

account_withdraw=[]


status=True

while status:
    menu="""
            1) Press 1 For Bank Manager
            2) Press 2 For Customer
            3) Press 3 For Exit



        """
    
    print(menu)

    user_choice=int(input("Enter Your Choice:"))

    if user_choice==1:
        user_status=True

        while user_status:
            type=input("Enter The Account Type:")
            account.append(type)
            name=input("Enter Your Name:")
            account_holder_name.append(name)
            accnumber=int(input("Enter Account Number:"))
            account_number.append(accnumber)
            balance=int(input(" The Minimum Account Balance:"))
            account_balance.append(balance)
            withdraw=int(input("Minimum Withdrawal Balance:"))
            account_withdraw.append(withdraw)
            


            choice=input("Do You Want To add more account? press y for yes and n for no:")
            if choice=='y' or choice=='Y':
                user_status=True

            else:
                user_status=False

    elif user_choice==2:
        print("Customer Panel")

        for i in range(0,len(account)):
            print(f"Account:{account[i]}\n Account Holder Name: {account_holder_name[i]} \n Account Number : {account_number[i]}\nMinimum Balance:   {account_balance[i]} \nMinimum Withdrawal: {account_withdraw[i]}")

    else:
        print("Thank You For Visiting Our Bank")
        status=False
