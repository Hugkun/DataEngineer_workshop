import utils.driver as driver
from selenium.webdriver.common.by import By
import pandas as pd

data = pd.read_csv("./csv/data.csv")
titles = data["title"]
urls = data["url"]

texts = []

chrome_driver = driver.chrome_driver

for url in urls:
    chrome_driver.get(url) 
    body_element = chrome_driver.find_element(By.TAG_NAME, "body")
    text = body_element.text
    texts.append(text[35:])
    
data["text"] = texts 
data.to_csv("./csv/articles_data.csv")
