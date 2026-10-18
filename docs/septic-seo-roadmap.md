# SepticBeacon: SEO Analizi ve Roadmap

Tarih: 17 Ekim 2026 · Site: https://septicbeacon.com · Kapsam: DataForSEO ve Search Console olmadan, siteden ve WordPress'ten okunan veriler.

> Bu belgedeki "fırsat" ve "boşluk" maddeleri hipotezdir. Arama hacmi ve sıralama verisi olmadan doğrulanmadı. Faz 1 sonunda Search Console verisiyle test edilecek.

## 0. Ana hedef: AdSense ile gelir

**Hedef başvuru tarihi: 15 Aralık 2026** (≈8 hafta). Başvuru, aşağıdaki kapı kriterlerinin tamamı sağlanırsa yapılır. Sağlanmazsa tarih bir hafta kaydırılır ve eksik madde kapatılır. Başvuruyu erken yapıp reddedilmek zaman kaybettirir.

> Aşağıdaki sayısal eşikler **bizim kendi hedeflerimiz**. Google AdSense için sabit bir trafik veya yazı sayısı şartı yayınlamıyor. Onay; içerik kalitesi, politika uyumu, gerekli sayfalar ve kullanıcı deneyimi üzerinden veriliyor.

### Başvuru kapısı (hepsi ✅ olmalı)

| # | Kriter | Hedef | Şu an |
|---|---|---|---|
| 1 | Yayınlanmış özgün yazı | ≥ 45 (her biri ≥ 1.500 kelime) | 33 |
| 2 | Search Console'da indekslenen sayfa | gönderilen tüm URL'lerin ≥ %95'i | bilinmiyor |
| 3 | Organik görünürlük | son 28 günde ≥ 3.000 gösterim ve ≥ 150 tıklama, artış eğiliminde | bilinmiyor |
| 4 | Gerekli sayfalar | About, Contact, Privacy (reklam/çerez bölümü dahil), Disclaimer, gezinme menüsünde | var (Privacy'ye reklam bölümü eklenecek) |
| 5 | Kimlik ve güven | Gerçek/tanımlı yazar sayfası, kaynak linkleri, favicon ve logo | yok (favicon ayarlı değil) |
| 6 | Çerez onayı (CMP) | EEA/UK/İsviçre için Google sertifikalı onay aracı | yok |
| 7 | Teknik sağlık | 404/kırık link yok, sitemap tam, mobil uyumlu, HTTPS, Core Web Vitals "iyi" | sitemap eksik |
| 8 | Politika temizliği | boş/ince sayfa yok, spam yorum yok, telif sorunu yok, "ince içerik" riski gözden geçirilmiş | gözden geçirilecek |

### Kontrol noktaları
- **7 Kasım:** Faz 0 ve Faz 1 bitti mi? Search Console verisi 3 haftalık oldu mu?
- **1 Aralık:** Go/no-go ön değerlendirmesi. Eksik kriterler için 2 haftalık plan.
- **15 Aralık:** Tüm kriterler tamam ise başvuru.
- Başvurudan sonra: onay gelirse `ads.txt` yayınla, reklam yerleşimini kademeli aç. Red gelirse gerekçeyi oku, düzelt, **en az 2 hafta** sonra tekrar başvur.

### AdSense için en büyük risk
Site yeni ve içerik hızlı üretilmiş görünüyor (33 yazı ~1 ayda). Google "düşük değerli / ölçekli üretilmiş içerik" nedeniyle reddedebilir. Azaltmak için: gerçek yazar kimliği, özgün görseller veya diyagramlar, kaynaklı veriler, uzman gözden geçirme notu, her yazıda ayırt edici bir bilgi (örnek hesap, kontrol listesi, karar ağacı). Bu madde Faz 2'nin önceliğidir.

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

### Faz 0'da keşfedilenler (17 Ekim)
- **Sitemap kök nedeni:** Rank Math ayarlarında hariç tutulan yazı yok. Post sitemap'in en yeni `lastmod` değeri 7 Ekim, yani sitemap önbelleği ~7 Ekim'den beri yenilenmemiş. Eksik 11 yazının 8'i çöp kutusundan geri alınmış (`_wp_trash_meta_*` kalıntısı), 3'ü sonradan yayınlanmış. Yazıların kendisi indekslenebilir (robots ve canonical doğru).
- **Google ve Bing site doğrulaması zaten yapılmış** (Rank Math'te doğrulama kodları var). Rank Math Analytics ve Instant Indexing modülleri açık.
- **Favicon / site simgesi ayarlı değil** (`site_icon` boş).
- **Yorumlar ve pingler açık** (spam riski, AdSense için temizlenmeli).
- **Breadcrumb kapalı.** İç link ve şema için açılabilir.
- **llms.txt:** Rank Math `llms_post_types` ayarı var ama `/llms.txt` 404 veriyor, rewrite kuralları yenilenmeli.
- **Meta açıklaması uzun** olan örnek: `signs-of-drain-field-failure` (~190 karakter).

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
- [ ] **Sitemap'i düzelt:** ⏳ Kök neden: eski önbellek. API üzerinden temizlenemedi, Rank Math'te Sitemap Settings → Save Changes ile elle yenilenmeli. 11 eksik yazı sitemap'e girsin (Rank Math sitemap önbelleğini yenile / neden eksik olduğunu bul). *Risk: düşük.*
- [ ] **Search Console'u bağla:** mülk doğrulaması, sitemap gönderimi, `gsc-api` reposuyla veri çekme. *Kullanıcıdan Google erişimi gerekir.*
- [x] **Ana sayfa / `/blog/` title ayrımı:** ana sayfa markayı ve konuyu, `/blog/` rehber arşivini anlatsın. *Risk: düşük.*
- [ ] **http→https ve www** yönlendirmesini doğrula.

### Faz 1: Hızlı kazanımlar (1 hafta)
- [x] **Meta düzeltmeleri:** 5 uzun açıklama, 4 title (160 / 60 karakter sınırı). ✅ 18 Eki: 6 açıklama ve 1 title kısaltıldı, `/blog/` için ayrı title/açıklama yazıldı. Canlı taramada 65+ karakterlik title ve 160+ açıklama kalmadı.
- [x] **İç link yeniden dağıtımı:** yetim ve tek linkli 8 yazıya, ilgili güçlü yazılardan bağlam içi linkler. Hedef: her yazıya en az 3 gelen link. ✅ 18 Eki: 21 yazıdaki "Related" kutusuna link eklendi. Yetim yazı kalmadı, her yazı en az 3 gelen link alıyor.
- [ ] **Kategori temizliği:** boş "System Types" ve "Uncategorized" için karar (kaldır veya doldur), yazıları doğru kategoriye al, kategori sayfalarına tanıtım metni ekle. *Kategori silmek URL değiştirir, 301 gerekir.*
- [ ] **llms.txt** ekle (Rank Math veya manuel). ⏳ Hâlâ 404. Rank Math → General Settings → Edit llms.txt ve Permalinks → Save ile rewrite yenilenmeli.
- [ ] **FAQPage şeması:** ⏸ Ertelendi. Google 2023'ten beri FAQ zengin sonuçlarını çoğunlukla devlet ve sağlık sitelerine gösteriyor, getirisi düşük, 23 yazıda toplu şema değişikliği riskine değmez.
- [ ] **Kurumsal sayfa şemaları:** ⏸ Ertelendi, düşük etki.
- [ ] **Güvenlik başlıkları:** sunucu/CDN düzeyinde. *Sunucu erişimi veya hosting paneli gerekir.*
- [x] **AdSense hazırlığı:** favicon ve site logosu ekle, yorumları ve pingleri kapat (veya moderasyona al), Privacy sayfasına reklam/çerez bölümü ekle, menüde About/Contact/Privacy/Disclaimer görünürlüğünü doğrula, breadcrumb'ı aç. ⏳ Kısmen: favicon ayarlandı (medya 409, 39 sayfada görünüyor), yorum ve ping yeni içerikte, 33 yazıda ve 6 sayfada kapatıldı. Doğrulananlar (18 Eki): Privacy sayfasında reklam/çerez bölümü zaten var, alt bilgide ve menüde About/Contact/Privacy/Disclaimer var, iletişim formu (`sb-contact-form`) var. Kalan: breadcrumb (ayar yazılamadı, elle açılmalı, tema kancası gerekir), iletişim formunun gönderim testi.

### Faz 2: Güven ve içerik kalitesi (2-4 hafta)
- [ ] **Yazar kimliği:** "Editorial Team" yerine gerçek yazar/gözden geçiren, kısa biyografi ve uzmanlık. *Kullanıcı kararı: gerçek bir kişi/uzman olmadan uydurma yazar eklenmez.*
- [ ] **Kaynak ve inceleme notları:** sigorta, garanti, finansman, güvenlik konularında kaynak linkleri ve "son gözden geçirme" tarihi.
- [ ] **Çerez onayı (CMP):** Google sertifikalı bir CMP kur (EEA/UK/İsviçre için zorunlu), AdSense'ten önce test et.
- [ ] **Yazı sayısını 45'e çıkar** (haftada ~1,5 yazı), her yazıda ayırt edici öğe (örnek hesap, kontrol listesi, karar ağacı) ve özgün görsel.
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


## 7. Faz 5: Büyüme araştırması (18 Ekim)
- [x] **Rakip analizi:** `docs/septic-competitor-analysis.md` (SERP arketipleri, sorgu bazlı gözlemler, konumlanma). Hacim/zorluk verisi yok, Search Console ve DataForSEO ile doğrulanacak.
- [x] **İçerik brief'leri:** `docs/briefs/` altında 9 brief (kış bakımı, sistem türleri hub, mound, perc test, riser, firma seçimi, filtre, malzemeler, eyalet dizini).
- [x] **Backlink planı:** `docs/septic-backlink-plan.md` (kurallar, linkable asset önerileri, hedef türleri, e-posta taslakları). **E-posta gönderilmedi.**
- [x] **Brief 1 yazıldı ve yayınlandı** (18 Eki): `septic-system-winter-care` (yazı 511), yalnızca MPCA (23 Ocak 2026) ve EPA metinlerine dayanıyor, 4 yazıdan link verildi.
- [ ] **Brief 2:** `types-of-septic-systems` (EPA types sayfasını `curl` ile okuyup yaz).
- [ ] **Eyalet dizini pilotu** (5 eyalet, resmi kurum sayfaları elle doğrulanarak).
- [ ] **Alıcı kontrol listesi PDF'i.**
- [ ] **Search Console bağlanınca:** backlink profilini ölç, brief önceliklerini veriye göre yeniden sırala.

## 8. İçerik denetimi ve kanibalizasyon (18 Ekim)
- [x] **İçerik denetimi:** `docs/septic-content-audit.md` (claude-seo kuralları: seo-page, seo-content, seo-cluster). 33 yazı + 6 sayfa.
- [x] **Görsel boyutları ve srcset:** 43 görselde `wp-image-ID` ve `width/height` eklendi (19 yazı).
- [x] **Kaynak bölümleri:** 8 yazıya doğrulanmış EPA "Further reading".
- [x] **Kanibalizasyon aksiyonu:** `septic-system-cost` pillar, `septic-tank-installation-cost` spoke olarak ayrıştırıldı (benzerlik 0,72 → 0,64).
- [x] **Birleştirme ve 301** (18 Eki, karar bende): `septic-tank-installation-cost` içeriği `septic-system-cost` pillar'ına taşındı, 301 yönlendirme Rank Math ile kuruldu ve doğrulandı, eski yazı taslağa alındı, 6 yazıdaki iç link güncellendi.
- [x] **Jetpack Image CDN açıldı** (18 Eki): görseller i0.wp.com üzerinden WebP olarak geliyor (örnek 273 KB → 60 KB). Gizlilik politikasına "Image delivery" bölümü eklendi.
- [ ] **İç link yoğunluğunu dengele:** 10 yazıya bağlam içi link, maliyet kümesinde azalt.
- [ ] **Satır içi görseli olmayan 14 yazı için özgün görsel/diyagram.**


## 9. Faz 6: Veri odaklı büyüme programı (kullanıcı talebi, 18 Ekim)
Önkoşullar: DataForSEO hesabı (ortam değişkenleri `DATAFORSEO_LOGIN`, `DATAFORSEO_PASSWORD`), Pexels anahtarı (`PEXELS_API_KEY`). Anahtarlar sohbete yazılmaz, bulut ortamı ayarlarından eklenir. Yeni oturum gerekir.

- [ ] **6.1 DataForSEO'yu bağla** (resmi `dataforseo-mcp-server` v3 veya CLI modu, claude-seo `seo-dataforseo` skill'i, maliyet koruması `dataforseo_costs.py`). *Bekleyen: anahtarlar.*
- [ ] **6.2 Düşük kaliteli / düşük tıklama ihtimalli / kanibalize içerik tespiti, sil veya birleştir (301 ile).** Kullanıcı silme ve birleştirme yetkisi verdi. Veri (Search Console + DataForSEO) gelince karar ver, kararları günlüğe yaz.
- [ ] **6.3 Genel teknik tarama ve şema (kusursuz):** tüm iç linkler (kırık), yönlendirme zincirleri, robots, sitemap geçerliliği, canonical, başlık/H1, görseller, güvenlik başlıkları, JSON-LD doğrulaması (Organization, WebSite, BreadcrumbList, Article/BlogPosting, AboutPage, ContactPage). claude-seo `seo-technical` ve `seo-schema` kuralları.
- [ ] **6.4 Site hızı:** PageSpeed ölçümü, görsel (CDN yapıldı), yazı tipleri, render-engelleyici, önbellek. Tema/sunucu müdahalesi için araç sınırı var (aşağıya bak).
- [ ] **6.5 İlk veri kaydı (baseline)** Google Drive'da Sheet: "Neredeydik, nereye geldik" (başlangıç ve şimdiki metrikler, yapılan değişiklikler).
- [ ] **6.6 Rakip analizi** (Sheet): trafik, en görünür anahtar kelimeler, en çok tıklanan sayfalar, backlink sayısı. Ayrı sekme: en önemli backlinkler (dofollow + düşük spam skoru + yüksek domain rank; nofollow olanlar ayrıca işaretli). Skill: claude-seo `seo-dataforseo`, `seo-backlinks`, `seo-competitor-pages`. Eksik kalırsa kendi skill'imiz yazılacak.
- [ ] **6.7 Anahtar kelime araştırması** (Sheet): hacim, zorluk, **CPC** (AdSense geliri için), boş alanlara doğrudan sıralama hedefi.
- [ ] **6.8 Anahtar kelime ve içerik boşluğu (gap)** rakiplere göre.
- [ ] **6.9 İçerik planı**, gap'lere dayalı.
- [ ] **6.10 Mevcut içerik analiz skill'i entegrasyonu:** claude-seo `seo-content` + `seo-page` + `seo-cluster` repoya vendor edilecek (`.claude/skills/`), eksik alanlar düzenlenecek.
- [ ] **6.11 Görsel altyapısı (yeni içerikten ÖNCE):** Pexels API ile görsel çekme (alt metin, fotoğrafçı kredisi, WebP, medya kitaplığına yükleme) + özgün diyagramlar (SVG/PNG, kendi ürettiğimiz). *Bekleyen: Pexels anahtarı.*

## 10. 18 Ekim kararları ve bulguları
- [x] **Editör kimliği (karar bende):** Gerçek yazar adı kullanılmıyor. "SepticBeacon Editorial Team" imzası + **Editorial Policy** sayfası (`/editorial-policy/`: kaynak yöntemi, yapay zekâ destekli taslak açıklaması, "uzman değiliz" beyanı, düzeltme e-postası, reklamdan bağımsızlık). 33 yazıya imza satırı ve politika linki eklendi, yazar alanı tekilleştirildi (PUBL → Editorial Team). Uydurma uzman yok. AdSense'te yazar adı zorunlu değil, şeffaflık ve kalite önemli.
- [x] **Sitemap** dinamik çalışıyor: yeni sayfa yayınlanınca `page-sitemap.xml` anında güncellendi. Rank Math kalıyor.
- [x] **llms.txt** açık, **breadcrumb** kullanıcı tarafından açıldı.
- [ ] **İletişim formu hatası ("We couldn't send that message")**: form tema kodunda (`generatepress-wpvibe-backup`, `sb_contact_submit`). Sayfalar (contact, privacy, about, disclaimer) tema şablonundan sabit metinle çiziliyor, WordPress sayfa içeriğini kullanmıyor. Yaptığım düzenlemeler canlıda görünmüyor. **Çözüm için tema dosyalarına erişim gerekiyor** (Easy MCP AI ayarlarında "privileged" araçları açmak, ya da tema kodunu düzenleyebilmek). Alıcı adresi `info@septicbeacon.com` olmalı.
- [ ] **Gizlilik politikası, Jetpack Image CDN bildirimi:** sayfa içeriğine ekledim ama şablon göstermiyor. Aynı tema erişimi gerekli.
- [ ] **Güvenlik başlıkları:** `docs/security-headers.md` içindeki kod `.htaccess`'e eklenecek (hosting).
