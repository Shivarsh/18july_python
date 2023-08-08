stock={}  #Declare blank dictionary

print("\t\t\t\tFruit Market")

menu="""
            1)Fruit Manager
            2)Customer
            
        """
    
print(menu)

choice=int(input("Enter Your Choice:"))
    
status=True


while status:
    
    
    if choice==1:
                
                fruit_manager_status=True
                menu1="""
                    1) Press 1 For Add Fruit Stock
                    2) Press 2 For View Fruit Stock
                    3) Press 3 For Update Fruit Stock
                """
        
                print(menu1)

                user_choice1=int(input("Select Your Role:"))


                if user_choice1==1:
                    user_status=True
                    while user_status:

                        spec={}   #declare dictionary for specification or nested dictionary
                        print("\t\t\tADD FRUIT STOCK")

                    # accept product and product details from product manager
                        fruit_name=input("Enter The Fruit Name:")
                        fruit_qty=int(input('Enter The Fruit Quantity(in kg):'))
                        fruit_price=int(input('Enter The Fruit Price(per kg):'))

                    # creating nested dictionary
                        spec['qty']=fruit_qty
                        spec['price']=fruit_price

                    #creating outer dictionary
                        stock[fruit_name]=spec   #{laptop: {'qty':5,'price':50000}}
                        print(stock)


                        manager_choice=input("Do you Want to add more fruit?:")
                        if manager_choice=='y' or manager_choice=='Y':
                            user_status=True
                        else:
                            user_status=False
                elif user_choice1==2:
                    print(stock)
                    print("CUSTOMER")
                    
                elif user_choice1==3:
                    spec={}   #declare dictionary for specification or nested dictionary
                    print("\t\t\tFruit Market Manager")

                    # accept product and product details from product manager
                    fruit_name=input("Enter The Fruit Name:")
                    fruit_qty=int(input('Enter The Fruit Quantity(in kg):'))
                    fruit_price=int(input('Enter The Fruit Price(per kg):'))

                    # creating nested dictionary
                    spec['qty']=fruit_qty
                    spec['price']=fruit_price

                    #creating outer dictionary
                    stock[fruit_name]=spec   #{laptop: {'qty':5,'price':50000}}
                    print(stock)


                    manager_choice=input("Do you Want to add more fruit?:")
                    if manager_choice=='y' or manager_choice=='Y':
                            user_status=True
                    else:
                            fruit_manager_status=False
                
            
                else:
                        print("Thank You For Visiting Our Shop..")
                        status=False                    
    else:
        print("Error!!!! Please Enter First Manager Department....\n Please try again later")
        status=False
        