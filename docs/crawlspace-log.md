# CrawlSpacePilot: Değişiklik Kaydı

Her satır: tarih, ne yapıldı, nereye (ID), eski → yeni.

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
