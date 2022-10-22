okul="
# BÜTÜN HARFLERİ BÜYÜTME
print(okul.upper())

# BÜTÜN HERFLERİ KÜÇÜLTME
print(okul.lower())

# her kelimenin ilk harflerini büyütmek
print(okul.title())

# karakter dizisinin ilk karakterini büyük diğerlerini küçük yapalım
print(okul.capitalize())

# birkarektin o dizede kaçkere geçtiğini bulma
print(okul.count("e"))
makale="Teknolojinin hızla geliştiği ve günlük hayatımızın her alanına sirayetettiği birçağda kalkınma ile teknolojik gelişme arasında doğru orantı kurmakmümkündür.Bu yüzden teknoloji okur-yazarlığı ve teknoloji öğretimi kavramları giderek önem kazanmıştır."
# "üretebilen bireyler yetiştirebilmeyi hedefleyecek şekilde geliştirmişlerdir.
# "Bu çalışmada ABD, İngiltere ve Fransa gibi kalkınmış ülkelerde uygulanan eğitim
# "rogramları içerisinde teknoloji öğretiminin yerinin saptaması veTürkiye’deki mevcut
# "durumla karşılaştırılması amaçlanmıştır. Yapılan karşılaştırmada adı geçen ülkelerin
# "teknoloji öğretimi açısından genel bir bilinç geliştirdikleri ve eğitim sistemlerini
# "de buna göre geliştirdikleri görülmüştür.Türkiye’de ise bu bilinç nispeten geç gelişmiş
# "ve diğer örneklerde olduğu gibisivil kurum ve kuruluşlardan yeterince destek alınamamıştır.
# "Ayrıca teknolojidersleriyle diğer dersler arasındaki yatay kaynaşıklığın yaratılması açısından
# "dafarklılıklar gözlenmiştir
# print(makale.lower().count("teknoloji"))
# Soldaki ve sağdaki boşluk karakterlerini temizleyelim: strip()
ad = input("Adınız: ")
print(ad + "|")
print(ad.strip() + "|")
# Soldaki ve sağdaki boşluk karakterlerini temizleyelim: strip("")
urun_kodu="hep20221022"
print(urun_kodu.strip("hep"))
# soldaki boşluk veya ifadeyi temizleyelim
print(ad+"|")
print(ad.lstrip()+"|")
print(urun_kodu.lstrip("hep"))
# karakter dizisini bölelim
print(makale.split("."))
# böldüğümüz ve listeye dönüşen ifadeleri birleştirelim
kelimeler=okul.split()
print(kelimeler)
print("\n".join(kelimeler))
