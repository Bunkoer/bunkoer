from .csv import csv_task
from .utils import gpt, utils
import os

class FileProcessingError(Exception):
    pass

def SecureFile(file_path, delete_src=False):
    model_name = "gpt-4-1106-preview"
    temperature = 1
    list_of_valid_file = ('.csv', '.json', '.yaml', '.yml')

    if not file_path.endswith(list_of_valid_file):
        raise FileProcessingError(f"The file '{file_path}' is not a valid file type.")

    if file_path.endswith(".csv"):
        header = csv_task.read_csv_header(file_path)
        if header is None:
            raise FileProcessingError("Error during the CSV anonymization - reading header failed.")

        prompt = ""
        blacklist_file = os.path.join(os.path.dirname(__file__), "blacklist")

        if os.path.isfile(blacklist_file):
            blacklist = utils.read_blacklist_line(blacklist_file)
            prompt = csv_task.prompt_csv(header, blacklist)
        else:
            raise FileProcessingError("No blacklist file found.")

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

