import schedule
import time
import os

def run_main_py():
    # Replace the file path below with the actual file path of your main.py script
    file_path = 'main.py'
    os.system(f'python {file_path}')

# Scheduling the main.py script to run every hour
schedule.every().hour.do(run_main_py)

while True:
    # Run the scheduled tasks
    schedule.run_pending()
    time.sleep(3600)
