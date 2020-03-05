

from termcolor import colored
from googletrans import Translator
translator = Translator(service_urls=[
      'https://translate.google.com/?hl=fa',
      'https://translate.google.cn/?hl=en',
    ])
while True:
    print(colored('Welcome ', 'red'), colored('if you want to exit Press Ctrl + z ', 'green'))
    x=str(input(("What do you want to translate?  " )))
    
    trans = Translator()
    t = trans.translate(
        x
    )
    print(f'{t.origin} -> {t.text}')
    
    print("--------")
