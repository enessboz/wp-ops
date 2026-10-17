# SepticBeacon: İçerik Denetimi ve Kanibalizasyon Raporu

Tarih: 18 Ekim 2026. Kapsam: 33 yazı + 6 sayfa (canlı site, 39 URL).

## 1. Kurallar ve yöntem
Kurallar `AgriciDaniel/claude-seo` skill'lerinden alındı (`seo-page`, `seo-content`, `seo-cluster`) ve dayandıkları Google belgelerine göre uygulandı:
- **Sayfa:** title 50-60, meta açıklama 150-160 karakter, tek H1, mantıklı başlık hiyerarşisi, canonical, OG/Twitter, şema, alt metin, görsel boyut ve `width/height`.
- **İçerik:** blog yazısı için 1.500 kelime tabanı (**hedef değil, kapsam tabanı**), E-E-A-T ("Who / How / Why"), şablonlanmış meta tespiti, içerik kalite skoru, iç link yoğunluğu (1.000 kelimede 3-5), dış kaynaklar, tazelik.
- **Kanibalizasyon (`seo-cluster`):** iki yazı aynı birincil anahtar kelimeyi paylaşmamalı. SERP örtüşmesi 7+ ise birleştir.
- Araçlar: skill'in `metadata_template.py` ve `content_quality.py` betikleri, kendi tarama betiğim (`curl` + BeautifulSoup), TF-IDF benzerlik ölçümü.

**Sınırlar:** (1) Skill betiklerinin SSRF koruması bu ortamın proxy'siyle çalışmıyor, sayfaları `curl` ile çektim. (2) Arama aracının SERP'i gerçek Google'ı yansıtmıyor (spam sayfalar, İngiltere ağırlıklı sonuçlar), bu yüzden SERP örtüşmesini **güvenilir ölçemedim**. Kanibalizasyonu bunun yerine sayfa içi benzerlikle ölçtüm. (3) Skill'in kendisi de skorların "heuristik" olduğunu, Google'ın iç verisi olmadığını söylüyor. Kesin doğrulama Search Console ile yapılacak.

## 2. Sonuçlar (önce → sonra)
| Kontrol | Önce | Sonra |
|---|---|---|
| H1 sayısı ≠ 1 | 0 | 0 |
| Başlık hiyerarşisi atlaması | 0 | 0 |
| OG / Twitter card / BlogPosting şeması eksik | 0 | 0 |
| Şablonlanmış meta | 0 | 0 |
| İçerik kalite skoru (skill) | 94-96 | 94-96 |
| Meta açıklama > 160 | 0 | 0 |
| Title 50-60 dışında | 10 | 6 |
| Meta açıklama 150-160 dışında | 15 | 9 |
| `width/height` eksik görsel (yazı sayısı) | 17 | **0** |
| Dış linki olmayan yazı | 2 | **0** |
| `septic-tank-installation-cost` ↔ `septic-system-cost` içerik benzerliği | 0,72 | **0,64** |

Kalan sorunsuz alanlar: tek H1, canonical, OG, şema, kalite skoru zaten iyiydi.

## 3. Yapılan düzeltmeler
- **Görseller:** 43 görselde `wp-image-ID` sınıfı ve `width/height` eklendi (19 yazı). WordPress artık otomatik `srcset` üretiyor, böylece 2,8 MB'lık PNG gibi görseller mobil/küçük ekranlarda küçük varyantla iniyor. Sayfa kayması (CLS) riski kalktı.
- **Kaynaklar:** 8 yazıya doğrulanmış EPA sayfalarıyla "Further reading" bölümü eklendi (bunlar atıf değil, ek okuma).
- **Meta:** 5 kısa açıklama ve 5 kısa title uzatıldı/yeniden yazıldı (yazı 224, 200, 257, 265, 93, 59, 103, 159, 160).

## 4. Kanibalizasyon
**Birebir aynı odak anahtar kelime:** yok (33 yazının hepsi benzersiz).
**Niyet ve içerik çakışması:** sayfa içi benzerliğe göre yalnızca bir çift gerçek sorun:

| Çift | Benzerlik | Karar |
|---|---|---|
| `septic-tank-installation-cost` ↔ `septic-system-cost` | 0,72 → **0,64** | **Çözüldü kısmen, birleştirme öneriliyor (aşağıda)** |
| `selling-house-with-bad-septic-system` ↔ `septic-inspection-when-buying-a-house` | 0,50 | Farklı niyet (satıcı / alıcı). Çapraz link var. Aksiyon yok |
| `septic-inspection-when-buying-a-house` ↔ `septic-inspection-cost` | 0,44 | Farklı niyet. Aksiyon yok |
| `septic-tank-replacement-cost` ↔ `septic-system-cost` | 0,41 | Kabul edilebilir |
| `home-warranty...` ↔ `does-homeowners-insurance...` | 0,41 | Farklı niyet |

**Yapılan:** `septic-system-cost` pillar'ına yeni rol verildi ("türe göre maliyet + sahip olma maliyeti"), `septic-tank-installation-cost` spoke ("yeni kurulum teklifleri ve bütçe"). Title ve meta farklılaştırıldı (ikisinde de "2026" çakışması bitti). Pillar'dan 5 çakışan bölüm kaldırılıp yönlendirmeye çevrildi: "installation costs overlooked", "how to compare quotes", "questions to ask installer", "how much contingency", "tank cost table", "new vs replacement". Quick answer yeniden yazıldı. (Tüm düzenlemeler WordPress revizyon geçmişinde, geri alınabilir.)

**Neden hâlâ 0,64:** İki yazı da "yeni bir septik sistemin maliyeti" konusunu anlatıyor. Arama niyeti büyük ihtimalle aynı ("septic system cost" ≈ "septic installation cost"). Daha fazla kırpmak ya içeriği boşaltır ya da ikisini de zayıflatır.
**Öneri (onay bekliyor):** `septic-tank-installation-cost` içeriğini `septic-system-cost` içine birleştir, eski URL'yi 301 ile pillar'a yönlendir. Bu skill'in kuralıyla da uyumlu (aynı niyet → tek yazı). Riskler: URL değişimi, iç linklerin güncellenmesi (yaklaşık 12 yazı). Site yeni olduğu için sıralama kaybı riski düşük.

## 5. Açık bulgular (öncelik sırasıyla)
1. **E-E-A-T:** 33 yazıda yazar bilgisi yok ("Editorial Team"), uzman gözden geçirme yok. Google'ın "Who" testinde zayıf. Gerçek yazar adı ve biyografi gerekli.
2. **Satır içi görseli olmayan 14 yazı** (maliyet/denetim kümesi ve birkaçı). Özgün görsel/diyagram üretilmeli.
3. **İç link yoğunluğu:** 10 yazı 1.000 kelimede 3'ün altında (özellikle `septic-system-lifespan` 1,1, `signs-of-drain-field-failure` 1,5, `septic-alarm-going-off` 1,6). 13 yazı 5'in üstünde (maliyet kümesi, `septic-system-cost` 10,7). Bağlam içi linkler yeniden dağıtılabilir.
4. **Kısa yazılar** (1.500 tabanının altı): `drain-field-replacement-cost` 1.254, `septic-tank-repair-cost` 1.277, `how-to-find-a-buried-septic-tank` 1.330, `what-is-a-septic-drain-field` 1.368, `how-to-know-if-septic-tank-is-full` 1.424, `how-often-pump-septic-tank` 1.427. Skill'e göre taban kapsam içindir, hedef değil. Search Console verisine göre karar ver.
5. **Kalan meta uzunlukları:** 6 title 50-60 dışında, 9 açıklama 150-160 dışında. Düşük etki.
6. **Görsel dosya boyutları:** 15 yazıda >200 KB dosyalar var (en büyüğü 2,8 MB PNG). `srcset` ile hafifledi ama asıl dosyalar yeniden sıkıştırılabilir. Jetpack "Image CDN" modülü bunu otomatik yapar ama üçüncü taraf CDN kullanımı gizlilik politikasını etkiler, onay bekliyor.
7. **Şema:** FAQPage eklemedim. Skill'in kendi notuna göre FAQ zengin sonuçları kalktı (QAPage yalnızca gerçek kullanıcı soruları için).
8. **Tazelik:** 33 yazının hepsinin `modified` tarihi aynı gün (17 Ekim). Toplu düzenleme izi. Görünür "son güncelleme" metni yalnız 7 yazıda var.
