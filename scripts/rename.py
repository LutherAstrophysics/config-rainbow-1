from pathlib import Path


# Kept inside run function to prevent from accidental execution
def run():
    folder_path = Path("H:\Raw Data\Summer 2018\July 8, 2018\Calibration Frames")
    for file in folder_path.glob('*.fit'):
        old_name = file.name
        new_name = old_name.replace('dsrk', 'dark')
        new_path = folder_path / new_name
        file.rename(new_path) 

run()