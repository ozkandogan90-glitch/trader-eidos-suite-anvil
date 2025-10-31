from anvil import *
import anvil.users
import anvil.server

class LoginPage:
    """
    Modern Login Page - Trader Eidos Suite
    Mokap v8 Design Compliant Light Theme
    """
    def __init__(self, **properties):
        self.mode = 'login'  # 'login' or 'signup'
    
    def form_show(self, **event_args):
        """Check if user already logged in, otherwise show login page"""
        try:
            user = anvil.users.get_user()
            if user:
                open_form('MainLayoutForm')
        except Exception as e:
            print(f"Auth check error: {str(e)}")
    
    def login_button_click(self, **event_args):
        """Handle login authentication"""
        try:
            email = self.email_input.text.strip()
            password = self.password_input.text
            
            if not email or not password:
                self.show_error("Email ve şifre gereklidir")
                return
            
            if not self._validate_email(email):
                self.show_error("Lütfen geçerli bir email girin")
                return
            
            user = anvil.users.login_with_email(email, password)
            if user:
                open_form('MainLayoutForm')
            else:
                self.show_error("Giriş başarısız")
        except Exception as e:
            self.show_error(f"Giriş hatası: {str(e)}")
    
    def signup_button_click(self, **event_args):
        """Handle user registration"""
        try:
            email = self.email_input.text.strip()
            password = self.password_input.text
            password_confirm = self.password_confirm_input.text
            
            if not email or not password or not password_confirm:
                self.show_error("Tüm alanlar gereklidir")
                return
            
            if not self._validate_email(email):
                self.show_error("Lütfen geçerli bir email girin")
                return
            
            if len(password) < 6:
                self.show_error("Şifre en az 6 karakter olmalıdır")
                return
            
            if password != password_confirm:
                self.show_error("Şifreler eşleşmiyor")
                return
            
            user = anvil.users.signup_with_email(email, password)
            if user:
                self.show_success("Kayıt başarılı! Giriş yapılıyor...")
                self.email_input.text = ""
                self.password_input.text = ""
                self.password_confirm_input.text = ""
                open_form('MainLayoutForm')
            else:
                self.show_error("Kayıt başarısız")
        except Exception as e:
            self.show_error(f"Kayıt hatası: {str(e)}")
    
    def toggle_mode_click(self, **event_args):
        """Toggle between login and signup modes"""
        self.mode = 'signup' if self.mode == 'login' else 'login'
        self.email_input.text = ""
        self.password_input.text = ""
        self.password_confirm_input.text = ""
        # Update UI based on mode
        self.update_mode_ui()
    
    def update_mode_ui(self):
        """Update UI elements based on login/signup mode"""
        # Bu fonksiyon Anvil form tasarımında kaynaklanmış UI güncellemelerini yapacak
        pass
    
    def show_error(self, message):
        """Display error message"""
        alert(message)
        # Alternative: self.error_label.text = message
    
    def show_success(self, message):
        """Display success message"""
        # self.success_label.text = message
        pass
    
    def _validate_email(self, email):
        """Basic email validation"""
        return '@' in email and '.' in email.split('@')[1]

