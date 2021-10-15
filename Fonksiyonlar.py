# -*- coding: utf-8 -*-
# =============================================================================
# 
# a=[1,2,3,4,5,6]
# #insert= indexe değer ataama
# a.insert(1,"enes")
# a.append("python")
# #pop : son indexte bulunan veya istenilen değğişkeni listeden çıkarmaya yarar.
# a.pop()
# print(a)
# #help fonksiyonu ile hangi fonksiyonların ne işe yaradığını gösterir.
# help(a.append)
# 
# =============================================================================

# =============================================================================
# #fonksiyon kullanımı
# def selamla():
#     print("Merhaba...")
#     print("Nasılsınıs?...")
# 
# type(selamla)
# 
# 
# def tanışma(isim):
#     print("İsminiz : ",isim)
#     
# tanışma("enes")
# 
# 
# def toplama(a,b,c):
#     print("Toplamları : ",a+b+c)
# 
# toplama(5,4,6)
# =============================================================================



# =============================================================================
# # Return ile fonksiyonlar
# 
# def toplama(a,b,c):
#     return a+b+c
# def ikiyleÇarp(a):
#     return a*2
# 
# toplam = toplama(3,4,5)
# print(ikiyleÇarp(toplam))
# 
# #default değerlerle optimizasyon 
# def selamla(isim="enes"):
#     print("selam",isim)
# 
# selamla()
# selamla("pusa" )
# =============================================================================

# tuplelar ile birden fazla değişken gönderebiliriz fonkiyonumuza
#o*********ÖNEMlİİİİİİİ..........
# =============================================================================
# def toplama(*a):
#     toplam=0
#     for i in a:
#         toplam+=i
#     print(toplam)
# 
# toplama(1,2,8,5,4,7,9,6,5,4,2,3,6,97)
# =============================================================================

# =============================================================================
# =============================================================================
# # #fonksiyon içinde tanımlanan değer localde tanımlı olduğu için hata verir.
# # def fonksiyon():
# #     a=10
# #     print(a)
# # 
# # fonksiyon()
# # print(a)
# # #fonksiyon dışında yani globalde tanımlanan değer her yerden erişim sağlanır.
# # b=5
# # def fonksiyon1():
# #     print(b)
# #     
# #     
# # fonksiyon1()
# # print(b)
# =============================================================================
# =============================================================================

#localdeki değeri globelleştirme

# =============================================================================
# =============================================================================
# # d=5
# # 
# # def fonksiyon():
# #     global d
# #     d=3
# #     print(d)
# # 
# # fonksiyon()
# # print(d)
# =============================================================================
# =============================================================================


    
#lambda kullanımı

def ikiyleÇarp(x):
    return x*2
print(ikiyleÇarp(3))

ikiyleçarp1 = lambda x : x*2
print(ikiyleçarp1(4))


tersçevirme = lambda s : s[::-1]
print(tersçevirme("python"))






#örnek code
def tam_bölenleri(sayi):
    tam_bölenler=[]
    for i in range(1,sayi+1):
            if(sayi%i==0):
                tam_bölenler.append(i)
    return tam_bölenler

while True:
    sayi = input("Sayı : ")
  
    
    if(sayi == "q"):
        print("Program Sonlandırılıyor.......")
        break
    else:
            sayi = int(sayi)
            print("Tam bölenler : ",tam_bölenleri(sayi))
    



birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okunus(sayı):
    birinci = sayı % 10
    ikinci = sayı // 10
    
    return onlar[ikinci] + " " + birler[birinci]

    
sayı =  int(input("Sayı:"))

print(okunus(sayı))




























