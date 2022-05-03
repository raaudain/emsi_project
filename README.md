# Esmi Burning Glass Project

### Assignment

Scrape Emsi BG's open job positions: [https://www.economicmodeling.com/open-positions/](https://www.economicmodeling.com/open-positions/)

The scraped data should be in a github repo and shared with us prior to doing a code review. The data should be collected and fielded as having at least job title, job description, and location, but should also contain any other relevant field you find valuable. 

### Tools Used For Assignment

- Python 3.10
- Scrapy 2.6
- Firefox DevTools

### My Experience Completing This Project

Since I already have experience scraping websites for job postings, finding the JSON file containing the jobs data was no issue.  

This is my first time using Scrapy to complete a project.  I decided to use Scrapy because it's the preferred framework for Emsi BG's data engineering team.  I spent a lot of time going through Scrapy's documentation, reading articles, and watching videos to completing this assignment.

By the time I was done, I understood why Scrapy is preferred over other scraping tools.  I wrote less code than I would have with BeautifulSoup or Selenium, and Scrapy's Item Loaders add more scalability.

### About My Code

- Data was cleaned using Scrapy's Item Loaders input processor MapCompose.
- Changed settings so that outputted JSON files are indented.
- To avoid Unicode issues, `emsi_jobs.json` uses numeric encoding.
- Code is formatted to follow the PEP 8 style guide.