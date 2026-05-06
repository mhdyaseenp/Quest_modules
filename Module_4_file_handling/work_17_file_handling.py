# Section 1: Basic File Operations
# Open the CSV file using open() in read mode and print its contents.
# with open("sample_data_50.csv",'r')as f:
#     print(f.read())
    
    
# Count the total number of lines in the file.
# coount=0
# with open("sample_data_50.csv",'r')as f:
#     for lin in f:
#         coount+=1
# print(coount)


# Read only the first 5 rows from the file.
# with open("sample_data_50.csv",'r')as f:
#     for i in range(5):
#         line=f.readline()
#         print(line.strip())


# Read the file line by line using readline().
# with open("sample_data_50.csv",'r')as f:
#     lin=f.readline()
#     # print(lin)
#     while lin:
#         print(lin.strip())
#         # print(lin)
#         lin=f.readline()

# Read all lines using readlines() and display them. 
# with open("sample_data_50.csv",'r')as f:
#     lin=f.readlines()
#     print(lin)
# for l in lin:
#     print(l.strip())

# Print only the header row of the CSV file.
# with open("sample_data_50.csv",'r')as f:
#     lin=f.readline()
#     print(lin.strip())


# Check whether the file exists before opening it.



# Close the file manually after reading.
# with open("sample_data_50.csv",'r')as f:
#     data=f.read()
#     print(data)
#     f.close()                                     #it will close automatically

# file=open("sample_data_50.csv", "r")
# data=file.read()
# print(data)
# file.close()

# Use with statement to open and read the file.



# Print file size in bytes.
# with open("sample_data_50.csv",'a+')as f:
#     f.seek(0)
#     a=f.read()
#     print(a)
    


# 🔹 Section 2: Working with CSV Data
# Read the CSV file using the csv module.
# Print all rows as lists.
# with open("sample_data_50.csv",'r')as f:
#     for l in f:
#         print(l.strip().split(","))
        # row=l.strip().split(",")
        # print(row)


# Print all rows as dictionaries using DictReader.



# Extract and print all names from the file.
# with open("sample_data_50.csv",'r')as f:
#     for l in f:
#         # print(l.strip().split(","))
#         row=l.strip().split(",")
#         print(row[1])



# Extract and print all cities.
# with open("sample_data_50.csv",'r')as f:
#     for l in f:
#         row=l.strip().split(",")
#         print(row[3])



# Count how many records are there in total.
# with open("sample_data_50.csv",'r')as f:
#     lines=f.readlines()
#     print(len(lines)-1)


# Print records where Age > 30.
# with open("sample_data_50.csv",'r')as f:
#     lines=f.readlines()
#     for lin in lines[1:]:
#         data=lin.strip().split(",")
#         age=int(data[2])
#         if age>30:
#             print(data)



# Print records where City = "Kochi".
# with open("sample_data_50.csv",'r')as f:
#     lines=f.readlines()
#     for lin in lines[1:]:
#         data=lin.strip().split(",")
#         city="Kochi"
#         if city in data:
#             print(data)


# Count how many people belong to each city.



# Find the maximum age in the dataset.



# 🔹 Section 3: Writing to CSV



# Create a new CSV file and write 5 records manually.
# Copy contents from original file to a new file.
# Append a new record to the existing CSV file.
# Write only names and ages to a new file.
# Save filtered data (Age > 25) into a new CSV.
# Write a CSV file with custom delimiter (e.g., ;).
# Write a file with uppercase names.
# Remove duplicate rows (if any) and write to new file.
# Write sorted data based on Age.
# Write data in reverse order.
# 🔹 Section 4: Data Processing
# Calculate average age of all records.
# Find youngest person in the dataset.
# Find oldest person in the dataset.
# Count how many people are from each city.
# Display names of people whose age is between 25–30.
# Replace all city names "Delhi" with "New Delhi".
# Convert all names to lowercase.
# Add a new column "Status" (Adult/Young based on age).
# Create a new CSV with only unique cities.
# Merge two CSV files (create another sample file).
# 🔹 Section 5: Intermediate Tasks
# Search for a record by name.
# Update age of a specific person and rewrite file.
# Delete a record based on ID.
# Sort data by Name alphabetically.
# Group data by City and display counts.
# Find top 5 oldest people.
# Find average age per city.
# Validate data (check for missing values).
# Handle exceptions while opening file.
# Build a menu-driven program:
# View records
# Add record
# Delete record
# Search record