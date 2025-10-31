from ._anvil_designer import LoginPageTemplate
from anvil import *
from ..MainLayoutForm import MainLayoutForm

class LoginPage(LoginPageTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def login_button_click(self, **event_args):
        # Simple demo: skip auth and open MainLayout
        open_form(MainLayoutForm())
