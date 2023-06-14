import os
from pathlib import Path
from datetime import datetime
from m23.constants import OUTPUT_NIGHT_FOLDER_NAME_DATE_FORMAT

def get_nights_sorted(year_folder : Path | str):
    if not isinstance(year_folder, Path):
        year_folder = Path(year_folder)

    if not year_folder.exists() or not year_folder.is_dir():
        print(f"Folder {year_folder} doesn't exist")
        os._exit(1)

    nights = []
    for night in year_folder.glob('*'): 
        if night.is_dir():
            nights.append(night)

    nights.sort(key=lambda x : datetime.strptime(x.name, OUTPUT_NIGHT_FOLDER_NAME_DATE_FORMAT).toordinal())
    return nights
