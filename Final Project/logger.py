import os
from datetime import datetime


class SimpleLogger:
    
    def __init__(self, filename: str = "app.log") -> None:
       
        self.__filename = filename

    def log(self, message: str) -> None:
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] {message}\n"
        try:
            with open(self.__filename, "a", encoding="utf-8") as f:
                f.write(line)
        except OSError as e:
            print(f"Logging error: {e}")
