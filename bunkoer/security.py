from .format import csv_task, pdf_task, text_task
from .utils import gpt, utils
import os

class FileProcessingError(Exception):
    pass

def SecureFile(file_path, mode="default", delete_src=False):
    model_name = "gpt-4-1106-preview"
    temperature = 1
    list_of_valid_file = ('.csv', '.txt', '.pdf')

    if not file_path.endswith(list_of_valid_file):
        raise FileProcessingError(f"The file '{file_path}' is not a valid file type.")

    if file_path.endswith(".pdf"):
        content = pdf_task.extract_text_from_pdf(file_path)
        secure_content = text_task.anonymize_text(content)
        anonimized_data = pdf_task.create_pdf_with_text(secure_content)
        return anonimized_data

    if file_path.endswith(".csv"):
        header = csv_task.read_csv_header(file_path)
        if header is None:
            raise FileProcessingError("Error during the CSV anonymization - reading header failed.")

        blacklist = "Name, Surname, Phone, Social Network Profile, Bank Account, IBAN, IP Adress, Passport Number, Precise address, Email Addresses, Social Security Numbers, ID Card Numbers, User Name, Pseudonym"
        prompt = ""
        if mode == "default":
            prompt = csv_task.prompt_csv(header, blacklist)
        elif mode == "contextual":
            prompt = csv_task.prompt_csv_contextual(header)
        else:
            raise ValueError(f"Error the mode you select : {mode} doesn't exist. PLease use a valid mode : safe, contextual")

        bad_column = gpt.send_gpt_request(prompt, model_name, temperature, max_tokens=None)
        if bad_column is None:
            raise FileProcessingError("Error during the CSV anonymization - GPT request failed.")

        bad_column = utils.extract_string_with_brackets(bad_column)
        if bad_column is None:
            raise FileProcessingError("Error during the CSV anonymization - extracting string failed.")

        bad_column = utils.string_to_list(bad_column)
        if bad_column is None:
            raise FileProcessingError("Error during the CSV anonymization - converting string to list failed.")

        if delete_src:
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                raise FileProcessingError(f"Source file: {file_path} cannot be deleted.")
        
        anonimized_data = csv_task.delete_columns_from_csv(file_path, bad_column)
        return anonimized_data
