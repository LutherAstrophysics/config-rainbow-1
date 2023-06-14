from pathlib import Path

year_folder = Path('E:/Data Processing/Python Processed/2014')

for night in year_folder.glob('*'): 
    night_path = str(night.absolute())
    night_path = night_path.replace("\\", "/")
    print(f'"{night_path}",')