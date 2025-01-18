scrapy startproject tutorial
scrapy crawl quotes
scrapy crawl quotes -o quotes.jsonl

scrapy crawl plants
scrapy crawl plants -o plants.jsonl
scrapy crawl plants -o ../data/plants_$(date +%Y-%m-%d).json
scrapy crawl plants -o ../data/plants_$(date +%Y-%m-%d_%H-%M-%S).json

scrapy shell "file:///Users/ilhamsj/github/ilhamsj/airflow-dags/tutorial/plants-indoor-plant.html"
response.css("title")
