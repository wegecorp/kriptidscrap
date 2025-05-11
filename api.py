from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/latest-news', methods=['GET'])
def latest_news():
    try:
        url = 'https://kript.id/category/news/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all news articles on the page
        articles = soup.select('article')
        
        if not articles:
            return jsonify({
                'status': 'error',
                'message': 'No articles found',
                'data': []
            }), 404

        news_list = []
        for article in articles[:5]:  # Get latest 5 articles
            title_elem = article.select_one('h2.entry-title a')
            if not title_elem:
                continue
                
            title = title_elem.get_text(strip=True)
            link = title_elem['href']
            
            # Get the date if available
            date_elem = article.select_one('.entry-date')
            date = date_elem.get_text(strip=True) if date_elem else None
            
            # Get the excerpt if available
            excerpt_elem = article.select_one('.entry-content p')
            excerpt = excerpt_elem.get_text(strip=True) if excerpt_elem else None
            
            news_list.append({
                'title': title,
                'link': link,
                'date': date,
                'excerpt': excerpt
            })

        return jsonify({
            'status': 'success',
            'data': news_list,
            'timestamp': datetime.now().isoformat()
        })

    except requests.RequestException as e:
        return jsonify({
            'status': 'error',
            'message': 'Failed to fetch website',
            'error': str(e)
        }), 503
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': 'Internal server error',
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 