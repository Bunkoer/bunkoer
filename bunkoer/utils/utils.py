import os 

def read_blacklist_line(file_path):
    """Reads the first line of a file and returns it as a string."""
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
    return first_line

def string_to_list(string):
    """
    Converts a string representation of a list to an actual list.

    Args:
    string (str): The string representation of a list.

    Returns:
    list: The converted list, or None if an error occurs.
    """
    import ast

    try:
        # Attempt to convert string to list using ast.literal_eval
        return ast.literal_eval(string)
    except (ValueError, SyntaxError):
        print("[ERROR] The string is not a valid list representation.")
        return None
    
def extract_string_with_brackets(text):
    """
    Extracts and returns the string including the first pair of square brackets in the given text.
    If no brackets are found or the text is not properly formatted, appropriate error handling is implemented.

    Args:
    text (str): The text from which to extract the string.

    Returns:
    str: The extracted string including square brackets, or None if an error occurs.
    """
    if not isinstance(text, str):
        print("[ERROR] Input is not a string.")
        return None

    try:
        start = text.index('[')
        end = text.index(']', start) + 1
        return text[start:end]
    except ValueError:
        print("[ERROR] No complete pair of square brackets found in the text.")
        return None
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred during the string extraction with brackets: {e}")
        return None

def delete_file(filepath):
    """
    Delete a file at the given filepath.

    Parameters:
    filepath (str): The path to the file to be deleted.
    """
    try:
        os.remove(filepath)
        print(f"File '{filepath}' has been successfully deleted.")
    except FileNotFoundError:
        print(f"File '{filepath}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
