"""
Kullanıcıdan elma, armut, kiraz meyvelerinden birini seçmesi ve kac kg istediği alan kodu yazınız.
Fiyat hesaplanarak ekrana yazdırınız.
"""

print("Elma:0\nArmut:1\nKiraz:2")
indis=int(input("Hangi meyveyi istiyorsunuz numarasını girin:"))
fiyat=[4,5,7]
x=int(input("Kaç kg meyve istiyorsunuz?"))
a=int(fiyat[indis])
tutar=x*a
print(tutar)