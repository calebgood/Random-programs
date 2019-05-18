import os,time
day=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
mdoom=[3,28,14,4,9,6,11,8,5,10,7,12]
while True:
    entry=input('Enter a date in DD/MM/YYYY format:')
    date,month,year = map(int,entry.split('/'))
    centdoom=[3,2,0,5]
    a=centdoom[((year//100)%4)-3]
    b=(year%100)//12
    c=(year%100)%12
    d=c//4
    e=a+b+c+d
    if year%4==0:
        mdoom[0],mdoom[1]=4,29
    ddoom=e%7
    r=mdoom[month-1]
    r=r%7
    r=ddoom-r
    date=date%7
    print(day[(r+date)%7])
    time.sleep(1.7)
    os.system('cls')
