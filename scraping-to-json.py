import requests
import json
from bs4 import BeautifulSoup

# リクエスト先URL1
url = "https://www.booking.com/searchresults.html?ss=Tokyo%2C+Japan&lang=ja&dest_id=4720&dest_type=region&checkin=2023-11-01&checkout=2023-11-10&group_adults=2&no_rooms=1&group_children=0p_adults=2&group_children=0&no_rooms=1&selected_currency=JPY"

# ヘッダー情報（User-Agent）の設定
headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5042.108 Safari/537.36"}

# URLへのリクエストとレスポンスの取得
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

print(response.status_code)

# ホテルの検索結果を格納するリスト
hotel_results = []

# 各ホテル情報の取得
for el in soup.find_all("div", {"data-testid": "property-card"}):
    review_score_element = el.find("div", {"data-testid": "review-score"})
    review_count = review_score_element.text.strip().split(" ")[1].replace("クチコミ", "")
    hotel_results.append({
            "name": el.find("div", {"data-testid": "title"}).text.strip(),
            "link": el.find("a", {"data-testid": "title-link"})["href"],
            "location": el.find("span", {"data-testid": "address"}).text.strip(),
            "rating": el.find("div", {"data-testid": "review-score"}).text.strip().split(" ")[0],
            "review_count": review_count,
            "thumbnail": el.find("img", {"data-testid": "image"})['src'],
        })

# 取得したホテル情報をJSON形式で表示
print(hotel_results)
#print(json.dumps(hotel_results, indent=4, sort_keys=True))
