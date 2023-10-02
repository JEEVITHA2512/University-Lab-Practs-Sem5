import numpy as np
from scipy.signal import medfilt
from scipy.interpolate import UnivariateSpline
from sklearn.linear_model import RANSACRegressor
from pykalman import KalmanFilter

# Given data
data = [1, 2, 3, 100, 4, 5, 200, 6, 7, 8]

# 1. Outlier Removal
def remove_outliers(data, threshold):
    return [x for x in data if abs(x - np.mean(data)) < threshold * np.std(data)]

cleaned_data_outliers = remove_outliers(data, 2.0)
print("Data after Outlier Removal:", cleaned_data_outliers)

# 2. Median Filtering
median_filtered_data = medfilt(data, kernel_size=3)
print("Data after Median Filtering:", median_filtered_data)

# 3. Smoothing using Moving Average
def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size)/window_size, mode='same')

smoothed_data = moving_average(data, window_size=3)
print("Data after Smoothing with Moving Average:", smoothed_data)

# 4. Robust Regression
def robust_regression(data, x):
    model_ransac = RANSACRegressor()
    model_ransac.fit(np.array(x).reshape(-1, 1), data)
    return model_ransac.predict(np.array(x).reshape(-1, 1))

x = range(len(data))
robust_regression_data = robust_regression(data, x)
print("Data after Robust Regression:", robust_regression_data)

# 5. Kalman Filtering
def kalman_filter(data):
    initial_state = data[0]
    transition_matrix = [1]
    observation_matrix = [1]
    kf = KalmanFilter(initial_state_mean=initial_state, n_dim_obs=1)
    filtered_state_means, _ = kf.filter(data)
    return filtered_state_means

kalman_filtered_data = kalman_filter(data)
print("Data after Kalman Filtering:", kalman_filtered_data)

