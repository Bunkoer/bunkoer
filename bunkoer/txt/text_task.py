from langchain_experimental.data_anonymizer import PresidioAnonymizer

def anonimize_txt(text):
    anonymizer = PresidioAnonymizer()
    safe_text= anonymizer.anonymize(text)
    return safe_text

def anonimize_txt_file(file_path):
    if not file_path.endswith('.txt'):
        print("Error: The file does not have a .txt extension.")
        return None

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
            safe_data = anonimize_txt(data)
            with open(file_path, 'w', encoding='utf-8') as file:
            
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except PermissionError:
        print(f"Permission denied: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None
