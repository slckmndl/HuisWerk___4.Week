

sesli_harfler = "a,e,ı,i,u,ü,o,ö,A,E,I,U,O"



with open("Futbolcular.txt", "r", encoding="Utf-8") as oku:
    for i in oku:
        for o in sesli_harfler:      
            if i.startswith(o):
                with open("Sesli HArfle Baslayanlar.txt", "a+", encoding="Utf-8") as yaz:
                    yaz.write(i)
                    


              
