import scrapy

class MySpider(scrapy.Spider):
    name = "scrapy_crawler"  # Spider name

    # Starting URLs for the spider (adjust as needed)
    start_urls = ["https://quotes.toscrape.com/"]

    # Maximum number of pages to crawl (adjust the limit)
    max_allowed_pages = 500

    # Maximum depth to follow links (adjust the limit)
    max_allowed_depth = 10

    # Internal variable to keep track of the current page count
    page_count = 0

    def parse(self, response):
        """
        Parse method to extract data from the response.
        """
        # Check if the page limit is reached
        if self.page_count >= self.max_allowed_pages:
            return
        # (Replace with specific logic for data extraction and saving)
        filename = f"page_{self.page_count}.html"  # Example filename format
        with open(filename, "wb") as f:
            f.write(response.body)

        self.page_count += 1

        # Follow links within the page (limited by depth)
        # Access depth from response.meta
        if response.meta.get('depth') < self.max_allowed_depth:
            # Iterate over links on the page and follow them if they are relative URLs
            for next_page in response.css("a::attr(href)").getall():
                if next_page.startswith("/"):
                    yield response.follow(next_page, callback=self.parse, meta={'depth': response.meta.get('depth', 0) + 1})
