from googletrans import Translator  
import pysrt
translator = Translator()
#Fill here
Filename="test"
OutputLang="ja"
InputLang="en"
#Opening file
subs = pysrt.open(Filename+".srt")
#Detecting Input Lang
if InputLang=="":
    InputLang=translator.detect(subs[0].text).lang
print("Detected Language:",InputLang)
#Translating...
for i in range(len(subs)):
    subs[i].text=translator.translate(subs[i].text,dest=OutputLang,src=InputLang).text
    if i%5==0:
        print("line:",i+1,"done...")
#Saving as new file
print("saving...")
subs.save(Filename+"-edit.srt", encoding='utf-8')
