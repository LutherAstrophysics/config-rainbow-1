import sys
from pathlib import Path
from folders import get_nights_sorted


year = sys.argv[1]
year_folder = Path(f'G:/Raw Data/Summer {year}')

nights = get_nights_sorted(year_folder)

for night in nights: 
    night_path = str(night.absolute())
    night_path = night_path.replace("\\", "/")
    print(f"""
    [[input.nights]]
    path = "{night_path}"
    masterflat = "E:/Data Processing/Master Flats/{year}/{year}--_masterflat.fit"
    """)

    