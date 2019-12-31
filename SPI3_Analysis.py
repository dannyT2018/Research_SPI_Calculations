import h5py
import numpy as np
import csv
from climate_indices import indices, compute
import time

start = time.time()

filename = 'C:\\Users\\Dannybaze\\Desktop\\india_prcp_merged.h5'

with h5py.File(filename, 'r') as f:
    # List all groups
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]

    # Get the data
    data = list(f[a_group_key])
    # Since the dimensions of each matrix is the same, we can simply use the rows/column dimension in the first matrix
    rows = len(data[0])
    columns = len(data[0][0])
    gridded_spi = []
    for i in range(0, rows - 1):
        row_spi = []
        for j in range(0, columns - 1):
            pixel_precipitations = []
            for clipped_image in data:
                pixel_precipitations.append(clipped_image[i][j])
            spi = indices.spi(np.array(pixel_precipitations), 90, indices.Distribution.gamma, 1989, 1989, 2018, compute.Periodicity.daily)
            print('Spi')
            print(spi)
            row_spi.append(spi)
        gridded_spi.append(row_spi)
    # Outputing the result as a CSV
    with open('spi3.csv', 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(gridded_spi)

    end = time.time()

    print('The process took %.2f minutes.' % ((end - start) / 60))

