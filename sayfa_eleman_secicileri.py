#tarayivimixi ixport edelim
from moduller.tarayici import Tarayici
from selenium.webdriver.common.by import  By
from time import sleep
tarayici_nesnesi = Tarayici()
tarayici= tarayici_nesnesi.al()
# =okulun internet sitesine gidelim
tarayici.get("https://teknolojiaihl.meb.k12.tr/")
tarayici.maximize_window()



baslik=tarayici.find_element(By.CLASS_NAME,"container")


print(baslik)


baslik.screenshot("./gorseller/baslik.png")

arama_kutusu   =  tarayici.find_element(By.CSS_SELECTOR,"#araTextBox")
arama_kutusu.send_keys("İnovasyon")
sleep(2)


arama_tus  =  tarayici.find_element(By.ID,"araButton")
# arama_tus.click()
# sleep(3)

twitter_title=tarayici.find_element(By.NAME,"twitter:title")
print(twitter_title.get_attribute("content"))

okullarimiz=tarayici.find_element(By.LINK_TEXT,"Okullarımız")
# okullarimiz.click()
# sleep(3)

aile_birligi=tarayici.find_element(By.PARTIAL_LINK_TEXT,"Aile Birliği")
# aile_birligi.click()
# sleep(2)
linkler=tarayici.find_elements(By.TAG_NAME,"a")
# print(len(linkler))

iletisim=tarayici.find_element(By.XPATH,'//*[@id="o_hakkinda"]')
iletisim.screenshot("./gorseller/iletisim.png")