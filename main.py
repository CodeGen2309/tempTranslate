import mocks

from deep_translator import GoogleTranslator
from time import sleep



def translateText(text='Всем привет!', locale = 'en' ):
  result = GoogleTranslator(source='ru', target=locale).translate(text)
  return result


def makeUpMessage (header='', title='', poster='', desc=''):
  reqObject = f" 'title' : {title}, 'poster' : {poster}, 'desc' : {desc} "
  return header + ' {' + reqObject + '}'


locales = mocks.locales
# locales = [ 'it' ]
decider = '--------------------------------------'

for lc in locales:
  print(lc)
  print(decider)

  title  = translateText(mocks.titleString, lc)
  poster = translateText(mocks.posterString, lc)
  desc   = translateText(mocks.descString, lc)

  welcomeHeader  = translateText(mocks.welcomeString, lc)
  welcomeMessage = makeUpMessage(welcomeHeader, title, poster, desc)
  print(welcomeMessage + '\n\n')

  anotherHeader  = translateText(mocks.anotherFilmString, lc)
  anotherMessage = makeUpMessage(anotherHeader, title, poster, desc)
  print(anotherMessage + '\n\n')

  getTralier     = translateText(text=mocks.getTrailerString, locale=lc)
  print(getTralier)
  print(decider + '\n\n')