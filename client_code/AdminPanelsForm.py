from anvil import *
import anvil.users
import anvil.server

class AdminPanelsForm:
    """
    Admin Panels - User and system management
    Mokap v8 Design Compliant - 'admin' tab
    """
    
    def __init__(self, **properties):
        pass
    
    def form_show(self, **event_args):
        """Initialize form"""
        try:
            user = anvil.users.get_user()
            if not user:
                open_form('LoginPage')
                return
            self.load_form_data()
        except Exception as e:
            alert(f"Form yükleme hatası: {str(e)}")
    
    def load_form_data(self):
        """Load form-specific data"""
        try:
            # Load data from backend
            pass
        except Exception as e:
            print(f"Data load error: {str(e)}")
    
    def refresh_data(self, **event_args):
        """Refresh form data"""
        try:
            self.load_form_data()
        except Exception as e:
            alert(f"Yenileme hatası: {str(e)}")
