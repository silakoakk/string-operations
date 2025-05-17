# Get input from the user
text = input("Enter a sentence or text: ")

# 1. Count total number of characters
char_count = len(text)
print("Total number of characters:", char_count)

# 2. Count number of vowels (a, e, i, o, u)
vowels = "aeiouAEIOU"
vowel_count = sum(1 for letter in text if letter in vowels)
print("Number of vowels:", vowel_count)

# 3. Convert all characters to uppercase
uppercase_text = text.upper()
print("Uppercase version:", uppercase_text)

# 4. Reverse the text
reversed_text = text[::-1]
print("Reversed text:", reversed_text)

# 5. Count the number of words
words = text.split()
word_count = len(words)
print("Number of words:", word_count)

# 6. Remove all spaces
no_spaces = text.replace(" ", "")
print("Text without spaces:", no_spaces)
