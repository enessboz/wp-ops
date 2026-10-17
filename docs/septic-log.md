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
