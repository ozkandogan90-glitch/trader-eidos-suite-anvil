"""
server_admin.py - Admin Panels (Yönetim Paneli)
Version: 8.0.0
"""

import anvil.server
from error_handler import handle_anvil_errors


@anvil.server.callable
@handle_anvil_errors
def get_users_list() -> dict:
    """Kullanıcı listesini al"""
    return {
        "users": [
            {"id": 1, "name": "Admin User", "role": "admin", "status": "active"},
            {"id": 2, "name": "Trader User", "role": "trader", "status": "active"},
        ],
        "total_count": 2
    }


@anvil.server.callable
@handle_anvil_errors
def get_scheduled_jobs() -> dict:
    """Planlanan işleri al"""
    return {
        "jobs": [
            {"id": "JOB_001", "name": "Daily Market Scan", "next_run": "2025-10-31 09:30:00"},
            {"id": "JOB_002", "name": "Weekly Report", "next_run": "2025-11-01 18:00:00"},
        ],
        "total_count": 2
    }


@anvil.server.callable
@handle_anvil_errors
def get_markets_list() -> dict:
    """Piyasalar listesini al"""
    return {
        "markets": [
            {"code": "NYSE", "name": "New York Stock Exchange", "status": "open"},
            {"code": "NASDAQ", "name": "NASDAQ", "status": "open"},
            {"code": "LSE", "name": "London Stock Exchange", "status": "closed"},
        ],
        "total_count": 3
    }


@anvil.server.callable
@handle_anvil_errors
def fetch_markets_from_eodhd(action: str, params: dict = None) -> dict:
    """EODHD API'den piyasaları getir (mock)"""
    return {
        "status": "ok",
        "message": "EODHD'den piyasa verisi simüle ediliyor",
        "mode": "MOCK_MODE",
        "data": {
            "markets_fetched": 150,
            "last_update": "2025-10-30T12:00:00Z"
        }
    }


@anvil.server.callable
@handle_anvil_errors
def update_exchange_rules(exchange_code: str, rules: dict) -> dict:
    """Borsa kurallarını güncelle"""
    return {
        "status": "ok",
        "exchange": exchange_code,
        "rules_updated": len(rules),
        "message": "Borsa kuralları güncellendi"
    }
