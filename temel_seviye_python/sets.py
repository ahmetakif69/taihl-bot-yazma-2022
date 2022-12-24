"""
sets listeleri süslü parantezler '{}' içinde tanımlanır.
sets liste elemanlarına indeks numaraları ile ulaşılamaz.
sets liste elemanlarına döngü içinde ulaşılır.
sets listeleri içinde aynı eleman birden fazla yer alamaz.
"""

# sets listesi oluşturalı
sets_liste={1,2,3,4}
# sets listesi içindekibir elamana ulaşalım
# print(sets_liste[0])
# sets liste elemanlarına ulaşalım
for eleman in sets_liste:
    print(eleman)

# sets listesine bir eleman eklemek
sets_liste.add(5)
print(sets_liste)

# sets listesine bir veya birden fazla eleman ekleyelim
sets_liste.update([19,20,21])
print(sets_liste)
liste=[1,2,3,1,15,16,1]
sets_liste=set(liste)
print (sets_liste)