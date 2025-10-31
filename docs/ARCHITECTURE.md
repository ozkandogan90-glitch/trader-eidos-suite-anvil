# 🏗️ Sistem Mimarisi

Bu dokümanda, Trader Eidos Suite - Anvil Skeleton projesinin teknik mimarisi açıklanmaktadır.

---

## 📐 Genel Mimarisi

```
┌─────────────────────────────────────────────────────────────────┐
│                      CLIENT LAYER                               │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  Anvil Web Framework (Python)                             │ │
│  │  ┌──────────────────────────────────────────────────────┐ │ │
│  │  │  MainLayoutForm (Navigation + Header)               │ │ │
│  │  │  ├─ MarketCompassForm                               │ │ │
│  │  │  ├─ LeadersLeagueForm                               │ │ │
│  │  │  ├─ DnaTestForm                                     │ │ │
│  │  │  ├─ StrategySimulatorForm                           │ │ │
│  │  │  ├─ CommandCenterForm                               │ │ │
│  │  │  ├─ DiscoveryLabForm                                │ │ │
│  │  │  ├─ PerformanceDashboardForm                        │ │ │
│  │  │  ├─ SimulationScreenForm                            │ │ │
│  │  │  ├─ AdminPanelsForm                                 │ │ │
│  │  │  └─ AboutForm                                       │ │ │
│  │  └──────────────────────────────────────────────────────┘ │ │
│  └────────────────────────────────────────────────────────────┘ │
└────────────────────┬────────────────────────────────────────────┘
                     │ anvil.server.call()
                     │ (RPC over HTTP/WebSocket)
                     ↓
┌─────────────────────────────────────────────────────────────────┐
│                    SERVER LAYER                                 │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  @anvil.server.callable Decorators                        │ │
│  │  ┌──────────────────────────────────────────────────────┐ │ │
│  │  │  Module Layer (11 modules, 41 functions)           │ │ │
│  │  │  ├─ server_main.py (5)                             │ │ │
│  │  │  ├─ server_market_compass.py (3)                   │ │ │
│  │  │  ├─ server_leaders_league.py (3)                   │ │ │
│  │  │  ├─ server_dna_test.py (3)                         │ │ │
│  │  │  ├─ server_simulator.py (3)                        │ │ │
│  │  │  ├─ server_command_center.py (4)                   │ │ │
│  │  │  ├─ server_discovery_lab.py (4)                    │ │ │
│  │  │  ├─ server_performance.py (4)                      │ │ │
│  │  │  ├─ server_simulation.py (4)                       │ │ │
│  │  │  └─ server_admin.py (5)                            │ │ │
│  │  └──────────────────────────────────────────────────────┘ │ │
│  │  ┌──────────────────────────────────────────────────────┐ │ │
│  │  │  Utility Layer                                       │ │ │
│  │  │  ├─ mock_data_generator.py (MockDataGenerator)      │ │ │
│  │  │  ├─ cache_manager.py (CacheManager + @cached)       │ │ │
│  │  │  ├─ error_handler.py (@handle_anvil_errors)         │ │ │
│  │  │  └─ shared_types.py (10+ dataclasses)              │ │ │
│  │  └──────────────────────────────────────────────────────┘ │ │
│  └────────────────────────────────────────────────────────────┘ │
└────────────────────┬────────────────────────────────────────────┘
                     │ Gelecek: Anvil Uplink
                     ↓
┌─────────────────────────────────────────────────────────────────┐
│                  BACKEND LAYER (Future)                         │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  trader_eidos_suite (Python Backend)                      │ │
│  │  ├─ indicators/ (Technical Analysis)                      │ │
│  │  ├─ signals/ (Signal Generation)                          │ │
│  │  ├─ backtest/ (Backtesting Engine)                        │ │
│  │  ├─ risk_management/ (Risk Controls)                      │ │
│  │  ├─ data/ (Data Management)                               │ │
│  │  └─ reporting/ (Report Generation)                        │ │
│  └────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Data Flow

### 1. Form Başlama
```
User açar MainLayoutForm
    ↓
MainLayoutForm.__init__()
    ↓
load_initial_data()
    ├─ anvil.server.call('health_check')
    ├─ anvil.server.call('get_global_scope')
    └─ load_form('dashboard')
    ↓
Tab navigasyonu görüntülenir ✅
```

### 2. Tab Değiştirme
```
User "Leaders" tab'ına tıklar
    ↓
leaders_button_click()
    ↓
load_form('leaders')
    ├─ anvil.server.call('switch_tab', 'leaders')
    └─ content_container.clear() + LeadersLeagueForm yükle
    ↓
LeadersLeagueForm.__init__()
    ↓
load_data()
    ├─ anvil.server.call('get_leaders_list')
    ├─ Mock veriler server_leaders_league.py'den döner
    └─ Form UI güncellenir ✅
```

### 3. Mock Veri Akışı
```
Client: anvil.server.call('get_leaders_list')
    ↓
Server: @anvil.server.callable
def get_leaders_list() → Dict
    ↓
Cache kontrolü: _global_cache.get("leaders_list")
    ├─ HIT (cache geçerli)
    │  └─ Cached value döndür
    └─ MISS (cache dolu veya yok)
       ├─ MockDataGenerator.generate_leaders_list()
       ├─ Sonuç cache'e ekle
       └─ Sonuç döndür
    ↓
Client: UI güncelle ✅
```

---

## 🔐 Type System

### Dataclasses (shared_types.py)

```python
@dataclass
class RegimeData:
    regime: Literal["LONG_ON", "SHORT_ON", "NEUTRAL"]
    trend_score: int  # 0-100
    market_structure: Literal["HH/HL", "LH/LL", "RANGE"]
    confidence: int  # 0-100
    timestamp: str  # ISO8601

@dataclass
class SignalData:
    symbol: str
    direction: Literal["LONG", "SHORT"]
    entry_price: float
    stop_loss: float
    take_profit: float
    confidence: int
    regime_at_entry: Literal["LONG_ON", "SHORT_ON", "NEUTRAL"]
    trend_score_at_entry: int
    win_probability: float
    signal_id: str

# ... ve 8+ daha
```

### Type Hints Patterns

```python
# ❌ Yanlış
def get_data(symbol):
    return data

# ✅ Doğru
def get_data(symbol: str) -> Dict[str, Any]:
    """Get data for symbol."""
    return data

# ✅ Complex types
def run_scan(
    symbols: List[str],
    params: Optional[Dict[str, Any]] = None,
    limit: int = 10
) -> Dict[str, List[Dict[str, Any]]]:
    """Run strategy scan."""
    return {"signals": [...]}
```

---

## 🎯 Mock Data System

### MockDataGenerator Sınıfı

```python
class MockDataGenerator:
    """Tüm test verileri FORMS_TO_BACKEND_MAPPING.csv'ye uyumlu"""
    
    @staticmethod
    def generate_regime_data() → Dict[str, Any]:
        """Output schema: {regime, trend_score, market_structure, confidence}"""
        
    @staticmethod
    def generate_leaders_list(count: int) → Dict[str, Any]:
        """Output schema: {leaders: List, total_count: int}"""
        
    @staticmethod
    def generate_dna_test_results(symbols: List[str]) → Dict[str, Any]:
        """Output schema: {results, pass_count, total_count, average_score}"""
        
    # ... ve 5+ daha
```

### Veri Uyumluluğu

```csv
Form,Server Module,Callable Function,Output Schema
MarketCompassForm,server_market_compass.py,get_market_regime,"{regime, trend_score, market_structure, confidence}"
LeadersLeagueForm,server_leaders_league.py,get_leaders_list,"{leaders: List, total_count: int}"
DnaTestForm,server_dna_test.py,run_dna_test,"{results: List, pass_count, total_count, average_score}"
# ... tüm output'lar MockDataGenerator tarafından üretilir ✅
```

---

## ⚡ Caching Architecture

### TTL-Based Cache

```python
class CacheManager:
    def __init__(self, ttl_minutes: int = 5):
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.ttl = timedelta(minutes=ttl_minutes)
    
    def get(self, key: str) -> Optional[Any]:
        """Geçerli cache'i al"""
        if key in self.cache:
            age = datetime.now() - cached["timestamp"]
            if age < self.ttl:
                return cached["value"]  # ✅ Hit
            else:
                del self.cache[key]  # TTL expired
        return None  # Miss
    
    def set(self, key: str, value: Any):
        """Cache'e ekle"""
        self.cache[key] = {
            "value": value,
            "timestamp": datetime.now()
        }
```

### Decorator Pattern

```python
@cached_result("market_regime", ttl_minutes=5)
def get_market_regime():
    # İlk çağrı: veri üret ve cache'e koy
    # 2-5 dakika içindeki çağrılar: cache'den dön
    # 5+ dakika sonra: yeniden üret ve cache'i güncelle
    return MockDataGenerator.generate_regime_data()
```

### Cache Keys
- `market_regime` - Piyasa rejimi (5 min)
- `trend_chart_data` - Grafik verileri (5 min)
- `leaders_list` - Liderler listesi (5 min)
- `global_scope` - Global filtre seçenekleri (60 min)
- `system_info` - Sistem bilgileri (10 min)

---

## 🛡️ Error Handling

### Exception Hierarchy

```python
Exception
└── AnvilError (Custom)
    ├── ValidationError
    ├── DataNotFoundError
    ├── BackendError
    └── (Custom exceptions)
```

### Decorator Pattern

```python
@handle_anvil_errors
def my_function():
    try:
        # İşlem yap
        return result
    except AnvilError as e:
        # Knowns errors - detailed logging
        logger.error(f"[{e.code}] {e.message}")
        return {
            "status": "error",
            "code": e.code,
            "message": e.message
        }
    except Exception as e:
        # Unknown errors
        logger.error(f"Unexpected error: {str(e)}")
        return {
            "status": "error",
            "code": "INTERNAL_ERROR",
            "message": "Beklenmeyen bir hata oluştu"
        }
```

### Response Format

```python
# Success
{
    "status": "success",
    "data": {...},
    "timestamp": "2025-10-30T12:00:00Z"
}

# Error
{
    "status": "error",
    "code": "VALIDATION_ERROR",
    "message": "Veri doğrulama hatası",
    "details": {...},
    "timestamp": "2025-10-30T12:00:00Z"
}
```

---

## 📋 Module Structure

### server_main.py
```
health_check() → System status
get_system_info() → Detailed system info
switch_tab(tab_name) → Tab management
get_global_scope() → Filter options
fetch_markets_from_scope() → Get markets
```

### server_market_compass.py
```
get_market_regime() → Regime detection
get_trend_chart_data() → Chart data
refresh_market_data() → Data refresh
```

### server_leaders_league.py
```
get_leaders_list() → Get top performers
apply_leaders_filter() → Dynamic filtering
get_leaders_statistics() → Statistics
```

### ... (8 more modules)

---

## 🔄 Integration Points

### Current State (Mock Mode)
```
Client → Server Modules → Mock Data Generator
                            ↓
                        Test/Development
```

### Future State (Real Backend)
```
Client → Server Modules → trader_eidos_suite
                            ├─ indicators
                            ├─ signals
                            ├─ backtest
                            └─ risk_management
                            ↓
                        Production
```

### Integration Method: Anvil Uplink

```python
# Mock (Current)
def get_market_regime():
    return MockDataGenerator.generate_regime_data()

# Real (Future)
def get_market_regime():
    from trader_eidos_suite.indicators import calculate_regime
    return calculate_regime(...)
```

---

## 📈 Performance Considerations

### Optimization Strategies
1. **Caching** - TTL-based with configurable timeouts
2. **Lazy Loading** - Forms load on demand
3. **Mock Data** - Fast generation for testing
4. **Batch Operations** - Multiple symbols in single call
5. **Async Ready** - Future websocket support

### Bottlenecks
- Mock data generation (negligible)
- Cache lookup O(1)
- Network latency (Anvil framework)
- Browser rendering

### Improvements (Future)
- Implement pagination for large datasets
- Add batch processing endpoints
- Optimize dataclass serialization
- Consider Redis for distributed caching

---

## 🧪 Testing Strategy

### Unit Testing
```python
def test_get_market_regime():
    result = get_market_regime()
    assert "regime" in result
    assert result["regime"] in ["LONG_ON", "SHORT_ON", "NEUTRAL"]
    assert 0 <= result["trend_score"] <= 100
```

### Integration Testing
```python
def test_form_to_server_communication():
    # Anvil form calls server function
    # Mock data returned
    # UI updated correctly
```

### Type Checking
```bash
mypy server_code/
# Should pass with no errors
```

---

## 📊 Scalability

### Current Limitations
- Single process (Anvil limitation)
- In-memory caching only
- No database persistence
- No authentication system

### Scalability Path
```
v8.0.0 (Current) → Mock, Single Anvil App
        ↓
v8.2.0 (Backend) → Real data, Single Anvil App
        ↓
v9.0.0 (Enterprise) → Multi-instance, Distributed caching
```

---

## 🔐 Security Considerations

### Current
- No authentication (open app)
- No input validation (mock mode)
- Mock data only

### Future
- Implement Anvil Auth
- Add input validation
- Use environment variables for keys
- Implement rate limiting
- Add API key management

---

## 📚 References

- [Anvil Documentation](https://anvil.works)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [Clean Code](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

---

*Last Updated: 30 Ekim 2025*  
*Version: 8.0.0*
