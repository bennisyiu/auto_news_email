import requests
import os
from dotenv import load_dotenv


class NewsFeed:
    """Representing multiple news titles and their links.
    """

    base_url = "https://newsapi.org/v2/everything?"
    load_dotenv()
    API_KEY = os.getenv('APIKEY')

    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        # e.g. https://newsapi.org/v2/everything?qintitle=messi&from=2024-02-08&to=2024-02-09&language=en&apiKey=79907952d84e42fa849ec8fda8e0405d
        # get url
        url = self._build_url()

        # get articles
        articles = self._get_articles(url)

        # contruct news feed display structure
        email_body = ''
        for article in articles:
            email_body += article['title'] + '\n' + article['url'] + \
                '\n' + '-----------------------------------' + '\n'
        return email_body

    def _build_url(self):
        url = f"{self.base_url}" \
            f"qintitle={self.interest}&" \
            f"from={self.from_date}&" \
            f"to={self.to_date}&" \
            f"language={self.language}&" \
            f"apiKey={self.API_KEY}"
        return url

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        return content['articles']


if __name__ == "__main__":
    news_feed = NewsFeed(interest, from_date, to_date, language='en')
    print(news_feed.get())
