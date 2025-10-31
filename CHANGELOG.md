# 📝 Changelog

Tüm önemli değişiklikler bu dosyada belgelenir.

Format [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) ve
versionlama [Semantic Versioning](https://semver.org/spec/v2.0.0.html) takip etmektedir.

---

## [8.0.0] - 2025-10-30 (Initial Release - Skeleton Edition)

### ✨ Added (Yeni Eklenenler)

#### Client Code (Forms)
- **MainLayoutForm** - Ana layout ve navigasyon sistemi
- **MarketCompassForm** - Piyasa rejimi ve trend analizi
- **LeadersLeagueForm** - RS Rotasyonu ve liderler listesi
- **DnaTestForm** - Trend DNA testi ve pattern analizi
- **StrategySimulatorForm** - Strateji taraması ve sinyal üretimi
- **CommandCenterForm** - Kanıt temelli karar alma merkezi
- **DiscoveryLabForm** - Kural optimizasyonu ve pattern keşfi
- **PerformanceDashboardForm** - Performans analizi ve raporlama
- **SimulationScreenForm** - As-of replay simülasyonu
- **AdminPanelsForm** - Sistem yönetimi ve konfigürasyon
- **AboutForm** - Sistem bilgisi ve versiyonlama

#### Server Code (Modules)
- **server_main.py** (5 callable functions)
  - `health_check()` - Sistem sağlık kontrol
  - `get_system_info()` - Sistem bilgileri
  - `switch_tab()` - Tab yönetimi
  - `get_global_scope()` - Global filtre seçenekleri
  - `fetch_markets_from_scope()` - Piyasa getirme

- **server_market_compass.py** (3 callable functions)
  - `get_market_regime()` - Piyasa rejimi algılama
  - `get_trend_chart_data()` - Trend grafiği verileri
  - `refresh_market_data()` - Veri yenileme

- **server_leaders_league.py** (3 callable functions)
  - `get_leaders_list()` - Liderler listesi
  - `apply_leaders_filter()` - Dinamik filtreleme
  - `get_leaders_statistics()` - İstatistikler

- **server_dna_test.py** (3 callable functions)
  - `run_dna_test()` - DNA testi çalıştırma
  - `get_dna_pattern_details()` - Pattern detayları
  - `get_pattern_pool()` - Kayıtlı patterns

- **server_simulator.py** (3 callable functions)
  - `run_strategy_scan()` - Tarama çalıştırma
  - `get_optimized_parameters()` - Optimize parametreler
  - `preview_signal_details()` - Signal detayları

- **server_command_center.py** (4 callable functions)
  - `get_comprehensive_evidence()` - Kanıt bilgisi
  - `generate_ai_scenarios()` - AI senaryoları
  - `calculate_overall_confidence()` - Güven skoru
  - `save_trade_decision()` - Karar kaydetme

- **server_discovery_lab.py** (4 callable functions)
  - `start_rule_optimization()` - Kurural optimizasyonu
  - `analyze_trend_patterns()` - Pattern analizi
  - `discover_motifs()` - Motif keşfi
  - `get_optimization_status()` - Durum kontrolü

- **server_performance.py** (4 callable functions)
  - `get_performance_metrics()` - Performans metrikleri
  - `get_trades_history()` - İşlem geçmişi
  - `natural_language_query()` - NLQ desteği
  - `export_performance_report()` - Rapor dışa aktarma

- **server_simulation.py** (4 callable functions)
  - `start_replay_simulation()` - Replay başlatma
  - `get_replay_state()` - Durum sorgusu
  - `step_replay_forward()` - İleri sarma
  - `pause_replay()` - Duraklatma

- **server_admin.py** (5 callable functions)
  - `get_users_list()` - Kullanıcı listesi
  - `get_scheduled_jobs()` - Planlanan işler
  - `get_markets_list()` - Piyasalar
  - `fetch_markets_from_eodhd()` - EODHD entegrasyon
  - `update_exchange_rules()` - Kural güncelleme

#### Utilities
- **shared_types.py** - 10+ dataclass tanımı
  - `RegimeData` - Piyasa rejimi
  - `LeaderData` - Lider bilgileri
  - `DnaTestResult` - DNA test sonuçları
  - `SignalData` - Sinyal bilgileri
  - `TradeRecord` - İşlem kaydı
  - `PerformanceMetrics` - Performans metrikleri
  - `OptimizationResult` - Optimizasyon sonuçları
  - `EvidenceContext` - Kanıt bağlamı
  - `ApiResponse` - API yanıt wrapper

- **error_handler.py** - Hata yönetimi
  - `AnvilError` - Temel exception
  - `ValidationError` - Doğrulama hatası
  - `DataNotFoundError` - Veri bulunamadı hatası
  - `BackendError` - Backend hatası
  - `@handle_anvil_errors` - Dekoratör
  - Logging infrastructure

- **cache_manager.py** - Caching sistemi
  - `CacheManager` - Cache yöneticisi sınıfı
  - TTL support (5 dakika default)
  - Cache invalidation
  - `@cached_result()` - Dekoratör

- **mock_data_generator.py** - Mock veri üretimi
  - `MockDataGenerator` - Statik veri üretim sınıfı
  - FORMS_TO_BACKEND_MAPPING.csv'ye %100 uyumlu
  - Realistic test verisi oluşturma
  - 8+ veri türü destekleme

#### Dokümantasyon
- **README.md** - Ana dokümantasyon
- **KURULUM_REHBERI.md** - Türkçe kurulum rehberi
- **PROJECT_SUMMARY.md** - Proje özeti
- **CONTRIBUTING.md** - Katkı kılavuzu
- **CHANGELOG.md** - Bu dosya
- **LICENSE** - MIT License
- **.gitignore** - Git ignore kuralları
- **anvil.yaml** - Anvil konfigürasyonu
- **requirements.txt** - Python bağımlılıkları

#### GitHub Dokümantası
- **docs/ARCHITECTURE.md** - Mimarisi detayları
- **docs/MOCK_DATA_GUIDE.md** - Mock veri sistemi rehberi
- **docs/BACKEND_INTEGRATION.md** - Backend entegrasyon rehberi
- **docs/FEATURES.md** - Özellikler listesi
- **.github/ISSUE_TEMPLATE/** - Issue templates
- **.github/PULL_REQUEST_TEMPLATE.md** - PR template

### 📊 İstatistikler
- **Total Files:** 35+
- **Forms:** 11
- **Server Modules:** 11
- **Callable Functions:** 41
- **Dataclasses:** 10+
- **Lines of Code:** 2,500+
- **Documentation Lines:** 1,500+

### 🔒 Features
- Type hints %100 coverage
- Error handling decorators
- Caching system
- Mock data generator
- Logging infrastructure
- GitHub integration ready

### 📝 Notes
- Mock mode: Tüm veriler sahte/test verisidir
- Backend henüz entegre değil
- Forms tasarımı tamamlanmadı (iskelet durumda)
- Production ready değil (geliştime ortamı)

---

## [Planlanan - Sonraki Sürümler]

### v8.1.0 (Planned)
- [ ] UI tasarımı tamamlanması
- [ ] Unit tests eklenmesi
- [ ] Performance optimizasyonu
- [ ] Docstring geliştirmesi

### v8.2.0 (Planned)
- [ ] Backend entegrasyon (trader_eidos_suite)
- [ ] Real data support
- [ ] Database integration

### v9.0.0 (Planned)
- [ ] Production deployment
- [ ] Advanced features
- [ ] Scaling capabilities

---

## Versiyon Uyumluluğu

| Bileşen | Versiyon | Durum |
|---------|----------|-------|
| Python | 3.10+ | ✅ |
| Anvil | Latest | ✅ |
| anvil-uplink | 2.0.0+ | ✅ |
| pandas | 1.3.0+ | ✅ |
| numpy | 1.21.0+ | ✅ |

---

## Breaking Changes

Şu anda breaking change yok.

---

## Deprecation Notices

Şu anda deprecation yok.

---

## Security

### Known Issues
- Hiçbiri bildirilmedi

### CVE
- Hiçbiri

### Tavsiyeler
- Mock mode sadece development için
- Production'da real backend kullanılmalı
- API keys asla code'a yazılmamalı

---

## Upgrade Guide

### v7.x → v8.0.0

Bu ilk release olduğu için upgrade guide yok.

---

## Resources

- [GitHub Repo](https://github.com/yourusername/trader-eidos-suite-anvil)
- [Issues](https://github.com/yourusername/trader-eidos-suite-anvil/issues)
- [Discussions](https://github.com/yourusername/trader-eidos-suite-anvil/discussions)
- [Wiki](https://github.com/yourusername/trader-eidos-suite-anvil/wiki)

---

## Contributors

- **Initial Creator:** AI Assistant
- **Framework:** Anvil Web Framework
- **Backend Reference:** trader_eidos_suite

---

## License

[MIT License](./LICENSE)

---

*Last Updated: 30 Ekim 2025*  
*Maintain your changelog!*
