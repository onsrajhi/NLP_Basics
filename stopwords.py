import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# Define a sample English text
english_text = "Hello, how are you doing? I hope you're doing well."

# Tokenize the text into words
words = word_tokenize(english_text)

# Load the English stop words
stop_words = set(stopwords.words('english'))

# Filter out the stop words from the text
filtered_words = [word for word in words if not word in stop_words]

# Join the filtered words into a string
filtered_text = ' '.join(filtered_words)

# Print the filtered text
print(filtered_text)