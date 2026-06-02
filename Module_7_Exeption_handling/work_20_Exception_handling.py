# PYTHON EXCEPTION HANDLING - PRACTICAL LAB EXERCISES
# =====================================================

# Topics Covered:
# - Error vs Exception
# - try, except, else, finally
# - Common Exception Types
# - Multiple except Blocks
# - raise
# - assert
# - Difference between raise and assert

# -----------------------------------------------------
# LEVEL 1 - BEGINNER
# -----------------------------------------------------

# 1. Safe Division Calculator
# Create a program that takes two numbers from the user and performs division.
# Handle ZeroDivisionError.

# 2. Integer Input Validation
# Ask the user to enter an age.
# Handle invalid input using ValueError.

# 3. Name Lookup
# Create a dictionary of employee IDs and names.
# Ask the user for an employee ID and handle KeyError.

# 4. List Access
# Store 5 product names in a list.
# Allow the user to enter an index and handle IndexError.

# 5. File Reader
# Ask the user for a filename and display its contents.
# Handle FileNotFoundError.

# 6. Type Mismatch
# Create a program that accidentally tries to add a string and integer.
# Handle TypeError.

# 7. Multiple Exception Handling
# Build a calculator that handles:
# - ValueError
# - ZeroDivisionError

# 8. else Block Practice
# Display "Operation Successful" only when no exception occurs.

# 9. finally Block Practice
# Simulate opening a file and ensure a cleanup message is always displayed.

# 10. Employee Salary Validator
# Accept salary input and ensure only numeric values are accepted.

# -----------------------------------------------------
# LEVEL 2 - INTERMEDIATE
# -----------------------------------------------------

# 11. Student Mark Analyzer
# Accept marks for 5 subjects.
# Handle invalid entries and calculate average safely.

# 12. ATM Withdrawal System
# Allow withdrawal from an account balance.
# Raise an exception if withdrawal amount exceeds balance.

# 13. Login System
# Allow only 3 login attempts.
# Handle invalid inputs gracefully.

# 14. CSV Data Processor
# Read data from a file.
# Handle:
# - FileNotFoundError
# - ValueError
# - IndexError

# 15. Product Inventory Search
# Search products in a dictionary.
# Handle missing product IDs.

# 16. Online Shopping Cart
# Validate quantity and price entered by the user.
# Handle all possible input errors.

# 17. Number Conversion Utility
# Convert user input to:
# - int
# - float
# Handle conversion errors separately.

# 18. Multi-Exception Banking Program
# Handle:
# - ValueError
# - ZeroDivisionError
# - KeyError
# using separate except blocks.

# 19. Employee Database Simulator
# Search employee records and generate custom error messages.

# 20. Safe JSON Parser
# Accept JSON-like data and handle malformed input exceptions.

# -----------------------------------------------------
# LEVEL 3 - ADVANCED
# -----------------------------------------------------

# 21. Custom Age Validation
# Raise ValueError if age is below 18.

# 22. E-Commerce Checkout Validation
# Raise exceptions for:
# - Invalid coupon
# - Out-of-stock product
# - Invalid payment amount

# 23. Banking Transaction Processor
# Validate:
# - Minimum balance
# - Transaction limits
# - Invalid account numbers

# 24. API Response Validator
# Simulate an API response.
# Raise exceptions when required fields are missing.

# 25. Flight Booking System
# Validate seat availability and passenger details using raise.

# 26. University Admission System
# Raise exceptions when:
# - Marks are below eligibility
# - Documents are missing

# 27. Password Policy Checker
# Raise exceptions if password does not meet:
# - Length requirements
# - Uppercase letter
# - Number
# - Special character

# 28. Payroll Management System
# Validate employee details and salary calculations using custom exceptions.

# 29. Online Examination Portal
# Handle:
# - Invalid answers
# - Missing questions
# - Submission timeout

# 30. File Upload Validator
# Raise exceptions for:
# - Invalid extension
# - Oversized files
# - Empty files

# -----------------------------------------------------
# ASSERTION PRACTICE
# -----------------------------------------------------

# 31. Assert Positive Number
# Use assert to ensure a number is positive.

# 32. Assert Product Price
# Ensure product price is greater than zero.

# 33. Assert Student Marks
# Ensure marks are between 0 and 100.

# 34. Assert Employee Experience
# Ensure experience is not negative.

# 35. Assert List Is Not Empty
# Verify a product list contains at least one item.

# -----------------------------------------------------
# INTERVIEW-STYLE QUESTIONS
# -----------------------------------------------------

# 36. Difference between Exception and Error
# Demonstrate with code examples.

# 37. When should assert be used instead of raise?

# 38. Why is except Exception generally preferred over bare except?

# 39. What happens if finally contains a return statement?

# 40. Can multiple except blocks execute for a single exception? Explain with code.

# 41. What is exception propagation? Demonstrate.

# 42. What happens if an exception is not handled?

# 43. Why should specific exceptions be written before general exceptions?

# 44. Explain the execution flow of:
# try -> except -> else -> finally

# 45. How does Python search for a matching except block?

# -----------------------------------------------------
# INDUSTRY-ORIENTED MINI PROJECTS
# -----------------------------------------------------

# 46. Banking Management System
# Implement robust exception handling for deposits, withdrawals, and transfers.

# 47. Inventory Management System
# Handle stock updates, product searches, and invalid transactions.

# 48. Hospital Appointment System
# Validate patient details and appointment schedules.

# 49. Food Delivery Application
# Handle payment failures, invalid coupons, and unavailable restaurants.

# 50. Employee Attendance Tracker
# Validate punch-in/punch-out records and generate exception reports.

# -----------------------------------------------------
# LOGICAL CHALLENGE QUESTIONS
# -----------------------------------------------------

# 51. Predict the output of a nested try-except-finally program.

# 52. Write a program where finally executes even after return.

# 53. Build a retry mechanism that retries an operation 3 times before failing.

# 54. Create a file-processing program that skips invalid records but continues processing.

# 55. Design a custom exception hierarchy for an e-commerce application.

# 56. Implement a transaction rollback simulation using exception handling.

# 57. Create a logger that records all exceptions to a file.

# 58. Process 100 user records and continue execution even if some records fail.

# 59. Build a menu-driven application using comprehensive exception handling.

# 60. Create a production-ready user registration system with validation, raise, and assertions.

# END OF LAB SHEET
