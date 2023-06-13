from pathlib import Path


# Kept inside run function to prevent from accidental execution
def run():
    path = Path("C:/Data Processing/Config Files")
    path.rmdir()