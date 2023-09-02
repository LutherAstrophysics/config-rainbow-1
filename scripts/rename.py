from pathlib import Path


# Kept inside run function to prevent from accidental execution
def run():
    folder_path = Path(r"G:\Raw Data\Summer 2005\FOO\July 22, 2005\Calibration Frames")
    for file in folder_path.glob('flat*'):
        old_name = file.name
        new_name = old_name.replace('2.50', '2.5-0')
        new_path = folder_path / new_name
        file.rename(new_path) 

run()