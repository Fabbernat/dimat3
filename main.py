# Function to add 1 bit to a float
import struct


def add_bit_to_float(value):
    # Pack the float into a binary string
    packed = struct.pack('!f', value)
    # Unpack it as an integer
    int_value = struct.unpack('!I', packed)[0]
    # Add 1 to the integer value
    int_value += 1
    # Pack it back into a float
    packed = struct.pack('!I', int_value)
    # Unpack it as a float
    return struct.unpack('!f', packed)[0]

# Example usage
original_value = 1.0
new_value = add_bit_to_float(original_value)
print(f"Original value: {original_value}")
print(f"New value: {new_value}")