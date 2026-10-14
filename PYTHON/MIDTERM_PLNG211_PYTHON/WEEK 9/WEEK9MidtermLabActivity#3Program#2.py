# MIDTERM LAB ACTIVITY # 3
# PROGRAM #2

print("\n--- PROGRAM #2 ---")

# 1. Initialize string literals
first_name = "Nestor"
last_name = "Guerrero"
print(f"First name: {first_name}")
print(f"Last name: {last_name}")

# 2. Concatenate strings
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# 3 & 4. Access characters and Demonstrate immutability
print(f"First character: {full_name[0]}")
print(f"Last character: {full_name[-1]}")

try:
    first_name[0] = "D"
except TypeError as e:
    print("Strings are immutable; individual characters\ncannot be changed directly.")

# 5 & 6. Create a new string and Traverse a string
new_name = "D" + first_name[1:]
print(f"New name: {new_name}")
print(f"Original name: {first_name}")

print("Characters in the full name:")
for char in full_name:
    print(char)

# 7. Slice a string
sliced_first = full_name[:5]
sliced_last = full_name[6:]
print(f"Sliced first name: {sliced_first}")
print(f"Sliced last name: {sliced_last}")

# 8. Search for a character
search_char = input("Enter one character to search: ")

# Handle empty input or multi-character input strictly as standard validation
if len(search_char) == 1:
    if search_char in full_name:
        index = full_name.find(search_char)
        print(f"Character found at index: {index}")
    else:
        print("Character not found in the full name.")
else:
    print("Please enter exactly one character.")
