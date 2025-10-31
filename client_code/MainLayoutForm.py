from anvil import *
import anvil.users
import anvil.server

class MainLayoutForm:
    """
    Main Application Layout - Trader Eidos Suite
    Master Header + Tab Navigation + Content Area
    Mokap v8 Design Compliant
    """
    
    def __init__(self, **properties):
        self.active_tab = 'dashboard'
        self.current_user = None
        self.global_scope = {
            'country': None,
            'exchange': None,
            'index_sector': None,
            'timeframe': 'D'
        }
    
    def form_show(self, **event_args):
        """Initialize form when opened"""
        try:
            # Check authentication
            self.current_user = anvil.users.get_user()
            if not self.current_user:
                open_form('LoginPage')
                return
            
            # Initialize UI
            self.setup_master_header()
            self.setup_tab_navigation()
            self.load_global_scope()
            self.switch_to_tab('dashboard')
            
        except Exception as e:
            alert(f"Başlangıç hatası: {str(e)}")
            open_form('LoginPage')
    
    def setup_master_header(self):
        """Setup master header with branding"""
        try:
            # Master header should be visible with:
            # - Suite branding: "⚡ TRADER EIDOS Suite V6.1"
            # - User info on right
            # - Version and tagline
            pass
        except Exception as e:
            print(f"Header setup error: {str(e)}")
    
    def setup_tab_navigation(self):
        """Setup sticky tab navigation"""
        try:
            # Tab navigation should include:
            tabs = [
                ('dashboard', '📊 Dashboard'),
                ('rfs', '🧭 Market Compass'),
                ('leaders', '🏆 Leaders League'),
                ('dna', '🧬 DNA Test'),
                ('simulator', '⚙️ Strategy Simulator'),
                ('command', '🎯 Command Center'),
                ('lab', '🔬 Discovery Lab'),
                ('report', '📈 Performance'),
                ('replay', '🎬 Replay'),
                ('admin', '⚙️ Admin'),
                ('about', 'ℹ️ About')
            ]
            # These tabs will be rendered dynamically
        except Exception as e:
            print(f"Tab setup error: {str(e)}")
    
    def setup_global_scope_filter(self):
        """Setup global scope filter dropdowns"""
        try:
            # Global scope filter should include:
            # - Country select
            # - Exchange select (dependent on country)
            # - Index/Sector select (dependent on exchange)
            # - Timeframe select
            
            # Populate with active markets from backend
            scope_data = anvil.server.call('get_global_scope')
            if scope_data:
                self.global_scope.update(scope_data)
        except Exception as e:
            print(f"Global scope error: {str(e)}")
    
    def load_global_scope(self):
        """Load global scope configuration"""
        try:
            scope_data = anvil.server.call('get_global_scope')
            if scope_data and scope_data.get('status') == 'success':
                self.global_scope = scope_data.get('data', self.global_scope)
        except Exception as e:
            print(f"Load global scope error: {str(e)}")
    
    def switch_to_tab(self, tab_name):
        """Switch to specified tab and load content"""
        try:
            self.active_tab = tab_name
            
            # Map tab names to form classes
            form_map = {
                'dashboard': 'DashboardForm',
                'rfs': 'MarketCompassForm',
                'leaders': 'LeadersLeagueForm',
                'dna': 'DnaTestForm',
                'simulator': 'StrategySimulatorForm',
                'command': 'CommandCenterForm',
                'lab': 'DiscoveryLabForm',
                'report': 'PerformanceDashboardForm',
                'replay': 'SimulationScreenForm',
                'admin': 'AdminPanelsForm',
                'about': 'AboutForm'
            }
            
            target_form = form_map.get(tab_name, 'DashboardForm')
            
            # Notify backend of tab switch
            anvil.server.call('switch_tab', tab_name)
            
            # Load form content
            # In Anvil, this would be done by updating the content container
            
        except Exception as e:
            alert(f"Tab geçişi hatası: {str(e)}")
    
    def navigate_to_form(self, form_name):
        """Navigate to specified form"""
        try:
            if form_name and form_name != self.active_tab:
                self.switch_to_tab(form_name)
        except Exception as e:
            alert(f"Navigasyon hatası: {str(e)}")
    
    def update_global_scope(self, country=None, exchange=None, 
                          index_sector=None, timeframe=None):
        """Update global scope selections"""
        try:
            if country:
                self.global_scope['country'] = country
            if exchange:
                self.global_scope['exchange'] = exchange
            if index_sector:
                self.global_scope['index_sector'] = index_sector
            if timeframe:
                self.global_scope['timeframe'] = timeframe
            
            # Persist to backend
            result = anvil.server.call(
                'update_global_scope',
                self.global_scope
            )
            
            if result and result.get('status') == 'success':
                # Refresh current tab with new scope
                self.refresh_current_tab()
        except Exception as e:
            alert(f"Kapsam güncelleme hatası: {str(e)}")
    
    def refresh_current_tab(self):
        """Refresh current tab with updated global scope"""
        try:
            # This triggers data refresh in the active tab
            self.switch_to_tab(self.active_tab)
        except Exception as e:
            print(f"Refresh error: {str(e)}")
    
    def logout_click(self, **event_args):
        """Logout current user"""
        try:
            confirmed = confirm(
                "Çıkış yapmak istediğinizden emin misiniz?",
                title="Çıkış Yap"
            )
            if confirmed:
                anvil.users.logout()
                open_form('LoginPage')
        except Exception as e:
            alert(f"Çıkış hatası: {str(e)}")
    
    def show_user_menu(self, **event_args):
        """Show user menu dropdown"""
        try:
            # Show user profile options
            pass
        except Exception as e:
            print(f"User menu error: {str(e)}")

