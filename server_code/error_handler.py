"""
error_handler.py - Hata Yönetimi ve Logging
Version: 8.0.0
"""

import logging
from typing import Callable, Any, Dict
from functools import wraps
from datetime import datetime

# Logger ayarları
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class AnvilError(Exception):
    """Anvil-specific hata"""
    def __init__(self, code: str, message: str, details: Dict[str, Any] = None):
        self.code = code
        self.message = message
        self.details = details or {}
        super().__init__(self.message)


class ValidationError(AnvilError):
    """Veri doğrulama hatası"""
    def __init__(self, message: str, details: Dict[str, Any] = None):
        super().__init__("VALIDATION_ERROR", message, details)


class DataNotFoundError(AnvilError):
    """Veri bulunamadı hatası"""
    def __init__(self, message: str, details: Dict[str, Any] = None):
        super().__init__("DATA_NOT_FOUND", message, details)


class BackendError(AnvilError):
    """Backend bağlantı hatası"""
    def __init__(self, message: str, details: Dict[str, Any] = None):
        super().__init__("BACKEND_ERROR", message, details)


def handle_anvil_errors(func: Callable) -> Callable:
    """
    Decorator: Anvil @server.callable fonksiyonları için hata yönetimi
    
    Tüm hataları yakalar ve standardize edilmiş yanıt döndürür.
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Dict[str, Any]:
        try:
            result = func(*args, **kwargs)
            logger.info(f"✓ {func.__name__} başarıyla çalıştı")
            return {
                "status": "success",
                "data": result,
                "timestamp": datetime.now().isoformat()
            }
        except AnvilError as e:
            logger.error(f"[{e.code}] {e.message}", extra=e.details)
            return {
                "status": "error",
                "code": e.code,
                "message": e.message,
                "details": e.details,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"✗ Beklenmeyen hata {func.__name__}: {str(e)}")
            return {
                "status": "error",
                "code": "INTERNAL_ERROR",
                "message": "Beklenmeyen bir hata oluştu",
                "details": {"error": str(e)},
                "timestamp": datetime.now().isoformat()
            }
    
    return wrapper


def safe_call(func: Callable, *args, **kwargs) -> Any:
    """İşlev güvenli çağırma (try-except wrapper)"""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        logger.error(f"Error in {func.__name__}: {str(e)}")
        raise AnvilError("OPERATION_FAILED", str(e))


def log_function_call(func: Callable) -> Callable:
    """Decorator: Fonksiyon çağrılarını logla"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"→ Çağırıldı: {func.__name__} args={args} kwargs={kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"← Tamamlandı: {func.__name__}")
            return result
        except Exception as e:
            logger.error(f"✗ Hata: {func.__name__} - {str(e)}")
            raise
    return wrapper
