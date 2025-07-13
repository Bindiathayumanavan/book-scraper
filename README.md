#  Book Scraper

A simple Python project to extract book data (title, price, and availability) from [books.toscrape.com](https://books.toscrape.com) using web scraping techniques.

This project was completed as part of an internship task to demonstrate practical skills in web scraping, data extraction, and data handling using Python.

---

##  Features

- Scrapes:
  - Book Titles
  - Prices
  - Availability Status
- Exports scraped data to:
  - `CSV` file (`books_data.csv`)
  - `Excel` file (`books_data.xlsx`) *(if included)*
- Clean and readable code using:
  - `requests`
  - `BeautifulSoup`
  - `pandas`

---

##  Tech Stack

| Technology   | Purpose                     |
|--------------|-----------------------------|
| Python       | Main programming language   |
| Requests     | Fetch HTML from webpage     |
| BeautifulSoup| Parse HTML content          |
| pandas       | Store and export data       |

---

##  Files Included

| File               | Description                              |
|--------------------|------------------------------------------|
| `scrape_books.py`  | Python script to scrape book data        |
| `books_data.csv`   | Scraped output in CSV format             |
| `books_data.xlsx`  | (Optional) Output in Excel format        |

---

##  How to Run

Make sure Python is installed, then run:

```bash
python scrape_books.py
