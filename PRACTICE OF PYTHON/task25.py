name=input("Enter Your Name:")
Maths=int(input("Maths marks:"))
English=int(input("English Marks:"))
Gujarati=int(input("Gujarati Marks:"))
Social_Science=int(input("Social_Science Marks:"))
Science=int(input("Science Marks:"))

total=Maths+English+Gujarati+Social_Science+Science
print("Total=",total)

per=total/5
print("Persentage:",per)

if per>=70:
    print("Result: Distinction")

elif per>=60:
    print("Result: First Class")

elif per>=50:
    print("Result: Second Class ")

elif per>=40:
    print("Result: Pass Class")

else:
    print("Result : Fail")
    





