#Make the variables o,e to be globals and print the result outside the func in the main method!!
a=int(input("Enter the number of numbers:"))
b=[]
c=[]
for i in range(a):
    print("Enter number",i+1,':',end='')
    b.append(int(input()))    

def rigourous_method():     #INCOMPLETE!!!
    for i in range(a):
        if b[0]<b[i]:
            b[i],b[0]=b[0],b[i]

def predefined_sort():
    b.sort()

def odd_or_even():
    o,e=0,0
    for i in range(a):
        if b[i]%2==0:
            e=e+1
        else:
            o=o+1
    print("\nNumber of odd numbers:",o)
    print("Number of even numbers:",e)

    
odd_or_even()               #odd or even

predefined_sort()           #sort ascending order

print("\nGiven numbers in ascending order:")
for i in range(a):
    print(b[i])



