from googletrans import Translator
cevir = ""
while cevir != "exit":
    translator = Translator() 
    cevir3 = input("hangi dil çevrilecek(çıkmak için exit yaz):")
    if cevir3 == "exit":
        break
    cevir1 = input("çevirmek istediğiniz kelime:")
    cevir2 = input("hangi dile çevirilecek:")
    a = translator.translate(src=cevir3,text=cevir1,dest=cevir2)
    print(a.text)
