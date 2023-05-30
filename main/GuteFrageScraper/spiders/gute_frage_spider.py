import scrapy

from GuteFrageScraper.XPathHelper import XPathHelper as XPath


def reprocess_text(data_dict: dict):
    text_list = data_dict["text"]
    # remove elements only containing white space chars
    text_list = [text.strip() for text in text_list if text.strip()]
    data_dict["text"] = " ".join(text_list)


def extract_data(question) -> dict:
    return {
        "author": XPath.rel_desc(question).div('ContentMeta-author').a().text().get(),
        "date": XPath.rel_desc(question).node('gf-relative-time').attribute('datetime').get(),
        "title": XPath.rel_desc(question).div('Question-title').text().get(),
        "text": XPath.rel_desc(question).div('ContentBody').skip.text().getall(),
        "has_image": XPath.rel_desc(question).div("ListingElement-image").bool(),
        "url": XPath.rel_desc(question).a('ListingElement-questionLink').href().get()
        }


class GuteFrageSpider(scrapy.Spider):
    name = "GuteFrage"
    base_url = "https://GuteFrage.net"
    start_urls = [f"{base_url}/wissen-wissenschaften"]
    
    # TODO: 
    # - save next_page as starting point for next scrape
    # - save last date to stop parsing there/ continue after last next_page
    def parse(self, response):
        for question in XPath.desc(response).node("gf-card-listing-inbox").div().build():
            data = extract_data(question)
            reprocess_text(data)
            # self.log(data)
            yield data

        next_page = XPath.desc(response).a("TabsPagination-nextLink").href().get
        self.log(f"Next Page is: {next_page}")
