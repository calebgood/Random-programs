a=['zero','one','two','three','four','five','six','seven','eight','nine']
b=['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
c=['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
k=[]
x=0
r=str()
while True:
    no=int(input("Enter a number:"))
    while no>0:
        x+=1
        k.append(no%10)
        no=int(no/10)
    k.reverse()
    def two_find():
            if k[x-2]==1 and k[x-1]!=0:
                r=b[k[x-1]-1]
            elif k[x-2]>=1 and k[x-1]==0:
                r=c[k[x-2]-1]
            elif k[x-2]>1 and k[x-1]>0:
                r=c[k[x-2]-1]+' '+a[k[x-1]]
            elif k[x-2]==0 and k[x-1]!=0:
                r=a[k[x-1]]
            elif k[x-2]==0 and k[x-1]==0:
                r=''
            return(r)
    if x>=1:
        r=a[k[x-1]]
    if x>=2:
        if k[x-2]!=0 or k[x-1]!=0:
            r=two_find()   
    if x>=3:     
        if k[x-2]==0 and k[x-1]==0:
            r=a[k[x-3]]+' hundred'
        else:
            r=a[k[x-3]]+' hundred and '+ r
    if x>=4:        
        if k[x-3]!=0 or k[x-2]!=0:
           r=a[k[x-4]]+' thousand '+r
        elif k[x-3]==0 and k[x-2]!=0:
           r=a[k[x-4]]+' thousand and'+two_find()
        elif k[x-3]==0 and k[x-2]==0 and k[x-1]==0:
            r=a[k[x-4]]+' thousand '       
    '''if x>=5:        
       if k[x-4]!=0 or k[x-3]!=0: 
            r=c[k[x-5]-1]+' '+ r
       if k[x-5]==1:
           r=b[k[x-4]]+' thousand '+r
       else:
            r=c[k[x-5]-1]+' thousand ' 
        
    if x>=6:
        for i in range(6,1,-1):
            if k[x-i]!=0:
                r=a[k[x-5]]+' lakh '+r
                break
    if x>=7:
        for i in range(7,1,-1):
            if k[x-i]!=0:
                r=a[k[x-5]]+' crore '+r
                break
    '''
    print("Your number is: "+str(r))
    k=[]
    r=''
    x=0
