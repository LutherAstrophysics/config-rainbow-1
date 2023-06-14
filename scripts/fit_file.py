from pathlib import Path
from m23.utils import get_raw_images
from astropy.io import fits

year_folder = Path('H:/Raw Data/Summer 2013/')

for folder in year_folder.glob('*'):
    m23 = folder / 'm23'
    calibration = folder / 'Calibration Frames'
    if len(list(m23.glob('*'))) == 0: 
        print(m23)
    elif len(list(calibration.glob('*'))) == 0: 
        print(calibration)