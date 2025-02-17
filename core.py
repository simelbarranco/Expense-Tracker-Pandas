import pandas as pd
import csv
from datetime import datetime

# Setting up a class that will contain the functions related to the CSV file.
class CSV:
    CSV_FILE = 'finance_data.csv'

    # This will have access to the class itself but it won't have access to its instance.
    @classmethod
    def initialize_csv(cls):
        # Initializing the csv file that will store the transactions, and creating it if it doesn't exist.
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["date", "amount", "category", "description"])