# import sqlite3
# import requests
# import json
# from bs4 import BeautifulSoup


# # connect/create db for saving scraped data
# conn = sqlite3.connect("scraped_data.db")
# c = conn.cursor()
# # c.execute("""CREATE TABLE news(id INT , url TEXT, title TEXT, sumamry TEXT, date_published INT) """)
# # We Scrap the URL to find all news

# response = requests.get("https://feeds.npr.org/1004/feed.json")
# soup = BeautifulSoup(response.text, "html.parser")
# site_json = json.loads(soup.text)
# all_news = site_json.get("items")

# dict_news = {}
# # saved each news sepratly on db
# for news in all_news:
#     id = news["id"]
#     url = news["url"]
#     title = news["title"]
#     sumamry = news["summary"]
#     date_published = news["date_published"]
#     c.execute("""INSERT OR REPLACE INTO news VALUES(?,?,?,?,?)""",
#               (id, url, title, sumamry, date_published))
# conn.commit()

# c.execute("""SELECT * FROM news""")
# result = c.fetchall()
# print(result)
