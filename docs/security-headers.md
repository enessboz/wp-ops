# Güvenlik başlıkları (hosting düzeyinde)

Sunucu LiteSpeed, `.htaccess` okur. WordPress'in kendi bloğunun **üstüne** (cPanel/hosting dosya yöneticisinde, `public_html/.htaccess`) ekle:

```apache
<IfModule mod_headers.c>
Header always set Strict-Transport-Security "max-age=31536000"
Header always set X-Content-Type-Options "nosniff"
Header always set X-Frame-Options "SAMEORIGIN"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
Header always set Permissions-Policy "camera=(), microphone=(), geolocation=()"
</IfModule>
```

Notlar:
- **CSP eklenmedi.** AdSense ve Jetpack CDN farklı alan adlarından içerik yükler, yanlış bir CSP reklamı ve görselleri bozar.
- HSTS'te `includeSubDomains` ve `preload` bilerek yok. Alt alan adları tamamen HTTPS ise sonra eklenebilir.
- Önce dosyanın yedeğini al. Siteyi açıp ana sayfanın yüklendiğini kontrol et.
- Doğrulama: `curl -sI https://septicbeacon.com/ | grep -iE "strict-transport|x-content|x-frame|referrer|permissions"`
