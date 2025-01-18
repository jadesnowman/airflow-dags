scrapy startproject tutorial
scrapy crawl quotes
scrapy crawl quotes -o quotes.jsonl

scrapy crawl plants
scrapy crawl plants -o plants.jsonl
scrapy crawl plants -o ../data/plants_$(date +%Y-%m-%d).json
scrapy crawl plants -o ../data/plants_$(date +%Y-%m-%d_%H-%M-%S).json

scrapy shell "https://quotes.toscrape.com/page/1/"
scrapy shell "https://bloomscape.com/shop/shop-all-plants/"

response.css("title")
response.css("title::text").get()
