# boş bir liste tranımlayalım
liste=[]
print(liste)
print(type(liste))

okul="snacaktepe teknoloji anadolu imam hatip lisesi"
kelimeler=okul.split()
print(kelimeler)

# belirli sıradaki kelimeleri yazdıralıjm
print(kelimeler[0])
print(kelimeler[1])
print(kelimeler[2])
print(kelimeler[3])
print(kelimeler[4])
print(kelimeler[5])
print(kelimeler[-1]) #son kelimeyi gösterir

ad="Ahmet Akif MARKOÇ"
print(ad[0])
print(ad[6:10])
print(ad[6:10:2])
print(ad[::-1]) #ÇOKRAM fikA temhA
print(ad[-8:-12:-1])
#liste içerisimde farklı türden veriler olabilir
liste=[1,12.3,"pyython",True,[1,2,3]]
print(liste[-1][-1])
print(liste[4][-1])
print(liste[4][2])
# iki listeyi birleştirelim
liste2 = [1, 2, 3]
liste3 = [4, 5, 6]
liste4 = liste2 + liste3
liste5 = liste3 + liste2
print(liste4)
print(liste5)