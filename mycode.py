import pandas as pd
import os

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Adding new row for V2
new_row1 = {'Name': 'Lisa', 'Age': 20, 'City': 'Miami'}
df.loc[len(df)] = new_row1

# Adding new row for V3
# new_row2 = {'Name': 'V3', 'Age': 22, 'City': 'City2'}
# df.loc[len(df)] = new_row2

# Ensure the "data" directory exists
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define the file path
file_path = os.path.join(data_dir, 'output.csv')

# Save the DataFrame to CSV
df.to_csv(file_path, index=False)
print(f"✅ File saved to {file_path}")
