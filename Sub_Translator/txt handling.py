import time
import pysrt
full=str()
subs = pysrt.open("test.srt")
l=len(subs)
for k in range(0,5):
    for i in range((k*l)//5,((k+1)*l//5)):
        full=full+subs[i].text+"\n\n"
print(full)
print(subs.text)
