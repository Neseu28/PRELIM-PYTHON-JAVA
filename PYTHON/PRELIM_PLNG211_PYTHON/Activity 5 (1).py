def print_last_word():
    """Prompt for three words and print the one last alphabetically."""
    first_word = input("Enter the first word: ")
    second_word = input("Enter the second word: ")
    third_word = input("Enter the third word: ")

    last_word = max(first_word, second_word, third_word)
    print("The word that comes last alphabetically is:", last_word)


print_last_word()
