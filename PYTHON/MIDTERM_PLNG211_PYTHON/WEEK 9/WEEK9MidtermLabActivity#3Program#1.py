# MIDTERM LAB ACTIVITY # 3
# PROGRAM #1

print("--- PROGRAM #1 ---")

# 1. Create a bytes object by encoding the message using UTF-8.
message = "Hello Python"
bytes_obj = message.encode('utf-8')
print(f"1. Bytes object: {bytes_obj}")

# 2. Convert the bytes object back to a string.
string_from_bytes = bytes_obj.decode('utf-8')
print(f"2. Bytes to string: {string_from_bytes}")

# 3. Convert the bytes object to a hexadecimal string.
hex_string = bytes_obj.hex()
print(f"3. Bytes to hex: {hex_string}")

# 4. Convert the hexadecimal string back to bytes.
bytes_from_hex = bytes.fromhex(hex_string)
print(f"4. Hex to bytes: {bytes_from_hex}")

# 5. Create a new bytearray object directly from the string "Hello Python".
new_bytearray = bytearray(message, 'utf-8')
print(f"5. New bytearray: {new_bytearray}")

# 6. Convert the bytes object from Task 1 into a separate bytearray.
bytearray_from_bytes = bytearray(bytes_obj)
print(f"6. Bytes to bytearray: {bytearray_from_bytes}")

# 7. Slice the original bytes object to extract "Python".
# "Python" starts at index 6 and goes to the end
sliced_bytes = bytes_obj[6:]
print(f"7. Sliced bytes: {sliced_bytes}")

# 8. Modify the first character of the converted bytearray from uppercase H to lowercase h, then decode it.
# ASCII value for 'h' is 104
bytearray_from_bytes[0] = 104
modified_message = bytearray_from_bytes.decode('utf-8')
print(f"8. Modified message: {modified_message}")
