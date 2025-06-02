import sys
import os

# Add 'src/' to sys.path so pyguiEZ can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from pyguiEZ.app import App
from pyguiEZ.label import Label
from pyguiEZ.button import Button

app = App("Example GUI")

label = Label(app, "Click the button!", pos=(50, 50))

def on_click():
    label.set_text("Hello from pyguiEZ!")

button = Button(app, "Click Me", pos=(50, 100), command=on_click)

app.run()
