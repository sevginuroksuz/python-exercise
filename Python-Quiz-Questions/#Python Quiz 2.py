"""
Python'da liste yapılarını kullanarak 5 adet il adı içeren bir liste oluşturunuz.
Kullanıcıdan bir adet sayı alınız. Kullanıcıdan girilen sayı listenin kaçıncı elemanına denk geliyorsa bu ilin ilk 2 ve son 2 karakterini ekrana basacak bir program yazınız. 
Örneğin listemizdeki ilk il "istanbul" olsun. Kullanıcıdan aldığımız sayı 0 ise ekrana İstanbul ilinin ilk 2 ve son 2 harfini alarak ekrana "İsul" yazacak. 
Özetle kullanıcı 0,1,2,3,4 rakamlarından birini girmiş ise bu rakamlara karşılık gelen il adının ilk 2 ve son 2 harfi ekrana yazılacaktır. 
Cevabınızı Thonny veya herhangi bir editörde yazıp aşağıya yapıştırınız. Süreniz 15 dakikadır.
"""
sayi= int(input("Bir sayi giriniz:")) #Kullanicidan sayi alinir.
listemm=["Amasya", "Ankara", "İstanbul", "Bursa", "İzmir"] 
karakter= listemm[sayi]     #Kullanicidan alinan sayiyiyla listeden eleman çekilir.
x=len(karakter)       #Listdeden kullanicinin seçtigi elemanin uzunlugu hesaplanir.
bas=karakter[0:2]     #Kullanicinin seçtigi elemanin ilk iki harfi bas'a atanir.
son=karakter[x-2:x]   #Kullanicinin seçtigi elemanin son iki harfi son'a atanir.
print(bas+son)
