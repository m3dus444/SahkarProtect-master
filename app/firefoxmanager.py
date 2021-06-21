import profile

from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver import findElements



profile = webdriver.FirefoxProfile()

download = webdriver.(By.XPath("//a[.='ダウンロード']"));

webdriver.

#profile.set_preference("browser.download.folderlist", 2)
#profile.set_preference("browser.download.dir", "C:\\Users\\julie\\Desktop")
#profile.set_preference("browser.download.defaultFolder","D:\Downloads")


profile.set_preference("browser.helperApps.alwaysAsk.force", False)
profile.set_preference("browser.download.manager.showWhenStarting",False)
profile.set_preference("browser.download.dir", "C:\\users\\julie\\desktop\\")
profile.set_preference("browser.download.downloadDir", "C:\\users\\julie\\desktop\\")
profile.set_preference("browser.download.defaultFolder", "C:\\users\\julie\\desktop\\")
driver = webdriver.Firefox(firefox_profile=profile)
driver.get("https://www.mediafire.com/file/rj5j4127ax7d4t9/SavedGames.rar/file")




"""
options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get("https://pythonbasics.org")
"""


"""
driver = webdriver.Firefox()
driver.get("https://dev.to")

driver.find_element_by_id("nav-search").send_keys("Selenium")
"""