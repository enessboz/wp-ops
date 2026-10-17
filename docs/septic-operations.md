# SepticBeacon: İşletme Kılavuzu (otomatik çalışma kuralları)

Bu belge, zamanlanmış çalışma oturumlarının uyacağı kalıcı kurallardır. Hedef: septicbeacon.com'u AdSense onayına (hedef başvuru 15 Aralık 2026) ve sürdürülebilir organik büyümeye taşımak. Plan: `docs/septic-seo-roadmap.md`. Değişiklik kaydı: `docs/septic-log.md`.

## Çalışma döngüsü
1. `docs/septic-seo-roadmap.md` içindeki işaretlenmemiş maddeleri sırayla al, yapabildiğini bitir.
2. Her değişiklikten sonra canlı sitede doğrula (tarama, REST okuma). Doğrulanmayan iş "bitti" sayılmaz.
3. Yaptığın her yazma işlemini `docs/septic-log.md` dosyasına tarihle ekle (ne, hangi ID, eski değer, yeni değer). Roadmap işaretlerini güncelle, `claude/confident-bardeen-075xyr` dalına commit ve push.
4. Roadmap'teki **tüm yapılabilir maddeler bitince** yeni fırsat keşfet: siteyi yeniden tara (teknik, içerik, iç link, şema, hız), Search Console verisi varsa oku, bulduklarını roadmap'e "Faz 5+" altında ekle ve başla.
5. Sabah özeti (aşağıda) için durumu güncel tut.

## Araçlar
- Septic sitesi: `WordPress - Septic` MCP araçları (`mcp__WordPress_-_Septic__*`). Yazma için `wp_update_post_meta`, `wp_replace_in_post`, `wp_update_post`, `wp_rest_write`.
- **CrawlSpacePilot başka bir sitedir. Dokunma.**
- Kamuya açık site okumaları için `curl` ve claude-seo betikleri (SSRF koruması proxy yüzünden çalışmıyor, `curl` kullan).
- Rank Math ayar yazma rotaları (`/rankmath/v1/updateSettings`, `toolsAction`) bu araçla hata veriyor, tekrar deneme. Bu işler kullanıcıya bırakılır.

## Serbest olanlar (onay gerekmez)
- Okuma, tarama, analiz, raporlama.
- Meta title/description düzeltmesi (title ≤ 60, açıklama ≤ 160 karakter), iç link ekleme (mevcut "Related" kutusu desenini kullan), yazım hatası düzeltme, görsel alt metni, kategori açıklaması.
- Yeni makale **taslak (draft)** olarak oluşturma (aşağıya bak).
- Roadmap, log, brief belgelerini güncelleme.

## Yetki durumu
Kullanıcı (18 Ekim) **tüm kararları ve işleri bana devretti**. Birleştirme, yönlendirme, görsel CDN gibi kararları ben veriyorum. Aşağıdaki liste artık "onay bekle" değil, **kendi koyduğum güvenlik sınırlarıdır**: geri alınamaz, para harcayan, kimliğe bağlı veya dışarıya giden işlerde yine de dikkatli ol.

## Güvenlik sınırları (sabah özetinde bilgi ver, tek taraflı yapma)
- Yazı, sayfa, kullanıcı, kategori, medya **silme** ya da çöpe atma.
- Plugin/tema kurma, güncelleme, silme. Rank Math global ayarları. Permalink veya URL değişikliği (301 gerekir).
- Yayınlanmış bir yazının ana içeriğini yeniden yazma.
- Para harcayan her şey (DataForSEO bakiyesi dahil).
- **AdSense başvurusunu göndermek.** Kullanıcı yapar. Kapı kriterleri sağlanınca sadece haber ver.
- Uydurma yazar, uzman, kaynak, istatistik, yorum, referans eklemek. Hiçbir koşulda.

## Yeni içerik kuralları
- Konu seçimi: roadmap bölüm 3'teki hipotezler ve Search Console verisi. Aynı niyetli iki yazı yazma (kanibalizasyon). Önce mevcut 33 yazıya bak.
- Septic bilgisi güvenlikle ilgilidir: yalnızca resmi kaynaklara (EPA, üniversite uzantı servisleri, eyalet sağlık/çevre kurumları) dayan, kaynak linklerini ekle, bilmediğin sayıyı yazma. Fiyat aralıklarında "yaklaşık/değişir" dili kullan ve kaynağını belirt.
- Her yazıda ayırt edici bir öğe (kontrol listesi, karar ağacı, örnek hesap, tablo) ve mevcut yazılarla iç linkler olsun. Mevcut yazıların biçimini (H2 yapısı, SSS, kaynaklar, `sb-note` Related kutusu) izle.
- Görsel: özgün olmayan görsel kullanma. Görseli olmayan taslak olarak bırak ve belirt.
- **Durum: taslak.** Yayınlama izni kullanıcıdan gelene kadar her yeni yazı `draft` kalır. Kullanıcı "otomatik yayınla" derse bu bölümü güncelle.
- Hız: haftada en fazla 2 yeni taslak.

## Sabah özeti (her sabah)
Türkçe, kısa, şu başlıklarla:
1. **Dün yapılanlar** (log'dan).
2. **Roadmap'te kalanlar:** yapabileceğim ve **sadece senin yapabileceğin** maddeler ayrı listelensin.
3. **Karar bekleyenler** (taslaklar, onay istekler).
4. **AdSense kapısı:** 8 kriterin durumu ve 15 Aralık'a kalan gün.
5. Telefon bildirimi için `PushNotification` aracını kullan (varsa).

## Kullanıcıya ait, bende bekleyen işler (özet her gün hatırlatır)
- Rank Math → Sitemap Settings → **Save Changes** (11 yazı sitemap'te yok).
- Rank Math → General Settings → **Breadcrumbs** aç + temada çıktıyı ekle (GeneratePress).
- Settings → Permalinks → **Save**, `/llms.txt` 404'ü için.
- **Çerez onayı (CMP)** eklentisi kur, Google sertifikalı (EEA/UK).
- **Yazar kimliği:** gerçek yazar adı ve kısa biyografi.
- İletişim formunu bir kez **test et** (gönderim ulaşıyor mu).
- Rank Math Analytics'e **Search Console** bağla (Google girişi).
- (İsteğe bağlı) DataForSEO hesabı ve API anahtarı.
