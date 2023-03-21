"""
Bu soruyu cevaplamak için 15 Dakikanız vardır.
Aşağıdaki şekilde kullanıcının girdiği bir değere göre çarpım tablosu oluşturan programı kodlayınız. 
"6" değeri ÖRNEK olarak verilmiştir. Kullanıcı hangi sayısı girerse o sayı için çarpım tablosu oluşturulacaktır.
Döngü kullanılmayan cevaplar sıfır alacaktır. 
Döngü değişkeni olarak ilk adınızın ilk harfini kullanınız. 
ilk Adınızın ilk harfi ö,ş,ç,ü ise bunun yerine o,s,c,u harflerini kullanınız. 
Bu kurala dikkat etmeyen başkasından kopya çekmiş olarak işlem görecektir.

kaçlar tablosu yapılacak?:6
6 x 0 = 0
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60

"""

x=int(input("Kaclar tablosu yapılacak?"))
def CarpımTablo(x):
       for i in range(11):
             carpim=x*i
             print(f'{x}x{i}={carpim}')

CarpımTablo(x)
        



