### Text Technology Project
Start scraping with
```
bash run.sh <data/filename.json>
```

fully scraped data of GuteFrage.net [Wissen/Wissenschaft] is stored in `data/full.json`
data from test runs is in `data/test*.json`

scraping spider is in `main/GuteFrageScraper/spiders/gute_frage_spieder.py`

script to fill database with scraped data is at `main/fill_database.py`

script to extract xml from database is at `main/query_db.py`

xml containing the filered question is at `data/output.full.xml`
xml containing a limited selection of 500 filtered questions is at `data/output.500.xml`

database is at `psql -h bergbussard -d ttws2021 -U ttws2021` using table `gutefrage`
