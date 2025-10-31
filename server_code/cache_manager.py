"""
cache_manager.py - Caching Yönetimi
Version: 8.0.0
Purpose: Mock veri performansını optimize etme
"""

from functools import wraps
from datetime import datetime, timedelta
from typing import Any, Optional, Callable, Dict
import hashlib
import json


class CacheManager:
    """Cache yöneticisi - Hafıza içinde saklama"""
    
    def __init__(self, ttl_minutes: int = 5):
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.ttl = timedelta(minutes=ttl_minutes)
    
    def _generate_key(self, prefix: str, *args, **kwargs) -> str:
        """Cache anahtarı oluştur"""
        cache_input = f"{prefix}:{str(args)}:{str(kwargs)}"
        return hashlib.md5(cache_input.encode()).hexdigest()
    
    def get(self, key: str) -> Optional[Any]:
        """Cacheden veri al"""
        if key not in self.cache:
            return None
        
        cached = self.cache[key]
        age = datetime.now() - cached["timestamp"]
        
        if age < self.ttl:
            return cached["value"]
        else:
            # Cache süresi doldu
            del self.cache[key]
            return None
    
    def set(self, key: str, value: Any) -> None:
        """Cache'e veri ekle"""
        self.cache[key] = {
            "value": value,
            "timestamp": datetime.now()
        }
    
    def clear(self) -> None:
        """Cache'i temizle"""
        self.cache.clear()
    
    def get_stats(self) -> Dict[str, Any]:
        """Cache istatistikleri"""
        return {
            "total_keys": len(self.cache),
            "ttl_minutes": self.ttl.total_seconds() / 60,
            "keys": list(self.cache.keys())
        }


# Singleton cache instance
_global_cache = CacheManager(ttl_minutes=5)


def cached_result(prefix: str, ttl_minutes: int = 5):
    """
    Decorator: Fonksiyon sonucunu cache'e koy
    
    Örnek:
        @cached_result("market_regime", ttl_minutes=10)
        def get_market_regime():
            return expensive_operation()
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # Cache anahtarı oluştur
            cache_key = _global_cache._generate_key(prefix, *args, **kwargs)
            
            # Cacheden kontrol et
            cached_value = _global_cache.get(cache_key)
            if cached_value is not None:
                return cached_value
            
            # Cache miss - fonksiyonu çalıştır
            result = func(*args, **kwargs)
            
            # Sonucu cache'e koy
            _global_cache.set(cache_key, result)
            
            return result
        
        return wrapper
    return decorator


def clear_cache_prefix(prefix: str) -> None:
    """Belirli prefix'teki cache'i temizle"""
    keys_to_delete = [k for k in _global_cache.cache.keys() if k.startswith(prefix)]
    for key in keys_to_delete:
        del _global_cache.cache[key]


def get_cache_stats() -> Dict[str, Any]:
    """Cache istatistiklerini al"""
    return _global_cache.get_stats()
