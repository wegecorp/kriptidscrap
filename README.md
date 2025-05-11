# Kript.id News Scraper

A web application that scrapes and displays the latest cryptocurrency news from Kript.id.

## Features

- Real-time news scraping from Kript.id
- Modern, responsive UI using Tailwind CSS
- Auto-refresh every 5 minutes
- RESTful API endpoint for news data

## Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd kript-news-scraper
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Start the Flask server:
```bash
python api.py
```

4. Open `index.html` in your web browser or serve it using a local server.

## API Endpoints

- `GET /api/latest-news`: Returns the latest 5 news articles from Kript.id

## Technologies Used

- Backend:
  - Python
  - Flask
  - BeautifulSoup4
  - Requests

- Frontend:
  - HTML5
  - JavaScript
  - Tailwind CSS

## License

MIT License 