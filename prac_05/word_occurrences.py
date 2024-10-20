word_to_count = {}
text = input("Text: ")
words = text.split()

for word in words:
    # Using a simpler approach to increment the count
    word_to_count[word] = word_to_count.get(word, 0) + 1

# Sort the words alphabetically
sorted_words = sorted(word_to_count.keys())

# Determine the length of the longest word for alignment
max_length = max(len(word) for word in sorted_words)

# Print the word counts in a nicely formatted way
for word in sorted_words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
