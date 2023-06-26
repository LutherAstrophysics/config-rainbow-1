import sys
from pathlib import Path
from folders import get_nights_sorted
import datetime


year = sys.argv[1]
year_folder = Path(f'E:/Data Processing/Python Processed/{year}/')

nights = get_nights_sorted(year_folder)
loggers = []

for night in nights: 
    logger = list(night.glob("*Processing-log*"))
    if len(logger) == 0 :
        continue
    logger = logger[0]
    loggers.append(logger)

loggers_sorted = sorted(loggers, key=lambda x: x.stat().st_mtime)
for l in loggers_sorted:
    print(l, datetime.datetime.fromtimestamp(l.stat().st_mtime))