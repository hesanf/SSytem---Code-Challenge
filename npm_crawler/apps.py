# import requests
# from bs4 import BeautifulSoup
# import json
# import sqlite3

# # connect/create db for saving scraped data
# conn = sqlite3.connect("scraped_data.db")
# c = conn.cursor()
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
#     sumamry = news["sumamry"]
#     date_published = news["date_published"]
#     c.execute("""INSERT INTO news VALUES(?,?,?,?,?)""",
#               (id, url, title, summary, date_published))
# conn.commit()
# # select last 5 record in db to show
# c.execute('''SELECT * FROM (
#                             SELECT * FROM news ORDER BY id DESC LIMIT 5)
#                             ORDER BY id ASC''')
# results = c.fetchall()
