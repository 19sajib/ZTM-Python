from translate import Translator

with open('./File IO/test.txt', mode = 'r') as my_file:
    text = my_file.read()

translator= Translator(to_lang="es")
translation = translator.translate(text)

print(translation)