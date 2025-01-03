# Wikipedia Tables Fetcher

A Python-based GUI application for fetching and displaying tables and introductory text from Wikipedia pages. This tool leverages web scraping with Beautiful Soup and Pandas to extract structured data and provides an intuitive interface for users to interact with.

---

## Features

- **Fetch Tables**: Extracts all tables from a given Wikipedia URL and displays them in a user-friendly format.
- **Save Tables**: Provides an option to save the fetched tables as CSV files.
- **Fetch Introduction**: Retrieves the introductory paragraphs of the Wikipedia page.
- **Save Introduction**: Allows saving the introduction as a `.txt` file.
- **Interactive GUI**: Built using `Tkinter` for a simple and easy-to-use interface.

---

## Prerequisites

Ensure you have the following installed:

- Python 3.7 or later
- Required Python libraries:
  - `pandas`
  - `tkinter` (comes pre-installed with Python)
  - `requests`
  - `beautifulsoup4`

Install the required libraries using:
```bash
pip install pandas requests beautifulsoup4
