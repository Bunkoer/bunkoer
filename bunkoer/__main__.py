import os
import subprocess
from utils.utils import check_api_key

def run_streamlit():
    check_api_key()
    os.chdir(os.path.dirname(__file__))  # Change to the directory of your Streamlit app
    subprocess.run(["python3","-m","streamlit", "run", "main_ui.py"])

if __name__ == '__main__':
    run_streamlit()
