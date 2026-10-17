# SepticBeacon: Rakip Analizi

Tarih: 18 Ekim 2026. Yöntem: 8 hedef sorgu için web araması (ABD) ve sonuçlardaki sayfa türlerinin sınıflandırılması.

> **Sınırlar:** Arama hacmi, anahtar kelime zorluğu, rakiplerin backlink sayısı ve trafik verisi yok (DataForSEO ertelendi, Search Console henüz bağlı değil). Aşağıdakiler **SERP'te gördüklerimize** dayanır, tahmin içerir ve Search Console verisiyle doğrulanmalıdır. Arama aracı gürültülü: sonuçların bir kısmı düşük kaliteli kopya/spam sayfalardı, bunları rakip saymadım.

## 1. Kim sıralanıyor? (4 arketip)

| Arketip | Örnekler (SERP'te görülen) | Güçlü yanı | Zayıf yanı |
|---|---|---|---|
| **Devlet / kurum** | EPA (`epa.gov/septic`), MN PCA, WA DOH, Snohomish Health District, eyalet sağlık bakanlıkları | Otorite, güven, en yüksek E-E-A-T | Genel, bölgesel, "ne yapmalı" derinliği ve karar desteği az |
| **Ulusal ev-hizmet medyası** | Bob Vila, Angi, HomeAdvisor, This Old House, HomeServe, Fixr, Homes & Gardens | Marka, backlink gücü, maliyet sorgularında baskın | Yüzeysel, listicle, tekrar eden içerik, güvenlik uyarıları zayıf |
| **Yerel/bölgesel septik firmaları** | WR Environmental, RC Worst, Roto-Rooter, Rite Way | Yerel güven, dönüşüm odaklı | Satış odaklı, kısa yazılar, bilgi derinliği düşük |
| **Üreticiler / tedarikçiler** | Premier Tech Aqua, Infiltrator (ADS), Wholesale Septic Supply, Barr Plastics | Teknik doğruluk | Ürün tanıtımı, ev sahibi dilinde değil |

## 2. Sorgu bazlı gözlemler

| Sorgu | SERP'te baskın olan | SepticBeacon'un fırsatı |
|---|---|---|
| septic tank pumping cost | Fixr, HomeAdvisor kaynaklı rakamlar, Bob Vila, thepricer; kaynaklar birbirleriyle çelişiyor ($250-$600 / $275-$800 / $289-$556) | Çelişen rakamları açıkça karşılaştıran, tank boyutu ve erişime göre hesaplanabilir, dürüst "değişir" dilli rehber. Mevcut yazımız var (`septic-tank-pumping-cost`). |
| how often to pump | Bob Vila, Homes & Gardens, Roto-Rooter, yerel firmalar | Yalnız "3-5 yıl" demek yerine ev halkı sayısı × tank boyutu tablosu. Mevcut yazımız var. |
| signs of drain field failure | Sağlık kurumları (SNOHD, WA DOH), yerel firmalar | Aciliyete göre sıralı belirtiler ve "dolu tank mı, drain field mi?" ayrımı. Yazımız var (`signs-of-drain-field-failure`), bu açı güçlü. |
| septic alarm going off | Premier Tech Aqua, Angi, WR Environmental, RC Worst | Zaten kapsıyoruz. Üreticilerin resmi adımlarıyla (sustur, güç, su kullanımını kıs, bekle, ara) çelişmemek önemli. |
| septic system types | EPA, Angi, WR Environmental | **Boşluk:** Bu konuda kendi yazımız yok ("System Types" kategorisi boş). EPA otorite ama okunması zor. Brief hazır. |
| perc test | Maliyet listicle'ları ($600-$800 / $750-$1.850 / $3.000+ çelişkili), HomeServe, Bob Vila | **Boşluk:** Süreç + maliyet + sonuçlar ne anlama gelir. Brief hazır. |
| septic risers lids | Perakendeciler, düşük kaliteli maliyet sayfaları ($660-$2.600 / $900-$4.000 / $1.500-$3.000 çelişkili) | **Boşluk:** Güvenlik açısı (kapak açılması, çocuk/hayvan güvenliği) ile maliyet. Brief hazır. |
| septic winter care | MN PCA, This Old House, Infiltrator, Barr Plastics | **Boşluk ve mevsimsel zamanlama:** Kış yaklaşıyor, hemen yayınlanırsa trafik alır. Brief hazır, öncelik 1. |

## 3. Genel kalıplar (neye karşı yazıyoruz)
1. **Çelişkili rakamlar:** Maliyet sayfalarının çoğu birbirine uymuyor ve kaynak göstermiyor. Kaynaklı, aralıklı, "neden değişir" odaklı içerik fark yaratır.
2. **Düşük kaliteli kopya içerik bol:** Kalabalık bir SERP, ama otoriteli sayfalar azdır. Dürüst ve kaynaklı içerik uzun vadede kazanır.
3. **Güvenlik zayıf:** Rakip sayfaların çoğu "tankı açın" gibi tavsiyelerden kaçınmıyor. Bizim "güvenlik kuralı" kutumuz (`sb-note`) farklılaştırıcı.
4. **Otorite boşluğu:** Büyük medya markaları bizden güçlü. Doğrudan "septic tank cost" gibi geniş sorgularda yarışmak zor. **Uzun kuyruk ve ev sahibi problem sorguları** daha gerçekçi.

## 4. SepticBeacon'un konumlanması
- **Ses:** Bağımsız, ev sahibi odaklı, güvenlik öncelikli.
- **Fark:** Karar diyagramları, aciliyet sıralamaları, çelişen rakamları açıklayan tablolar, kaynaklı alıntılar.
- **Zayıflık:** Yeni site, yazar kimliği yok, backlink yok (tahmin). E-E-A-T boşluğu Faz 2'de kapanmalı.

## 5. Sonraki veri adımları
- Search Console bağlanınca: görünüm alan sorgular, ortalama sıra, CTR'ye göre öncelik yeniden sırala.
- DataForSEO eklenince: anahtar kelime hacmi ve zorluğu, rakip backlink profilleri.
- Aylık: aynı 8 sorgunun SERP'ini yeniden kontrol et, yeni rakipleri not et.
