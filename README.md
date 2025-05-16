# deneme
###### Python notlarım ####

PRİNT FONKSİYONLARI

print("wwww",".","gokhanaltay",".","com",sep="") #sep parametresi aralardaki bosluklara etki eder.
print("Pardus ve Ubuntu birer Linux dağılımıdır",end="...")#end parametresi sonuna etki eder.

dosya = open("deneme.txt","w")
print("Ben Python,Monty python!",file=dosya) # print e file parametresi ile dosyaya yazı yazdırma işlemi

dosya = open("kisisel_bilgiler.txt","w")
name = "Gökhan "
surname = "ALTAY"
age = 37
city = "Kocaeli"
work = "Formen"

print("İsim :  " + name,"Soy İsim :  " + surname,"Yaş :  " + str(age),"Şehir :  "+ city,"Meslek :  "+work,sep="\n",file=dosya),
Çıktısı AŞağıdaki gibi
İsim :  Gökhan 
Soy isim :  ALTAY
Yaş :  37
şehir :  Kocaeli
Meslek :  Formen

print(*"TBMM",sep=".")#Yıldızlı parametreler Çıktının T.B.M.M şeklinde vermesini sağlar.
print(*"GALATASARAY",sep="-")  G-A-L-A-T-A-S-A-R-A-Y şeklinde çıktı vermeye yarar.

Örnekler : 
baslik = "Türkiye'de Özgür Yazılımın Geçmişi"
print(baslik,"\n","-"*len(baslik),sep="")
Çıktısı  su şekilde olur:
Türkiye'de Özgür Yazılımın Geçmişi
----------------------------------
print(r"C:\yeniklasor\dosya.txt")  # Kaçış karakterleri işlenmez

input () kullanıcıdan bir veri girmesini sağlar unutma kullanıcının girdiği her verinin tipi str yani metinseldir.

eğer aritmetik işlem yapacaksak tür dönüşümüne gideriz. int(input("Bir değer giriniz: " ) gibi
