import sys
from folders import get_nights_sorted
from pathlib import Path

year = sys.argv[1]
year_folder = Path(f'E:/Data Processing/Python Processed/{year}')

for night in get_nights_sorted(year_folder): 
    night_path = str(night.absolute())
    night_path = night_path.replace("\\", "/")
    print(f'"{night_path}",')

    