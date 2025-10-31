from ._anvil_designer import MainLayoutFormTemplate
from anvil import *
from ..DashboardForm import DashboardForm

class MainLayoutForm(MainLayoutFormTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.show_tab('dashboard')

    def clear_content(self):
        self.content_panel.clear()

    def show_tab(self, name):
        self.clear_content()
        if name == 'dashboard':
            self.content_panel.add_component(DashboardForm())
        else:
            # Placeholders for other tabs
            self.content_panel.add_component(Label(text=f"{name} - coming soon"))

    def dashboard_btn_click(self, **event_args):
        self.show_tab('dashboard')

    def rfs_btn_click(self, **event_args):
        self.show_tab('rfs')

    def leaders_btn_click(self, **event_args):
        self.show_tab('leaders')

    def dna_btn_click(self, **event_args):
        self.show_tab('dna')
