def descendu(n):
    j,i=1,1
    j,x=n,0
    while i<=n:
        x=x+1
        while j>0:
            print(j,end='   ')
            j=j-1
        print(end='\n')
        i=i+1
        j=n+j-x
def ascend(n):
    j,i=1,1
    while i<=n:
        while j<=i:
            print(j,end='   ')
            j=j+1
        print(end='\n')
        i=i+1
        j=1       
def descend(n):
    j,i=1,1
    x=0
    while i<=n:
        while j<=n-x:
            print(j,end='   ')
            j=j+1
        print(end='\n')
        i=i+1
        j=1
        x=x+1
def ascendu(n):
    j,i,k=1,1,n
    while i<=n:
        while j<=i and j>0:
            print(k,end='   ')
            k=k-1
            j=j+1
        print(end='\n')
        k=n
        i=i+1
        j=1
ascend(5)
descend(5)     #Instead of printing variables u can create a string/list and use the array index as the variables 
ascendu(5)
descendu(5)
