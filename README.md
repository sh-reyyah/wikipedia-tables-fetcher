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
```

---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/sh-reyyah/wikipedia-tables-fetcher.git
   cd wikipedia-tables-fetcher
   ```

2. Run the application:
   ```bash
   python table_fetcher.py
   ```

3. Enter a valid Wikipedia URL in the GUI (e.g., `https://en.wikipedia.org/wiki/Python_(programming_language)`).

4. Click **Load Tables** to fetch data:
   - View all tables from the page in a new window.
   - Optionally, save tables as CSV files.

5. Fetch and save the introduction text from the page as a `.txt` file.

---

## Example

- **Input**: Wikipedia URL - `https://en.wikipedia.org/wiki/Artificial_intelligence`
- **Output**:
  - List of tables displayed in a new window.
  - Option to save tables as CSV files.
  - Introduction text saved as a `.txt` file.

---

## Project Structure

```
wikipedia-tables-fetcher/
├── table_fetcher.py     # Main application script
└── README.md            # Project documentation
```

---

## Troubleshooting

- Ensure the URL is a valid Wikipedia page starting with `https://en.wikipedia.org/wiki/`.
- If no tables or introduction are found, verify the page content.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- Wikipedia for the data source.

---

## Author

Developed by [Shreya Bharati](https://github.com/sh-reyyah).