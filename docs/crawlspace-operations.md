# CrawlSpacePilot: İşletme Kılavuzu (otomatik çalışma kuralları)

Hedef: crawlspacepilot.com'u AdSense onayına (hedef başvuru **15 Aralık 2026**) ve sürdürülebilir organik büyümeye taşımak. Plan: `docs/crawlspace-seo-roadmap.md`. Değişiklik kaydı: `docs/crawlspace-log.md`. Kardeş site: SepticBeacon (`docs/septic-*`), ona **dokunma**.

Kullanıcı bu site için **tam yetki** verdi ve sürekli soru sorulmasını istemiyor. Kurallar Septic'ten daha serbesttir.

## Çalışma döngüsü
1. `docs/crawlspace-seo-roadmap.md` içindeki işaretlenmemiş maddeleri sırayla al, yapabildiğini bitir.
2. Her değişiklikten sonra canlı sitede doğrula (WebFetch/REST okuma). Doğrulanmayan iş "bitti" sayılmaz.
3. Her yazma işlemini `docs/crawlspace-log.md` dosyasına tarihle ekle (ne, ID, eski → yeni). Roadmap işaretlerini güncelle. wp-ops reposunda `claude/serene-brown-qahegf` dalına commit ve push.
4. **Tüm yapılabilir maddeler bitince** siteyi yeniden tara, bulduklarını roadmap'e "Faz 5+" altında ekle ve başla.
5. Sabah özeti için durumu güncel tut.

## Araçlar
- CrawlSpacePilot: `mcp__CrawlSpacePilot_WordPress__*` (Rank Math yetenekleri `wp_ability_rank_math_*` çalışıyor; `wp_cli_run` ile `post update`, `option update`, `menu ...` kullanılabilir).
- **SepticBeacon başka sitedir (`mcp__WordPress_-_Septic__*`). Dokunma.**
- Tema dosyaları yalnızca okunabilir (`wp_privileged_files_read_query`, yol `wp-content`'e göre). Düzenleme kullanıcıdadır.
- Çıktısı büyük olan işlemleri (eklenti güncelleme) paralel yapma; sonucu `wp_list_plugins` ile doğrula.

## Serbest olanlar (onay gerekmez)
- Okuma, tarama, analiz, raporlama.
- Meta title/description (title ≤ 60, açıklama ≤ 160), focus keyword, iç link, dış kaynak linki, görsel alt metni, kategori açıklaması, menü, Rank Math ayarları.
- **Yeni yazı oluşturma ve yayınlama** (kalite kapısından sonra), **haftada en fazla 3**.
- Yayındaki yazıya iyileştirme. Büyük yeniden yazım öncesi eski durumu log'a not et (`wp_history_*` ile de geri alınabilir).
- Eklenti/tema güncelleme (ayda bir kontrol, tek tek, sonucu doğrula) ve gereksiz pasif eklenti/tema kaldırma.
- Roadmap, log, brief belgelerini güncelleme.

## Yapma / kullanıcıya bırak
- **AdSense başvurusunu göndermek, AdSense/Google hesabı işlemleri.**
- Para harcayan işler (DataForSEO, ücretli eklenti/CMP).
- Permalink/slug değişikliği (301 olmadan). Yazı/sayfa silme: yalnızca açıkça gereksiz içerik ve log'a yazarak.
- **Uydurma yazar, uzman, kaynak, istatistik, yorum, referans eklemek. Hiçbir koşulda.** Fiyat aralığı yalnızca doğrulanmış kaynakla; yoksa "fiyat işin kapsamına göre değişir" dili.
- Tema dosyaları, hosting/PHP, DNS: yapılamıyor, kullanıcı listesine ekle.

## Yeni içerik kuralları
- Konu seçimi: roadmap bölüm 3 ve GSC verisi. Aynı niyetli iki yazı yazma (kanibalizasyon). Önce mevcut yazılara bak.
- Konu güvenlik/sağlık/yapı ile ilgili. Yalnızca resmi/akademik kaynaklara (EPA, ENERGY STAR, DOE, CDC, Building Science Corp., üniversite uzantı servisleri, eyalet kurumları) dayan, kaynak linkleri ekle, bilmediğin sayıyı yazma. Kaynağa erişemediysen o iddiayı yazma.
- Mevcut yazıların biçimini izle: H2 yapısı, tablo, SSS, "ne zaman profesyonel çağırılmalı", kaynaklar, ilgili yazılara iç link (en az 3).
- Her yazıda ayırt edici öğe (kontrol listesi, karar ağacı, örnek hesap, tablo).
- Görsel: yalnızca lisanslı ve kredisi verilebilen (mevcut desen: Pexels kredisi) veya özgün görsel. Uydurma "önce-sonra" fotoğrafı kullanma. Görsel yoksa öne çıkan görselsiz bırak ve log'a yaz.
- Rank Math: focus keyword, title ≤ 60, açıklama ≤ 160, doğru kategori.
- **Kalite kapısı (yayın öncesi):** ≥ 1.500 kelime, kanibalizasyon yok, kaynaklı, iç link ≥ 3, meta tamam. Geçemiyorsa taslak bırak.
- Yayın tarihlerini doğal dağıt (toplu günlük yayın izlenimi verme), en az 1 gün ara.

## Sabah özeti (her sabah, Türkçe, kısa)
1. **Dün yapılanlar** (log'dan).
2. **Roadmap'te kalanlar:** yapabileceğim ve **sadece senin yapabileceğin** maddeler ayrı.
3. **Karar bekleyenler** (varsa).
4. **AdSense kapısı:** 8 kriterin durumu ve 15 Aralık'a kalan gün.
5. Telefon bildirimi için `PushNotification` aracı varsa kullan.

## Kullanıcıya ait, bende bekleyen işler (özet her gün hatırlatır)
- Tema: `header.php` ve `footer.php`'e About + Contact (veya `wp_nav_menu`) ekle. (`primary` konumu Primary Menu'ye atanmış durumda.)
- Rank Math → Analytics / Search Console'u Google girişiyle bağla, `sitemap_index.xml` gönder.
- PHP 8.3 (hosting).
- Çerez onayı (CMP) için Google sertifikalı eklenti seçimi.
- Yazar/gözden geçiren gerçek kimlik kararı (isteğe bağlı).
- Güvenlik başlıkları (hosting/CDN).
