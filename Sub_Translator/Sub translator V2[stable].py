from googletrans import Translator  
import pysrt
translator = Translator()
full=str()
full_trans=str()
#Fill here
Filename="Avengers Infinity War (2018) [WEBRip] [1080p] [YTS.AM]"
OutputLang="en"
InputLang=""
a=50
#Opening file
subs = pysrt.open(Filename+".srt")
#Detecting Input Lang
if InputLang=="":
    InputLang=translator.detect(subs[0].text).lang
print("Detected Language:",InputLang)
if InputLang==OutputLang:
    OutputLang=input("Enter Output Language:")
print("Output Language:",OutputLang)
#Translating...
print("Started Translating:")
for k in range(0,a):
    for i in range((k*len(subs))//a,((k+1)*len(subs))//a):
        full=full+subs[i].text+"\n\n"
    full_trans+="\n\n"+translator.translate(full,dest=OutputLang,src=InputLang).text
    full=""
    print(k+1,"/",a,"parts Done")
full=full_trans.split('\n\n')

full.pop(0)

'''print(len(full),"or",len(subs))
print(full_trans,"\n\n")
print(full,"\n\n")
print(subs.text,"\n\n")'''


for i in range(len(subs)):
    subs[i].text=full[i]
#Saving as new file
print("saving...")
subs.save(Filename+"-"+OutputLang+".srt", encoding='utf-8')

