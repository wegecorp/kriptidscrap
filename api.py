from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(__name__)

@app.route('/api/latest-news', methods=['GET'])
def latest_news():
    try:
        url = 'https://kript.id/'
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the latest 5 news article links (adjust selector as needed)
        articles = soup.select('article h2 a')[:5]
        links = [a['href'] if a['href'].startswith('http') else url + a['href'].lstrip('/') for a in articles]

        today = datetime.now().strftime('%Y-%m-%d')
        formatted = f"{today},\n" + '\n'.join([f"{i+1}. [{link}]" for i, link in enumerate(links)])
        return jsonify({'result': formatted})
    except Exception as e:
        return jsonify({'error': 'Failed to scrape news', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 