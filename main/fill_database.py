import json
import psycopg2

with open('main/data/full.json', 'r') as json_file:
    data = json.load(json_file)

conn = psycopg2.connect(database="ttws2021", user="ttws2021", password="acid", host="bergbussard")
cur = conn.cursor()

for page in data:
    page_url = ["url"]
    for record in page["questions"]:
        url = record['url']
        title = record['title']
        text = record['text']
        has_image = record['has_image']
        author = record['author']
        date = record['date']
        if not url:
            continue
        insert_query = "INSERT INTO gutefrage (url, title, text, has_image, author, date, page_url) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cur.execute(insert_query, (url, title, text, str(has_image), author, date, page_url))

conn.commit()
conn.close()
