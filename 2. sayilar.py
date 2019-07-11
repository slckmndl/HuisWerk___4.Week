
kharf="a,b,c,ç,d,e,f,g,ğ,h,ı,i,j,k,l,m,n,o,ö,p,r,s,ş,t,u,ü,v,y,z"
bharf="A,B,C,Ç,D,E,F,G,Ğ,H,I,I,J,K,L,M,N,O,Ö,P,R,S,Ş,T,U,Ü,V,Y,Z"
sayi="1,2,3,4,5,6,7,8,9,0"


#Yukarida tanimladigimiz karakterler haricindekileri else ile yapcaz

Text = input("Please Write hier\t:")

sayisayisi=0
kharfsayisi=0
bharfsayisi=0
digerkarakterler=0

# Belirtilen karakterlerden kac tane kullanildigini anlamamiz icin anahtari 0 yaparak saymaya baslatiyoruz.

for i in Text:
    if i in sayi:
        sayisayisi+=1
        continue
    elif i in kharf:
        kharfsayisi+=1
        continue
    elif i in bharf:
        bharfsayisi+=1
        continue
    else:
        digerkarakterler+=1
        continue


print(Text, 'yazisindaki toplam rakam sayisi :',sayisayisi)
print(Text, 'yazisindaki toplam kucuk harf sayisi :',kharfsayisi)
print(Text, 'yazisindaki toplam buyuk harf sayisi :',bharfsayisi)
print(Text, 'yazisindaki toplam ozel karakter sayisi :',digerkarakterler)