"""la diff stem:ya3ti racine kelma yna7i suffix , preffix , yrj3ha basic kelma
Le stemming est plus rapide mais moins précis, car il ne tient pas compte des nuances grammaticales ou sémantiques.
La lemmatisation est plus lente mais plus précise, car elle prend en compte le contexte et produit des mots valides.
"""


from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

text = "The quick brown foxes jumped over the lazy dogs"

# Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in word_tokenize(text)]
print(stemmed_words)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in word_tokenize(text)]
print(lemmatized_words)
