# CrawlSpacePilot: SEO Analizi ve Roadmap

Tarih: 17 Ekim 2026 · Site: https://crawlspacepilot.com · Kapsam: WordPress MCP (Rank Math audit, Site Health, içerik ve eklenti envanteri) ve canlı ön yüz okuması. Search Console / DataForSEO verisi yok.

> "Fırsat" ve "boşluk" maddeleri hipotezdir, arama hacmi/sıralama verisi olmadan doğrulanmadı.

## 0. Ana hedef: AdSense ile gelir

**Hedef başvuru tarihi: 15 Aralık 2026** (≈8 hafta, SepticBeacon ile aynı). Başvuru, kapı kriterlerinin tamamı sağlanırsa yapılır. Sağlanmazsa tarih bir hafta kayar. Erken başvurup reddedilmek zaman kaybettirir. **Başvuruyu kullanıcı gönderir**, kriterler sağlanınca sadece haber verilir.

> Sayısal eşikler bizim kendi hedeflerimiz; Google sabit trafik/yazı şartı yayınlamıyor.

### Başvuru kapısı (hepsi ✅ olmalı)

| # | Kriter | Hedef | Şu an |
|---|---|---|---|
| 1 | Yayınlanmış özgün yazı | ≥ 45 (her biri ≥ 1.500 kelime) | 23 |
| 2 | Search Console'da indekslenen sayfa | gönderilenlerin ≥ %95'i | bilinmiyor (GSC bağlı değil) |
| 3 | Organik görünürlük | son 28 günde ≥ 3.000 gösterim, ≥ 150 tıklama, artış eğiliminde | bilinmiyor |
| 4 | Gerekli sayfalar | About, Contact, Privacy (reklam/çerez bölümü), Disclaimer; menüde görünür | sayfalar var; header/footer'da About/Contact yok (tema sabit kodlu) |
| 5 | Kimlik ve güven | tanımlı yazar sayfası, kaynak linkleri, favicon/logo | yazar "CrawlSpacePilot Editorial Team" yapıldı; favicon/logo kontrol edilecek |
| 6 | Çerez onayı (CMP) | EEA/UK/İsviçre için Google sertifikalı CMP | yok |
| 7 | Teknik sağlık | 404/kırık link yok, sitemap tam, mobil uyumlu, HTTPS, CWV "iyi" | sitemap/robots iyi; cache yok, CSS minify edilmemiş |
| 8 | Politika temizliği | boş/ince sayfa yok, spam yorum yok, telif temiz, "ince içerik" riski gözden geçirilmiş | yorumlar kapatıldı; boş kategoriler var |

### Kontrol noktaları
- **7 Kasım:** Faz 0-1 bitti mi? GSC verisi 3 haftalık mı?
- **1 Aralık:** Go/no-go ön değerlendirmesi.
- **15 Aralık:** Tüm kriterler tamamsa başvuru.
- Onay gelirse `ads.txt` yayınla (şu an 404), reklam yerleşimini kademeli aç. Red gelirse gerekçeyi oku, düzelt, **en az 2 hafta** sonra tekrar başvur.

### En büyük risk
Site yeni ve içerik hızlı üretilmiş görünüyor (23 yazı ~4 haftada, çoğu 26 Eyl-7 Eki arasında günlük planla). "Düşük değerli / ölçekli içerik" reddi olasılığı var. Azaltmak için: tanımlı yazar, kaynaklı bilgi (EPA, ENERGY STAR, üniversite uzantı servisleri, Building Science Corp.), her yazıda ayırt edici öğe (kontrol listesi, karar ağacı, örnek hesap, tablo), lisanslı görsel ve kredi, gözden geçirme tarihi. About sayfasındaki "yazılım araçlarıyla hazırlanabilir" ifadesi dürüst ama editoryal doğrulama kanıtıyla birlikte görünür olmalı.

## 1. Mevcut durum

| Konu | Durum |
|---|---|
| Yaş / hacim | Site 19 Eylül 2026'da açıldı. 23 yazı, 9 sayfa (Sample Page silindi). |
| Teknik | Rank Math audit 80/100. HTTPS, canonical, sitemap (`sitemap_index.xml`), robots, www yönlendirme iyi. Kırık link yok. Yanıt ~0,6 sn. Sayfa cache yok, CSS minify edilmemiş, mobil hız testi çalışmadı. PHP 8.2. |
| İçerik | Uzun, yapılandırılmış rehberler (örnek: drainage ≈4.000 kelime), tablo, SSS, kaynak/foto kredisi. Fiyat uydurmama ilkesi doğru. |
| Kategoriler | Costs 9, Moisture & Water 7, Encapsulation & Waterproofing 6, Repair & Foundation 1, Mold & Air Quality 0, Products & Equipment 0, Uncategorized 0 (varsayılan, silinemez). |
| Güven (E-E-A-T) | Yazar "CrawlSpacePilot Editorial Team". Uzman incelemesi/kimlikli yazar yok. |
| Altyapı | WordPress 7.1.3, özel tema `crawlspacepilot` (header/footer sabit kodlu), Rank Math, Backuply, Loginizer, GoSMTP, Easy MCP AI. |

## 2. Bulgular

### Kritik / yüksek
1. **Header/footer sabit kodlu, menü kullanmıyor.** Header: kategoriler + Guides + Search. Footer: Explore + Privacy/Terms/Cookie/Disclaimer/Affiliate. **About ve Contact hiçbir yerde linklenmiyor.** Tema `register_nav_menus` ile `primary` konumunu kaydetmiş ama `header.php` `wp_nav_menu` çağırmıyor. Tema dosyaları MCP ile yazılamıyor, kullanıcı/FTP işi.
2. **Odak anahtar kelime ve meta kapsama:** 18 yazı + 10 sayfada focus keyword yok. Yazı başlığı/açıklama şablonu `%excerpt%`.
3. **İç/dış link:** link raporuna göre 12 yazıda iç link yok, 16 yazıda dış kaynak linki yok.
4. **İçerik dengesi:** Mold & Air Quality 0, Products & Equipment 0, Repair & Foundation 1 yazı.
5. **Search Console Rank Math'e bağlı değil** (doğrulama kodu girili).

### Orta
6. Ana sayfada meta description ve OG description/görsel yoktu (description Faz 1'de eklendi; OG görseli kaldı). Site adı "My website" idi (düzeltildi).
7. Sayfa cache yok, `dist/styles.css` minify edilmemiş, mobil hız ölçülmedi.
8. `ads.txt` 404 (onaydan sonra eklenecek). Çerez banner'ı yok.
9. `llms.txt` modülü kapalı.
10. Görsellerin bir kısmı JPG (67 jpg, 12 webp), boyut/CLS kontrolü gerekli.

### Düşük
11. Pasif Akismet, SpeedyCache, SpeedyCache Pro. PHP 8.3 önerisi. Otomatik güncelleme kapalı (kullanıcı kararı: elle takip).
12. Author sitemap açık (tek yazar, gereksiz).

## 3. İçerik boşluğu hipotezleri (doğrulanmamış)
Mevcut kümeler: maliyet, encapsulation, drainage/sump, mold remediation, insulation, vapor barrier, dehumidifier. Zayıf/eksik olabilecekler:
- **Mold & Air Quality:** musty smell, crawl space mold (genel), radon, stack effect, havalandırmalı vs kapalı crawl space.
- **Repair & Foundation:** floor joist repair/sistering, destek direkleri, ahşap çürümesi, termit/haşere ve nem, sagging floor teşhisi.
- **Products & Equipment:** nem ölçer (hygrometer), sump pump alım rehberi, crawl space kapısı/vent.
- **Teşhis / how-to:** humidity level, how to dry out, standing water, condensation.
- **Yüklenici/süreç:** teklif karşılaştırma, izin/lisans, garanti.
- **Mevsim/olay:** sel sonrası, kış donması, yaz yoğuşması.
Öncelik Search Console verisi gelince netleşecek.

## 4. Roadmap

### Faz 0: Temizlik ✅ (17 Eki)
- [x] Backuply yedeği (kullanıcı aldı).
- [x] Sample Page + çöpteki 21 yazı kalıcı silindi.
- [x] Güncellemeler: Rank Math 1.0.280, Backuply Pro 1.5.9, GoSMTP Pro 1.2.4, Loginizer Pro 2.1.2, SpeedyCache 1.4.3.
- [x] WPVibe silindi (Easy MCP AI kaldı). Pasif temalar silindi.
- [x] Yorumlar ve pingler kapatıldı (varsayılan yorum + 23 yazı).
- [x] Otomatik güncelleme: kapalı, elle takip (kullanıcı kararı, ayda bir kontrol).
- [ ] ⏸ Uncategorized: varsayılan kategori, silinemez; boş.
- [ ] PHP 8.3: hosting panelinden, **kullanıcı**.

### Faz 1: Kimlik ve güven (1 hafta)
- [x] Rank Math Website Identity: CrawlSpacePilot, Organization.
- [x] Ana sayfa SEO title, description, focus keyword.
- [x] Yazar: görünen ad ve slug `editorial-team` (eski slug kullanıcı adını sızdırıyordu), bio eklendi.
- [x] Breadcrumb açıldı (Rank Math ayarı). Tema çıktısı doğrulanacak.
- [x] WP menüleri oluşturuldu: "Primary Menu" (id 9, `primary` konumuna atandı), "Footer Menu" (id 10). **Tema kullanmıyor** (Bulgu 1).
- [ ] **Header/footer'da About + Contact:** tema düzenlemesi, **kullanıcı**.
- [ ] Search Console'u bağla, sitemap gönder. **Kullanıcı (Google girişi).**
- [ ] Favicon/site simgesi ve logo kontrol et.
- [ ] OG varsayılan görseli belirle.
- [ ] `llms.txt` modülünü aç, `/llms.txt` doğrula.
- [ ] Author sitemap'i kapat (tek yazar).
- [ ] Kategori sayfalarına tanıtım metni, boş kategorileri doldurma planı.
- [ ] Hakkında sayfasına editoryal doğrulama/kaynak yaklaşımı bölümünü güçlendir (yalnızca doğru beyanlar).

### Faz 2: İçerik ve kalite (2-8 hafta)
- [ ] **Yazı sayısını 45'e çıkar** (haftada ≤ 3 yazı), önce Mold & Air Quality, Repair & Foundation ve Products & Equipment.
- [ ] 18 yazıya focus keyword, title ≤ 60 / açıklama ≤ 160 gözden geçirme.
- [ ] 12 yazıya iç link, 16 yazıya otorite dış kaynak (doğrulanmış linkler).
- [ ] Rank Math skoru zayıf yazı: `crawl-space-encapsulation` (26/100) iyileştir.
- [ ] Kategori hub'ları ve ana sayfa içeriği genişlet.
- [ ] CMP (Google sertifikalı) kur. **Kullanıcı eklenti seçimi gerekebilir.**
- [ ] Yazarın/gözden geçirenin gerçek kimliği: **kullanıcı kararı**; uydurma uzman eklenmez.

### Faz 3: Performans ve teknik
- [ ] Cache (SpeedyCache) etkinleştir, CSS minify, görseller webp, PageSpeed mobil ≥ 80.
- [ ] Güvenlik başlıkları (sunucu/CDN, kullanıcı).
- [ ] Reklam yer tutucuları sabit yükseklik (CLS), reklam kodu onaydan sonra.
- [ ] Pasif eklenti temizliği, aylık güncelleme kontrolü.

### Faz 4: Veri ve genişleme
- [ ] GSC verisine göre boşluk hipotezlerini doğrula.
- [ ] Araç fikirleri: dehumidifier boyutu hesaplayıcı, teklif karşılaştırma kontrol listesi.
- [ ] DataForSEO (ertelendi, para harcar).
- [ ] Güncelleme döngüsü: maliyet yazılarını yıllık yenile.

### Faz 5+: Keşif
Tüm yapılabilir maddeler bitince siteyi yeniden tara, bulduklarını buraya ekle ve başla.

## 5. Ölçüm
GSC bağlanınca haftalık: indekslenen/gönderilen sayfa, gösterim, tıklama, ortalama konum, sorgu başına en iyi sayfalar, CWV.
