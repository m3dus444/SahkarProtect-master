import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

""" Options """

chrome_options = webdriver.ChromeOptions()
#p = {'download.default_directory': 'C:\\Users\\julie\\Desktop'}
# add options to browser
#chrome_options.add_experimental_option('prefs', p)

chrome_options.add_experimental_option("prefs", {"download.default_directory": r"C:\Users\julie\Desktop",
                                                 "download.prompt_for_download": False,
                                                 "download.directory_upgrade": True,
                                                 "safebrowsing.enabled": True})

"""
chrome_options.AddUserProfilePreference("download.default_directory", @"D:\DataTest")
chrome_options.AddUserProfilePreference("intl.accept_languages", "nl")
chrome_options.AddUserProfilePreference("disable-popup-blocking", "true")
var driver = new ChromeDriver(@"D:\chromedriver_win32\", chromeOptions)
"""
# download = Chromedriver.find_elements(by.Xpath, "//a[.='ダウンロード']")
# download = Chromedriver.find_element_by_xpath("//a[.='ダウンロード']")


""" Service starting """

service = Service('C:/Users/julie/Documents/SAHKAR/desktop_cleaner-master/desktop_cleaner/chromedriver.exe')
service.start()
Chromedriver = webdriver.Remote(service.service_url, options=chrome_options)

""" Requests """

Chromedriver.get("https://www.mediafire.com/file/79lw4pp2a79nrh8/fichier_test_chrome_driver.txt/file")

# Chromedriver.get('http://www.google.com/');
time.sleep(100)  # Let the user actually see something!

try:
    Chromedriver.quit()
except:
    service.send_remote_shutdown_command()
