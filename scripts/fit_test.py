from pathlib import Path
from m23.utils import get_raw_images
from astropy.io import fits


images = get_raw_images(Path('H:/Raw Data/Summer 2014/May 29, 2014/m23/'))

# for i in range(1, 5):
#     with fits.open(make_path(i)) as fd:
#         header = fd[0].header
#         data = fd[0].data

for index, im in enumerate(images):
    print("Running file", images[index])
    im.data()

# fits.getdata('H:/Raw Data/Summer 2014/May 29, 2014/m23/m23_7.0-765.fit')