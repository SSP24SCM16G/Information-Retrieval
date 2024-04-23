import scrapy
import json
import os

class CustomSpider(scrapy.Spider):
    name = "custom"

    # Seed URL for starting the crawling process
    start_urls = ["https://www.wikihow.com/Main-Page"]

    # Maximum number of iterations to crawl (adjust as needed)
    max_iterations = 200

    # Maximum depth to follow links (adjust as needed)
    max_links_depth = 2

    # Current iteration count (internal variable)
    current_iteration = 1

    def parse(self, response):
        """
        Parse method for extracting data from each webpage response.
        :param response: The response object containing the webpage content
        """
        # Check if the maximum iteration limit is reached
        if self.current_iteration > self.max_iterations:
            return

        # Dictionary to store the extracted page data
        page_data = {
            "link": response.url,
            "article": response.css('h1>a::text').get(),
            "intro": str(response.css('div.mf-section-0>p::text').get()).replace("\n", ""),
            "points": []
        }

        # Extract data for each section on the webpage
        for section in response.css("div.section.steps"):
            point = {
                "name": str(section.css('h3>span.mw-headline::text').get()).replace("\n", ""),
                "steps": []
            }

            # Extract data for each step within a section
            for points in section.css("div.section_text>ol>li"):
                step = {
                    "step": str(points.css('li>div.step_num::text').get()).replace("\n", ""),
                    "title": str.join("", points.css('li>div.step>b::text').getall()).replace("\n", ""),
                    "subtitle": str.join("", points.css('li>div.step::text').getall()).replace("\n", ""),
                    "sub-points": []
                }

                # Extract sub-points for each step
                for subPoint in points.css('li>div.step>ul>li'):
                    step["sub-points"].append(str.join("", subPoint.css('li::text').getall()).replace('\n', ''))
                    point["steps"].append(step)

                page_data["points"].append(point)

        # Save the parsed page data to a JSON file
        if page_data["article"] is not None:
            filename = f"IR_Project/crawler/data/page_{self.current_iteration}.json"

            with open(filename, "w", encoding="ISO-8859-1") as f:
                json.dump(page_data, f, ensure_ascii=False, indent=4)

            self.current_iteration += 1

        # Follow links within the page (limited by depth)
        if response.meta.get('depth') < self.max_links_depth:
            for next_page in response.css("a::attr(href)").getall():
                # Filter internal wiki links (avoid disambiguation pages)
                if next_page.startswith("/Quizzes") or next_page.startswith("/Course"):
                    continue
                elif next_page.startswith('https://') or next_page.startswith('http://'):
                    continue
                elif next_page.startswith('/wikiHow'):
                    continue
                elif next_page.__contains__('/Category:'):
                    continue
                yield response.follow(next_page, callback=self.parse, meta={'depth': response.meta.get('depth', 0) + 1})
