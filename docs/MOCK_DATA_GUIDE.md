# 🎲 Mock Data Sistemi Rehberi

Bu dokümanda mock data generator'ın nasıl çalıştığı açıklanmaktadır.

## 📋 İçindekiler
1. [Genel Bakış](#genel-bakış)
2. [MockDataGenerator](#mockdatagenerator)
3. [FORMS_TO_BACKEND_MAPPING Uyumluluğu](#forms-to-backend-mapping-uyumluluğu)
4. [Veri Türleri](#veri-türleri)
5. [Örnekler](#örnekler)
6. [Gelecek: Real Backend](#gelecek-real-backend)

## 🎯 Genel Bakış

MockDataGenerator, FORMS_TO_BACKEND_MAPPING.csv'deki tüm output şemalarına
%100 uyumlu test verisi oluşturur.

**Avantajlar:**
- ✅ Gerçek backend olmadan geliştirme
- ✅ Hızlı prototipleme
- ✅ Tutarlı test verileri
- ✅ Könnü switch to real backend

## 📊 MockDataGenerator

Dosya: `server_code/mock_data_generator.py`

```python
class MockDataGenerator:
    SYMBOLS = ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN", ...]
    
    # 8+ veri üretim methodu
    @staticmethod
    def generate_regime_data() → Dict
    @staticmethod
    def generate_leaders_list() → Dict
    @staticmethod
    def generate_dna_test_results() → Dict
    # ... ve daha fazla
```

## 🔄 FORMS_TO_BACKEND_MAPPING Uyumluluğu

### Örnek 1: Market Compass

```csv
Form,Module,Function,Output Schema
MarketCompassForm,server_market_compass.py,get_market_regime,"{regime, trend_score, market_structure, confidence}"
```

**Generator:**
```python
MockDataGenerator.generate_regime_data() → {
    "regime": "LONG_ON",
    "trend_score": 82,
    "market_structure": "HH/HL",
    "confidence": 90,
    "timestamp": "2025-10-30T12:00:00Z"
}
```

✅ Schema'ya tamamen uyumlu!

## 📝 Veri Türleri

### 1. RegimeData
```python
{
    "regime": "LONG_ON" | "SHORT_ON" | "NEUTRAL",
    "trend_score": int (0-100),
    "market_structure": "HH/HL" | "LH/LL" | "RANGE",
    "confidence": int (0-100),
    "timestamp": str (ISO8601)
}
```

### 2. LeadersData
```python
{
    "leaders": [
        {
            "rank": int,
            "symbol": str,
            "rs_score": float,
            "trend_score": int,
            "market_structure": str,
            "last_price": float,
            "change_percent": float
        }
    ],
    "total_count": int
}
```

### 3. DnaTestResults
```python
{
    "results": [
        {
            "symbol": str,
            "dna_score": int (0-100),
            "status": "PASS" | "FAIL",
            "confidence": int,
            "last_pattern_match": str (ISO8601),
            "pattern_name": str
        }
    ],
    "pass_count": int,
    "total_count": int,
    "average_score": float
}
```

## 💡 Örnekler

### Örnek 1: Market Regime Al

```python
# server_market_compass.py
@anvil.server.callable
@handle_anvil_errors
@cached_result("market_regime", ttl_minutes=5)
def get_market_regime(symbol: str = "SPY") → Dict:
    regime_data = MockDataGenerator.generate_regime_data()
    return regime_data
```

**Çıktı:**
```json
{
    "regime": "LONG_ON",
    "trend_score": 82,
    "market_structure": "HH/HL",
    "confidence": 90,
    "timestamp": "2025-10-30T12:00:00Z"
}
```

### Örnek 2: Liderler Listesi Al

```python
# server_leaders_league.py
@anvil.server.callable
@handle_anvil_errors
@cached_result("leaders_list", ttl_minutes=5)
def get_leaders_list(limit: int = 20) → Dict:
    return MockDataGenerator.generate_leaders_list(min(limit, 20))
```

**Çıktı:**
```json
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
        ...
    ],
    "total_count": 10
}
```

## 🔀 Gelecek: Real Backend

### Mock → Real Transformation

```python
# MOCK (Current)
@anvil.server.callable
def get_market_regime():
    return MockDataGenerator.generate_regime_data()

# REAL (Future - with trader_eidos_suite)
@anvil.server.callable
def get_market_regime():
    from trader_eidos_suite.indicators import calculate_market_regime
    return calculate_market_regime(symbol="SPY")
```

### Integration Adımları
1. trader_eidos_suite'i yükle
2. Anvil Uplink'i kur
3. Mock çağrıları gerçek functions'larla değiştir
4. Test et
5. Deploy et

---

*Last Updated: 30 Ekim 2025*
