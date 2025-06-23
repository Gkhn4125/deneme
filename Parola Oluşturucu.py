import random
import string

print("🔐 Şifre Oluşturucu")

length = int(input("Şifre uzunluğunu girin: "))
use_letters = input("Harf kullanılsın mı? (e/h): ").lower() == 'e'
use_digits = input("Rakam kullanılsın mı? (e/h): ").lower() == 'e'
use_symbols = input("Sembol kullanılsın mı? (e/h): ").lower() == 'e'

char_pool = ""

if use_letters:
    char_pool += string.ascii_letters
if use_digits:
    char_pool += string.digits
if use_symbols:
    char_pool += string.punctuation

if not char_pool:
    print("⚠️ En az bir karakter türü seçmelisiniz!")
else:
    password = ''.join(random.choice(char_pool) for _ in range(length))
    print("🔑 Oluşturulan şifre:", password)
