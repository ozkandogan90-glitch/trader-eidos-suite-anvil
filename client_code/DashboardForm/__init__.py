from ._anvil_designer import DashboardFormTemplate
from anvil import *

class DashboardForm(DashboardFormTemplate):
    """Native Anvil version of the dashboard mockup.
    Provides: global filters + top KPIs + content placeholders.
    """
    def __init__(self, **properties):
        self.init_components(**properties)
        # Initialize filters
        self.country_dropdown.items = ["TR", "US", "EU"]
        self.exchange_dropdown.items = ["BIST", "NASDAQ", "NYSE", "XETRA"]
        self.index_sector_dropdown.items = ["BIST 30", "S&P 500", "Tech", "Financials"]
        self.timeframe_select.items = [("Günlük","D"), ("Haftalık","W"), ("Aylık","M"), ("4 Saat","H4"), ("1 Saat","H1")]
        # Set KPIs with placeholders
        self.regime_badge.text = "Risk-On"
        self.trend_score_label.text = "82 / 100"
        self.confidence_label.text = "Yüksek"
