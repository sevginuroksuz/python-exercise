"""
Aşağıdaki gibi "r" birim yarıçaplı bir merkez çember verilmiştir. 
Kullanıcıdan alacağınız x ve y değerlerine karşılık gelen (x,y) noktasının bu çemberin içinde olup olmadığını kontrol  eden python fonksiyonu yazınız.  
Eğer verilen nokta çemberin içindeyse 1 sonucunu, değilse 0 sonucunu döndürecektir.
Not: Sadece fonksiyonu yazmanız yeterlidir.  Fonksiyon şu değişkenleri alacak ve şu adlı olacaktır.
cemberkontrol( r , x , y )

"""
import math
x=float(input("x degerini giriniz: "))
y=float(input("y degerini giriniz: "))
r=1
def cemberkontrol( r , x , y ):
    a=math.sqrt((math.pow(x,2))+(math.pow(y,2)))
    if(a<r):
        print("Tebrikler cember içi")
        return 1
    else:
        print("Agır ol cember disina ciktin")
        return 0
cemberkontrol( r , x , y)
