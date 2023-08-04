mystr=input("Enter a String:")

if len(mystr)<3:
    print("Unchanged",mystr)

if mystr.endswith('ing'):
    mystr+='ly'

elif len(mystr)>=3:
    mystr+='ing'

print(mystr)