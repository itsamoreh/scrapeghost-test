from scrapeghost import SchemaScraper
from pprint import pprint

url = "https://www.ilga.gov/house/rep.asp?MemberID=3071"
scrape_legislators = SchemaScraper(
  schema={
      "name": "string",
      "url": "url",
      "district": "string",
      "party": "string",
      "photo_url": "url",
      "offices": [{"name": "string", "address": "string", "phone": "string"}],
  }
)

response = scrape_legislators(url)
pprint(response.data)
print(f"Total Cost: ${response.total_cost:.3f}")
