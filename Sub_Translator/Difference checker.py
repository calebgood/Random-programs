import pysrt
a = pysrt.open("testen.srt")
b = pysrt.open('test.srt')
k=0
sh=[]
for i in range(len(a)):
    if a[i].text!=b[i].text:
        k+=1
        print("\n\n")
        print(a[i].text)
        print("\n")
        print(b[i].text)
        print("\n\n")
    else:
        sh.append(i)   

print("No of lines:",len(a),"or",len(b))
print("Different lines:",k)
print("Same lines:",len(sh))
if len(sh)<=10:
    for i in sh:
        print("line:",i)
        print(a[i].text,end="\n\n")


