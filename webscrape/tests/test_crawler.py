# webscrape/tests/test_crawler.py
import pytest
from selenium.webdriver.common.by import By
from crawler import Crawler


@pytest.fixture(scope="module")
def crawler():
    crawler = Crawler()
    yield crawler
    crawler.quit()


def test_fetch(crawler):
    url = "https://www.muji.us/collections/"
    crawler.fetch(url)
    assert "Collections — MUJI USA" == crawler.driver.title


def test_parse_collections(crawler):
    results = crawler.parse_collections()
    assert all(results) == True


def test_parse_products_per_collection(crawler):
    urls = [
        "https://www.muji.us/collections/apparel",
        "https://www.muji.us/collections/new-arrivals"
    ]
    for u in urls:
        crawler.fetch(u)
        results = crawler.parse_products_per_collection()
        assert all(results) == True