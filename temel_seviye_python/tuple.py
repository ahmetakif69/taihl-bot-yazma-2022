liste=[1,2,3]
tuple=("bir","iki","üç")
# tuplı ekrana yazdıralım
print(liste)
print(type(liste))
print(tuple)
print(type(tuple))
print(tuple[0])
liste[0] =7
print(liste)
# tuple[0]=7
# print(tuple)
# tuple içindeki belirli bir elemanın indexini bulma: index()
print(tuple.index("iki"))
# iki tuplı birleştirelim
tuple1=(1,1,1)
tuple = "bir","iki","üç"
x=tuple1+tuple
print(x)
