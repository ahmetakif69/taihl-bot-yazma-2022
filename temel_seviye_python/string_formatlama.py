# kullanıcıdan isim soyad veyaş bilgilerini alalım
c
# Kullanıcı bilgilerini yazdıralım
# -> Adınız: Eren Özdal, Yaşınız: 36
print("Adınız: " + isim + " " + soyad + ", Yaşınız: " + yas)
print("Adınız: {} {}, Yaşınız: {}".format(isim, soyad, yas))
print("Adınız: {2} {0}, Yaşınız: {1}".format(soyad, yas, isim))
print("Adınız: {x} {y}, Yaşınız: {z}".format(y=soyad, z=yas, x=isim))
print(f"Adınız: {isim} {soyad}, Yaşınız: {yas}")