from pathlib import Path


# Kept inside run function to prevent from accidental execution
def run(dry=True):
    folder_path = Path(r"H:\Raw Data\Summer 2012\July 11, 2012\Calibration Frames")
    for file in folder_path.glob('m23*'):
        old_name = file.name
        new_name = old_name.replace('m23', 'flat')
        new_path = folder_path / new_name
        if dry:
            print("Old:", old_name)
            print("New:", new_name, end="\n"*2)
        else:
            file.rename(new_path) 

# Set this to true if you want to rename
# Setting this to false will merely show you what the
# renaming looks like.
DESTRUCTIVE_RUN=False

run(dry=not DESTRUCTIVE_RUN)