This is a program that provides screenshots and the source code of any site that it is given. 
It passes all requests through the tor network so these sites can be .onion sites. 

===== SETUP GUIDE =====

How to install python dependencies:
1. Create a python virtual environment: </br>
    "python -m venv yourVirtualEnvironmentName"
2. Activate this environment, (do this every time you want to run the code) </br>
    (BASH AND ALL UNIX BASED SYSTEMS): "source yourVirtualEnvironmentName/Scripts/activate" </br>
    (Windows): "yourVirtualEnvironmentName\Scripts\activate"
3. Install the dependencies: </br>
    "pip install -r requirements.txt"

Now run setup.py to create the necessary directories: </br>
    "python setup.py"

You will also need tor browser installed in this directory. Your file tree should now look like this: </br>
tor-scraper </br>
->yourVirtualEnvironmentName (folder) </br>
->Tor Browser (folder) </br>
->htmldata (folder) </br>
->screenshots (folder) </br>
->modules (folder) </br>
->scraper.py (file) </br>
->requirements.txt </br>

Finally you will need to install geckodriver from: https://github.com/mozilla/geckodriver/releases </br>
and place it in the top directory of this repository so that your file tree looks like this: </br>
tor-scraper </br>
->yourVirtualEnvironmentName (folder) </br>
->Tor Browser (folder) </br>
->htmldata (folder) </br> 
->screenshots (folder) </br>
->modules (folder) </br>
->geckodriver.exe (file) </br>
->scraper.py (file) </br>
->requirements.txt </br>

==== USAGE GUIDE ==== 

TO DO 
