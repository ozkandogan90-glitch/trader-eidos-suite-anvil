"""
server_main.py - Ana Server Modülü
Version: 8.0.0
Purpose: Sistem bilgisi, health check, tab yönetimi

Callable Functions:
- health_check() -> {status: ok, ...}
- get_system_info() -> {status: ok, version: str, ...}
- switch_tab(tab_name: str) -> {status: ok}
- get_global_scope() -> {countries: [...], exchanges: [...]}
"""

import anvil.server
from error_handler import handle_anvil_errors
from mock_data_generator import MockDataGenerator
from cache_manager import cached_result
from datetime import datetime


# ============================================================================
# HEALTH CHECK & SYSTEM INFO
# ============================================================================

@anvil.server.callable
@handle_anvil_errors
def health_check() -> dict:
    """Sistem sağlık kontrol"""
    return {
        "status": "ok",
        "version": "8.0.0",
        "timestamp": datetime.now().isoformat(),
        "components": {
            "server": "ready",
            "database": "connected",
            "cache": "active"
        }
    }


@anvil.server.callable
@handle_anvil_errors
@cached_result("system_info", ttl_minutes=10)
def get_system_info() -> dict:
    """Sistem bilgilerini al"""
    return MockDataGenerator.generate_system_info()


# ============================================================================
# TAB MANAGEMENT
# ============================================================================

@anvil.server.callable
@handle_anvil_errors
def switch_tab(tab_name: str) -> dict:
    """Tab değiştirme işlemini logla"""
    valid_tabs = [
        "dashboard", "rfs", "leaders", "dna", "simulator",
        "command", "lab", "report", "replay", "admin", "about"
    ]
    
    if tab_name not in valid_tabs:
        return {
            "status": "error",
            "message": f"Geçersiz tab: {tab_name}",
            "valid_tabs": valid_tabs
        }
    
    return {
        "status": "ok",
        "current_tab": tab_name,
        "timestamp": datetime.now().isoformat()
    }


# ============================================================================
# GLOBAL SCOPE FILTER
# ============================================================================

@anvil.server.callable
@handle_anvil_errors
@cached_result("global_scope", ttl_minutes=60)
def get_global_scope() -> dict:
    """Global scope filter seçenekleri"""
    return {
        "countries": [
            {"code": "US", "name": "United States"},
            {"code": "TR", "name": "Türkiye"},
            {"code": "GB", "name": "United Kingdom"},
            {"code": "DE", "name": "Germany"},
            {"code": "JP", "name": "Japan"}
        ],
        "exchanges": [
            {"code": "NYSE", "name": "New York Stock Exchange"},
            {"code": "NASDAQ", "name": "NASDAQ"},
            {"code": "LSE", "name": "London Stock Exchange"},
            {"code": "BORSA", "name": "Borsa İstanbul"}
        ],
        "default_country": "US",
        "default_exchange": "NYSE"
    }


@anvil.server.callable
@handle_anvil_errors
def fetch_markets_from_scope(country_code: str, exchange_code: str) -> dict:
    """Verilen scope'a göre piyasaları getir"""
    mock_markets = {
        "markets": [
            {"symbol": "AAPL", "name": "Apple Inc."},
            {"symbol": "GOOGL", "name": "Alphabet Inc."},
            {"symbol": "MSFT", "name": "Microsoft Corporation"},
            {"symbol": "TSLA", "name": "Tesla Inc."},
            {"symbol": "AMZN", "name": "Amazon.com Inc."},
        ],
        "country": country_code,
        "exchange": exchange_code,
        "timestamp": datetime.now().isoformat()
    }
    return mock_markets


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

@anvil.server.callable
@handle_anvil_errors
def test_backend_connection() -> dict:
    """Backend bağlantısını test et"""
    # Mock mode'da her zaman başarılı
    return {
        "backend_status": "connected",
        "mode": "MOCK_MODE",
        "message": "Mock veriler kullanılmaktadır. Gerçek backend'e henüz bağlanılmamıştır.",
        "timestamp": datetime.now().isoformat()
    }


@anvil.server.callable
@handle_anvil_errors
def get_app_version() -> dict:
    """Uygulama versiyonunu al"""
    return {
        "version": "8.0.0",
        "build_date": "2025-10-30",
        "status": "skeleton",
        "message": "Bu proje iskeleton (skeleton) sürümüdür. Mock veriler kullanılmaktadır."
    }
