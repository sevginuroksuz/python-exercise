#Girilen 5 sayıdan en büyüğünü gösteren programın python kodlarını yazınız.
sayilar=[]
n=int(input("Kac adet sayi girilecek?:"))
for i in range(n):
    sayi=int(input("Sayi girin:"))
    sayilar.append(sayi)
en_kucuk=min(sayilar)
en_buyuk=max(sayilar)
print(f"Listedeki en buyuk sayi:{en_buyuk}\nListedeki en kucuk sayi:{en_kucuk}")
