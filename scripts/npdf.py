# This program opens all normfactor charts for a year
# in a pdf. Just provide the year as a cmd line arg.

import os
from m23.constants import CHARTS_FOLDER_NAME
from PIL import Image 

import sys
from pathlib import Path
from folders import get_nights_sorted

charts_for_radius = "Four"

if len(sys.argv) > 1:
    year = sys.argv[1]
    year_folder = Path(f'E:/Data Processing/Python Processed/{year}')
else:
    year_folder = Path('E:/Data Processing/Python Processed/2015')

nights = get_nights_sorted(year_folder)

# Taken from
# https://stackoverflow.com/questions/27327513/create-pdf-from-a-list-of-images

images = []
for night in nights:
    charts_folder = night / CHARTS_FOLDER_NAME
    if len(list(charts_folder.glob('*'))) == 0:
        continue # Skip since no photos
    candidates = list(charts_folder.glob(f'*normfactor*{charts_for_radius}*.png'))
    c = sorted(candidates, key=lambda x: x.stat().st_mtime, reverse=True)[0]
    png = Image.open(c)
    png.load()
    bg = Image.new("RGB", png.size, (255, 255, 255))
    bg.paste(png, mask=png.split()[3])
    images.append(bg)

import random
r = random.randint(1, 2)
pdf_path = Path(f"E:\Data Processing\Config Files/tmp/{year_folder.name}_{r}.pdf")
if pdf_path.exists():
    pdf_path.unlink()

if len(images) == 0:
    print("No images found. Radius given:", charts_for_radius)
    os._exit(1)
elif len(images) == 1:
    images[0].save(pdf_path, "PDF", resolution=300.0, save_all=True)
else:
    images[0].save(pdf_path, "PDF", resolution=300.0, save_all=True, append_images=images[1:])

if len(images) > 0:
    print(f"Saved in {pdf_path}")
    os.startfile(pdf_path)
