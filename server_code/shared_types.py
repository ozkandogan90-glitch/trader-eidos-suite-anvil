"""
shared_types.py - Anvil Server Modülleri Arasında Paylaşılan Veri Modelleri
Version: 8.0.0
Purpose: Type safety ve veri konsistansı sağlama
"""

from typing import Literal, List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime
import json


@dataclass
class RegimeData:
    """Piyasa Rejimi Bilgisi"""
    regime: Literal["LONG_ON", "SHORT_ON", "NEUTRAL"]
    trend_score: int  # 0-100
    market_structure: Literal["HH/HL", "LH/LL", "RANGE"]
    confidence: int  # 0-100
    timestamp: str  # ISO8601 format
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class LeaderData:
    """Liderler Ligi - RS Rotasyonu"""
    rank: int
    symbol: str
    rs_score: float
    trend_score: int  # 0-100
    market_structure: Literal["HH/HL", "LH/LL", "RANGE"]
    last_price: float
    change_percent: float
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class DnaTestResult:
    """Trend DNA Testi Sonuçları"""
    symbol: str
    dna_score: float  # 0-100
    status: Literal["PASS", "FAIL"]
    confidence: int  # 0-100
    last_pattern_match: str  # ISO8601
    pattern_name: str
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class SignalData:
    """Strateji Sinyali"""
    symbol: str
    direction: Literal["LONG", "SHORT"]
    entry_price: float
    stop_loss: float
    take_profit: float
    confidence: int  # 0-100
    regime_at_entry: Literal["LONG_ON", "SHORT_ON", "NEUTRAL"]
    trend_score_at_entry: int
    win_probability: float  # 0-1
    signal_id: str
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class TradeRecord:
    """İşlem Kaydı"""
    trade_id: str
    entry_date: str  # ISO8601
    symbol: str
    direction: Literal["LONG", "SHORT"]
    entry_price: float
    exit_price: float
    pnl_percent: float
    duration_days: int
    market_condition: str
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class PerformanceMetrics:
    """Performans Metrikleri"""
    total_trades: int
    win_rate: float  # 0-1
    avg_win: float
    avg_loss: float
    profit_factor: float
    max_drawdown: float  # 0-1
    total_return: float
    sharpe_ratio: float
    sortino_ratio: float
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class OptimizationResult:
    """Kurural Optimizasyon Sonuçları"""
    parameter_set: Dict[str, Any]
    win_rate: float
    sharpe_ratio: float
    profit_factor: float
    max_drawdown: float
    total_return: float
    optimization_score: float  # Normalize score
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class EvidenceContext:
    """Kanıt Bağlamı (Command Center için)"""
    market_regime: Optional[RegimeData]
    selected_leader: Optional[LeaderData]
    dna_results: Optional[List[DnaTestResult]]
    strategy_signals: Optional[List[SignalData]]
    lab_parameters: Optional[Dict[str, Any]]
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "market_regime": self.market_regime.to_dict() if self.market_regime else None,
            "selected_leader": self.selected_leader.to_dict() if self.selected_leader else None,
            "dna_results": [r.to_dict() for r in self.dna_results] if self.dna_results else None,
            "strategy_signals": [s.to_dict() for s in self.strategy_signals] if self.strategy_signals else None,
            "lab_parameters": self.lab_parameters,
        }


# Response Wrapper
class ApiResponse:
    """API Yanıt Standardı"""
    
    def __init__(self, status: Literal["success", "error"], data: Any = None, 
                 message: str = "", error_code: str = ""):
        self.status = status
        self.data = data
        self.message = message
        self.error_code = error_code
        self.timestamp = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "status": self.status,
            "data": self.data,
            "message": self.message,
            "error_code": self.error_code,
            "timestamp": self.timestamp,
        }
    
    def to_json(self) -> str:
        return json.dumps(self.to_dict())
