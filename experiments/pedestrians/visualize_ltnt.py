import csv
import numpy as np
import matplotlib.pyplot as plt

extracted_lines = []
# with open("../beta_np.csv", "r") as f:
with open("./z_logits_orignal.csv", "r") as f:
    reader = csv.reader(f)
    
    # Iterate over each row in the CSV file
    for i, row in enumerate(reader):
        # Check if the current row is the 99th line
        if (i + 9) % 198 == 0:
            extracted_lines.append(row)

# fig, axs = plt.subplots(nrows=8, ncols=1, figsize=(6, 12))

print("len of extracted_lines",len(extracted_lines))
print("len of extracted_lines[0]",len(extracted_lines[0]))

each_lt = []

# Iterate over each set of 25 numbers
for i in range(25):
    # Extract the i-th element from each list in data
    values=[float(item[i]) for item in extracted_lines]
    each_lt.append(values)

# print(each_lt[0])
# plt.plot(each_lt[24], label='z0')

fig, axs = plt.subplots(nrows=5, ncols=5, figsize=(6, 12))
for i in range(25):
    print(int(i/5),",",i%5)
    axs[int(i/5),i%5].plot(each_lt[i], label=f'z{i}')
    
    # Set labels and title
    axs[int(i/5),i%5].set_xlabel('Index')
    axs[int(i/5),i%5].set_ylabel(f'Value {i+1}')
    axs[int(i/5),i%5].set_title(f'Plot {i+1}')

# Adjust layout to prevent overlap
# plt.tight_layout()

# Show the plot
plt.show()