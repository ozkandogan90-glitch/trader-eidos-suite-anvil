"""
server_leaders_league.py - Leaders League (Liderler Ligi)
Version: 8.0.0

Callable Functions:
- get_leaders_list() -> {leaders: List, total_count: int}
- apply_leaders_filter() -> Filtrelenmiş liste
- get_leaders_statistics() -> İstatistikler
"""

import anvil.server
from error_handler import handle_anvil_errors
from mock_data_generator import MockDataGenerator
from cache_manager import cached_result
from typing import Optional, List


@anvil.server.callable
@handle_anvil_errors
@cached_result("leaders_list", ttl_minutes=5)
def get_leaders_list(limit: int = 20) -> dict:
    """
    Liderler listesini al
    Output: {leaders: List[Dict], total_count: int}
    """
    return MockDataGenerator.generate_leaders_list(min(limit, 20))


@anvil.server.callable
@handle_anvil_errors
def apply_leaders_filter(
    regime_filter: Optional[str] = None,
    min_rs_score: Optional[float] = None,
    min_trend_score: Optional[int] = None,
    limit: int = 20
) -> dict:
    """
    Liderler listesine filtre uygula
    Input: {regime_filter?, min_rs_score?, min_trend_score?}
    Output: {leaders: List[Dict], total_count: int}
    """
    all_leaders = MockDataGenerator.generate_leaders_list(20)
    filtered = all_leaders["leaders"]
    
    # Filtreleri uygula
    if regime_filter:
        filtered = [l for l in filtered if l["market_structure"] == regime_filter]
    
    if min_rs_score is not None:
        filtered = [l for l in filtered if l["rs_score"] >= min_rs_score]
    
    if min_trend_score is not None:
        filtered = [l for l in filtered if l["trend_score"] >= min_trend_score]
    
    # Sıralamayı düzelt
    for i, leader in enumerate(filtered[:limit], 1):
        leader["rank"] = i
    
    return {
        "leaders": filtered[:limit],
        "total_count": len(filtered),
        "applied_filters": {
            "regime": regime_filter,
            "min_rs_score": min_rs_score,
            "min_trend_score": min_trend_score
        }
    }


@anvil.server.callable
@handle_anvil_errors
def get_leaders_statistics() -> dict:
    """Liderler istatistikleri"""
    leaders = MockDataGenerator.generate_leaders_list(20)
    data = leaders["leaders"]
    
    if not data:
        return {"count": 0}
    
    return {
        "total_leaders": len(data),
        "avg_rs_score": round(sum(l["rs_score"] for l in data) / len(data), 2),
        "avg_trend_score": round(sum(l["trend_score"] for l in data) / len(data), 2),
        "avg_change": round(sum(l["change_percent"] for l in data) / len(data), 2),
        "leaders_up": len([l for l in data if l["change_percent"] > 0]),
        "leaders_down": len([l for l in data if l["change_percent"] < 0])
    }
