# REGULAR EXPRESSION PRACTICAL QUESTIONS (30)

# BEGINNER LEVEL
# 1. Extract all email addresses.
# 2. Extract all phone numbers in Indian format.
# 3. Extract all dates in DD/MM/YYYY format.
# 4. Extract all dates in YYYY-MM-DD format.
# 5. Extract all employee IDs.
# 6. Extract all order IDs.
# 7. Extract all salaries.
# 8. Extract all URLs.
# 9. Count the total number of email addresses.
# 10. Count the total number of phone numbers.

# INTERMEDIATE LEVEL
# 11. Extract usernames from email addresses.
# 12. Extract only Gmail addresses.
# 13. Extract all IP addresses.
# 14. Validate whether extracted IP addresses follow IPv4 format.
# 15. Extract all passwords.
# 16. Find passwords containing special characters.
# 17. Extract all UPI IDs.
# 18. Extract all PIN codes.
# 19. Extract all PAN numbers.
# 20. Extract all GSTIN numbers.

# ADVANCED LEVEL
# 21. Extract only valid email addresses and ignore invalid ones.
# 22. Find all records where salary is greater than 50000.
# 23. Extract domain names from URLs.
# 24. Extract all log levels (ERROR, INFO, WARNING).
# 25. Extract timestamps from server logs.
# 26. Find all customer names from order records.
# 27. Mask phone numbers except the last 4 digits using regex substitution.
# 28. Replace all email domains with 'hidden.com'.
# 29. Validate strong passwords (uppercase, lowercase, digit, special character).
# 30. Generate a summary showing:
#     - Total emails
#     - Total phone numbers
#     - Total URLs
#     - Total IP addresses
#     - Total transactions

# BONUS REAL-WORLD TASKS
# 1. Build an email extractor tool.
# 2. Build a log analyzer using regex.
# 3. Create a password strength checker.
# 4. Create a data masking utility for sensitive information.
# 5. Build a customer data validation script.


import re

with open("regex_data.txt", "r+") as f:
    data=f.read()
    
    
    #emails 
    result= re.findall(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', data)
    # result= re.findall(r'[a-zA-Z0-9]+@gmail\.com', data)
    
    print("All Email  :")
    cont=0
    for i in result:
        cont+=1
        print(cont," :",i)
    
    
    #emails 
    result1= re.findall(r'\+\d+[-]\d{10}', data)
    print("All Phone number in indian format  :")
    cont=0
    for i in result1:
        cont+=1
        print(cont," :",i)
    
    