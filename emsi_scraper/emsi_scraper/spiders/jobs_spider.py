import scrapy
import json


class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["api.lever.co"]
    start_urls = ["https://api.lever.co/v0/postings/economicmodeling?mode=json"]

    def parse(self, response):
        data = json.loads(response.body)

        for d in data:
            job_id = d["id"]
            job_title = d["text"]
            job_description = " ".join(d["descriptionPlain"].split())
            location = d["categories"]["location"] if "location" in d["categories"] else None
            date_posted = d["createdAt"]
            commitment = d["categories"]["commitment"] if "commitment" in d["categories"] else None
            department = d["categories"]["department"] if "department" in d["categories"] else None
            team = d["categories"]["team"] if "team" in d["categories"] else None
            job_url = d["hostedUrl"]

            yield {
                "id": job_id,
                "job_title": job_title,
                "job_description": job_description,
                "location": location,
                "date_posted": date_posted,
                "department": department,
                "team": team,
                "commitment": commitment,
                "job_posting_url": job_url
            }
