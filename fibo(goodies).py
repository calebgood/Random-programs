def fib(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
def fib1(n):   # return Fibonacci series up to n terms
    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(a)
        a, b = b, a+b
    return result
def fib2(n):    # writes Fibonacci series up to n terms
    a,b=0,1
    for i in range(n):
        b,a=a+b,b
        print(a)
a=int(input("Enter number:"))
#print(fib(a))
#fib2(a)
b=fib1(a)
print('value    no of digits')
for i in range(a):  #finding number of digits in each number of sequence
    x=0
    while b[i]/10!=0:
        x=x+1
        b[i]=int(b[i]/10)
    print(x,'         ',i+1)   
