x=int(input("Enter number:"))

c=0
for i in range(1,x+1):
    if x%i==0:
        print("factor",c+1,":",i)
        c=c+1

print("Total number of factors:",c)
