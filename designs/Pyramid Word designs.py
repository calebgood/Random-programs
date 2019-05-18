from math import factorial 
n=int(input("Enter a number:"))
a,b,j=1,1,0
k,x=n,1
for i in range(n):
        j=k-i-1
        while j>0:
                print(end='\t')
                j-=1          
        while a<=x:
                print('a',end='\t')         
                a+=1
        print()
        a=1
        x=x+2
        
