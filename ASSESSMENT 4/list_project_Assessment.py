fruit_name=[]

fruit_quantity=[]

fruit_price=[]

print("\t\t\tWelcome Fruit Market")

menu="""
            1) Press 1 For Manager
            2) Press 2 For Customer
        """
    
print(menu)

user_choice=int(input("Select Your Role:"))

status=True


while status:
    

    if user_choice==1:
        # print("\t\tFruit Market Manager")
        user_status=True
        
        menu="""
             1) Press 1 For Add Fruit Stock
             2) Press 2 For View Fruit Stock
             3) Press 3 For Update Fruit Stock
            """
    
        print(menu)

        user_choice1=int(input("Select Your Role:"))

        if user_choice1==1:
            user_status=True
            print("\t\t\tFruit Market Manager")
            while user_status:

                name=input("Enter Fruit name:")
                fruit_name.append(name)
                quantity=input("Enter Quantity(In Kg):")
                fruit_quantity.append(quantity)
                price=int(input("Enter Price(For Kg):"))
                fruit_price.append(price)
                
                


                choice=input("Do You Want To add more account? press y for yes and n for no:")
                if choice=='y' or choice=='Y':
                    user_status=True

                else:
                    user_status=False

        elif user_choice1==2:
            
            print("View Fruit Stock")
            for i in range(0,len(fruit_name)):
                print(f"::\nFruit Name: {fruit_name[i]} \nFruit Quantity : {fruit_quantity[i]}\nFruit Price : {fruit_price[i]} ")
        
        elif user_choice1==3:
            # user_status=True
            name=input("Enter Fruit name:")
            fruit_name.append(name)
            quantity=input("Enter Quantity(In Kg):")
            fruit_quantity.append(quantity)
            price=int(input("Enter Price(For Kg):"))
            fruit_price.append(price)

            choice=input("Do You Want To add more account? press y for yes and n for no:")
            if choice=='y' or choice=='Y':
                    user_status=True

            else:
                    user_status=False
   

        else:
            print("Thank You For Visiting Our Shop")
            status=False
    else:
         print("Please  Enter First Manager Panel.....\n Please Try Again!!!!!")
         status=False