from googletrans import Translator  
translator = Translator()
print(translator.translate('test sentence',dest='ja'))
