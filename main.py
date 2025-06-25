import json

from deep_translator import GoogleTranslator
from iso639 import iter_langs
from time import sleep


def getLocales ():
  with open('langlist.json', 'r') as file:
    raw = file.read()
    locales = json.loads(raw)

  return locales



def translate_text( locale = 'en' ):
  result = GoogleTranslator(source='ru', target=locale).translate('Всем привет!')
  print(result)
  return result



def main ():
  locales = getLocales()

  for lc in locales:
    print(lc)
    hola = translate_text(locale=lc)
    print(hola)
  

main()