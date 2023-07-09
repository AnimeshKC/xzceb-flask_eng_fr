'''Module responsible for translation'''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''
    Translates English text to French text
    '''
    french_text = MyMemoryTranslator('en-AU', 'french').translate(english_text)
    return french_text


def french_to_english(french_text):
    '''
    Translates French text to English text
    '''
    english_text = MyMemoryTranslator('french', 'en-AU').translate(french_text)
    return english_text
    