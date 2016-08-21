from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config')

path = parser.get('fangraph_download', 'download_path')
hitter_url = parser.get('fangraph_download', 'hitter_url')

# To prevent download dialog
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2)  # custom location
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', path)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

browser = webdriver.Firefox(profile)
browser.get(hitter_url)

browser.find_element_by_id('LeaderBoard1_cmdCSV').click()

browser.close()
