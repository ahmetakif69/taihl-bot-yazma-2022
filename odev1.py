url = "https://teknolojiaihl.meb.k12.tr"

# 1- "url" içinde kaç karakter olduğunu yazdır.
# print(len(url))

# 2- "url" içindeki "meb" sözcüğünü ekrana yazdırın.

# 3- "url" içindeki "k12" sözcüğünü ekrana yazdırın.

# 4- Kullanıcıdan adını, en sevdiği yemeği alın ve cümle içinde yazdırın.
# ÖRNEK CÜMLE: Adınız: Eren. En sevdiğiniz yemek: Pırasa

# 5- Öğrencinin 2 sınav notunu alın. Notunu hesaplayıp cümle içinde yazdırın.
# 1. sınav oranı: %35
# 2. sınav oranı: %65
# ÖRNEK CÜMLE: 1. sınav: 70 puan, 2. sınav: 90 puan, Notunuz: 83.0

# 6- Kullanıcının adını alın ve yan yana 100 defa yazdırın.
# 1.odev
print(len(url))
# 2.odev
print(url[22:25])


# 3.odev
print(url[26:29])

# 4.odev
isim = input("İsminiz: ")
yemek  = input("en sevdiğiniz yemek: ")

print("Adınız: " + isim + " en sevdiğiniz yemek:  "+yemek )
# 5.odev
x = 0.35
y = 0.65
print((45*x)+(89*y))
# 6.odev
isim = input("İsminiz: ")
print(isim*100)