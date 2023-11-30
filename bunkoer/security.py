from .csv import csv_task
from .utils import gpt, utils
import os



def SecureFile(file_path, delete_src=False):
        
    model_name="gpt-4-1106-preview"
    temperature= 1
    list_of_valid_file = ('.csv','.json', '.yaml' , '.yml')

    if not file_path.endswith(list_of_valid_file):
        print(f"[ERROR] The file '{file_path}' is not a csv file .")

    if file_path.endswith(".csv"):
        header = csv_task.read_csv_header(file_path)
        if header == None:
            print("[ERROR] during the csv anonymization ")
            exit(1)

        if os.path.isfile("./blacklist"):
            blacklist = utils.read_blacklist_line("./blacklist")
        else:
            print("f[ERROR] No black list file find")
        prompt = csv_task.prompt_csv(header, blacklist)

        bad_clumn =  gpt.send_gpt_resquest(prompt, model_name, temperature, max_tokens=None)
        if bad_clumn == None:
            print("[ERROR] during the csv anonymization ")
            exit(1)

        bad_clumn = utils.extract_string_with_brackets(bad_clumn)
        if bad_clumn == None:
            print("[ERROR] during the csv anonymization ")
            exit(1)

        bad_clumn = utils.string_to_list(bad_clumn)
        if bad_clumn == None:
            print("[ERROR] during the csv anonymization ")
            exit(1)
                
        if delete_src == True:
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                print(f"[ERROR] Source file : {file_path} can be deleted. ")    

    
