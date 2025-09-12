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

# 抽出したテキストをdata辞書に追加


print("--- 修正前のデータ ---")
print(data['text'].iloc[0])


# --- 2. text列の改行コードを半角スペースに置換 ---
# df['text']の全ての行に対して、改行コード(\n or \r\n)を半角スペース(' ')に置換します
data['text'] = data['text'].str.replace(r'\r|\n', ' ', regex=True)

# --- 3. Pandas DataFrameに変換してCSVに保存 ---
try:
    # データをPandasのDataFrame形式に変換
    df = pd.DataFrame(data)

    # DataFrameをCSVファイルに保存（文字化けと不要な列を防ぐ設定）
    df.to_csv(
        './csv/articles_data.csv', 
        index=False, 
        encoding='utf-8-sig'
    )
    
    print("スクレイピング結果を './csv/articles_data.csv' に正常に保存しました。")

except Exception as e:
    print(f"CSV保存中にエラーが発生しました: {e}")
# data.to_csv("./csv/articles_data.csv")
