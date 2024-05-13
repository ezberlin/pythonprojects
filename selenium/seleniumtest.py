from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

options = Options()
options.add_argument("--headless")  # Verstecke GUI

# Erstellen Sie ein neues Firefox-Profil
profile = FirefoxProfile()

# Deaktivieren Sie das Laden von Bildern
profile.set_preference("permissions.default.image", 2)

# Setzen Sie das Profil in den Optionen
options.profile = profile

# Erstellen Sie den Browser mit den angegebenen Optionen
browser = webdriver.Firefox(options=options)

browser.get("https://www.twitch.tv/directory/game/Art")