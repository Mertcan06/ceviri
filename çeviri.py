from googletrans import Translator
cevir = ""
while cevir != "exit":
    translator = Translator() 
    cevir1 = input("çevirmek istediğiniz kelime(çıkmak için exit yaz):")
    if cevir1 == "exit":
        break
    cevir2 = input("hangi dile çevirilecek:")
    a = translator.translate(cevir1,dest=cevir2)
    print(a.text)
