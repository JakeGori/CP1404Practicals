"""
Word Occurrences Program
"""


# Ask the user for a string input
text = input("Text: ")


# Initialize an empty dictionary to store word counts
word_counts = {}


# Split the text into words
words = text.split()


# Count occurrences of each word
for word in words:
   # Use lower() to make counting case-insensitive
   word = word.lower()
   if word in word_counts:
       word_counts[word] += 1
   else:
       word_counts[word] = 1


# Sort the words alphabetically
sorted_words = sorted(word_counts.keys())


# Find the longest word length for formatting
max_length = max(len(word) for word in sorted_words)


# Print the word counts with aligned formatting
for word in sorted_words:
   print(f"{word:{max_length}} : {word_counts[word]}")
