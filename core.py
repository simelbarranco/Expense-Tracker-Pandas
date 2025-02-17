import pandas as pd
import csv
from datetime import datetime

# Setting up a class that will contain the functions related to the CSV file.
class CSV:
    CSV_FILE = 'finance_data.csv'
    COLUMNS = ["date", "amount", "category", "description"]

    # This will have access to the class itself but it won't have access to its instance.
    @classmethod
    def initialize_csv(cls):
        # Initializing the csv file that will store the transactions, and creating it if it doesn't exist.
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMMS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        # Storing the new data entry into a python dictionary when using the CSV Writer, to write into the correct columns.
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        # Appending the entry to the end of the file.
        with open(cls.CSV_FILE, "a", newline="") as csvfile: # context manager: handles closing the file, cleans up memory.
            # This takes a dictionary and writes it into the specified csv file.
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully.")

CSV.initialize_csv()
CSV.add_entry("2025-01-01", 432.52, "Income", "Salary")