# 🚀 Trader Eidos Suite - GitHub & Anvil Setup Guide

## ⚡ Quick Start (GitHub to Anvil)

### 1️⃣ GitHub'a Push Et (5 dakika)

```bash
cd trader-eidos-suite-anvil
git add -A
git commit -m "chore: update to Anvil-ready structure"
git push origin master
```

### 2️⃣ GitHub Doğrulaması

Şu adrese git: https://github.com/ozkandogan90-glitch/trader-eidos-suite-anvil

✅ Repo root'unda görmeli:
- `anvil.yaml`
- `client_code/` folder
- `server_code/` folder
- `theme/` folder
- `.anvil/` folder

### 3️⃣ Anvil'den Clone Et

1. **Anvil Dashboard** açın: https://anvil.works/build
2. **"Clone from GitHub"** seçin
3. **URL girin:**
   ```
   https://github.com/ozkandogan90-glitch/trader-eidos-suite-anvil.git
   ```
4. **Clone** butonuna basın
5. ⏳ 30 saniye bekleyin
6. ✅ **Proje yüklenecek!**

---

## 📋 Gerekli Yapı Doğrulaması

```bash
# Terminal'de yerel repo'da çalıştır:

# 1. Root dosyaları kontrol et
ls -la anvil.yaml client_code/ server_code/ theme/

# 2. Meta folder kontrol et
ls -la .anvil/

# 3. Git config
git remote -v
git branch

# ✅ Hepsi görünmeli
```

---

## 🔍 Sorun Çıkarsa

| Hata | Çözüm |
|------|-------|
| `CredentialsProvider` error | `anvil.yaml` root'ta mı? GitHub'da kontrol et |
| "Branch not found" | Default branch = `master` olmalı (GitHub Settings) |
| "No modules found" | `client_code/` ve `server_code/` klasörleri var mı? |
| Clone başarısız | Repository public mı? URL doğru mu? |

---

## 📁 Anvil-Ready Yapı

Bu ZIP'te önceden hazırlı:

```
✅ anvil.yaml                (Anvil config - root'ta)
✅ .anvil/metadata          (Anvil metadata)
✅ client_code/             (11 Form)
✅ server_code/             (14 Module)
✅ theme/                   (CSS styling)
✅ public/                  (Assets)
✅ .gitignore              (Git rules)
✅ requirements.txt        (Dependencies)
```

---

## 🎯 Sonrası

Clone başarılı oldu? Şimdi:

1. **Forms:** Anvil Designer'da UI düzenle
2. **Server:** Backend logic ekle
3. **Backend:** trader_eidos_suite entegre et
4. **Deploy:** Push et ve Anvil'de test et

---

## 💡 İpuçları

- Branch: **master** (Anvil genelde bunu tercih eder)
- Format: **YAML** (anvil.yaml - JSON değil!)
- Root: **Subfolder içinde değil!**
- Meta: **.anvil/metadata** kritik!

---

**Başarılar! 🎉**
