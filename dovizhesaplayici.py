print("""
______________________________
| DÖVİZ KURU HESAPLAYICI 
______________________________
| 
| Sürüm   : v1.1
| Yapımcı : Beetlejuicetr (MID)
| Dil     : Python 3.9
| Tarih   : 27/12/2021
______________________________

Kullanim;

1) TL - USD
2) USD - TL

3) TL - EUR
4) EUR - TL

5) EUR - USD
6) USD - EUR

""")

tl_usd = 0.087
usd_tl = 11.47

tl_eur = 0.077
eur_tl = 13

eur_usd = 1.13
usd_eur = 0.88

while True:
	try:
		girdi = input("Yapilacak işlemi seçiniz: ")
		girdi2 = input("Dönüştürmek istediğiniz miktarı giriniz: ")
	except ValueError:
		print("[UYARI] Sadece sayı girmelisiniz.")
	if girdi == "1":
		print("_"*25)
		print("Seçilen işlem : 'TL-USD' ")
		print("İşlem çıktısı: ",float(girdi2)*tl_usd)
		print("_"*25)
	if girdi == "2":
		print("_"*25)
		print("Seçilen işlem : 'USD-TL' ")
		print("İşlem çıktısı: ",float(girdi2)*usd_tl)
		print("_"*25)
	if girdi == "3":
		print("_"*25)
		print("Seçilen işlem : 'TL-EUR' ")
		print("İşlem çıktısı: ",float(girdi2)*tl_eur)
		print("_"*25)
	if girdi == "4":
		print("_"*25)
		print("Seçilen işlem : 'EUR-TL' ")
		print("İşlem çıktısı: ",float(girdi2)*eur_tl)
		print("_"*25)
	if girdi == "5":
		print("_"*25)
		print("Seçilen işlem : 'EUR-USD' ")
		print("İşlem çıktısı: ",float(girdi2)*eur_usd)
		print("_"*25)
	if girdi == "6":
		print("_"*25)
		print("Seçilen işlem : 'USD-EUR' ")
		print("İşlem çıktısı: ",float(girdi2)*usd_eur)
		print("_"*25)

	
	
