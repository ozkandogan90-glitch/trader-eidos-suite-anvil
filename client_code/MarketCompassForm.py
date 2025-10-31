from anvil import *
import anvil.users
import anvil.server

class MarketCompassForm:
    """
    Market Compass (RFS - Regime/Flow/Structure) Analysis
    Trend Score, Market Structure, Regime Detection
    Mokap v8: 'rfs' tab
    """
    
    def __init__(self, **properties):
        self.market_regime = {}
        self.index_data = {}
        self.chart_data = []
    
    def form_show(self, **event_args):
        """Initialize Market Compass"""
        try:
            user = anvil.users.get_user()
            if not user:
                open_form('LoginPage')
                return
            self.load_market_regime_data()
            self.load_index_data()
        except Exception as e:
            alert(f"Market Compass yükleme hatası: {str(e)}")
    
    def load_market_regime_data(self):
        """Load market regime analysis (Regime, Trend Score, Structure)"""
        try:
            data = anvil.server.call('get_market_regime')
            if data and data.get('status') == 'success':
                self.market_regime = data.get('data', {})
                self.display_regime_analysis()
        except Exception as e:
            print(f"Market regime error: {str(e)}")
    
    def load_index_data(self):
        """Load current index OHLC and indicator data"""
        try:
            data = anvil.server.call('get_index_data')
            if data and data.get('status') == 'success':
                self.index_data = data.get('data', {})
                self.display_index_metrics()
        except Exception as e:
            print(f"Index data error: {str(e)}")
    
    def display_regime_analysis(self):
        """Display regime analysis components"""
        try:
            # Components to display:
            # - Regime badge (LONG_ON, SHORT_ON, NEUTRAL)
            # - Trend Score gauge (0-100)
            # - Market Structure indicator
            # - Confidence level
            pass
        except Exception as e:
            print(f"Display regime error: {str(e)}")
    
    def display_index_metrics(self):
        """Display index metrics"""
        try:
            # Display:
            # - Current price
            # - Open, High, Low, Close
            # - Daily change
            # - Technical indicators
            pass
        except Exception as e:
            print(f"Display index metrics error: {str(e)}")
    
    def refresh_market_data(self, **event_args):
        """Refresh market data from API"""
        try:
            result = anvil.server.call('refresh_market_data')
            if result and result.get('status') == 'success':
                self.load_market_regime_data()
                self.load_index_data()
                alert("Pazar verileri güncellendi")
        except Exception as e:
            alert(f"Yenileme hatası: {str(e)}")

