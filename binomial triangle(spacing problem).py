from math import factorial 
n=int(input("Enter a number:"))
a,b,j=1,1,0
k,x=n,1
u,v=0,0
def digits(n,r):        
        q=int(factorial(n)/(factorial(n-r)*factorial(r)))
        return(q)
for i in range(n):
        j=k-i-1
        while j>0:
                print(end='\t')
                j-=1          
        if x-1<3:
                while a<=x:
                        print(digits(i+1,u),end='\t')        
                        u+=1
                        a+=1
                x=x+2
        else:
                while a<=x-1:
                        print(digits(i+1,u),end='\t')        
                        u+=1
                        a+=1
                x=x+1
        print()
        a=1
        
        u=0


''' while v<=u:    #spacing problem
        print(end=' ')
        v+=1
        v=0'''
