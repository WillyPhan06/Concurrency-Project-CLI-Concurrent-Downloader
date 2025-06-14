import os
from datetime import datetime

class Logger:
    def __init__(self, log_path):
        self.log_path = log_path
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        with open(self.log_path, 'w') as f:
            f.write("Download Log\n")
            f.write("=" * 50 + "\n")

    def log(self, url, status, details=""):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{time}] {status.upper()} - {url} {details}\n"
        with open(self.log_path, 'a') as f:
            f.write(line)
