# 🤝 Katkıda Bulunma Rehberi

Bu dokümanda, **Trader Eidos Suite - Anvil Skeleton** projesine nasıl katkıda bulunabileceğiniz açıklanmaktadır.

---

## 📋 İçindekiler

1. [Başlamadan Önce](#başlamadan-önce)
2. [Geliştirme Ortamı Kurulumu](#geliştirme-ortamı-kurulumu)
3. [Katkı Türleri](#katkı-türleri)
4. [Kod Standartları](#kod-standartları)
5. [Pull Request Süreci](#pull-request-süreci)
6. [Commit Mesajları](#commit-mesajları)

---

## 👋 Başlamadan Önce

### Projeyi Anla
- [README.md](./README.md) - Proje hakkında genel bilgi
- [PROJECT_SUMMARY.md](./PROJECT_SUMMARY.md) - Detaylı proje özeti
- [KURULUM_REHBERI.md](./KURULUM_REHBERI.md) - Kurulum talimatları
- [docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md) - Mimarisi detayları

### Formu Klonla
```bash
git clone https://github.com/yourusername/trader-eidos-suite-anvil.git
cd trader-eidos-suite-anvil
git remote add upstream https://github.com/original/trader-eidos-suite-anvil.git
```

---

## 🔧 Geliştirme Ortamı Kurulumu

### 1. Python 3.10+ Yükle
```bash
# macOS
brew install python@3.10

# Ubuntu/Debian
sudo apt-get install python3.10

# Windows
# https://www.python.org/downloads/ indir ve yükle
```

### 2. Virtual Environment Oluştur
```bash
python3.10 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. Bağımlılıkları Yükle
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Development tools
```

### 4. Pre-commit Hooks Kur
```bash
pre-commit install
```

---

## 🎯 Katkı Türleri

### 1. Bug Raporları
**Issue açmadan önce kontrol et:**
- [ ] Sorun halen geçerli mi?
- [ ] Başkası bunu rapor etti mi?
- [ ] Hangi Anvil versiyonunu kullanıyorsun?

**Issue başlığı formatı:**
```
[BUG] Kısa açıklama - 5 satır altında
```

**Issue açıklaması:**
```markdown
## Sorun Açıklaması
Ne olması gerekiyordu?

## Mevcut Davranış
Ne oluyor?

## Adımlar Tekrarla
1. Adım 1
2. Adım 2
3. Adım 3

## Beklenen Davranış
Ne olması gerekiyordu?

## Ortam Bilgisi
- Anvil Versiyon: X.X.X
- Python Versiyon: 3.10+
- OS: macOS/Linux/Windows
```

### 2. Özellik Önerileri
**Issue başlığı formatı:**
```
[FEATURE] Kısa açıklama
```

**Issue açıklaması:**
```markdown
## Açıklama
Bu özelliği neden istiyorsun?

## Çözüm Önerisi
Nasıl uygulanmalı?

## Alternatifler
Başka seçenekler var mı?

## Bağlam
İlgili diğer issue'lar veya PR'lar
```

### 3. Dokümantasyon İyileştirmeleri
- Yazım hatalarını düzelt
- Açıklamaları geliştir
- Örnekler ekle
- Çeviriler yap (Türkçe/English)

### 4. Kod İyileştirmeleri
- Performance optimizasyonu
- Code cleanup
- Test'ler ekleme
- Type hints iyileştirme

---

## 📝 Kod Standartları

### Stil Rehberi
Python kodunuz **PEP 8** ve **Black** formatını takip etmelidir.

```bash
# Biçimlendirmeyi kontrol et
black --check server_code/
flake8 server_code/

# Otomatik olarak biçimlendir
black server_code/
```

### Type Hints
**Tüm fonksiyonlar type hint'ler içermeli:**

```python
# ❌ Yanlış
def get_market_regime(symbol):
    return {}

# ✅ Doğru
def get_market_regime(symbol: str) -> Dict[str, Any]:
    """Piyasa rejimi bilgisini al."""
    return {}
```

### Docstrings
**NumPy stili docstring'ler kullan:**

```python
def run_strategy_scan(symbols: List[str], limit: int = 10) -> Dict[str, Any]:
    """
    Strateji taraması yap.
    
    Parameters
    ----------
    symbols : List[str]
        Taranacak hisse senedi sembolleri
    limit : int, optional
        Maksimum sinyal sayısı (default 10)
    
    Returns
    -------
    Dict[str, Any]
        Sinyal detaylarını içeren sözlük
        
    Examples
    --------
    >>> result = run_strategy_scan(["AAPL", "GOOGL"])
    >>> result["signals_found"]
    5
    """
    pass
```

### Logging
```python
import logging

logger = logging.getLogger(__name__)

logger.info("İşlem başladı")
logger.error(f"Hata oluştu: {error}")
```

### Error Handling
```python
from error_handler import handle_anvil_errors, AnvilError

@handle_anvil_errors
def my_function():
    if not data:
        raise AnvilError("DATA_NOT_FOUND", "Veri bulunamadı")
    return data
```

---

## 🔄 Pull Request Süreci

### 1. Feature Branch Oluştur
```bash
git checkout -b feature/amazing-feature
# veya
git checkout -b bugfix/issue-123
# veya
git checkout -b docs/add-architecture
```

### 2. Değişiklikleri Yap
```bash
# Kodunuzu değiştir
vim server_code/server_main.py

# Değişiklikleri kontrol et
git status
git diff
```

### 3. Commit Et
```bash
git add server_code/server_main.py
git commit -m "feat: piyasa rejimi fonksiyonunu geliştir"
```

### 4. Push Et
```bash
git push origin feature/amazing-feature
```

### 5. Pull Request Aç
- GitHub'da "Create Pull Request" tıkla
- Başlığı ve açıklamasını doldur
- Reviewer'ları ata
- Checks'lerin geçmesini bekle

### 6. Code Review
- Geri bildirimleri dikkate al
- Değişiklikleri yap
- Tekrar push et (PR otomatik güncellenecek)

### 7. Merge
- Reviewer onayladıktan sonra
- "Squash and merge" önerilir
- Branch'i sil

---

## 💬 Commit Mesajları

**Format:**
```
<type>: <subject>

<body>

<footer>
```

### Type (Tür)
- `feat:` - Yeni özellik
- `fix:` - Bug fix
- `docs:` - Dokümantasyon
- `style:` - Code style (formatting, etc.)
- `refactor:` - Kod yeniden düzenleme
- `perf:` - Performance iyileştirme
- `test:` - Test ekleme/değiştirme
- `chore:` - Build, dependencies, etc.

### Subject (Konu)
- İmperative mood kullan ("add", "fix", "remove" değil "adds", "fixes", "removes")
- Büyük harf kullanma
- Nokta kullanma
- 50 karakterden az

### Body (Gövde)
- Değişikliğin **neden** yapıldığını açıkla
- Ne değiştiğini değil, neden değiştiğini koy
- 72 karakterde satır ara

### Footer (Alt bilgi)
```
Closes #123
Related-To: #456
Breaking-Change: açıklama
```

### Örnekler
```
feat: piyasa rejimi algılama algoritmasını geliştir

Trend score hesaplaması daha doğru hale getirildi.
Market structure tespiti optimize edildi.

Closes #42
```

```
fix: cache invalidation hatası düzelt

TTL süresi dolmuş cache'in silinmemiş olduğu hata giderildi.

Fixes #315
```

---

## ✅ Kontrol Listesi

PR açmadan önce kontrol et:

- [ ] Branch en güncel upstream/main'den oluşturuldu
- [ ] Kod PEP 8 ve Black formatını takip ediyor
- [ ] Tüm fonksiyonlar type hint'ler içeriyor
- [ ] Docstring'ler mevcut ve doğru
- [ ] Tests yazıldı/güncellendi
- [ ] README veya docs güncellendi (gerekirse)
- [ ] CHANGELOG.md güncellenecek mi?
- [ ] Commit mesajları anlamlı
- [ ] Hiç debug code yok (print, console.log, etc.)
- [ ] Hiç sensitive data yok (.env, keys, etc.)

---

## 🧪 Testing

### Unit Tests Çalıştır
```bash
pytest tests/
pytest -v  # Verbose
pytest --cov=server_code  # Coverage raporu
```

### Anvil'de Test Et
```
Anvil Editor → F5
Test modu başla ve mock veriyi kontrol et
```

### Type Check
```bash
mypy server_code/
```

### Code Quality
```bash
flake8 server_code/
pylint server_code/
black --check server_code/
```

---

## 📖 Dokümantasyon

Yeni özellik eklerseniz dokümantasyon yazın:

- **Feature eklendi:** `docs/FEATURES.md` güncellenecek
- **API değişti:** Docstring'ler güncellenecek
- **Kurulum değişti:** `KURULUM_REHBERI.md` güncellenecek
- **Mimarisi değişti:** `docs/ARCHITECTURE.md` güncellenecek

---

## 🎓 Geliştirme Temaları

### Backend Entegrasyon
Dosya: `docs/BACKEND_INTEGRATION.md`

Mock fonksiyonları gerçek backend fonksiyonlarıyla değiştirme.

### UI Tasarım
Anvil Designer'da form'ları geliştirme.

### Performance
Caching ve query optimizasyonu.

### Testing
Unit ve integration test'ler yazma.

---

## 📞 Destek

Sorularınız varsa:

1. 📖 Dokümantasyonu oku
2. 💬 GitHub Issues'ta sor
3. 🔍 Mevcut issue'ları ara
4. 📧 Proje maintainers'a yaz

---

## 🙏 Teşekkürler!

Projeye katkıda bulunmak için teşekkürler! Her katkı değerlidir.

---

**Happy Coding! 🚀**

*Last Updated: 30 Ekim 2025*
