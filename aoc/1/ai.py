def sum_calibration_values(calibration_document):
    total_sum = 0
    
    for line in calibration_document:
        # Find the first and last digits
        first_digit = next(char for char in line if char.isdigit())
        last_digit = next(char for char in reversed(line) if char.isdigit())
        
        # Combine the first and last digits to get the calibration value
        calibration_value = int(first_digit + last_digit)
        
        # Add the calibration value to the total sum
        total_sum += calibration_value
    
    return total_sum

# Example calibration document
calibration_document = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
]

# Calculate the sum of calibration values
result = sum_calibration_values(calibration_document)

# Print the result
print(result)
