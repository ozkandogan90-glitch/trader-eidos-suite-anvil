"""
server_market_compass.py - Market Compass (Piyasa Pusulası)
Version: 8.0.0
Purpose: Piyasa rejimi, trend score ve piyasa yapısı verisi

Callable Functions:
- get_market_regime() -> {regime, trend_score, market_structure, confidence}
- get_trend_chart_data() -> Chart verisi (mock)
- refresh_market_data() -> {status: ok, ...}
"""

import anvil.server
from error_handler import handle_anvil_errors
from mock_data_generator import MockDataGenerator
from cache_manager import cached_result
from datetime import datetime


@anvil.server.callable
@handle_anvil_errors
@cached_result("market_regime", ttl_minutes=5)
def get_market_regime(symbol: str = "SPY", period: str = "D") -> dict:
    """
    Piyasa Rejimi Tespiti
    
    Output Schema (FORMS_TO_BACKEND_MAPPING):
    {regime: str, trend_score: int, market_structure: str, confidence: int}
    """
    regime_data = MockDataGenerator.generate_regime_data()
    return {
        "regime": regime_data["regime"],
        "trend_score": regime_data["trend_score"],
        "market_structure": regime_data["market_structure"],
        "confidence": regime_data["confidence"],
        "symbol": symbol,
        "period": period,
        "timestamp": regime_data["timestamp"]
    }


@anvil.server.callable
@handle_anvil_errors
@cached_result("trend_chart_data", ttl_minutes=5)
def get_trend_chart_data(symbol: str = "SPY", period: str = "D") -> dict:
    """Trend grafiği verisi (mock chart points)"""
    
    # Mock chart points
    chart_points = []
    base_value = 100
    
    for i in range(30):
        value = base_value + (i * 0.5) + MockDataGenerator.random.uniform(-2, 2)
        chart_points.append({
            "date": f"2025-{10-i//10:02d}-{30-i%10:02d}",
            "value": round(value, 2)
        })
    
    return {
        "symbol": symbol,
        "period": period,
        "chart_data": chart_points,
        "current_value": chart_points[-1]["value"],
        "min_value": min(p["value"] for p in chart_points),
        "max_value": max(p["value"] for p in chart_points),
        "timestamp": datetime.now().isoformat()
    }


@anvil.server.callable
@handle_anvil_errors
def refresh_market_data(symbol: str = "SPY") -> dict:
    """Piyasa verisini yenile"""
    regime = MockDataGenerator.generate_regime_data()
    
    return {
        "status": "ok",
        "message": f"{symbol} piyasa verisi güncellendi",
        "regime": regime,
        "last_refresh": datetime.now().isoformat()
    }


@anvil.server.callable
@handle_anvil_errors
def get_market_structure_explanation() -> dict:
    """Piyasa yapısı açıklamalarını al"""
    return {
        "HH/HL": "Higher High / Higher Low - Yukarı trend (bullish)",
        "LH/LL": "Lower High / Lower Low - Aşağı trend (bearish)",
        "RANGE": "Konsolidasyon - Yatay hareket"
    }
