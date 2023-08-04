s1=int(input("Enter Side 1:"))
s2=int(input("ENter Side 2:"))
s3=int(input("ENter Side 3:"))

if s1==s2 and s2==s3:
    print("Triangle is equilateral")

elif s1==s2 or s2==s3 or s1==s3:
    print("Triangle is isosceles")

else:
    print("Triangle is Scalene")