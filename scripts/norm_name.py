import sys
from pathlib import Path
from folders import get_nights_sorted

if len(sys.argv) > 1:
    year = sys.argv[1]
    year_folder = Path(f'E:/Data Processing/Python Processed/{year}')
else:
    year_folder = Path('E:/Data Processing/Python Processed/2015')

nights = get_nights_sorted(year_folder)

for night in nights: 
    night_path = str(night.absolute())
    night_path = night_path.replace("\\", "/")
    print(f"""
    [[input.nights]]
    path = "{night_path}"
    first_logfile_number = 
    last_logfile_number = 
    """)

    