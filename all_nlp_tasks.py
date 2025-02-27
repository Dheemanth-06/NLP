# -*- coding: utf-8 -*-
"""All NLP Tasks.ipynb"""

!pip install blis

!pip install -U spacy

"""### Word Tokenization"""

import nltk
import spacy

text = "Hello! How are you? I am learning NLP. Welcome to U.S.A. "

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)
spacy_tokens = [token.text for token in doc]

word_tokens = [token.text for token in doc]

sent_tokens = [sent.text for sent in doc.sents]

print("Word Tokens:", word_tokens)
print("Sentence Tokens:", sent_tokens)
print("SpaCy Tokens:", spacy_tokens)

"""### Stop word removal"""

spacy_stopwords = [token.text for token in doc if not token.is_stop]

print("SpaCy Filtered Words:", spacy_stopwords)

"""### Lemmatization"""

lemmatized_words = [token.lemma_ for token in doc]

print("Lemmatized Words:", lemmatized_words)

"""### Lower case and Remove Punctuations"""

import re

text = "Hello!! This is NLP 101. Visit https://example.com"
cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic characters
lower_text = cleaned_text.lower()

print("Cleaned Text:", lower_text)

"""### parts of Speech"""

for token in doc:
    print(f"{token.text} --> {token.pos_}")

"""### NER"""

for ent in doc.ents:
    print(f"{ent.text} --> {ent.label_}")

"""### Word2Vec Embeddings"""

from gensim.models import Word2Vec
from gensim.test.utils import common_texts


model = Word2Vec(sentences=common_texts, vector_size=2, window=5, min_count=1, workers=4)

"""#### Embeddings for a word"""

print("Vector for 'computer':", model.wv['computer'])

"""#### Most similar words"""

print("Most similar words to 'computer':", model.wv.most_similar('eps'))

"""#### Visualizing closest words"""

import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec
from sklearn.decomposition import PCA


word_vectors = model.wv[model.wv.index_to_key]  # Get the word vectors
pca = PCA(n_components=2)  # Initialize PCA
result = pca.fit_transform(word_vectors)  # Fit and transform the word vectors


plt.figure(figsize=(10, 8))
plt.scatter(result[:, 0], result[:, 1])


words = list(model.wv.index_to_key)
for i, word in enumerate(words):
    plt.annotate(word, xy=(result[i, 0], result[i, 1]), fontsize=12)

plt.title("Word Embeddings Visualization")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.grid()
plt.show()

