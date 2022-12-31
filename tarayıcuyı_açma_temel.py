#selenium ve diğer paketleri içeri atma
from moduller.tarayici import  Tarayici
from time import sleep
tarayici_nesnesi=Tarayici()
tarayici= tarayici_nesnesi.al()



#tarayıcıda gezinme
tarayici.get("https://www.diyanet.gov.tr/tr-TR")
sleep(2)



#geri dönme
tarayici.back()
print(tarayici.title)
sleep(1)









# ileri gidelim

tarayici.forward()
print(tarayici.title)
sleep(1)

print(tarayici.get_window_size())

tarayici.set_window_size(500, 300)
sleep(2)
print(tarayici.get_window_position())

tarayici.set_window_position(100,500)
sleep(2)

#penceremizi tam ekran yapalım
tarayici.maximize_window()
sleep(2)



#tarayiciyi küçültme
tarayici.minimize_window()
sleep(1)

#pencereyi tam ekran yağalım
tarayici.fullscreen_window()
sleep(1)

tarayici.save_screenshot("./gorseller/bot-yazma.png")

