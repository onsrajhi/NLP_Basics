#tokenize exercice
import nltk
text = "Hello I'am Ons ! How are you doing , I hope ypu are fine, have a good day"
sentences = nltk.sent_tokenize(text)
tokens = nltk.word_tokenize(text)
print(sentences)
print(tokens)

#stop words exercice
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stopwords.words('english') #can see anylanguage