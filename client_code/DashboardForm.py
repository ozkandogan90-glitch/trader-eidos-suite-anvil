from anvil import *
import anvil.users
import anvil.server

class DashboardForm:
    """
    Dashboard / Ana Sayfa - Trader Eidos Suite
    Global Scope Filter + System KPIs + Market Overview
    Mokap v8 Design Compliant
    """
    
    def __init__(self, **properties):
        self.markets_data = {}
        self.system_info = {}
        self.selected_scope = {
            'country': None,
            'exchange': None,
            'index_sector': None,
            'timeframe': 'D'
        }
    
    def form_show(self, **event_args):
        """Initialize dashboard"""
        try:
            user = anvil.users.get_user()
            if not user:
                open_form('LoginPage')
                return
            
            self.load_dashboard_data()
            self.setup_global_scope_filter()
            self.load_system_info()
            self.load_market_overview()
            
        except Exception as e:
            alert(f"Dashboard yükleme hatası: {str(e)}")
    
    def load_dashboard_data(self):
        """Load dashboard configuration"""
        try:
            # Get active markets and system configuration
            data = anvil.server.call('get_system_info')
            if data and data.get('status') == 'success':
                self.system_info = data.get('data', {})
        except Exception as e:
            print(f"Dashboard data load error: {str(e)}")
    
    def setup_global_scope_filter(self):
        """Setup global scope filter with cascading dropdowns"""
        try:
            # Get list of active countries/exchanges
            scope_data = anvil.server.call('get_global_scope')
            
            if scope_data and scope_data.get('status') == 'success':
                data = scope_data.get('data', {})
                
                # Populate country dropdown
                countries = data.get('countries', [])
                exchanges = data.get('exchanges', [])
                
                # These would be set in Anvil form UI
                # self.country_dropdown.items = [(c, c) for c in countries]
                
        except Exception as e:
            print(f"Global scope setup error: {str(e)}")
    
    def country_select_change(self, **event_args):
        """Handle country selection change"""
        try:
            country = self.selected_scope.get('country')
            if not country:
                return
            
            # Fetch exchanges for selected country
            scope_data = anvil.server.call(
                'get_global_scope',
                country=country
            )
            
            if scope_data and scope_data.get('status') == 'success':
                exchanges = scope_data.get('data', {}).get('exchanges', [])
                # Update exchange dropdown with cascading values
        
        except Exception as e:
            print(f"Country select error: {str(e)}")
    
    def exchange_select_change(self, **event_args):
        """Handle exchange selection change"""
        try:
            exchange = self.selected_scope.get('exchange')
            if not exchange:
                return
            
            # Fetch sectors/indices for selected exchange
            scope_data = anvil.server.call(
                'get_global_scope',
                exchange=exchange
            )
            
            if scope_data and scope_data.get('status') == 'success':
                sectors = scope_data.get('data', {}).get('sectors', [])
                # Update sector dropdown
        
        except Exception as e:
            print(f"Exchange select error: {str(e)}")
    
    def timeframe_select_change(self, **event_args):
        """Handle timeframe selection change"""
        try:
            self.selected_scope['timeframe'] = self.timeframe_select.selected_value
            self.refresh_dashboard()
        except Exception as e:
            print(f"Timeframe select error: {str(e)}")
    
    def load_system_info(self):
        """Load system information and metrics"""
        try:
            info = anvil.server.call('get_system_info')
            if info and info.get('status') == 'success':
                data = info.get('data', {})
                
                # Display system metrics
                # Version, build date, available modules, etc.
                system_details = {
                    'version': data.get('version', 'N/A'),
                    'build_date': data.get('build_date', 'N/A'),
                    'status': data.get('status', 'OK'),
                    'database': data.get('database_status', 'Connected'),
                    'available_modules': len(data.get('available_modules', [])),
                }
                
                self.display_system_info(system_details)
        
        except Exception as e:
            print(f"System info load error: {str(e)}")
    
    def display_system_info(self, info_dict):
        """Display system information in KPI tiles"""
        try:
            # These would update KPI tiles in the form:
            # self.version_label.text = info_dict.get('version')
            # self.build_label.text = info_dict.get('build_date')
            # self.status_badge.text = info_dict.get('status')
            pass
        except Exception as e:
            print(f"Display system info error: {str(e)}")
    
    def load_market_overview(self):
        """Load market overview and quick stats"""
        try:
            # Get global market regime
            regime_data = anvil.server.call('get_market_regime')
            
            if regime_data and regime_data.get('status') == 'success':
                market_data = regime_data.get('data', {})
                
                overview = {
                    'regime': market_data.get('regime', 'NEUTRAL'),
                    'trend_score': market_data.get('trend_score', 0),
                    'market_structure': market_data.get('market_structure', 'RANGE'),
                    'confidence': market_data.get('confidence', 0),
                    'timestamp': market_data.get('timestamp', 'N/A')
                }
                
                self.display_market_overview(overview)
        
        except Exception as e:
            print(f"Market overview error: {str(e)}")
    
    def display_market_overview(self, overview_dict):
        """Display market overview in UI"""
        try:
            # Update market overview section:
            # self.regime_badge.text = overview_dict.get('regime')
            # self.trend_score_label.text = str(overview_dict.get('trend_score'))
            # self.confidence_label.text = str(overview_dict.get('confidence'))
            pass
        except Exception as e:
            print(f"Display market overview error: {str(e)}")
    
    def refresh_dashboard(self):
        """Refresh dashboard with current scope selection"""
        try:
            self.load_system_info()
            self.load_market_overview()
        except Exception as e:
            alert(f"Dashboard yenileme hatası: {str(e)}")
    
    def apply_scope_filter(self, **event_args):
        """Apply global scope filter and refresh all data"""
        try:
            # Validate selections
            if not self.selected_scope.get('country'):
                alert("Lütfen ülke seçin")
                return
            
            if not self.selected_scope.get('exchange'):
                alert("Lütfen borsa seçin")
                return
            
            # Update global scope in MainLayoutForm
            # This would typically be called on parent form
            
            self.refresh_dashboard()
            alert("Kapsam filtreleri uygulandı")
        
        except Exception as e:
            alert(f"Filtre uygulama hatası: {str(e)}")
    
    def reset_filters(self, **event_args):
        """Reset all filters to defaults"""
        try:
            self.selected_scope = {
                'country': None,
                'exchange': None,
                'index_sector': None,
                'timeframe': 'D'
            }
            self.refresh_dashboard()
        except Exception as e:
            alert(f"Filtreleri sıfırlama hatası: {str(e)}")
