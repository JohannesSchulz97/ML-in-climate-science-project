import numpy as np

data = np.load("../data/data.npy")
_, lon_dim, lat_dim = data.shape

data_centered = np.zeros_like(data)

for i in range(lon_dim):
    for j in range(lat_dim):
        time_frame = data[:, i, j]
        data_centered[:, i, j] = time_frame - np.mean(time_frame)

np.save("../data/data_centered.npy", data_centered)
