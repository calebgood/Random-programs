a=int(input("Enter a number:"))
b=[]
c=0
while a/10!=0:
    b.append(a%10)
    a=int(a/10)
for i in range(len(b)):
    c=c+b[i]
print("Sum of digits:",c)
