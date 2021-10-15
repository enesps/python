# -*- coding: utf-8 -*-

#for döngüsü

# =============================================================================
# liste= [(1,2),(3,4),(5,6),(7,8)]
# 
# for eleman in liste:
#     print(eleman)
#     
# for (i,j) in liste:
#     print("i: {}  j: {} ".format(i,j))
#     
#     
# #for ile dictionary kullanımı 
# 
# sozluk= {"bir":1,"iki":2,"üç":3,"dört":4}
# 
# for eleman in sozluk.values():
#     print(eleman)
# 
# for eleman in sozluk.keys():
#     print(eleman)
# 
# 
# sozluk.items()
# 
# for i,j in sozluk.items():
#     print("Anahtar: ",i,"  Değer: ",j)
# =============================================================================
   

    
#while döngüsü
#range kullanımı
# =============================================================================
# 
# for i in range(1,10):
#     print("*"*i)
# 
# =============================================================================


#  List Comprehesion(liste kavarama)

# =============================================================================
# liste1 =[1,2,3,4,5]
# liste2 = list()
# 
# for i in liste1:
#     liste2.append(i)
# print(liste2)
# 
# liste3= [i for i in liste1]
# print(liste3)
# 
# 
# liste= [3,4,5]
# 
# liste4 = [i*2 for i in liste ]
# print(liste4)
# 
# liste6 = [(1,2),(3,4),(5,6)]
# liste1 = [i*j for i,j in liste6]
# print(liste1)
# 
# liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
# liste1= list()
# 
# for i in liste:
#     for x in i:
#         liste1.append(x)
# print(liste1)
# 
# liste1 =[x for i in liste for x in i]
# print(liste1)
# =============================================================================


# Örnek(Atm programı)
print("""***********************
 Hesap Makinesi Programı
 
 İşlemler;
 
 1. Bakiye Sorgulama 
 
 2. Para Yatırma

 3. Para Çekme
 

 
     
 
 ***********************""")
bakiye=1000
while  True:
    islem = input("İşlem seçiniz: ")
    if (islem == "q"):
        print("Yine bekleriz.....")
        break
    elif (islem=="1"):
        print("Bakiyeniz {} tl dir.".format(bakiye))
    elif (islem=="2"):
        miktar =  int(input("Miktarı Giriniz: "))
        bakiye+=miktar
    elif (islem=="3"):
        miktar= int(input("Miktarı Giriniz: "))
        
        if (bakiye-miktar<0):
            print("Böyle bir miktar çekemezsiniz....")
            continue
        bakiye-=miktar
    else:
        print("Geçersiz İşlem.....")
        


#fibonacci örneği

a=1
b=1
fibonacci=[a,b]
for i in range(10):
    a,b=b,a+b
    fibonacci.append(b)
print(fibonacci)













