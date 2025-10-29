import pandas as pd

# ----------------------------- #
# Step 1: Load the data
# ----------------------------- #

file_path = "data.csv"  

try:
    data = pd.read_csv(file_path)
    print("Data loaded successfully!\n")
except FileNotFoundError:
    print("File not found! Please check the file name and path.")
    exit()

# ----------------------------- #
# Step 2: Display first and last 5 rows
# ----------------------------- #
print("First 5 rows of the data:")
print(data.head(), "\n")

print("Last 5 rows of the data:")
print(data.tail(), "\n")

# ----------------------------- #
# Step 3: Show available columns
# ----------------------------- #
print("Available columns in the dataset:")
for col in data.columns:
    print("-", col)
print()

# ----------------------------- #
# Step 4: Interactive column selection for statistics
# ----------------------------- #
while True:
    column_name = input("Enter the column name to compute statistics: ")
    
    if column_name not in data.columns:
        print(f"Column '{column_name}' does not exist. Please choose from the available columns.\n")
        continue
    
    if not pd.api.types.is_numeric_dtype(data[column_name]):
        print(f"Column '{column_name}' is not numeric. Please choose a numeric column.\n")
        continue
    
    # Compute statistics 
    mean_value = data[column_name].mean()
    median_value = data[column_name].median()
    std_value = data[column_name].std()
    
    print(f"\nDescriptive statistics for column '{column_name}':")
    print(f"- Mean: {mean_value:.2f}")
    print(f"- Median: {median_value:.2f}")
    print(f"- Standard Deviation: {std_value:.2f}\n")
    break

# ----------------------------- #
# Step 5: Clean data by removing missing values
# ----------------------------- #
before_rows = len(data)
data_cleaned = data.dropna()
after_rows = len(data_cleaned)

print("Data cleaned from missing values.")
print(f"- Number of rows removed: {before_rows - after_rows}")
print(f"- Number of rows remaining: {after_rows}\n")

# ----------------------------- #
# Step 6: Save cleaned data
# ----------------------------- #
data_cleaned.to_csv("cleaned_data.csv", index=False)
print("Cleaned data has been saved to: cleaned_data.csv")

print("\nExecution finished successfully. Data analysis complete.")
