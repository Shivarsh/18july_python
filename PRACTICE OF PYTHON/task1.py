s1=int(input("Enter Your Marks:"))
s2=int(input("Enter Your Marks:"))
s3=int(input("Enter Your Marks:"))
s4=int(input("Enter Your Marks:"))
s5=int(input("Enter Your Marks:"))


total=s1+s2+s3+s4+s5
print("Total:",total)

per=total/5
if per>=70:
    print("Distinction")

elif per>=60:
    print("First Class")

elif per>=50:
    print("Second Class")

elif per>=40:
    print("Pass Class")

else:
    print("Fail")
