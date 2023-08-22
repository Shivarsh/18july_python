mylist=[]

n=int(input('How Many items do you want to enter?:'))

for items in range(n):
    el=input("Enter The Elements:")
    mylist.append(el)

print(mylist)
if mylist==[]:
    print('Empty List')
else:
    print('List is not empty')