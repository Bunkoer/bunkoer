from .csv import csv_task
from .utils import gpt, utils
# from .csv_task import read_csv_header,prompt_csv
# from .utils import extract_string_with_brackets,string_to_list

import os



def secure_csv(file_path, confimation=True, delete_src=False):
        
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
        prompt = csv_task.prompt_csv(header)

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
        
        if confimation == False:    
            delete_columns_from_csv(file_path, bad_clumn)    
        
        if delete_src == True:
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                print(f"[ERROR] Source file : {file_path} can be deleted. ")    

    
def secure_json(file_path):
    print (f"TEst csv : {file_path}")
