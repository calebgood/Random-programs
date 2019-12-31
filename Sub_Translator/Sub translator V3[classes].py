import sys
from googletrans import Translator  
import pysrt


class Trans:

    global translator
    global full
    global full_trans
    global OutputLang
    global InputLang
    global a
    global subs
    global Filename
    
    def __init__(self):
        self.accept()
        self.outlang("Japanese")
        self.save()
        
    def accept(self):
        global translator
        global full
        global full_trans
        global OutputLang
        global InputLang
        global a
        global subs
        global Filename

        Value ="test"
        translator = Translator()
        full=str()
        full_trans=str()
        Filename=Value
        InputLang="English"
        a=50
        subs = pysrt.open(Filename+".srt")
        #InputLang=translator.detect(subs[0].text).lang
        print(InputLang)
        print(Filename)
        InputLang=self.lang(InputLang)

    def outlang(self,text):
        global OutputLang
        OutputLang=self.lang(text)
        
    def lang(self,text):
        if text=="English":
            text="en"
        elif text=="Japanese":
            text="ja"
        elif text=="Korean":
            text="ko"
        return(text)

    def translate(self):
        global translator
        global full
        global full_trans
        global OutputLang
        global InputLang
        global a
        global subs
        global Filename


        #Translating...
        print("Started Translating:")

        for k in range(0,a):
            for i in range((k*len(subs))//a,((k+1)*len(subs))//a):
                full=full+subs[i].text+"\n\n"
            full_trans+="\n\n"+translator.translate(full,dest=OutputLang,src=InputLang).text
            full=""
            #self.progressBar.setProperty("value",((k+1)/a)*100)
            print(k+1,"/",a,"parts Done")
        full=full_trans.split('\n\n')

        full.pop(0)

        for i in range(len(subs)):
            subs[i].text=full[i]

    def save(self):
        global translator
        global full
        global full_trans
        global OutputLang
        global InputLang
        global a
        global subs
        global Filename

        print("saving...")
        subs.save(Filename+"-"+OutputLang+".srt", encoding='utf-8')

    def close_application(self):
        sys.exit()

if __name__=="__main__":
    
    app=Trans()
