# 🎯 Trader Eidos Suite - Anvil Proje İskeleti Kurulum Rehberi

**Versiyon:** 8.0.0  
**Tarih:** 30 Ekim 2025  
**Platform:** Anvil Web Framework + Mock Data Server  

---

## 📋 İçindekiler

1. [Hızlı Başlangıç](#hızlı-başlangıç)
2. [Kurulum Adımları](#kurulum-adımları)
3. [Proje Yapısı](#proje-yapısı)
4. [Mock Veri Sistemi](#mock-veri-sistemi)
5. [Sık Sorulan Sorular](#ssk)
6. [Bir Sonraki Adımlar](#bir-sonraki-adımlar)

---

## 🚀 Hızlı Başlangıç

### Bu .zip Dosyasında Neler Var?

```
anvil_project_skeleton/
├── anvil.yaml                 # Anvil proje konfigürasyonu
├── client_code/               # Anvil Forms (İstemci Kodu)
│   ├── MainLayoutForm.py
│   ├── MarketCompassForm.py
│   ├── LeadersLeagueForm.py
│   ├── DnaTestForm.py
│   ├── StrategySimulatorForm.py
│   ├── CommandCenterForm.py
│   ├── DiscoveryLabForm.py
│   ├── PerformanceDashboardForm.py
│   ├── SimulationScreenForm.py
│   ├── AdminPanelsForm.py
│   ├── AboutForm.py
│   └── __init__.py
│
├── server_code/               # Anvil Server Modülleri
│   ├── shared_types.py        # Paylaşılan veri modelleri
│   ├── error_handler.py       # Hata yönetimi
│   ├── cache_manager.py       # Caching sistemi
│   ├── mock_data_generator.py # Mock veri üretimi ⭐
│   ├── server_main.py         # Ana sistem fonksiyonları
│   ├── server_market_compass.py
│   ├── server_leaders_league.py
│   ├── server_dna_test.py
│   ├── server_simulator.py
│   ├── server_command_center.py
│   ├── server_discovery_lab.py
│   ├── server_performance.py
│   ├── server_simulation.py
│   ├── server_admin.py
│   └── __init__.py
│
└── KURULUM_REHBERI.md         # Bu dosya!
```

---

## 📦 Kurulum Adımları

### Adım 1: Anvil'e Giriş Yapın

1. https://anvil.works adresine git
2. Hesabınıza giriş yapın (Yoksa kayıt olun)
3. "Create New App" butonuna tıklayın

### Adım 2: Projeyi İçe Aktar (Import)

#### Seçenek A: Zip Dosyasından İçe Aktar
```
1. Anvil Dashboard'da "Create New App" seçin
2. "Upload" seçeneğine tıklayın
3. Bu .zip dosyasını seçin
4. "Import" butonuna basın
```

#### Seçenek B: Git Üzerinden
```bash
git clone <repo_url>
cd anvil_project_skeleton
# Anvil CLI kullanarak yükle
anvil up
```

### Adım 3: Projeyi Açın

```
Anvil Dashboard'da "Trader Eidos Suite" projesine tıklayın
→ Proje açılacaktır ve Test modu başlayacaktır
```

---

## 🏗️ Proje Yapısı

### Client Code (Forms)

Her form, Mokap_ADMIN_v8.html'deki bir tab'a karşılık gelir:

| Form | Amaç | Durum |
|------|------|-------|
| **MainLayoutForm** | Ana navigasyon ve layout | ✅ Hazır |
| **MarketCompassForm** | Piyasa rejimi ve trend | ⚙️ İskeleton |
| **LeadersLeagueForm** | RS Rotasyonu | ⚙️ İskeleton |
| **DnaTestForm** | Trend DNA Testi | ⚙️ İskeleton |
| **StrategySimulatorForm** | Strateji Taraması | ⚙️ İskeleton |
| **CommandCenterForm** | Komuta Merkezi | ⚙️ İskeleton |
| **DiscoveryLabForm** | Keşif Laboratuvarı | ⚙️ İskeleton |
| **PerformanceDashboardForm** | Performans Analizi | ⚙️ İskeleton |
| **SimulationScreenForm** | Replay Simülasyonu | ⚙️ İskeleton |
| **AdminPanelsForm** | Sistem Yönetimi | ⚙️ İskeleton |
| **AboutForm** | Sistem Bilgisi | ⚙️ İskeleton |

### Server Code (Modules)

Her server modülü, FORMS_TO_BACKEND_MAPPING.csv'deki @anvil.server.callable fonksiyonları içerir:

| Modül | Fonksiyonlar | Mock Veri |
|-------|-------------|----------|
| `server_main.py` | health_check, get_system_info, switch_tab | ✅ Aktif |
| `server_market_compass.py` | get_market_regime, get_trend_chart_data | ✅ Aktif |
| `server_leaders_league.py` | get_leaders_list, apply_leaders_filter | ✅ Aktif |
| `server_dna_test.py` | run_dna_test, get_dna_pattern_details | ✅ Aktif |
| `server_simulator.py` | run_strategy_scan, get_optimized_parameters | ✅ Aktif |
| `server_command_center.py` | get_comprehensive_evidence, calculate_overall_confidence | ✅ Aktif |
| `server_discovery_lab.py` | start_rule_optimization, analyze_trend_patterns | ✅ Aktif |
| `server_performance.py` | get_performance_metrics, get_trades_history | ✅ Aktif |
| `server_simulation.py` | start_replay_simulation, get_replay_state | ✅ Aktif |
| `server_admin.py` | get_users_list, get_scheduled_jobs, get_markets_list | ✅ Aktif |

---

## 🎲 Mock Veri Sistemi

### Mock Veriler Neden Kullanılıyor?

Bu proje **MOCK MODE**'da çalışır. Anlamı:

```
✅ Uygulamayı ANINDA test edebilirsiniz
✅ Gerçek backend bağlantısını beklemenize gerek yok
✅ UI/UX tasarımı tamamlayabilirsiniz
✅ Sonra backend'i entegre edebilirsiniz
```

### Mock Data Generator (mock_data_generator.py)

`MockDataGenerator` sınıfı, FORMS_TO_BACKEND_MAPPING.csv'deki her "Şema (Output)"'a uygun veriler üretir:

```python
# Örnek 1: Market Compass Mock Veri
{
    "regime": "LONG_ON",           # string
    "trend_score": 82,             # int (0-100)
    "market_structure": "HH/HL",   # string
    "confidence": 90               # int (0-100)
}

# Örnek 2: Leaders League Mock Veri
{
    "leaders": [
        {
            "rank": 1,
            "symbol": "AAPL",
            "rs_score": 0.85,
            "trend_score": 75,
            "market_structure": "HH/HL",
            "last_price": 175.50,
            "change_percent": 2.3
        },
        # ... more leaders
    ],
    "total_count": 10
}
```

### Caching Sistemi

Performansı artırmak için veriler cache'lenmiştir:

```python
@cached_result("market_regime", ttl_minutes=5)
def get_market_regime():
    # 5 dakika boyunca cache'ten döndürülür
```

---

## ❓ Sık Sorulan Sorular (SSS)

### S1: Neden sahte veriler görüyorum?

**C1:** Bu **mock mode**'da çalışan bir skeleton (iskelet) uygulamadır. Gerçek backend henüz entegre edilmemiştir. Bu normal ve beklenen davranıştır!

### S2: Formlar neden boş/eksik?

**C2:** Bu iskeletonun amacı tam fonksiyonel olmak değil, **yapı sağlamak**'tır. Mocklar form'ların çağışlıp çalıştığını gösterir. Tasarım ve layout'u Anvil Designer'da tamamlayabilirsiniz.

### S3: Backend'i ne zaman entegre edeceğim?

**C3:** Aşağıdaki "Bir Sonraki Adımlar" bölümüne bakın. `UPLINK_BACKEND_INTEGRATION_GUIDE.md` dosyasında detaylı yönergeler bulunur.

### S4: Cache ne kadar süre tutulur?

**C4:** Varsayılan olarak 5 dakika. `cache_manager.py`'de değiştirebilirsiniz:
```python
_global_cache = CacheManager(ttl_minutes=10)  # 10 dakikaya çıkart
```

### S5: Hata ayıklama nasıl yapılır?

**C5:** Anvil'in yerleşik debugger'ı kullanın:
1. Anvil Editor'da kodu satırına breakpoint koyun
2. Test modu başlat
3. Errors panelinde hatalar gösterilecektir

---

## 🔗 Bir Sonraki Adımlar

### Aşama 1: UI Tasarımını Tamamla

**Görev:** MainLayoutForm ve tüm Forms'u Anvil Designer'da düzenle

```
Anvil Editor → Design (tab) → Bileşenleri sürükle-bırak ile düzenle
```

**Referans:** Mokap_ADMIN_v8.html dosyasındaki UI'yi takip et

---

### Aşama 2: Server Modüllerini Tamamla

**Görev:** FORMS_TO_BACKEND_MAPPING.csv'deki tüm functions'ları implement et

Şu şekilde ilerle:
1. FORMS_TO_BACKEND_MAPPING.csv'de satır 2'yi aç (MainLayoutForm)
2. Belirtilen "Callable Functions"'ları kontrol et
3. server_main.py'deki function'lar zaten implement edilmiş mi? ✅
4. Benzer şekilde diğer form'lar için ilerle

---

### Aşama 3: Backend'i Entegre Et

**Dosya:** `UPLINK_BACKEND_INTEGRATION_GUIDE.md` (ayrı olarak sağlanacak)

**Özet:**
```
Mock Mode:
  get_market_regime() → {"regime": "LONG_ON", ...}  # Mock veri

↓ Sonra ↓

Real Backend Mode:
  get_market_regime() → 
    from trader_eidos_suite import calculate_market_regime
    return calculate_market_regime(...)  # Gerçek backend
```

---

### Aşama 4: Test ve Deploy

1. **Unit Test:** `server_code/`'daki tüm functions'ları test et
2. **Integration Test:** Forms' server'a düzgün çağrı yapıyor mu?
3. **UI Test:** Mokap_ADMIN_v8.html'de göründüğü gibi mi?
4. **Deploy:** Anvil'de "Publish" butonuna tıkla

---

## 📞 Destek

Bu iskelet proje hakkında sorularınız varsa:

1. **ANVIL_MODULAR_PROJECT_PLAN.md** - Proje mimarisi
2. **FORMS_TO_BACKEND_MAPPING.csv** - Form → Backend eşlemesi
3. **QUICK_REFERENCE.md** - Hızlı referans rehberi
4. **IMPLEMENTATION_TIMELINE.md** - Geliştirme zaman çizelgesi

---

## 📝 Notlar

- ✅ Mock data sistemi FORMS_TO_BACKEND_MAPPING.csv'ye tamamen uyumlu
- ✅ Tüm server modules @anvil.server.callable dekoratörlü
- ✅ Type hints ve docstring'ler eklenmiş
- ✅ Error handling ve logging implementasyonu tamamlanmış
- ✅ Caching sistemi aktif ve çalışıyor

---

**Proje Hazırdır. Kodlamaya Başlayabilirsiniz! 🚀**

---

**Oluşturulma Tarihi:** 30 Ekim 2025  
**Versiyon:** 8.0.0 (Skeleton Edition)
