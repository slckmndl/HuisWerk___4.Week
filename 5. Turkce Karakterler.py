a = open("Futbolcular.txt", "r",encoding="Utf-8")


for i in a:
    i= i.replace("ı","i")
    i= i.replace("ü","u")
    i= i.replace("ö","o")
    i= i.replace("ç","c")
    i= i.replace("ş","s")
    i= i.replace("ğ","g")
    i= i.replace("İ","i")
    i= i.replace("Ü","u")
    i= i.replace("Ö","O")
    i= i.replace("Ç","c")
    i= i.replace("Ş","S")

    with open("Yeni dosya.txt","a+",encoding="cp1254") as yaz:
        yaz.write(i)
        print(i)
   
