"""if ve else blokları ile mantıksal öperatörler kullanarak programın akışını değiştirilebilir"""

# kullanıcıdan iki sayı alalım .
# bu sayılardan hangisinin büyük aolduğunu bullalım
# ÖRNEK:1. sayı (5),2.sayıdan (3) büyüktür
# ÖRNEK:2. sayı (9),1.sayıdan (4) büyüktür
sayi1 =float(input("1. sayıyı yazin:"))
sayi2 =float(input("2. sayıyı yazin:"))


if sayi1 > sayi2:
    print(f"1.sayı({sayi1}),2.sayıdan ({sayi2})büyüktür.")
else:
    print(f"2.sayı({sayi2}),1.sayıdan ({sayi1})büyüktür.")