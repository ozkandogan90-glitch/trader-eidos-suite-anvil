"""
server_simulator.py - Strategy Simulator (Strateji Simülatörü)
Version: 8.0.0

Callable Functions:
- run_strategy_scan() -> Tarama sonuçları
- get_optimized_parameters() -> Optimize edilmiş parametreler
- preview_signal_details() -> Signal detayları
"""

import anvil.server
from error_handler import handle_anvil_errors
from mock_data_generator import MockDataGenerator
from typing import List, Optional, Dict, Any


@anvil.server.callable
@handle_anvil_errors
def run_strategy_scan(
    symbols: Optional[List[str]] = None,
    regime_filter: Optional[str] = None,
    strategy_params: Optional[Dict[str, Any]] = None,
    limit: int = 10
) -> dict:
    """
    Strateji taraması yap
    Input: {symbols: List[str], regime_filter?: str, strategy_params?: Dict}
    Output: {signals_found: int, signals: List[Dict], timestamp: str}
    """
    if not symbols:
        symbols = ["AAPL", "GOOGL", "MSFT", "TSLA"]
    
    scan_result = MockDataGenerator.generate_signals(limit)
    
    # Regime filtresini uygula
    if regime_filter:
        scan_result["signals"] = [
            s for s in scan_result["signals"] 
            if s["regime_at_entry"] == regime_filter
        ]
    
    scan_result["signals_found"] = len(scan_result["signals"])
    scan_result["scanned_symbols"] = symbols
    scan_result["strategy_params"] = strategy_params or {}
    
    return scan_result


@anvil.server.callable
@handle_anvil_errors
def get_optimized_parameters(
    symbols: Optional[List[str]] = None,
    time_period: Optional[tuple] = None,
    strategy_template: str = "Default"
) -> dict:
    """Optimize edilmiş parametrelergerektiği al"""
    return MockDataGenerator.generate_optimization_results()


@anvil.server.callable
@handle_anvil_errors
def preview_signal_details(signal_id: str) -> dict:
    """Signal detaylarını görüntüle"""
    signals = MockDataGenerator.generate_signals(1)["signals"]
    
    if not signals:
        return {"error": "Signal not found"}
    
    signal = signals[0]
    signal["signal_id"] = signal_id
    signal["detailed_analysis"] = {
        "entry_rationale": "Price tested support level with bullish divergence",
        "risk_reward_ratio": round(
            (signal["take_profit"] - signal["entry_price"]) / 
            (signal["entry_price"] - signal["stop_loss"]), 2
        ),
        "market_bias": "Bullish on daily, neutral on 4h",
        "alternative_exit": signal["take_profit"] * 1.1
    }
    
    return signal


@anvil.server.callable
@handle_anvil_errors
def validate_strategy_parameters(params: Dict[str, Any]) -> dict:
    """Strateji parametrelerini doğrula"""
    errors = []
    
    if "stop_loss" in params and params["stop_loss"] > 10:
        errors.append("Stop Loss % çok yüksek (max 10)")
    
    if "take_profit" in params and params["take_profit"] < 0.5:
        errors.append("Take Profit % çok düşük (min 0.5)")
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": []
    }
