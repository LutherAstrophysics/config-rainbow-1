import sys
from pathlib import Path
from folders import get_nights_sorted


year = sys.argv[1]
year_folder = Path(f'E:/Data Processing/Python Processed/{year}/')

nights = get_nights_sorted(year_folder)

for night in nights: 
    logger = list(night.glob("*Processing-log*"))
    if len(logger) == 0 :
        continue
    logger = logger[0]
    with open(logger, 'r') as fd:
        lines = fd.readlines()
        last_line = "".join(lines[-2:])
        if "Completed generating sky background file" in last_line:
            print(night)
    