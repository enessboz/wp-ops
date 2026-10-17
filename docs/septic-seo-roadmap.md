# SepticBeacon: SEO Analizi ve Roadmap

Tarih: 17 Ekim 2026 · Site: https://septicbeacon.com · Kapsam: DataForSEO ve Search Console olmadan, siteden ve WordPress'ten okunan veriler.

> Bu belgedeki "fırsat" ve "boşluk" maddeleri hipotezdir. Arama hacmi ve sıralama verisi olmadan doğrulanmadı. Faz 1 sonunda Search Console verisiyle test edilecek.

## 1. Mevcut durum

| Konu | Durum |
|---|---|
| Yaş / hacim | ~1 aylık site. 33 yazı (23 Eylül, 10 Ekim), 6 sayfa. |
| Teknik | 32 taranan URL'nin hepsi 200. noindex yok, canonical doğru, medyan yanıt 0,63 sn, her sayfada tek H1. |
| İçerik | Yazı başına medyan ~2.500 kelime, ortalama 14 H2, 2,4 tablo, 6,5 dış link. 23/33 yazıda SSS, hepsinde içindekiler. |
| Şema | Organization, WebSite, WebPage, BlogPosting, Person, ImageObject, CollectionPage. 4 kurumsal sayfada şema yok. |
| Güven (E-E-A-T) | Yazar "SepticBeacon Editorial Team". Hakkımızda sayfası editoryal yaklaşımı anlatıyor. Uzman incelemesi veya kimlikli yazar yok. |
| Altyapı | WordPress 7.1.3 güncel, GeneratePress, Rank Math aktif. Site sağlığında 0 kritik, 5 öneri. |

Kategoriler: Costs & Inspections 12, Septic Basics 8, Maintenance 6, Problems & Fixes 6, Parts & Sizing 1, System Types 0, Uncategorized 0.

## 2. Bulgular

### Kritik / yüksek
1. **11 yazı sitemap'te yok.** WordPress'te 33 yazı yayında, post sitemap'te 23 URL var. Eksikler:
   `aerobic-septic-system`, `septic-vs-sewer`, `septic-tank-size`, `septic-inspection-cost`, `septic-tank-replacement-cost`, `septic-tank-repair-cost`, `drain-field-replacement-cost`, `septic-system-replacement-financing`, `selling-house-with-bad-septic-system`, `home-warranty-septic-system-coverage`, `does-homeowners-insurance-cover-septic-systems`.
   Neden eksik olduğu doğrulanmadı (önbellek şüphesi).
2. **Ana sayfa ve `/blog/` aynı title'a sahip:** "Septic System Guides for Homeowners | SepticBeacon".
3. **Yetersiz iç link:** `septic-tank-additives` yetim (gövdede ona hiçbir link yok). `septic-alarm-going-off`, `drain-field-maintenance`, `what-is-a-septic-drain-field`, `garbage-disposal-septic-system`, `what-not-to-put-in-septic-tank`, `septic-tank-fills-up-quickly`, `septic-vs-sewer` yalnızca 1 iç link alıyor. Buna karşılık maliyet kümesi iyi bağlı (9-10 gelen link). Sorun, trafik çeken "problem" ve "bakım" yazılarının zayıf bağlanması.

### Orta
4. **llms.txt yok** (404). AI arama görünürlüğü için eklenmeli.
5. **Güvenlik başlıkları yok** (HSTS, X-Content-Type-Options, X-Frame-Options, Referrer-Policy).
6. **Title/meta uzunlukları:** 4 sayfada title sınırın dışında (`septic-system-lifespan` 61 karakter, `privacy-policy`, iki kategori sayfası). 5 yazının meta açıklaması 160 karakteri aşıyor (`septic-alarm-going-off`, `signs-of-drain-field-failure`, `garbage-disposal-septic-system`, `how-to-find-septic-system-records`, `septic-tank-maintenance`).
7. **Ana sayfa içeriği ince** (389 kelime) ve kategori sayfaları kısa. Kategori sayfaları için kısa tanıtım metni yok.
8. **Kategori yapısı:** "System Types" ve "Uncategorized" boş, "Parts & Sizing" 1 yazı. Boş kategoriler ince/tekrar eden arşiv sayfası üretir. Yazılar yanlış kategoride olabilir (`septic-vs-sewer` ve `aerobic-septic-system` Septic Basics'te, "System Types" boş).
9. **E-E-A-T:** Yazar kimliği yok. Sağlık/güvenlik/yasal/finansal konular (sigorta, garanti, finansman, güvenlik) uzman incelemesi ve kaynak gerektirir. Yazar listesinde "PUBL" adlı kullanıcı 14 yazının yazarı olarak görünüyor, görünen yazar adı doğrulanmalı.
10. **Şema eksikleri:** About, Contact, Disclaimer, Privacy sayfalarında şema yok. SSS bölümü olan 23 yazıda FAQPage şeması bulunmuyor (şema türlerinde yok).

### Düşük
11. 6 pasif plugin (SiteSEO, SiteSEO Pro, SpeedyCache x2, Akismet, Hello Dolly), 4 pasif tema, 5 bekleyen plugin güncellemesi.
12. PHP 8.2 yerine 8.3 önerilir. `action_scheduler_run_queue` görevi başarısız.
13. İki yazma yetkili MCP eklentisi aktif (Easy MCP AI ve WPVibe), birine inilmeli.
14. Kalıcı nesne önbelleği yok (APCu desteği var).

### Bilinmeyenler (veri gerekir)
- Hangi sorgularda çıkıldığı, gösterim/tıklama, indekslenen sayfa sayısı (Search Console).
- Arama hacmi, rakipler, backlink profili (DataForSEO sonra).
- Core Web Vitals saha verisi.
- http→https yönlendirmesi doğrulanmadı.

## 3. İçerik boşluğu hipotezleri (doğrulanmamış)
Mevcut kümeler: maliyetler, bakım, sorunlar, temel bilgi. Olmayan veya zayıf olabilecek konular:
- **Sistem türleri** (boş kategori): mound sistem, drip dağıtım, çakıl/alan, kum filtre. Aerobik sistem var.
- **Parçalar ve boyutlandırma:** tank malzemesi (beton/plastik/fiberglas), kapak/riser, efluent filtresi, pompa/alarm.
- **Süreç ve izin:** perk testi, izin, tasarım, yeni inşaat, eyalet/ilçe farkları.
- **Mevsim ve olaylar:** kış bakımı, sel/su baskını, ağaç kökleri, çamaşır/su yumuşatıcı etkisi.
- **Yüklenici seçimi:** pompalama firması seçme, sorulacak sorular, teklif karşılaştırma.
- **Araçlar:** tank boyutu hesaplayıcı, pompalama sıklığı hesaplayıcı.

Öncelik sırası Search Console verisi gelince netleşecek.

## 4. Roadmap

Her madde için: durum, risk ve onay ihtiyacı belirtilir. Yazma işlemleri Septic'e yapılır ve öncesinde onay alınır.

### Faz 0: Temel (1-2 gün)
Amaç: indekslemeyi ve ölçümü açmak.
- [ ] **Sitemap'i düzelt:** 11 eksik yazı sitemap'e girsin (Rank Math sitemap önbelleğini yenile / neden eksik olduğunu bul). *Risk: düşük.*
- [ ] **Search Console'u bağla:** mülk doğrulaması, sitemap gönderimi, `gsc-api` reposuyla veri çekme. *Kullanıcıdan Google erişimi gerekir.*
- [ ] **Ana sayfa / `/blog/` title ayrımı:** ana sayfa markayı ve konuyu, `/blog/` rehber arşivini anlatsın. *Risk: düşük.*
- [ ] **http→https ve www** yönlendirmesini doğrula.

### Faz 1: Hızlı kazanımlar (1 hafta)
- [ ] **Meta düzeltmeleri:** 5 uzun açıklama, 4 title (160 / 60 karakter sınırı).
- [ ] **İç link yeniden dağıtımı:** yetim ve tek linkli 8 yazıya, ilgili güçlü yazılardan bağlam içi linkler. Hedef: her yazıya en az 3 gelen link.
- [ ] **Kategori temizliği:** boş "System Types" ve "Uncategorized" için karar (kaldır veya doldur), yazıları doğru kategoriye al, kategori sayfalarına tanıtım metni ekle. *Kategori silmek URL değiştirir, 301 gerekir.*
- [ ] **llms.txt** ekle (Rank Math veya manuel).
- [ ] **FAQPage şeması:** SSS içeren 23 yazı için, Rank Math şema alanlarıyla.
- [ ] **Kurumsal sayfa şemaları:** AboutPage, ContactPage.
- [ ] **Güvenlik başlıkları:** sunucu/CDN düzeyinde. *Sunucu erişimi veya hosting paneli gerekir.*

### Faz 2: Güven ve içerik kalitesi (2-4 hafta)
- [ ] **Yazar kimliği:** "Editorial Team" yerine gerçek yazar/gözden geçiren, kısa biyografi ve uzmanlık. *Kullanıcı kararı: gerçek bir kişi/uzman olmadan uydurma yazar eklenmez.*
- [ ] **Kaynak ve inceleme notları:** sigorta, garanti, finansman, güvenlik konularında kaynak linkleri ve "son gözden geçirme" tarihi.
- [ ] **Ana sayfa ve kategori hub'ları** genişlet (konu haritası, en önemli rehberlere link).
- [ ] **Bakım/temizlik:** pasif plugin ve temalar, PHP 8.3, bekleyen güncellemeler (önce yedek), bir MCP eklentisini kaldır.

### Faz 3: Genişleme (aylık)
- [ ] **Search Console verisine göre** boşluk hipotezlerini doğrula ve önceliklendir (bölüm 3).
- [ ] **Yeni içerik:** ayda 4-8 yazı, claude-seo `seo-content-brief` ve `seo-cluster` ile brief.
- [ ] **Araçlar:** boyut/pompalama hesaplayıcı.
- [ ] **Güncelleme döngüsü:** maliyet yazılarını yıllık yenile, `dateModified` doğru tutulsun.

### Faz 4: Veri ve otomasyon
- [ ] **DataForSEO** (ertelendi): anahtar kelime hacmi, rakip, backlink. 50 dolarlık bakiye.
- [ ] **Zamanlanmış denetim:** haftalık salt okunur tarama + rapor.
- [ ] **Hermes Agent** (isteğe bağlı): ayrı sunucu gerekir, ancak zamanlanmış görevler yeterli kalırsa gerek olmayabilir.
- [ ] **Backlink / dijital PR** stratejisi (veri gelince).

## 5. Ölçüm
Faz 0 sonunda Search Console'dan şunlar kaydedilir ve haftalık izlenir:
- İndekslenen / gönderilen sayfa sayısı (hedef: 38/38 URL)
- Gösterim, tıklama, ortalama konum
- Sorgu başına en iyi sayfalar
- Çekirdek web verileri (CrUX)

## 6. Çalışma kuralları
- Her yazma işleminden önce onay. Önce önizleme/diff, sonra uygulama.
- Rank Math / WordPress değişikliklerinde önceki değer kaydedilir (geri alınabilir).
- Toplu değişiklikler küçük gruplar halinde yapılır, her grup sonrası kontrol edilir.
