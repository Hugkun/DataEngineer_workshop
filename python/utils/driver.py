from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()

options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument('--proxy-server="direct://"')
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--no-sandbox")
options.add_argument('--blink-settings=imagesEnabled=false') # 画像を読み込まないで軽くする
options.add_argument('--headless')
options.add_argument("--start-maximized")


chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)