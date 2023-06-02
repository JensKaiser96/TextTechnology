# Scrapy settings for GuteFrageScraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "GuteFrageScraper"

SPIDER_MODULES = ["GuteFrageScraper.spiders"]
NEWSPIDER_MODULE = "GuteFrageScraper.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "GuteFrageScraper"

FEEDS = {
    'data/full.json': {
        'format': 'json',
        'encoding': 'utf8',
        'overwrite': False,
        'append': True,
    }
}

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

RETRY_ENABLED = True
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 408]  # HTTP response codes to retry

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
