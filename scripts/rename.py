from pathlib import Path


# Kept inside run function to prevent from accidental execution
def run():
    folder_path = Path("E:\Data Processing\August 28, 2019\Flux Logs Combined\Four Pixel Radius")
    for file in folder_path.glob('*'):
        old_name = file.name
        new_name = old_name.replace('7.0_', '7.0-')
        new_path = folder_path / new_name
        file.rename(new_path) 

run()