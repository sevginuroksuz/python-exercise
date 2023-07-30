
#Kullanıcının belirlediği sayıda kişinin okuldan ne kadar zaman sonra mezun olacağını hesaplayınız.

dogumTarihi=[]
yil=2022
x=int(input("Kac kisi?"))
for i in range(x):
    dogum=int(input("Dogum yilinizi giriniz:"))
    dogumTarihi.append(dogum)
    yas=yil-int(dogumTarihi[i])
    if yas==18:
        print("Mezun olaman 4 yil var")
    elif yas==19:
        print("Mezun olaman 3 yil var")
    elif yas==20:
        print("Mezun olaman 2 yil var")
    elif yas==21:
        print("Mezun olaman 4 yil var"),
    elif yas==22:
        print("Gecmis olsun yeni mezun taze issiz")
    elif yas<18:
        print("Daha yolun var caylak")
    else:
        print("Sen bu yollari coktan astin ustad")
