yorumlar = []
uzunluklar = []


while True:
    girdi = input("Bir yorum giriniz (0 ile çıkış yapar): ")

    if girdi == "0":
        break

    yorumlar.append(girdi)
    uzunluklar.append(len(girdi))

olumlu_yorum_say = 0

for yorum in yorumlar:
    for kelime in yorum.split(" "):
        if kelime.lower().find("iyi") >= 0:
            olumlu_yorum_say += 1
            break

uzun_yorum = yorumlar[0]
kisa_yorum = yorumlar[0]
uzun_konum = 0
kisa_konum = 0

for konum in range(1,len(uzunluklar)):
    if uzunluklar[konum] > uzunluklar[uzun_konum]:
        uzun_yorum = yorumlar[konum]
        uzun_konum = konum

    if uzunluklar[konum] < uzunluklar[kisa_konum]:
        kisa_yorum = yorumlar[konum]
        kisa_konum = konum

toplam = 0
ort = 0

for uzuluk in uzunluklar:
    toplam += uzuluk

ort = toplam / len(uzunluklar)

print("Toplam yorum sayısı: ", len(uzunluklar))
print("\"iyi\" geçen yorum sayısı: ", olumlu_yorum_say)
print("En uzun yorum: ", uzun_yorum)
print("En kısa yorum: ", kisa_yorum)
print("Ortalama uzunluk: ", ort, "karekter ")