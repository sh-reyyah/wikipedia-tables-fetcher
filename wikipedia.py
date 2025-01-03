import pandas as pd
import ssl
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import requests
from bs4 import BeautifulSoup

ssl._create_default_https_context = ssl._create_unverified_context

# Function to fetch tables and titles from the given URL
def fetch_tables(url):
    try:
        tables = pd.read_html(url)
        if not tables:
            raise ValueError("No tables found on this page.")
        return tables
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch tables from URL: {str(e)}")
        return []

# Function to fetch the introduction text from the Wikipedia URL
def fetch_introduction(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the first paragraph in the main content section of the page
        content = soup.find('div', {'class': 'mw-parser-output'})
        if not content:
            raise ValueError("Main content not found.")
        
        intro_paragraphs = content.find_all('p', recursive=False)
        
        # Get the first few paragraphs of text to form the introduction
        introduction = ""
        for para in intro_paragraphs:
            if para.get_text(strip=True):  # Skip empty paragraphs
                introduction += para.get_text(strip=True) + "\n"
        
        if not introduction:
            raise ValueError("Introduction not found.")
        
        return introduction.strip()  # Return cleaned introduction text
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch introduction: {str(e)}")
        return ""

# Function to save the CSV files
def save_csv(table, filename):
    try:
        file_path = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV Files', '*.csv')])
        if file_path:
            table.to_csv(file_path, index=False)
            messagebox.showinfo('Success', f'{filename} saved successfully!')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file: {str(e)}")

# Function to save the introduction text to a .txt file
def save_introduction(introduction, title):
    try:
        file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt')])
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(introduction)
            messagebox.showinfo('Success', f'Introduction for {title} saved successfully!')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save introduction: {str(e)}")

# Function to display data in a new window with title
def show_table(table, title):
    new_window = tk.Toplevel()
    new_window.title("Table Data")

    # Create and display the table title
    title_label = tk.Label(new_window, text=f"Table Title: {title}", font=("Arial", 14, "bold"))
    title_label.pack(pady=(10, 5))

    # Create a Text widget to display the table data
    text_area = tk.Text(new_window, wrap=tk.WORD, width=100, height=20)
    text_area.insert(tk.END, table.to_string(index=False))  # Display without index to make it cleaner
    text_area.pack(padx=20, pady=20)

    # Add a Scrollbar to the Text widget
    scroll_bar = tk.Scrollbar(new_window, command=text_area.yview)
    scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
    text_area.config(yscrollcommand=scroll_bar.set)

    # Create a save button with the table title as the button text
    button_save = tk.Button(new_window, text=f"Save {title}", command=lambda table=table, title=title: save_csv(table, title))
    button_save.pack(pady=10)

# Function to handle the GUI actions
def create_gui():
    root = tk.Tk()
    root.title("Wikipedia Tables Fetcher")

    # Set the window size and add padding
    root.geometry("600x400")
    root.config(padx=20, pady=20)

    # Add a header label
    header_label = tk.Label(root, text="Fetch Tables from Wikipedia", font=("Arial", 16, "bold"))
    header_label.pack(pady=(0, 10))

    # Label for URL input
    label_url = tk.Label(root, text="Enter Wikipedia URL:", font=("Arial", 12))
    label_url.pack(pady=5)

    # Entry field for URL input
    url_entry = tk.Entry(root, width=50, font=("Arial", 12))
    url_entry.pack(pady=10)

    # Function to load and display the tables from the given URL
    def load_and_display():
        url = url_entry.get()
        if not url.startswith('https://en.wikipedia.org/wiki/'):
            messagebox.showwarning("Invalid URL", "Please enter a valid Wikipedia URL.")
            return
        
        # Show loading message while fetching tables and introduction
        loading_label = tk.Label(root, text="Fetching tables... Please wait.", font=("Arial", 12), fg="blue")
        loading_label.pack(pady=10)
        root.update_idletasks()  # Update the UI before long-running task
        
        # Fetch the introduction text
        introduction = fetch_introduction(url)

        # If an introduction was fetched, give an option to save it
        if introduction:
            button_save_intro = tk.Button(root, text="Save Introduction as TXT", command=lambda: save_introduction(introduction, url.split('/')[-1]))
            button_save_intro.pack(pady=5)

        # Fetch tables
        tables = fetch_tables(url)

        # Remove loading message
        loading_label.pack_forget()

        if tables:
            # Create a new window to list the tables
            list_window = tk.Toplevel()
            list_window.title("Available Tables")

            # Label for listing the tables
            list_label = tk.Label(list_window, text="Click on a table to view:", font=("Arial", 14, "bold"))
            list_label.pack(pady=10)

            # Create a Frame to hold the table buttons in a grid
            frame = tk.Frame(list_window)
            frame.pack(pady=20)

            # Arrange buttons in a grid layout, two buttons per row
            for i, table in enumerate(tables):
                # Use "Table 1", "Table 2", etc. as titles
                title = f"Table {i + 1}"

                # Create a button for each table
                button_table = tk.Button(frame, text=title, command=lambda table=table, title=title: show_table(table, title))
                button_table.grid(row=i // 2, column=i % 2, padx=10, pady=5)  # Place buttons in two columns

    # Button to fetch and display tables
    button_load = tk.Button(root, text="Load Tables", font=("Arial", 12), bg="lightblue", command=load_and_display)
    button_load.pack(pady=20)

    # Start the GUI event loop
    root.mainloop()

# Run the GUI application
create_gui()
