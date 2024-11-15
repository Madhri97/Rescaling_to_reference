import matplotlib.pyplot as plt
import numpy as np

# File paths
reference_file = 'reference.hist'
query_file = 'query_file.tsv'
sample_rescaled_file = 'sample_rescaled.hist'

# Function to read data from a file
def read_data(file_path, columns):
    data = np.loadtxt(file_path, delimiter='\t', skiprows=1)
    return data[:, columns]

# Read the data from the files
reference_data = read_data(reference_file, (0, 1))  # Fragment length and Normalized Frequency
query_data = np.loadtxt(query_file, delimiter='\t', skiprows=1)  # Fragment length, Count, Normalized Frequency
query_data = query_data[:, [0, 2]]  # Extract Fragment length and Normalized Frequency
sample_rescaled_data = read_data(sample_rescaled_file, (0, 1))  # Fragment length and Normalized Frequency

# Create the plot
plt.figure(figsize=(12, 9))

# Plot each dataset
plt.plot(reference_data[:, 0], reference_data[:, 1], label='Reference', color='forestgreen', lw=2, marker='o', markersize=5)
plt.plot(query_data[:, 0], query_data[:, 1], label='Query', color='magenta', lw=2, marker='x', markersize=6)
plt.plot(sample_rescaled_data[:, 0], sample_rescaled_data[:, 1], label='Sample Rescaled', color='blue', lw=2, marker='^', markersize=7)

# Customize plot
plt.xlabel('Fragment Length')
plt.ylabel('Normalized Frequency')
plt.xticks(np.arange(0, 701, 100))
plt.yticks(np.arange(0, 0.025, 0.005))
plt.xlim(0, 700)
plt.ylim(0, 0.025)
plt.legend(loc='upper right')
plt.grid(True)

# Save the plot as a PNG image
plt.savefig('rescale_to_reference.png', dpi=300)

# Display the plot
plt.show()

