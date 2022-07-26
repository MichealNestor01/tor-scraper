# setup.py
# this should only be run once, it creates the htmldata folder and then screenshots folder. Then also sets tor to auto connect
import os
from pywinauto import Application
from time import sleep

# create directories
os.mkdir("./htmldata")
os.mkdir("./screenshots")

# SETUP TOR 
app = Application(backend="win32").start(r"./Tor Browser/Browser/firefox.exe").connect(title="Tor Browser", timeout=10)
#print(app.TorBrowser.print_control_identifiers())
torInstance = app.TorBrowser.wrapper_object()
sleep(2)
torInstance.type_keys("{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}{TAB}")
torInstance.type_keys("{SPACE}")
# CLOSE TOR
sleep(2)
app.kill()