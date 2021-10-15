# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 12:48:14 2021

@author: User
"""

# =============================================================================
# 
# a=True
# type(a)
# b= None #henüz bir değer atamadık
# print(b)
# "mehmet"=="mehmet"
# "murat"!="mehmet"
# =============================================================================




#if koşulu

# =============================================================================
# yas=int(input("Yaşınızı girin:\n"))
# 
# if yas<18:
#     print("Mekana giremezsiniz!")
# else:
#     print("Mekana hoşgeldiniz!")
# =============================================================================


# if-elif-else durumu

# =============================================================================
# islem=input("İşlem giriniz: ")
# 
# if islem == "1":
#     print("İşlem 1 seçildi")
# elif islem == "2":
#     print("İşlem 2 seçildi")
# elif islem == "3":
#     print("İşlem 3 seçildi")
# elif islem == "4":
#     print("İşlem 4 seçildi")
# else:
#     print("Geçersiz İşlem!!")
# =============================================================================
    

#hesap makinesi programı
# =============================================================================
# print("""***********************
# Hesap Makinesi Programı
# 
# İşlemler;
# 
# 1. Toplama İşlemi
# 
# 2. Çıkarma İşlemi
# 
# 3. Çarpma İşlemi
# 
# 4. Bölme İşlemi
# 
#     
# 
# ***********************""")
# 
# a=int(input("Birinci Sayı: "))
# b=int(input("İkinci Sayı: "))
# 
# 
# islem = input("işlemi giriniz: ")
# 
# if islem=="1":
#         print("{} ile {} in toplamı {} dir".format(a,b,a+b))
# elif islem=="2":
#         print("{} ile {} in farkı {} dir".format(a,b,a-b))
# elif islem=="3":
#         print("{} ile {} in çarpımı {} dir".format(a,b,a*b))
# elif islem=="4":
#         print("{} ile {} in bölümü {} dir".format(a,b,a/b))
# else:
#         print("Geçersiz işlem.........")
# =============================================================================



sys_kullanici_adi="eenes"
sys_parola="pusa12345"

kullanici_adi = input("Kullanıcı Adı : ")
parola = input("Parola : ")


if(kullanici_adi == sys_kullanici_adi and sys_parola !=parola):
    print("parola hatalı....")
elif(kullanici_adi != sys_kullanici_adi and sys_parola ==parola):
    print("Kullanıcı Adı hatalı....")
elif(kullanici_adi != sys_kullanici_adi and sys_parola !=parola):
    print("Kullanıcı Adı ve Parola   hatalı....")
else:
    print("Sisteme başarıyla Giriş yapıldı...")



























