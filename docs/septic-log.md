# SepticBeacon: Değişiklik Kaydı

Her satır: tarih, ne yapıldı, nereye (ID), eski → yeni.

## 2026-10-18
- Site simgesi: medya 409 (`sepicbeacon-site-icon.png`) yüklendi, `site_icon` 0 → 409.
- Ayarlar: `default_comment_status` open → closed, `default_ping_status` open → closed.
- Yorum/ping kapatıldı: 33 yazı (tümü) ve 6 sayfa (32, 26, 24, 23, 22, 3).
- Meta açıklaması kısaltıldı: yazı 234, 170, 204, 248, 173, 259 (161-200 → 155-157 karakter, uzunlar ≤160).
- Meta title kısaltıldı: yazı 250 ("... and What Affects It" → "... & What Affects It", 61 → 59).
- `/blog/` (sayfa 26): title "Septic System Guides for Homeowners | SepticBeacon" → "Septic Guides & Articles for Homeowners | SepticBeacon", açıklama yeniden yazıldı (ana sayfa ile çakışma giderildi).
- İç linkler: yazı 173, 224, 104, 159, 209, 93, 234, 160, 200, 257, 161, 68 mevcut "Related" kutusuna; 248, 241, 198, 59, 229, 68, 259, 196, 214, 163, 94, 162 yeni "Related" kutusu eklendi. Sonuç: tüm yazılar ≥3 gelen iç link, yetim yok.
- Denendi ve başarısız: Rank Math `updateSettings` (sitemap, general) ve `toolsAction` (sitemap önbelleği). Ayarlar değişmedi (dışa aktarma ile doğrulandı).

## 2026-10-18 (Faz 5)
- Eklendi: `docs/septic-competitor-analysis.md`, `docs/briefs/` (9 brief), `docs/septic-backlink-plan.md`. Siteye yazma yok, e-posta gönderilmedi.

## 2026-10-18 (içerik denetimi)
- Kanibalizasyon: yazı 159 (`septic-system-cost`) içinden çakışan bölümler kaldırılıp yönlendirmeye çevrildi: "Installation costs homeowners often overlook", "How to compare septic system quotes" + "Questions to ask before hiring an installer" + "How much contingency should you keep?", "Tank cost is only one part of the project" (tablo kaldırıldı), "New installation vs. septic replacement" (kısaltıldı). Quick answer yeniden yazıldı. İçerik uzunluğu 19.021 → 16.256 karakter. Geri alma: WordPress yazı revizyonları.
- Title/meta: yazı 159 ("Septic System Cost by Type: Conventional, Mound & Aerobic"), 160 ("Septic Tank Installation Cost: New Install Quotes & Budget"), açıklamaları yeniden yazıldı.
- Meta uzatma: yazı 224, 200 (title+desc), 257, 265, 93 (açıklama), 59, 103 (title).
- Görseller: 43 `<img>` etiketine `class="wp-image-ID" width height` eklendi. Yazılar: 259 (3), 257 (2), 250 (2), 248 (3), 209 (2), 214 (2), 241 (2), 234 (3), 229 (3), 224 (3), 59 (3), 105 (1), 204 (2), 94 (3), 173 (1), 104 (2), 103 (2), 93 (2), 68 (2).
- "Further reading" (EPA) eklendi: yazı 196, 209, 214, 241, 234, 229, 224, 204.

## 2026-10-18 (birleştirme, CDN)
- **Jetpack Image CDN (photon)** etkinleştirildi (`/jetpack/v4/module/photon/active`). Doğrulama: görseller `i0.wp.com`'dan, 273.216 bayt JPEG → 60.496 bayt WebP.
- **Gizlilik politikası** (sayfa 3): "Image delivery" bölümü eklendi (Automattic görsel CDN'i, IP/tarayıcı bilgisi işlenir).
- **Rank Math Redirections modülü** açıldı (`/rankmath/v1/saveModule` redirections=on). Not: modül listesinde yoktu, bu yolla açıldı.
- **Birleştirme:** yazı 160 (`septic-tank-installation-cost`) benzersiz bölümleri yazı 159'a (`septic-system-cost`) taşındı: hidden costs, quote comparison table, questions to ask installer, low quote warning, budget above quote, before signing. Quick answer/giriş notu ve FAQ güncellendi. İç link çakışmaları temizlendi. Yazı 159 title: "Septic System Cost & Installation: Prices by Type (2026)", odak anahtar kelime: "septic system cost,septic tank installation cost". İçerik 16.256 → 19.259 karakter.
- **301:** `/septic-tank-installation-cost/` → `/septic-system-cost/` (Rank Math redirection id 1, `updateRedirection` hasRedirect=true). `curl` ile doğrulandı: 301. Yazı 160 **draft**'a alındı (silinmedi), yönlendirme draft iken de çalışıyor.
- **İç linkler** `septic-tank-installation-cost` → `septic-system-cost`: yazı 406, 196, 265, 250, 204, 161.
- **Zamanlanmış görevler** kuruldu: sabah özeti (07:56 İstanbul) ve günlük çalışma (12:59 İstanbul), ikisi de bu oturuma bağlı.

## 2026-10-18 (yeni yazı)
- **Yeni yazı yayınlandı:** yazı 511 `septic-system-winter-care` (kategori Maintenance). Kaynaklar `curl` ile okundu: MPCA "Don't let your septic system freeze" (23 Ocak 2026) ve EPA "How to Care for Your Septic System". Rank Math: title 50, açıklama 152, odak anahtar kelime "septic system winter care". Görsel yok (özgün görsel gerekli).
- İç linkler eklendi (Related kutusu): yazı 173, 214, 209, 59 → `/septic-system-winter-care/`.

## 2026-10-18 (editör kimliği, sitemap, iletişim formu)
- **Sayfa 518 `/editorial-policy/` yayınlandı** (Rank Math title/açıklama ayarlandı). Yayın anında `page-sitemap.xml`'e girdiği doğrulandı (6 URL).
- **Yazar tekilleştirme:** yazı 196, 259, 257, 250, 248, 209, 214, 241, 234, 229, 224, 198, 200, 204 `author` 3 (PUBL) → 1 (SepticBeacon Editorial Team).
- **İmza satırı** (`<p class="sb-byline">By SepticBeacon Editorial Team · How we create our guides</p>`) 33 yazının başına eklendi (511 dahil). Canlıda doğrulandı.
- **Jetpack Forms modülü** etkinleştirildi (`contact-form`). **Sayfa 23 (contact)** içeriğine Jetpack form + `info@septicbeacon.com` eklendi, ancak tema şablonu içeriği göstermediği için canlıda görünmüyor (etkisiz). Eski form (`sb_contact_submit`) tema kodunda, bu yüzden düzeltilemedi.
- **Bulgu:** contact/privacy/about/disclaimer sayfaları tema şablonuyla çiziliyor. Sayfa 3 (privacy) "Image delivery" eklemem canlıda görünmüyor.
- **Docs:** `docs/security-headers.md` (hosting için `.htaccess` kodu), `scripts/seo/` (denetim betikleri).

## 2026-10-18 (Faz 6: anahtar testleri, görseller, veri, şema)
- **Anahtar testleri:** DataForSEO `appendix/user_data` başlıksız 401, ortam değişkenleriyle (`DATAFORSEO_LOGIN/PASSWORD`) 200; bakiye başlangıçta $1.62. Pexels başlıksız 401 ("Missing API key"), `PEXELS_API_KEY` ile 200. Değerler hiçbir yere yazılmadı.
- **6.11 Görseller:** 14 yazıya Pexels fotoğrafı eklendi (ilk H2'den önce, `<figure>` + "Photo by X on Pexels" kredisi, alt metin konuya uygun ve fotoğrafı olduğu gibi anlatıyor). Medya ID → yazı: 552→511, 553→159, 554→161, 555→162, 556→163, 557→169, 558→170, 559→171, 560→172, 561→196, 562→198, 563→200, 564→265, 565→406. Dosyalar JPEG yüklendi, Jetpack Image CDN WebP + srcset olarak sunuyor (canlıda doğrulandı). Yazı 200'e ayrıca özgün satır içi SVG akış diyagramı eklendi (erişilebilir `<title>/<desc>`). Satır içi görseli olmayan yazı: 14 → 0. Not: Pexels'te "septic tank" konulu uygun foto yok; görseller genel (ekskavatör, denetçi, sigorta belgesi vb.) ve alt metinler septik sistemi göstermediğini açıkça belirtiyor.
- **6.3 Teknik tarama (45 URL, sitemap'ten):** hepsi 200, yönlendirme yok, tek H1, canonical doğru, title ≤60, açıklama 70-160, alt metin/`width` eksiği yok, kırık iç link yok (4 ek hedef kontrol edildi), tekrar eden title yok, `http`→`https` ve `www`→apex 301, `robots.txt` ve `llms.txt` 200, 404 sayfası 404 döndürüyor. Bulgu: BreadcrumbList şeması hiç yoktu (görünür breadcrumb tema HTML'i). **33 yazıya içerik içi JSON-LD BreadcrumbList eklendi** (Home > Kategori > Yazı), canlıda ayrıştırıldı ve doğrulandı. Eklenemeyenler: about/contact/privacy/disclaimer (tema şablonu). Güvenlik başlıkları hâlâ yok.
- **6.4 Hız:** PageSpeed API anahtarsız kullanımda 429 (kota) verdi, veri uydurulmadı. curl ölçümü: TTFB medyan 0,54 sn (maks 1,57), HTML medyan 73 KB, 3 küçük CSS (Brotli), yazı tipi dosyası yok, GTM + Jetpack stats betikleri. CWV değerleri için Search Console CrUX veya bir PSI API anahtarı gerekir.
- **6.1/6.6/6.7/6.8/6.9 DataForSEO:** harcama ≈ $0.91 (kalan ≈ $0.70). Backlinks API fiyatı resmi sayfadan doğrulandı (pay-as-you-go, istek başına $0.024 + satır başına $0.000036), özet çağrısı $0.024036 geldi. Rakipler `serp_competitors` ile 30 sorgudan seçildi: angi.com, homeserve.com, wrenvironmental.com, theseptic.guide, septicandwell.com, premiertechaqua.com, epa.gov. Çıktılar `docs/septic-data/*.csv` ve Drive klasörü "SepticBeacon SEO Log" (10 Sheet, her biri bir sekme).
- **6.2 Karar:** hiçbir yazı silinmedi veya birleştirilmedi. Veri: site 47 kelimede sıralanıyor, hepsi 21. sıra ve altı, tahmini trafik ≈ 0,5 (düşük kalite sinyali değil, sitenin yaşı). Search Console olmadan tıklama verisi yok; 160→159 birleştirmesi dışında benzer çift bulunmadı (en yüksek benzerlik 0,50, farklı niyet). Eylem: içerik planında 2 mevcut yazıyı kelimeye hizala, silme yok.
- **6.10 Engellendi:** claude-seo skill'lerinin `.claude/skills/` altına kopyalanması araç izin sistemi tarafından reddedildi; denemeyi tekrarlamadım. Depo `/home/user/agricidaniel/claude-seo` olarak klonlandı (ortam içinde), vendor etme kullanıcı onayı bekliyor.

## 2026-10-18 (Pazar günlük çalışma, haftalık tarama)
- **Haftalık tarama** (`scripts/seo/weekly_scan.py`, yeni): sitemap 45 URL (post, page, category). Durum ≠200: 0. Title >65: 0. Meta >160 veya <70: 0. H1 ≠1: 0. Canonical kendisi değil: 0. noindex: 0. Gelen iç link en az 3 (blog, disclaimer, privacy-policy, garbage-disposal, septic-smell).
- **6.10 kararı:** claude-seo skill'leri repoya kopyalanmaz, `scripts/seo/setup.sh` ile oturum başına klonlanır.
- Faz 6 oturumunun (session_014KTazYsAw434gwDcHiqQVr) çıktıları çekildi: `docs/septic-data/*.csv`, `scripts/seo/dfs.py`.

## 2026-10-18 (öğleden sonra: görsel düzeltmesi + mound yayını, Enes oturumu)
- Öne çıkan görsel: yazı 511 → medya 614 (Pexels 754276); 94 → medya 615 (Pexels 12683080, eski 20 yazı 173 ile paylaşılıyordu); 406 → 565; 265 → 564 (0 → ID).
- **Yazı 408 `septic-mound-system` yayınlandı** (draft → publish, kategori System Types, odak "septic mound system"). EPA mound.pdf linki 404'tü → `www.epa.gov/sites/default/files/2015-06/documents/mound.pdf`; "1–4 feet" ifadesi PDF'te doğrulandı. 301'li installation-cost linki kaldırıldı; byline, BreadcrumbList, güvenlik notu eklendi; yorum/ping kapalı; görsel medya 616 (Pexels 28487515, temsili). Geri linkler: 68, 159, 200, 104.
- Yazı 406: kategori Septic Basics → System Types, breadcrumb güncellendi.
- Not: haftalık ≤2 yazı kuralı, Enes'in "her gün 1 yazı" kuralıyla değişti (boz-agent `company/policies/web-ops.md`).

## 2026-10-19 (Septic günü, web turu)
- **Yazı 626 `types-of-septic-systems` yayınlandı** (System Types, odak "types of septic systems", 2593 kelime). Kaynaklar: EPA types, WA DOH types, TAMU OSSF (curl ile okundu). Görsel medya 630 (Pexels 12503553, temsili). Geri linkler: 68, 159, 200, 406, 408 (FAQ/Sources öncesi paragraf).
- **Yazı 159 `septic-system-cost`:** bozuk "$" düzeltildi: ",593 to ,463" → "$3,593 to $12,463" (×2); ",500 to ,500 installed" → "$3,500 to $8,500 installed"; ",000 to ,000" → "$4,000 to $15,000" (×2); "0 to ,500 for" → "$900 to $1,500 for" (×2); "A complete ,000 quote … a ,500 quote" → "A complete, itemized quote … a lower-looking quote" (orijinal rakamlar bilinmiyordu).
- **Yazı 105 `septic-tank-pumping-cost`:** excerpt "$300–$600" → "Angi $292–$565, HomeGuide $300–$700"; 3 iç link (septic-tank-size, septic-system-cost, septic-tank-maintenance) FAQ öncesi.
- Sitemap önbelleği temizlendi.

## 2026-10-20 (web turu)
- **Yazı 94 `how-to-find-a-buried-septic-tank` genişletildi** (T-0024): "A university extension method: measure from the sewer pipe" bölümü + güvenlik kontrol listesi eklendi (University of Georgia Extension septic folder PDF'i curl ile okundu; mesafeler "tek Georgia rehberinden tipik değerler" diye etiketlendi). Kaynak listesine UGA satırı eklendi; `how-to-find-septic-system-records` iç linki eklendi. Önce 1340 kelime. Başlık/H1 hizalaması yapılmadı.

## 2026-10-21 (Septic günü, web turu)
- **Yazı 645 `septic-tank-risers-and-lids` yayınlandı** (Parts & Sizing, odak "septic tank risers", 2581 kelime). Kaynaklar: WA DOH lid safety, San Diego County pumping checklist, Thurston County riser kurulum sayfası (curl ile okundu). Maliyet rakamı yok. Görsel medya 646 (Pexels 37554739, temsili).
- Geri linkler (FAQ öncesi paragraf): 94, 105, 173, 163. Sitemap önbelleği temizlendi.

## 2026-10-21 (web turu, 02:08)
- **Yazı 104 `drain-field-replacement-cost` genişletildi** (1265 → 1931 kelime): "What a state health department says about drain field failure" bölümü (WA DOH Signs of Septic System Failure, curl ile okundu) + kaynak satırı; iç linkler eklendi. Rakam eklenmedi.

## 2026-10-22 (web turu, 00:08)
- **Yazı 103 `septic-tank-repair-cost` genişletildi** (T-0023): "Who does septic repairs? What a state health department says" bölümü (WA DOH Hiring a Septic System Professional, curl ile okundu) + profesyonel türleri tablosu + soru listesi; kaynak satırları (hiring-professional, signs-failure) ve iç linkler eklendi. Rakam eklenmedi.

## 2026-10-23 (Septic günü, web turu)
- **Yazı 656 `concrete-vs-plastic-septic-tank` yayınlandı** (Parts & Sizing, odak "concrete vs plastic septic tank", 2019 kelime). Kaynaklar: Maine 10-144 CMR ch.241, Massachusetts 310 CMR 15.226, Texas 30 TAC §285.32 (Cornell LII, curl ile okundu). Ömür/fiyat rakamı yok. Görsel medya 660 (Pexels 4790056, temsili).
- Geri linkler: 161 (FAQ öncesi), 250 ("When to Stop Troubleshooting" öncesi), 645 (riser yazısına Maine/Texas riser kuralı paragrafı + link). Sitemap önbelleği temizlendi.
- (23 Ekim 01:09) Yazı 265 `septic-tank-size`: `/concrete-vs-plastic-septic-tank/` geri linki eklendi ("When to talk to a professional" öncesi paragraf).
