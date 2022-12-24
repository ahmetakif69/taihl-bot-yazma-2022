# öğrencini adını ekrana yazdıralım
ogrenciler = ["Eren","Ahmet","Akif"]


for ogrenci in ogrenciler:
        print(f"öğrencinin adı:{ogrenci}")


# çinde ikiili verilerden oluşan tuple verileri olduğu bir liste oluşturakım
sayilar = [(1,2),(3,4),(5,6)]
for a,b in sayilar:
    print(f"1.sayı:{a},2.sayı:{b}")
# okulumuzun adını yer aldığı bir değişkeni kelimelere
# bölüp her kelimeyi döngü içinde ekrene yazdıralım
okul="sancaketpe teknoloji anadolu imam hatip lisesi"
for kelime in okul.split():
    print(kelime)
#öğrencilerin yer aldığı br dict oluşturalım
ogrenciler = {

  1:{ "ad" : "eren",
      "soyad":"özdal",
      "cinsihet":True,
      "dersler":["pe","maths"]
},
45: { "ad" : "zeynep",
      "soyad":"özdal",
      "cinsihet":False,
      "dersler":["pe","maths"]}}
# öğrencilerin bilgilerini yazdıralım
for no,ogrenci in ogrenciler.items():
    print(f"{no}numaralı öğrenci:{[ogrenci]}")