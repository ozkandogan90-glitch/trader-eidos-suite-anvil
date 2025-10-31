"""
server_simulation.py - Simulation Screen (Simülasyon Ekranı)
Version: 8.0.0
"""

import anvil.server
from error_handler import handle_anvil_errors
from mock_data_generator import MockDataGenerator


@anvil.server.callable
@handle_anvil_errors
def start_replay_simulation(strategy_id: str, symbol: str, date_range: tuple, speed: float = 1.0) -> dict:
    """Replay simülasyonu başlat"""
    return {
        "simulation_id": f"SIM_{MockDataGenerator.random.randint(10000, 99999)}",
        "status": "started",
        "strategy": strategy_id,
        "symbol": symbol,
        "speed": speed,
        "total_bars": 100
    }


@anvil.server.callable
@handle_anvil_errors
def get_replay_state(simulation_id: str) -> dict:
    """Replay durumunu al"""
    return {
        "simulation_id": simulation_id,
        "current_bar": 45,
        "current_date": "2025-08-15",
        "price": 150.25,
        "status": "running",
        "events": [
            {"type": "entry", "price": 148.50},
            {"type": "update", "price": 150.25}
        ]
    }


@anvil.server.callable
@handle_anvil_errors
def step_replay_forward(simulation_id: str, steps: int = 1) -> dict:
    """Replay'i ileri sar"""
    return {
        "simulation_id": simulation_id,
        "current_bar": 46,
        "current_price": 150.50,
        "new_events": []
    }


@anvil.server.callable
@handle_anvil_errors
def pause_replay(simulation_id: str) -> dict:
    """Replay'i duraklat"""
    return {
        "simulation_id": simulation_id,
        "status": "paused"
    }
