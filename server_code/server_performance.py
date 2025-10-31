"""
server_performance.py - Performance Dashboard (Performans Panosu)
Version: 8.0.0
"""

import anvil.server
from error_handler import handle_anvil_errors
from mock_data_generator import MockDataGenerator


@anvil.server.callable
@handle_anvil_errors
def get_performance_metrics(date_range: tuple = None, filters: dict = None) -> dict:
    """Performans metriklerini al"""
    metrics = MockDataGenerator.generate_performance_metrics()
    metrics["date_range"] = date_range or ("2025-01-01", "2025-10-30")
    metrics["filters"] = filters or {}
    return metrics


@anvil.server.callable
@handle_anvil_errors
def get_trades_history(limit: int = 20, filters: dict = None) -> dict:
    """İşlem geçmişini al"""
    trades = MockDataGenerator.generate_trades_history(limit)
    
    return {
        "trades": trades,
        "total_count": len(trades),
        "filters": filters or {}
    }


@anvil.server.callable
@handle_anvil_errors
def natural_language_query(query: str) -> dict:
    """Doğal dil sorgusu - NLQ"""
    mock_responses = {
        "win rate": "Win rate %52.5 olarak hesaplanmıştır.",
        "profit": "Toplam kâr $12,450 civarındadır.",
        "drawdown": "Maximum drawdown %18.3 seviyesinde gözlenmiştir.",
        "trades": "Toplam 47 işlem gerçekleştirilmiştir."
    }
    
    response = None
    for key, value in mock_responses.items():
        if key.lower() in query.lower():
            response = value
            break
    
    return {
        "query": query,
        "response": response or "Sorgunuzu anlamadım. Lütfen başka şekilde deneyin.",
        "confidence": 0.85
    }


@anvil.server.callable
@handle_anvil_errors
def export_performance_report(format: str = "pdf") -> dict:
    """Performans raporunu dışa aktar"""
    return {
        "status": "ok",
        "filename": f"performance_report.{format}",
        "size_mb": 2.5,
        "created_at": "2025-10-30T12:00:00Z"
    }
