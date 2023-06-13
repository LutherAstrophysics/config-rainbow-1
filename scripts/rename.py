from pathlib import Path


# Kept inside run function to prevent from accidental execution
def run():
    folder_path = Path("F:/Summer 2012/October 3, 2012/m23")
    for file in folder_path.glob('*.fit'):
        old_name = file.name
        new_name = old_name.replace('dark', 'm23')
        new_path = folder_path / new_name
        file.rename(new_path) 

run()