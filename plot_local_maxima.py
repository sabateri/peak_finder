import rasterio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import maximum_filter
from skimage.feature import peak_local_max

# Load the TIFF file
#tif_path = "data/srtm_23_24.tif"
tif_path = "data/srtm_37_08.tif"

with rasterio.open(tif_path) as dataset:
    elevation = dataset.read(1)  # Read the first band (DEM data)

    
# Define the window size (for example, a 3x3 window)
window_size = 500

# Apply a maximum filter
local_max = maximum_filter(elevation, size=window_size)

# Create a boolean mask where the elevation is equal to the local maximum
peaks_mask = (elevation == local_max)

# Optionally, exclude plateaus by requiring that the value is strictly greater than its neighbors:
# Here, one can compute a minimum filter or apply additional logic if needed


# Using skimage's peak_local_max
# Note: correct the typo 'elevetaion' to 'elevation'
coordinates = peak_local_max(elevation, min_distance=20)
peak_y_sk, peak_x_sk = coordinates[:, 0], coordinates[:, 1]


# Plot the results
plt.figure(figsize=(10, 6))
plt.imshow(elevation, cmap="terrain", origin="upper")
plt.colorbar(label="Elevation (m)")
plt.title("Elevation Map with Local Maxima")
plt.xlabel("X Pixel")
plt.ylabel("Y Pixel")

# Overlay the detected peaks as red dots
peak_y, peak_x = np.where(peaks_mask)
plt.scatter(peak_x, peak_y, color='red', s=10, label='Local Maxima')
# Overlay skimage peaks (in blue)
plt.scatter(peak_x_sk, peak_y_sk, color='blue', s=10, label='skimage peak_local_max Peaks')

plt.legend()
plt.show()

