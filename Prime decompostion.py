x=int(input("Enter number:"))
c=[]    #load the exponential powers here
b=[]    #load the primes here
i,k,f=0,0,2
l=100
def primes(i,n):            #returns all primes between i and n
    primes = []
    for possiblePrime in range(i,n+1): 
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return(primes)

while x!=1:
    try:
        while x%b[k]==0:            #extract every prime from the number and store their resp exp powers
            i+=1                    #counts the power of the prime stored in b[k]
            x=x//b[k]               #Removes the prime number from the given number
        k+=1
        c.append(i)
        i=0
    except IndexError:              #if list of primes are not enough...add more of them
            b=b+primes(f,l)         
            l+=10000

print("Prime Numbers:    ",[b[i] for i in range(len(c)) if c[i]!=0])   #prints the primes    
c=[c[i] for i in range(len(c)) if c[i]!=0]        
print("Respective Powers:",c)                                          #prints their respective powers


