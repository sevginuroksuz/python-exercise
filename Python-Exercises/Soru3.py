"""
Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ=ağırlık/(boy*boy), boymetre cinsinden verilmeli) hesaplayınız.
VKİ 18 ile < 25 aralığındaysa normal, VKİ 25 ile <30 aralığındaysa kilolu, VKİ 30 ve daha yüksekse obez, VKİ 35 ve daha fazlaysa ciddi obez olarak kabul edilir. 
VKİ’ni hesaplayarak kişinin durumunu yazdırınız.
"""
print("---------Vucut Kutle Indeksi Hesaplama--------")
import math
boy=float(input("\nBoyunuzu santimetre cinsinden giriniz:"))
agirlik=float(input("Agirliginizi giriniz:"))
def VKİ_Hesapla(boy,agirlik):
     VKİ=(agirlik/10)/(math.pow((boy/100),2))
     if VKİ>=18 and VKİ<25:
         print("\nDurumunuz: Normal")
         print("Vücut kütle indeksiniz normal. İdeal kilo ve boydasiniz.\n")
     elif VKİ>25 and VKİ<30:
         print("\nDurumunuz: Kilolu")
         print("Vücut kütle indeksiniz biraz fazla. İdeal kilo ve boy oranina ulasmak icin kilo vermelisiniz.\n")
     elif VKİ>=30 and VKİ<35:
         print("\nDurumunuz: Obez")
         print("Vücut kütle indeksiniz biraz fazla. İdeal kilo ve boy oranina ulasmak icin kilo vermelisiniz.")
     elif VKİ>=35:
         print("\nDurumunuz: Ciddi Obez")
         print("Vücut kütle indeksiniz biraz fazla. İdeal kilo ve boy oranina ulasmak icin kilo vermelisiniz.")

VKİ_Hesapla(boy,agirlik)
