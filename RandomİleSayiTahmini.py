# -*- coding: utf-8 -*-
import random
import time
print("""***************************
   
      Sayı Tahmini Oyunu
      
      1 ile 40 arasındaki sayıyı tahmin edelim.
      
********************************""")

rastgele_sayi = random.randint(1,40)
tahmin_hakki = 7

while True:
    tahmin = int(input("Tahmininiz: "))
    
    if(tahmin<rastgele_sayi):
        print("Bilgiler Sorgulanıyor.....")
        time.sleep(2)
        tahmin_hakki-=1
        print("Daha yüksek bir sayı söyleyiniz.....")
    elif(tahmin>rastgele_sayi):
        print("Bilgiler Sorgulanıyor.....")
        time.sleep(2)
        
        print("Daha düşük bir sayı söyleyiniz.....")
        tahmin_hakki-=1
    
    else:
            print("Bilgiler Sorgulanıyor....")
            time.sleep(2)
            print("Tebrikler! Sayımız: ",rastgele_sayi)
            break
    
    if(tahmin_hakki==0):
        print("Tahmin Hakkınız Bitti.....")
        print("Sayiimiz",rastgele_sayi)
        break
            