import random
random_sayi = random.randint(0,100)
hak = 7
skor = 100

print(" Sayi Tahmin Oyununa Hos Geldiniz...")
print(f"0 ile 100 arasında Bir Sayı Tuttum Hakkınız {hak} Skorunuz {skor}")

while (hak > 0):
    try : 
        tahmin = int(input("  Bir Sayi Giriniz : "))
    
    except ValueError:
        print("Lütfen Geçerli Bir Değer Giriniz...")
        continue
    if not 0 <= tahmin <= 100:
        print("Lütfen 0 ile 100 arasında bir sayı giriniz.")
        continue

    if (tahmin == random_sayi ):
        print(f"Tebrikler Tuttuğum Sayı {random_sayi} ! {hak} hakkınızda tahmin ettiniz...")
        break
    else : 
        hak -= 1
        skor -= 20
        if(tahmin < random_sayi):
            print("Büyük Bir Sayı Girmesiliniz...")
            print(f"{hak} hakkınız kaldı Skorunuz =  {skor} ")
        
        elif (tahmin > random_sayi):
            print("Küçük Bir Sayı Girmesiliniz...")
            print(f"{hak} hakkınız kaldı Skorunuz =  {skor} ")
    if (hak == 0):
        print(f"Oyun Bitti ....Tutulan Sayi : {random_sayi}")
    
