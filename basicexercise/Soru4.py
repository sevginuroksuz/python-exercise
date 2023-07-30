 #Kenarları Girilen Dikdörtgenin Alanı ve Çevresini Bulan Python Örneği
print("-----------Alan hesapla----------")
UzunKenar=int(input("\nDörtgenin kisa kenarini bulun:"))
KisaKenar=int(input("Dörtgenin uzun kenarini bulun:"))

def AlanHesapla(UzunKenar,KisaKenar):
    Alan=UzunKenar*KisaKenar
    Cevre=2*(UzunKenar+KisaKenar)
    print(f"Dörtgenin Alani:{Alan}")
    print(f"Cevre:{Cevre}")
AlanHesapla(UzunKenar,KisaKenar)