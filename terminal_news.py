import requests
from bs4 import BeautifulSoup
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

def get_latest_news():
    try:
        url = 'https://kript.id/category/news/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article', class_='post')
        
        news_links = []
        for article in articles:
            heading = article.find(['h2', 'h3', 'h4'])
            if heading:
                a_tag = heading.find('a', href=True)
                if a_tag and a_tag['href'] and not a_tag['href'].startswith('/category/'):
                    news_links.append(a_tag['href'])
            if len(news_links) == 5:
                break
        return news_links

    except requests.RequestException as e:
        print(f"Error fetching news: {str(e)}")
        return []
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return []

@app.route('/api/latest-news')
def latest_news():
    news_links = get_latest_news()
    return jsonify({
        'fetched_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'news_links': news_links
    })

if __name__ == '__main__':
    app.run(debug=True, port=8000) 