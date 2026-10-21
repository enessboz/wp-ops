# CrawlSpacePilot: Değişiklik Kaydı

Her satır: tarih, ne yapıldı, nereye (ID), eski → yeni.

## 2026-10-18
- Rank Math focus keyword (boş → değer), 23 yazı: 182 "sump pump in crawl space", 172 "crawl space insulation", 177 "crawl space drainage", 167 "crawl space encapsulation contractor", 148 "crawl space sump pump cost", 143 "vapor barrier vs encapsulation", 162 "crawl space waterproofing cost", 133 "crawl space mold removal", 118 "crawl space drainage cost", 155 "sagging floor repair cost", 127 "crawl space vapor barrier cost", 122 "is crawl space encapsulation worth it", 138 "crawl space mold remediation cost", 113 "best crawl space vapor barrier", 106 "crawl space dehumidifier cost", 101 "crawl space dehumidifier size", 96 "best crawl space dehumidifier", 85 "crawl space encapsulation", 10 "crawl space encapsulation cost", 9 "wet crawl space", 8 "crawl space repair cost", 7 "crawl space waterproofing", 6 "moisture in crawl space".
- Site simgesi: Python/PIL ile üretilmiş özgün 512 px PNG (ev + kriş arch) medya 224 olarak yüklendi, `site_icon` 0 → 224. Canlı sitede `<link rel="icon">` doğrulanacak.
- Kategori açıklamaları eklendi: 7 (Mold & Air Quality), 6 (Products & Equipment).
- Arşivde not: Sayfa/yazı focus keyword'leri title/description ile uyum için sonraki turda gözden geçirilecek; yazı title şablonu `%title% %sep% %sitename%` olduğundan bazı SEO title'ları 60 karakteri aşıyor olabilir (kontrol edilecek).
- Not: Sabah görevi 05:48 UTC'de tetiklendi. Backuply yedeğini bu araçlarla tetikleyemiyorum, ilk günkü kullanıcı yedeğine güveniliyor.

## 2026-10-17
- Tarama: Rank Math audit 80/100; Site Health 0 kritik; 23 yazı, 10 sayfa; link raporu 12 yazıda iç link yok, 16 yazıda dış link yok.
- Sayfa 2 (Sample Page) ve çöpteki 21 yazı (ID 41-60 ve 1) kalıcı silindi.
- Eklenti güncellemeleri: Rank Math 1.0.278 → 1.0.280, SpeedyCache 1.4.1 → 1.4.3, Backuply Pro 1.5.7 → 1.5.9, GoSMTP Pro 1.2.2 → 1.2.4, Loginizer Pro 2.1.0 → 2.1.2 (ücretsiz Backuply, GoSMTP, Loginizer da yükseldi).
- WPVibe önce devre dışı, sonra silindi. Temalar silindi: twentytwentythree, twentytwentyfour, crawlspacepilot-wpvibe-backup.
- `default_comment_status` open → closed, `default_ping_status` open → closed (`wp_cli_run option update`). 23 yazıda (182, 172, 177, 167, 148, 143, 162, 133, 118, 155, 127, 122, 138, 113, 106, 101, 96, 85, 10, 9, 8, 7, 6) comment_status ve ping_status → closed.
- Rank Math Website Identity: tür person → company, ad "My website" → "CrawlSpacePilot", alternatif ad "Crawlspace Pilot", organizasyon açıklaması eklendi.
- Ana sayfa (ID 34) Rank Math: title "CrawlSpacePilot - Independent Crawl Space Guides for Homeowners", description eklendi, focus keyword "crawl space guides".
- Kullanıcı 1: display name "Admin-gPD9i" → "CrawlSpacePilot Editorial Team", slug "admin-gpd9i" → "editorial-team", url → /about/, bio eklendi. Giriş kullanıcı adı değişmedi.
- Rank Math breadcrumbs false → true, ancestor categories → true. Tema çıktısı doğrulanacak.
- Menüler: Primary Menu (id 9; Home, Moisture & Water, Encapsulation & Waterproofing, Costs, Repair & Foundation, About, Contact), Footer Menu (id 10; Privacy, Terms, Cookie, Disclaimer, Affiliate). `primary` konumu → Primary Menu. Canlı sitede header/footer değişmedi: tema `wp_nav_menu` çağırmıyor.
- Rank Math author sitemap (`authors_sitemap`) true → false.
- Rank Math `llms-txt` modülü false → true, `rewrite flush`. `/llms.txt` 404 → içerik dönüyor ("# CrawlSpacePilot", Rank Math üretimi).
- Zamanlanmış görev: her gün 08:47 (Europe/Istanbul), bu oturuma gelir. Talimat wp-ops `docs/crawlspace-operations.md` dosyasına bağlı.

## 2026-10-18 (öğleden sonra, Enes oturumu)
- Rank Math sitemap önbelleği temizlendi: page-sitemap'teki var olmayan `/sample-page/` (404) kalktı; contact ve about girdi.
- Meta açıklama (boş/otomatik "Last updated: …" → yazıldı): sayfa 14, 15, 13, 12, 3. Blog sayfası 35: Rank Math title "Crawl Space Guides: Moisture, Encapsulation and Costs" + açıklama.
- Meta açıklama ≤160'a kısaltıldı: yazı 133 (166), 162 (170), 143 (165), 148 (161).
- Bulgu (açık): ana sayfa + 7 sayfada og:image yok; varsayılan OG görseli gerekli (kuyruk T-0020). Rank Math audit 86/100. 8 sayfada odak kelime yok. GSC bağlı değil.

## 2026-10-18 (tur 2, 17:57)
- Meta açıklama ≤160: yazı 101, 122, 162.
- Yazı 6 (moisture-in-crawl-space): "What EPA Guidance Says About Crawl Space Moisture" bölümü + Sources and Further Reading (EPA mold-course-chapter-2, EPA Brief Guide) eklendi; kaynaklar curl ile okundu. Yazı 9 (wet-crawl-space): "What EPA Guidance Says About Water Under a House" + Sources eklendi.
- Bulgu: yazı 6, 9, 7, 8, 10 <1.500 kelime ve otorite kaynağı yok ("AI assistant" kutusu linkleri kaynak değil). 7, 8, 10 sırada.
- Açık: ana sayfa OG görseli (meta yazıldı, çıktıya yansımadı).

## 2026-10-18 (tur 3) — iç link / kanibalizasyon (T-0017)
- wp_replace_in_post ile 15 yazıya FAQ öncesi "Related Guides" bölümü eklendi: 6, 7, 8, 9, 10, 85, 118, 122, 133, 138, 143, 148, 162, 177, 182 (geri alma: wp_history / revizyon). Önce hiçbir çiftte karşılıklı link yoktu.
- Sonuç: birleştirme yok, 301 yok; odak kelimeler değişmedi.

## 2026-10-18/19 (tur 4) — T-0022 yazı 7
- Yazı 7 (basement-crawl-space-waterproofing): "Related Guides" öncesine bölüm eklendi (DOE Building America + Rudd/BSC 2014 raporu, karar tablosu, sorular, Sources, last reviewed). +~4,5 KB HTML. Geri alma: wp revizyon.

## 2026-10-19 (tur 5) — T-0022 yazı 8, 10
- Yazı 8 (crawl-space-repair-cost): "Why the Cause Decides the Repair Bill" + tablo + sıra + Sources (EPA brief guide, DOE). Fiyat rakamı yok.
- Yazı 10 (crawl-space-encapsulation-cost): DOE/BSC/IRC R408.3 kapsam bölümü + kalem tablosu + Sources. Fiyat rakamı yok. Geri alma: revizyon.

## 2026-10-19 (tur 6) — T-0022 yazı 6, 9
- Yazı 9 (wet-crawl-space): "What to Document Before You Call a Contractor" bölümü + DOE kaynağı Sources'a eklendi, last reviewed 19 Eki.
- Yazı 6 (moisture-in-crawl-space): "How to Check Whether Your Fixes Are Working" bölümü + tablo. Geri alma: revizyon.

## 2026-10-20 (İstanbul; site saati 19 Eki 17:12) — yeni yazı
- Yazı 254 `musty-smell-from-crawl-space` oluşturuldu (taslak → yayın), kategori 7 Mold & Air Quality, medya 255 öne çıkan (Pexels 10847194), Rank Math title/açıklama/odak kelime. Geri linkler (Related Guides): 6, 9, 133, 138. Geri alma: yazıyı taslağa al (silme yok).

## 2026-10-20 (tur 8) — içerik denetimi
- Yazı 85: DOE + Rudd/BSC bölümü + Sources. Yazı 96, 101: EPA nem hedefi bölümü + Sources. Yazı 106: değişiklik yok (Angi çekincesi doğru). Geri alma: revizyon.

## 2026-10-20 (tur 9) — odak kelimeler, og:image
- Odak kelime: sayfa 34 "crawl space guides" (set_homepage_seo), 35 "crawl space articles", 191 "about CrawlSpacePilot", 192 "contact CrawlSpacePilot". Yasal sayfalara yazılmadı.
- og:image: 191'e rank_math_facebook_image/twitter_image URL yazıldı (etkisiz); varsayılan OG görseli Enes'e verildi (Rank Math → Titles & Meta → Global Meta → OpenGraph Thumbnail).

## 2026-10-21 (tur 10) — içerik denetimi
- Yazı 113, 127: IRC R408.3 kapsam bölümü (Rudd/BSC 2014) + Sources. Yazı 143: DOE + BSC bölümü + Sources. 167, 172: kaynak eksik, açık. Geri alma: revizyon.

## 2026-10-21 (tur 11) — içerik denetimi
- Yazı 172, 167: DOE Home Improvement Expert "Vented to Unvented Crawl Space" kontrol listesi bölümü + Sources. Geri alma: revizyon.

## 2026-10-22 (İstanbul; site saati 21 Eki 17:10) — yeni yazı
- Yazı 269 `crawl-space-vents-open-or-closed` oluşturuldu (taslak → yayın), kategori 2 Moisture & Water, medya 270 öne çıkan (Pexels 36056459), Rank Math title/açıklama/odak kelime. Geri linkler (Related Guides): 143, 6, 85, 9. Geri alma: taslağa al (silme yok).
