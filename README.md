# Kript.id Latest News Scraper

This web application scrapes the five latest news articles from [kript.id](https://kript.id) and displays them in a simple frontend. The backend is built with Flask and deployed as a serverless function on Vercel.

## Features
- Scrapes the five latest news article links from kript.id
- Displays the results in the format:
  ```
  YYYY-MM-DD,
  1. [link1]
  2. [link2]
  3. [link3]
  4. [link4]
  5. [link5]
  ```
- Basic error handling for scraping and API failures

## Local Development
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Flask API:
   ```bash
   python api.py
   ```
3. Open `frontend.html` in your browser to view the frontend (you may need to adjust the API URL for local testing).

## Deployment on Vercel
1. Install [Vercel CLI](https://vercel.com/download):
   ```bash
   npm i -g vercel
   ```
2. Deploy:
   ```bash
   vercel
   ```
3. The API will be available at `/api/latest-news` and the frontend at `/frontend.html`.

## Notes
- The HTML selector in `api.py` may need adjustment if kript.id changes its layout.
- For production, consider adding caching or rate limiting to avoid overloading the target site. 