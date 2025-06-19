text = "This is a sentence"
long_words = [word for word in text.split() if len (word) > 3 ]
print(long_words)