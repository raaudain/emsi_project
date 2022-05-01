import scrapy
import json
from emsi_scraper.items import EmsiScraperItem
from scrapy.loader import ItemLoader


class JobsSpider(scrapy.Spider):
    name = "emsi"
    allowed_domains = ["api.lever.co"]
    start_urls = ["https://api.lever.co/v0/postings/economicmodeling?mode=json"]

    def parse(self, response):
        jobs = json.loads(response.body)

        for job in jobs:
            loader = ItemLoader(item = EmsiScraperItem())

            loader.add_value("job_id", job.get("id"))
            loader.add_value("job_title", job.get("text"))
            loader.add_value("job_description", job.get("descriptionPlain"))
            loader.add_value("additional_job_details", job.get("lists"))
            loader.add_value("location", job.get("categories").get("location"))
            loader.add_value("date_posted", job.get("createdAt"))
            loader.add_value("commitment", job.get("categories").get("commitment"))
            loader.add_value("department", job.get("categories").get("department"))
            loader.add_value("team", job.get("categories").get("team"))
            loader.add_value("job_posting_url", job.get("hostedUrl"))

            yield loader.load_item()
