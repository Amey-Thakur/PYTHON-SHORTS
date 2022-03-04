from translate import Translator

ilang = input("Enter Original Language: ")
tlang = input("Enter Tranlated Language:")
sent = input("Enter sentence to be transalated:")

translator= Translator(from_lang=ilang,to_lang=tlang)
translation = translator.translate(sent)

print (translation)
