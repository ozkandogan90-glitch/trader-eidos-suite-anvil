# 🔌 Backend Entegrasyon Rehberi

Mock mode'dan gerçek backend'e geçiş rehberi.

## 📋 Adımlar

### 1. Anvil Uplink Kur
```bash
pip install anvil-uplink
```

### 2. Server Credentials Oluştur
Anvil Dashboard → Server Configuration → Create Server Link
- Credentials URL'sini kopyala

### 3. Mock Çağrıları Değiştir
```python
# MOCK (Current)
from mock_data_generator import MockDataGenerator

def get_market_regime():
    return MockDataGenerator.generate_regime_data()

# REAL (Future)
import uplink
from trader_eidos_suite import calculate_market_regime

def get_market_regime():
    return calculate_market_regime(symbol="SPY")
```

### 4. Test Et
```bash
pytest tests/
```

### 5. Deploy Et
```
Anvil → Publish
```

---

*For detailed instructions, see KURULUM_REHBERI.md*
