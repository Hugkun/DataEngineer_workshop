import utils.driver as driver
from selenium.webdriver.common.by import By
import pandas as pd

chrome_driver = driver.chrome_driver
url = "https://hugkun.com/" # 各自で変更する
chrome_driver.get(url)  # driverでURLのページを開きます
# 記事のタイトルを入れる配列
titles = []
# 記事のurlを入れる配列
urls = []

data = pd.DataFrame()

# 以下部分は選択したサイトに合わせて変更してください
articles = chrome_driver.find_elements(By.CSS_SELECTOR, "li a") 

for article in articles:

    title = article.text.strip()

    url = article.get_attribute("href")

    # titles、urlsのそれぞれの配列に、取得したtitle、urlを入れます
    if title and url :
        
        if title not in titles and url not in urls : 
            titles.append(title)
            urls.append(url)
    


data["title"] = titles
data["url"] = urls
data.to_csv("./csv/data.csv")

