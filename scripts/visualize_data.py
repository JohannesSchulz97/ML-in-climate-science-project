import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import pandas as pd
import time
import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeat

import datetime as dt
from dateutil.relativedelta import relativedelta


FILE_DATA = "../data/data.npy"
FILE_DATA_CENTERED = "../data/data_centered.npy"

START_DATE = dt.datetime(1979, 1, 1)
LON_COORD = (-15, 40)
LAT_COORD = (75, 35)


def get_image_of_data(file_name, t, use_cartopy=True):
    if use_cartopy:
        pass
    else:
        plt.imsave(file_name, data[t])


# Load the data
data = np.load(FILE_DATA)
data_centered = np.load(FILE_DATA_CENTERED)
