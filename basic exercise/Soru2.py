"""
Kullanıcıya lokanta menüsü oluşturulacak. Para limiti girmesi istenecek ve şiparişi alınacak. 
Kullanıcı limitini aşarsa "Yetersiz Bakiye" uyarısı belirecek. Litin altında ve eşitse "Siparişiniz alındı. Hazırlanıyor." 
Şeklinde ekrana yazı yazdırılacak.
"""
print("------LEZZET DURAGI LOKANTASINA HOS GELDINIZ-----")
print("\nMENU")
print("\n----CORBALAR-----")
print("1-Mercimek: 15 TL")
print("2-Ezogelin: 20 TL")
print("3-Kremali_Mantar: 18 TL")
print("4-Tavuk_Suyu: 22 TL")
print("5-Kelle_Paca: 27 TL")
print("\n------ANA YEMEKLER------")
print("6-HunkarBegendi: 30 TL")
print("7-AlinazikKebabi: 32 TL")
print("8-TavukSis: 32 TL")
print("9-Karisik_Tavuk_Izgara: 35 TL")
print("10-Beyti: 37 TL")
print("11-Iskender: 46 TL")
print("\n--------SALATALAR-------")
print("12-CobanSalata: 15 TL")
print("13-AdenizSalata: 22 TL")
print("14-SezarSalata: 26 TL")
print("-------TATLILAR-------")
print("15-TavukGogsu: 14 TL")
print("16-Kazandibi: 12 TL")
print("17-FirinSutlac: 15 TL")
print("18-Keskul: 17 TL")
print("19-Gullac: 18 TL")
print("\n--------ICECEKLER--------")
print("20-Cay: 4 TL")
print("21-FincanCay: 10 TL")
print("22-Fanta: 8 TL")
print("23-CocaCola: 12 TL")
print("24-Pepsi: 12 TL")
print("25-Ayran: 3 TL")
print("26-Salgam: 10 TL")
Menu=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
MenuFiyat=[15,20,18,22,27,30,32,32,35,37,46,15,22,26,14,12,15,17,18,4,10,8,12,12,3,10]
Tutar=0
Limit=int(input("Cebinizdeki para tutari:"))
Siparis=[int(input("Lezzet Duragi Lokantasina Hosgeldiniz. Ne arzu ederdiniz? ")), int(input()), int(input()), int(input()), int(input()), int(input())]

for eleman in Siparis:
     if eleman in Menu:
         Tutar+=int(MenuFiyat[eleman])

if Tutar <= Limit:
 print(f"Hesap:{Tutar}")
 print("Siparisiniz alındı. Hazırlanıyor.")
else:
 print("Yetersiz Bakiye")




