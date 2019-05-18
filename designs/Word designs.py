def ascend(a):
    n=len(a)-1
    j,i=0,0
    while i<=n:
        while j<=i:
            print(a[j],end='   ')
            j=j+1
        print(end='\n')
        i=i+1
        j=0

def descend(a):
    n=len(a)-1
    j,i=0,0
    x=0
    while i<=n:
        while j<=n-x:
            print(a[j],end='   ')
            j=j+1
        print(end='\n')
        i=i+1
        j=0
        x=x+1
b=str(input('Enter a String:'))
ascend(b)
descend(b)
