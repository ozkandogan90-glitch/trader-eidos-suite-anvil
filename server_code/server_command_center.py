"""
server_command_center.py - Command Center (Komuta Merkezi)
Version: 8.0.0
"""

import anvil.server
from error_handler import handle_anvil_errors
from mock_data_generator import MockDataGenerator


@anvil.server.callable
@handle_anvil_errors
def get_comprehensive_evidence(symbol: str, context: dict = None) -> dict:
    """Kapsamlı kanıt bilgisi"""
    evidence = MockDataGenerator.generate_command_center_evidence()
    evidence["symbol"] = symbol
    evidence["context"] = context or {}
    return evidence


@anvil.server.callable
@handle_anvil_errors
def generate_ai_scenarios(evidence: dict) -> dict:
    """AI senaryolarını oluştur (S1-S6)"""
    return MockDataGenerator.generate_command_center_evidence()["scenarios"]


@anvil.server.callable
@handle_anvil_errors
def calculate_overall_confidence(evidence: dict) -> float:
    """Genel güven skoru hesapla"""
    return MockDataGenerator.generate_command_center_evidence()["overall_confidence"]


@anvil.server.callable
@handle_anvil_errors
def save_trade_decision(symbol: str, decision: str, evidence: dict) -> dict:
    """İşlem kararını kaydet"""
    return {
        "status": "ok",
        "message": f"Karar kaydedildi: {decision}",
        "symbol": symbol,
        "decision_id": f"DEC_{MockDataGenerator.random.randint(10000, 99999)}"
    }
