import random

while True:
    deger = int(input("Şifre oluşturmak için --> 1 Çıkış yapmak için --> 0  Tıklayın :"))

    if deger == 1:
        karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        sifre = int(input("Şifreniz kaç karakter olsun?"))
        password = ""
        for i in range(sifre):
            password += random.choice(karakter)
        print("Şifreniz :" ,password)
        
    elif deger == 0:
        print("Daha şifre üretilmeyecek.")
        quit()
