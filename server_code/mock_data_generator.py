"""
mock_data_generator.py - Sahte Veri Üretimi
Version: 8.0.0
Purpose: FORMS_TO_BACKEND_MAPPING.csv'deki şemalara uygun mock veriler oluşturma
"""

import random
from datetime import datetime, timedelta
from typing import List, Dict, Any
from shared_types import (
    RegimeData, LeaderData, DnaTestResult, SignalData, 
    TradeRecord, PerformanceMetrics
)


class MockDataGenerator:
    """Mock veriler üreten yardımcı sınıf"""
    
    SYMBOLS = ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN", "META", "NFLX", "NVDA"]
    
    @staticmethod
    def generate_regime_data() -> Dict[str, Any]:
        """Market Compass - Piyasa Rejimi Verisi
        FORMS_TO_BACKEND_MAPPING.csv Schema Output: 
        {regime: str, trend_score: int, market_structure: str, confidence: int}
        """
        regime = random.choice(["LONG_ON", "SHORT_ON", "NEUTRAL"])
        return {
            "regime": regime,
            "trend_score": random.randint(30, 95),
            "market_structure": random.choice(["HH/HL", "LH/LL", "RANGE"]),
            "confidence": random.randint(70, 99),
            "timestamp": datetime.now().isoformat()
        }
    
    @staticmethod
    def generate_leaders_list(count: int = 10) -> Dict[str, Any]:
        """Leaders League - RS Rotasyonu Listesi
        Schema Output: {leaders: List[Dict], total_count: int}
        """
        leaders = []
        for rank in range(1, count + 1):
            leaders.append({
                "rank": rank,
                "symbol": random.choice(MockDataGenerator.SYMBOLS),
                "rs_score": random.uniform(0.5, 1.0),
                "trend_score": random.randint(40, 95),
                "market_structure": random.choice(["HH/HL", "LH/LL", "RANGE"]),
                "last_price": random.uniform(50, 500),
                "change_percent": random.uniform(-5, 5)
            })
        
        return {
            "leaders": leaders,
            "total_count": len(leaders),
            "timestamp": datetime.now().isoformat()
        }
    
    @staticmethod
    def generate_dna_test_results(symbols: List[str]) -> Dict[str, Any]:
        """DNA Test - Trend DNA Testi Sonuçları
        Schema Output: {results: List[Dict], pass_count: int, total_count: int, average_score: float}
        """
        results = []
        pass_count = 0
        
        for symbol in symbols:
            score = random.randint(30, 100)
            status = "PASS" if score >= 60 else "FAIL"
            
            if status == "PASS":
                pass_count += 1
            
            results.append({
                "symbol": symbol,
                "dna_score": score,
                "status": status,
                "confidence": random.randint(70, 99),
                "last_pattern_match": (datetime.now() - timedelta(days=random.randint(1, 30))).isoformat(),
                "pattern_name": random.choice(["Uptrend", "Downtrend", "Consolidation"])
            })
        
        avg_score = sum(r["dna_score"] for r in results) / len(results) if results else 0
        
        return {
            "results": results,
            "pass_count": pass_count,
            "total_count": len(results),
            "average_score": round(avg_score, 2),
            "timestamp": datetime.now().isoformat()
        }
    
    @staticmethod
    def generate_signals(count: int = 5) -> Dict[str, Any]:
        """Strategy Simulator - Strateji Sinyalleri
        Schema Output: {signals_found: int, signals: List[Dict], timestamp: str}
        """
        signals = []
        
        for i in range(count):
            entry_price = random.uniform(50, 500)
            direction = random.choice(["LONG", "SHORT"])
            
            if direction == "LONG":
                stop_loss = entry_price * 0.98
                take_profit = entry_price * 1.05
            else:
                stop_loss = entry_price * 1.02
                take_profit = entry_price * 0.95
            
            signals.append({
                "symbol": random.choice(MockDataGenerator.SYMBOLS),
                "direction": direction,
                "entry_price": round(entry_price, 2),
                "stop_loss": round(stop_loss, 2),
                "take_profit": round(take_profit, 2),
                "confidence": random.randint(60, 95),
                "regime_at_entry": random.choice(["LONG_ON", "SHORT_ON", "NEUTRAL"]),
                "trend_score_at_entry": random.randint(40, 95),
                "win_probability": round(random.uniform(0.4, 0.8), 2),
                "signal_id": f"SIG_{i+1:04d}"
            })
        
        return {
            "signals_found": count,
            "signals": signals,
            "timestamp": datetime.now().isoformat()
        }
    
    @staticmethod
    def generate_performance_metrics() -> Dict[str, Any]:
        """Performance Dashboard - Performans Metrikleri
        Schema Output: {total_trades: int, win_rate: float, profit_factor: float}
        """
        total_trades = random.randint(20, 100)
        win_count = random.randint(int(total_trades * 0.3), int(total_trades * 0.7))
        
        return {
            "total_trades": total_trades,
            "win_rate": round(win_count / total_trades if total_trades > 0 else 0, 3),
            "avg_win": round(random.uniform(0.5, 3.0), 2),
            "avg_loss": round(random.uniform(-3.0, -0.5), 2),
            "profit_factor": round(random.uniform(1.0, 3.0), 2),
            "max_drawdown": round(random.uniform(-0.05, -0.01), 3),
            "total_return": round(random.uniform(-10, 50), 2),
            "sharpe_ratio": round(random.uniform(0.5, 2.0), 2),
            "sortino_ratio": round(random.uniform(0.8, 2.5), 2),
            "timestamp": datetime.now().isoformat()
        }
    
    @staticmethod
    def generate_trades_history(count: int = 10) -> List[Dict[str, Any]]:
        """İşlem Geçmişi"""
        trades = []
        for i in range(count):
            entry_price = random.uniform(50, 500)
            exit_price = entry_price * random.uniform(0.95, 1.05)
            pnl = ((exit_price - entry_price) / entry_price) * 100
            
            trades.append({
                "trade_id": f"TRD_{i+1:05d}",
                "entry_date": (datetime.now() - timedelta(days=random.randint(1, 90))).isoformat(),
                "symbol": random.choice(MockDataGenerator.SYMBOLS),
                "direction": random.choice(["LONG", "SHORT"]),
                "entry_price": round(entry_price, 2),
                "exit_price": round(exit_price, 2),
                "pnl_percent": round(pnl, 2),
                "duration_days": random.randint(1, 30),
                "market_condition": random.choice(["Trending Up", "Trending Down", "Ranging"])
            })
        
        return trades
    
    @staticmethod
    def generate_command_center_evidence() -> Dict[str, Any]:
        """Command Center - Kanıt Bağlamı
        Schema Output: {evidence: Dict, scenarios: Dict, confidence: float}
        """
        return {
            "evidence": {
                "market_regime": MockDataGenerator.generate_regime_data(),
                "selected_leader": MockDataGenerator.generate_leaders_list(1)["leaders"][0],
                "dna_results": MockDataGenerator.generate_dna_test_results(["AAPL"])["results"],
                "strategy_signals": MockDataGenerator.generate_signals(1)["signals"],
            },
            "scenarios": {
                "S1": {"title": "İnkübasyon Fırsatı Tespit Edildi", "probability": 0.45},
                "S2": {"title": "Trend Başlangıcı Bekleniyor", "probability": 0.30},
                "S3": {"title": "Yapı Teyidi Bekleniyor", "probability": 0.25},
                "S4": {"title": "Global Rejim Uyarısı", "probability": 0.15},
                "S5": {"title": "Parametreler Eksik", "probability": 0.10},
                "S6": {"title": "Tüm Kanıtlar Olumlu", "probability": 0.65},
            },
            "overall_confidence": round(random.uniform(0.6, 0.95), 2),
            "timestamp": datetime.now().isoformat()
        }
    
    @staticmethod
    def generate_optimization_results() -> Dict[str, Any]:
        """Discovery Lab - Optimizasyon Sonuçları
        Schema Output: {job_id: str, status: str, progress?: float}
        """
        return {
            "job_id": f"OPT_{random.randint(10000, 99999)}",
            "status": "COMPLETED",
            "progress": 100.0,
            "best_parameters": {
                "stop_loss_percent": round(random.uniform(1.0, 5.0), 2),
                "take_profit_percent": round(random.uniform(2.0, 10.0), 2),
                "entry_condition": random.choice(["Breakout", "Retest", "Reversal"]),
            },
            "best_result": {
                "win_rate": round(random.uniform(0.4, 0.7), 3),
                "sharpe_ratio": round(random.uniform(1.0, 2.5), 2),
                "profit_factor": round(random.uniform(1.5, 3.5), 2),
            },
            "timestamp": datetime.now().isoformat()
        }
    
    @staticmethod
    def generate_system_info() -> Dict[str, Any]:
        """Sistem Bilgisi
        Schema Output: {status: ok, version: str, timestamp: str}
        """
        return {
            "status": "ok",
            "version": "8.0.0",
            "app_name": "Trader Eidos Suite",
            "environment": "MOCK_MODE",
            "uptime_hours": random.randint(1, 720),
            "database_status": "Connected",
            "api_status": "OK",
            "last_sync": datetime.now().isoformat(),
            "timestamp": datetime.now().isoformat()
        }
