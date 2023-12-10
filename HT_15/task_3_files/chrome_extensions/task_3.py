import subprocess

if __name__ == "__main__":
    subprocess.run(["scrapy", "crawl", "my_google_spider", "-O", "data.csv"])
