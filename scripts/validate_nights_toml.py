from m23.processor.config_loader import validate_file
from pathlib import Path
import sys

def main():
    def on_success(*args):
        print("Looking good")
    
    if len(sys.argv) == 1:
        print("File name to validate not provided")
        return
    
    file = Path(sys.argv[1])
    if not file.exists():
        print(f"File: {file} doesn't exist")
        return 

    validate_file(file, on_success)


if __name__ == "__main__":
    main()