#************* Soru 1 *************

sayi = int(input("Bir sayı giriniz: "))

if sayi > 0:
    print("Pozitif", end =" ")
elif sayi < 0:
    print("Negatif", end =" ")
else:
    print("Sıfır", end =" ")

if sayi % 2 == 0:
    print("Çift")
else:
    print("Tek")

#************* Soru 2 *************

kelime = input("Bir kelime giriniz: ")
harf_sayilari = {}

for harf in kelime:
    if harf in harf_sayilari:
        harf_sayilari[harf] += 1
    else:
        harf_sayilari[harf] = 1

print(harf_sayilari)

#************* Soru 3 *************

sifre = input("Bir sifre giriniz: ")

if len(sifre) < 8:
    print("Şifre en az 8 karekter olmalı")
else:
    kontrol = False
    for harf in sifre:
        if harf.isupper():
            kontrol = True
            break
    if not kontrol:
        print("En az bir büyük karekter olmalı")
    else:
        kontrol = False
        for harf in sifre:
            if harf.isnumeric():
                kontrol = True
                break

        if not kontrol:
            print("En az bir sayısal değer içermeli")
        else:
            print("Şifreniz oluşturulmuştur")

#************* Soru 4 *************

liste = [12,4,9,25,30,7,18]
toplam = 0
ort = 0
buyuk_liste = []

for num in liste:
    toplam += num
ort = toplam / len(liste)

for num in liste:
    if num > ort:
        buyuk_liste.append(num)

print("Ortalama = ", ort)
print("Liste = ", buyuk_liste)

#************* Soru 5 *************

boyut = int(input("Bir boyutin giriniz: "))

for i in range(boyut):
    tur = i + 1
    yazi = ""
    for j in range(tur):
        yazi += "*"
    print(yazi)

#************* Soru 6 *************

toplam = 0
ortalama = 0
tur = 0
while True:
    girdi = int(input("Bir sayı giriniz (0 girerseniz bitirir): "))

    if girdi == 0:
        break
    else:
        toplam += girdi
        tur += 1

ortalama = toplam / tur
print("Toplam = ", toplam)
print("Ortalama = ", ortalama)

#************* Soru 7 *************

kelime = input("Bir kelime giriniz: ")
ters = kelime[::-1]
if kelime == ters:
    print("Palindrom")
else:
    print("Değil")

#************* Soru 8 *************

bolunenler = []

for i in range(1,100):
    if i % 3 == 0 and i % 5==0:
        bolunenler.append(i)

print(bolunenler)

#************* Soru 9 *************

v