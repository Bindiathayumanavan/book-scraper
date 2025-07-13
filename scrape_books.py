import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Set the URL
url = 'https://books.toscrape.com/catalogue/page-1.html'

# Step 2: Make a request to the website
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Find all book containers
books = soup.find_all('article', class_='product_pod')

# Step 4: Extract the data
titles = []
prices = []
stocks = []

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    stock = book.find('p', class_='instock availability').text.strip()

    titles.append(title)
    prices.append(price)
    stocks.append(stock)

# Step 5: Save the data to CSV
df = pd.DataFrame({
    'Title': titles,
    'Price': prices,
    'Availability': stocks
})

df.to_csv('books_data.csv', index=False)
print("✅ Scraping complete. Data saved to 'books_data.csv'")
