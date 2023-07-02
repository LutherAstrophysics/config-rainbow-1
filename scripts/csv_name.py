from pathlib import Path

year_folder = Path('F:/Python_Processed/2021')

for night in year_folder.glob('*'): 
    night_path = str(night.absolute())
    night_path = night_path.replace("\\", "/")
    print(f'"{night_path}",')

    