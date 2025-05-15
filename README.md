# deneme
###### Python notlarım ####
print Fonksiyonları

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
