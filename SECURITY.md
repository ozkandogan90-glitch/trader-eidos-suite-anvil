# 🔒 Security Policy

## Desteklenen Versiyonlar

| Version | Supported |
|---------|-----------|
| 8.0.x   | ✅ Yes    |
| < 8.0   | ❌ No     |

## Security Vulnerability Raporla

**Lütfen security issue'ları GitHub Issues'ta açMAYIN!**

Bunun yerine security@example.com adresine özel mesaj gönder veya
GitHub Security Advisory'sini kullan:

https://github.com/yourusername/trader-eidos-suite-anvil/security/advisories

### Raporlama Formatı
1. Vulnerability'nin açıklaması
2. Etkilenen versiyonlar
3. Örnek proof-of-concept (varsa)
4. Önerilen fix (varsa)

## Security Best Practices

### Development
- [ ] Tüm input'lar validate et
- [ ] Environment variables kullan (hardcode etme)
- [ ] Dependencies güncel tut
- [ ] Code review yap
- [ ] Tests yaz

### Deployment
- [ ] HTTPS kullan
- [ ] Authentication uygula
- [ ] Rate limiting ekle
- [ ] Logging ve monitoring
- [ ] Regular backups

### Sensitive Data
```python
# ❌ Yanlış
API_KEY = "sk-12345"

# ✅ Doğru
import os
API_KEY = os.getenv("API_KEY")
```

### Dependency Management
```bash
# Check for vulnerabilities
pip audit

# Keep dependencies updated
pip install --upgrade -r requirements.txt
```

## Security Updates

Güvenlik güncellemeleri:
- CHANGELOG.md'ye kaydedilir
- GitHub Security Advisory'de duyurulur
- Özel bir release'de yayınlanır

## Sorular?

Email: security@example.com

---

*Last Updated: 30 Ekim 2025*
