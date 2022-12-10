"""
break :döngüyü sonlandırır
cöntinue : döngünün ilgili turunu sonlandırır


"""

# 0 dan 10n a kadar lolan sayıları ekrana yazdırraalım

for sayi in range(10):
    if sayi == 5:
        continue

    print(sayi)

for sayi in range(10):
    if sayi == 5:
        break
    print(sayi)
for sayi in range(1,100):
    if sayi %2 == 0:
        continue

    print(sayi)