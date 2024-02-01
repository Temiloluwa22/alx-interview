#!/usr/bin/python3
"""
UTF-8 validation module
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    num_bytes = 0

    for byte in data:
        # Check if the most significant bit is 0 or 1
        if num_bytes == 0:
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            # Check if the byte is a continuation byte (starts with 10)
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0

# Example usage
data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
  
