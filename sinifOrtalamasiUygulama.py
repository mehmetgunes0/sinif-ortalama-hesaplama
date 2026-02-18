ogrenciSayisi = int(input("Öğrenci Sayısını Girin: "))

# Öğrencileri tutacak boş bir liste
ogrenciler = []
for i in range(ogrenciSayisi):
     print(f"\n öğrenci bilgilerini girin:")     #\n bir satır atlamak için kullanılır.

     ad = input("Adını Girin: ")
     soyad = input("Soyadını Girin: ")
     yas = int(input("Yaşını Girin: "))
# Notları tutacak boş bir liste
     notlar = []
     for j in range(3):
        ogrenciNotu = int(input(f"{j+1}. not: "))
        notlar.append(ogrenciNotu)

     ortalama = int(sum(notlar) / len(notlar))        #"sum()" liste içindeki verilerin tamamını toplamak için kullanılır. "len()" liste içinde kaç eleman olduğunu gösterir.

     durum = "Geçti" 
     if ortalama >= 50:
        print("Geçti")
     else:
        print("Kaldı")
# Öğrenciler bir sözlük içinde toplanır.
ogrenci = {
    "ad" : ad,
    "soyad" : soyad,
    "yas" : yas,
    "notlar" : notlar,
    "ortalama" : ortalama,
    "durum" : durum
}
ogrenciler.append(ogrenci)


# Öğrencileri liste görünümünde yazdırır.
print("\n --> ÖĞRENCİ BİLGİLERİ <--")

for o in ogrenciler:        # range yerine direkt ogrenciler yazılmasının sebebi tür dönüşümü ile uğraşmadan direkt olarak hazır listemizi yazdırmak. range sayı değerleri yazdırdığı için print içerisinde tür dönüşümü yapmamız gerekirdi.
     print(f"{o['ad']} {o['soyad']} ({o['yas']} yaşında)")
     print(f"Notlar: {o['notlar']}")
     print(f"Ortalama: {o['ortalama']} --> Durum: {o['durum']}")
# Sınıf ortalaması hesaplanır.

ortalamaListesi = [o["ortalama"] for o in ogrenciler]    # for o in ogrenciler komutu ile yukarıda yazdıırdığımız liste görünümünün içinden veri alınmasını sağlar.
enYuksek = max(ortalamaListesi)     # max() değişken iiçerisindeki en büyük değeri alır.
enDusuk = min(ortalamaListesi)      # min() değişken içerisindeki en küçük değeri alır.
sinifOrtalamasi = sum(ortalamaListesi) / len(ortalamaListesi)

print("\n---> SINIF ORTALAMASI <---")
print(f"En Yüksek Ortalama: {enYuksek}")
print(f"En Düşük Ortalama: {enDusuk}")
print(f"Sınıf Ortalaması: {sinifOrtalamasi}")