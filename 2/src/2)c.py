# -*- coding: utf-8 -*-
"""2)c

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dskVrrnpgx4IoMuYqweWc1fpnks1WV4X
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("/content/drive/MyDrive/Assignment 4&5/diabetes.csv")

cols_to_clean = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
data[cols_to_clean] = data[cols_to_clean].replace(0, np.nan)

data_cleaned = data.dropna()

def bootstrap_sampling(data, n_samples, sample_size):
    samples = []
    for _ in range(n_samples):
        sample = data.sample(n=sample_size, replace=True)
        samples.append(sample)
    return samples

bootstrap_samples = bootstrap_sampling(data['BloodPressure'], 500, 150)

bootstrap_means = [sample.mean() for sample in bootstrap_samples]
bootstrap_std = [sample.std() for sample in bootstrap_samples]
bootstrap_95th_percentile = [np.percentile(sample.dropna(), 95) for sample in bootstrap_samples]

population_mean_bp = data['BloodPressure'].mean()
population_std_bp = data['BloodPressure'].std()
population_95th_percentile_bp = np.percentile(data['BloodPressure'], 95)

plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.hist(bootstrap_means, bins=20, alpha=0.7, color='blue', label='Bootstrap Sample Means')
plt.axvline(population_mean_bp, color='red', linestyle='dashed', linewidth=1, label='Population Mean')
plt.xlabel('Blood Pressure Mean')
plt.ylabel('Frequency')
plt.title('Comparison of Blood Pressure Mean')
plt.legend()

plt.subplot(1, 3, 2)
plt.hist(bootstrap_std, bins=20, alpha=0.7, color='green', label='Bootstrap Sample Std Deviation')
plt.axvline(population_std_bp, color='red', linestyle='dashed', linewidth=1, label='Population Std Deviation')
plt.xlabel('Blood Pressure Std Deviation')
plt.ylabel('Frequency')
plt.title('Comparison of Blood Pressure Std Deviation')
plt.legend()

plt.subplot(1, 3, 3)
plt.hist(bootstrap_95th_percentile, bins=20, alpha=0.7, color='purple', label='Bootstrap 95th Percentile')
plt.axvline(population_95th_percentile_bp, color='red', linestyle='dashed', linewidth=1, label='Population 95th Percentile')
plt.xlabel('Blood Pressure 95th Percentile')
plt.ylabel('Frequency')
plt.title('Comparison of Blood Pressure 95th Percentile')
plt.legend()

plt.tight_layout()
plt.show()

