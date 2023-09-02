from folders import get_nights_sorted
from pathlib import Path

year_folder = Path('E:/Data Processing/Python Processed/2003')

for night in get_nights_sorted(year_folder): 
    night_path = str(night.absolute())
    night_path = night_path.replace("\\", "/")
    print(f'"{night_path}",')

    