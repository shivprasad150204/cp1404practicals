"""Word Frequency Counter
Estimate: 20 minutes
Actual: 2025-06-23 11:21
"""

sentence = input("Enter text: ")
word_counter = {}

for word in sentence.split():
    word_counter[word] = word_counter.get(word, 0) + 1

max_word_len = max((len(word) for word in word_counter), default=0)
for word in sorted(word_counter.keys()):
    print(f"{word:<{max_word_len}} : {word_counter[word]}")
