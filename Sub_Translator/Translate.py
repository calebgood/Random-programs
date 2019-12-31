from googletrans import Translator  # Import Translator module from googletrans package

translator = Translator()

translated = translator.translate('안녕하세요') 

print(" Source Language:" + translated.src) 
# Output: Source Language: ko

print(" Translated string:" + translated.text)
# Output: Translated string: Good evening

translated = translator.translate('안녕하세요', src='ko') # Pass only source language
translated = translator.translate('안녕하세요', dest='en') # Pass only destination language
translated = translator.translate('안녕하세요', src='ko', dest='en') # Pass both source and destination


translated = translator.translate('안녕하세요', src='ko', dest='ja')

print(" Source Language:" + translated.src)
# Output: Source Language: ko

print(" Translated string:" + translated.text) 
# Output: Translated string: こんにちは

print(" Pronunciation:", translated.pronunciation)
# Output: Pronunciation: Kon'nichiwa​​​​


translatedList = translator.translate(['Hello Friends','Welcome on Codeproject',
'Have a good day'], dest='ja')

for translated in translatedList:
           print(translated.origin, '->', translated.text)




detected = translator.detect(' 皆さん、こんにちは')


print('Detected Language:', detected.lang, ' with confidence: ', detected.confidence)
