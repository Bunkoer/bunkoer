import csv
import os
from datetime import datetime

def prompt_csv(header):
    return f"Here's a header from a csv file. Can you list only the columns that could contain Name, Surname, Email, Phone, Social Network,  in the header I provide to you .You'll need to return this list in python format without any further comment from you : {header}"

def read_csv_header(file_path):
    """
    Reads the header of a CSV file and returns it. Includes error handling for various scenarios.

    Args:
    file_path (str): The path to the CSV file.

    Returns:
    list: A list containing the header of the CSV file, or None if an error occurs.

    """
    
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"[ERROR] The file '{file_path}' does not exist.")
        return None

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader, None)

            if header is None:
                print("[ERROR] The csv file is empty")
                return None
            return header

    except Exception as e:
        print(f"[ERROR] An error occurred during the csv reading process : {e}")
        return None
    

def delete_columns_from_csv(file_path, columns_to_delete):
    """
    Deletes specified columns from a CSV file.

    Args:
    file_path (str): The path to the CSV file.
    columns_to_delete (list): A list of column names to be deleted.

    Returns:
    bool: True if the operation was successful, False otherwise.
    """
    
    output_file =  datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    try:
        # Read the CSV file and store data
        with open(file_path, mode='r', encoding='utf-8', newline='') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
            columns = reader.fieldnames

        # Check if columns to delete exist in the CSV
        if not all(col in columns for col in columns_to_delete):
            print("[ERROR] One or more columns to delete are not found in the CSV.")
            return False

        # Remove specified columns
        for row in data:
            for col in columns_to_delete:
                row.pop(col, None)

        # Write the modified data back to a new CSV file
        with open(output_file, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=[col for col in columns if col not in columns_to_delete])
            writer.writeheader()
            writer.writerows(data)

        return output_file
    except Exception as e:
        print(f"[ERROR] An error occurred during the delting clumns process : {e}")
        return False
