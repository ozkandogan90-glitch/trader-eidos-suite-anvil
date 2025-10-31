"""
server_dna_test.py - DNA Test (Trend DNA Testi)
Version: 8.0.0

Callable Functions:
- run_dna_test(symbols, threshold) -> Test sonuçları
- get_dna_pattern_details(symbol) -> Pattern detayları
- save_dna_test_results(results) -> {status: ok}
"""

import anvil.server
from error_handler import handle_anvil_errors
from mock_data_generator import MockDataGenerator
from typing import List, Optional


@anvil.server.callable
@handle_anvil_errors
def run_dna_test(symbols: List[str], threshold: Optional[int] = 60) -> dict:
    """
    Trend DNA Testini çalıştır
    Input: {symbols: List[str], threshold?: int}
    Output: {results: List, pass_count: int, total_count: int, average_score: float}
    """
    if not symbols:
        symbols = ["AAPL", "GOOGL", "MSFT"]
    
    return MockDataGenerator.generate_dna_test_results(symbols[:5])


@anvil.server.callable
@handle_anvil_errors
def get_dna_pattern_details(symbol: str) -> dict:
    """DNA pattern detaylarını al"""
    return {
        "symbol": symbol,
        "pattern_name": "Bullish Consolidation",
        "pattern_score": MockDataGenerator.random.randint(60, 100),
        "formation_bars": MockDataGenerator.random.randint(10, 50),
        "breakout_direction": MockDataGenerator.random.choice(["UP", "DOWN"]),
        "success_rate": round(MockDataGenerator.random.uniform(0.5, 0.9), 2),
        "avg_move_after_breakout": f"{MockDataGenerator.random.uniform(2, 10):.1f}%",
        "last_occurrence": "2025-10-15"
    }


@anvil.server.callable
@handle_anvil_errors
def save_dna_test_results(results: dict) -> dict:
    """DNA test sonuçlarını kaydet"""
    return {
        "status": "ok",
        "message": "DNA test sonuçları kaydedildi",
        "results_count": len(results.get("results", [])),
        "saved_at": "2025-10-30T12:00:00Z"
    }


@anvil.server.callable
@handle_anvil_errors
def get_pattern_pool() -> dict:
    """Kayıtlı pattern havuzunu al"""
    return {
        "patterns": [
            {
                "name": "Bullish Flag",
                "frequency": 15,
                "win_rate": 0.72,
                "avg_return": 2.5
            },
            {
                "name": "Bearish Pennant",
                "frequency": 8,
                "win_rate": 0.68,
                "avg_return": -2.1
            },
            {
                "name": "Double Top",
                "frequency": 12,
                "win_rate": 0.65,
                "avg_return": -3.2
            }
        ],
        "total_patterns": 3
    }
