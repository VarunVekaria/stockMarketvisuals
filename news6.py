from pprint import pprint
from newsapi import NewsApiClient
from datetime import datetime, timedelta
import json

# Get your API key from NewsAPI
newsapi = NewsApiClient(api_key=api_key)

# Calculate the date 30 days ago
one_month_ago = datetime.now() - timedelta(days=30)

# Format the date for News API
from_date = one_month_ago.strftime('%Y-%m-%d')

# Fetch the first page to get totalResults
first_page = newsapi.get_everything(
    q='msft',  # Search for Microsoft-related articles
    from_param=from_date,
    to=datetime.now().strftime('%Y-%m-%d'),
    language='en',
    sort_by='relevancy',  # or 'popularity'
    page=1
)

# Get the total number of results and calculate pages
total_results = first_page.get('totalResults', 0)
page_size = 20  # NewsAPI returns 20 results per page by default
total_pages = (total_results + page_size - 1) // page_size  # Round up to include partial pages

print(f"Total Results: {total_results}")
print(f"Total Pages: {total_pages}")

# Fetch all articles (up to the total pages)
all_articles = []
for page in range(1, min(total_pages, 6) + 1):  # Iterate through pages, up to a max of 6
    articles = newsapi.get_everything(
        q='msft',
        from_param=from_date,
        to=datetime.now().strftime('%Y-%m-%d'),
        language='en',
        sort_by='relevancy',
        page=page
    )
    all_articles.extend(articles['articles'])

# Post-filter articles for relevant topics
relevant_articles = []
keywords = ['business', 'technology', 'science']  # Keywords to match
for article in all_articles:
    title = article.get("title", "").lower()
    description = article.get("description", "").lower()
    if any(keyword in title or keyword in description for keyword in keywords):
        relevant_articles.append({
            "title": article.get("title"),
            "publishedAt": article.get("publishedAt"),
            "url": article.get("url")
        })

# Save to a JSON file
with open("filtered_articles2.json", "w", encoding="utf-8") as f:
    json.dump(relevant_articles, f, indent=4)

print(f"Filtered articles saved to filtered_articles.json.")
