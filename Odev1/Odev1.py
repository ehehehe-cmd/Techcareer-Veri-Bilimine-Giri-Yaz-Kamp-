#************ Bölüm 1 ************#

#************ Soru 1  ************#

ad = input("Adınızı Giriniz")
yas = int(input("Yaşınızı Giriniz"))
boy = float(input("Boyunuzu Giriniz"))

print("Ad : %1s, Yaş : %1d, Boy : %1f" % (ad, yas, boy))

#************ Soru 2  ************#

mat = 80
fizik = 70
kimya = 85

ort = (mat + fizik + kimya) / 3

print("Not ortalaması: %1f" % (ort))


#************ Soru 3  ************#

kelime = "Hello World!"

print("İlk karekter : %1s, Son Karekter : %1s, Uzunluk : %1d, Ters %s" % (kelime[0], kelime[-1], len(kelime), kelime[::-1]))

#************ Bölüm 2 ************#

#************ Soru 4  ************#

say1 = input("İlk sayıyı giriniz: ")
say2 = input("İkinci sayıyı giriniz: ")

topla = int(say1) + int(say2)
cıkart = int(say1) - int(say2)
carp = int(say1) * int(say2)
bol = int(say1) / int(say2)
mod = int(say1) % int(say2)

print("Toplam : %1d, Çıkarma : %1d, Çarpma : %1d, Bölme %1f, Mod : %1f" % (topla, cıkart, carp, bol, mod))

#************ Soru 5  ************#

ortalama = int(input("Ortalamanızı girin: "))

if(ortalama > 50):
    print("Geçti")
else:
    print("Kaldı")

#************ Soru 6  ************#

yas = int(input("Yaşınızı Giriniz"))

if(yas > 18):
    print("Ehliyet Alabilirsin")
else:
    print("Ehliyet Alamazsın")

#************ Soru 7  ************#

fiyat = float(input("Fiyat: "))
indirim = float(input("Indirim: "))

print("İndirimli Fiyat: " , ((fiyat * (100 - indirim))/100))

#************ Soru 8  ************#

dogru = True
yanlıs = False

print("1 and 1: ", (dogru and dogru),  "1 and 0: " , (dogru and yanlıs), "1 or 0: " , (dogru or yanlıs), "1! or 0: " , (not dogru or yanlıs))

#************ Bölüm 3 ************#

#************ Soru 9  ************#

ilk_urun = int(input("Ilk urun: "))
ikinci_urun = int(input("Ikinci urun: "))
ucuncu_urun = int(input("Ucuncu urun: "))

toplam = ilk_urun + ikinci_urun + ucuncu_urun

if(toplam > 200):
    print("Tutar: ", (toplam * 0.9))
else:
    print("Tutar: ", toplam)

#************ Soru 10  ************#

from datetime import date

yil = int(input("Doğum yılınızı giriniz: "))

yas = date.today().year - yil

if(yas > 18):
    print("Yetişkinsiniz")
elif(13 < yas < 18):
    print("Ergensiniz")
elif(0 < yas < 13):
    print("Çocuksunuz")
else:
    print("Hata Yaş 0 dan küçük olamaz")
