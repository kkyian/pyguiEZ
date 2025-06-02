import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from pyguiEZ.app import App  # ✅ matches renamed folder

def test_app_initialization():
    app = App()
    assert app.running
