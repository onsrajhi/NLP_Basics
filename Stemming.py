import nltk
from nltk.stem import PorterStemmer

# Create a stemmer object
stemmer = PorterStemmer()

# Stem some example words
words = ["walking", "jumps", "jumped", "jumping"]
for word in words:
    stemmed_word = stemmer.stem(word)
    print(f"{word} -> {stemmed_word}")
