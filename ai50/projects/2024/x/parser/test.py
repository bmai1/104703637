import nltk

sentence = "the Fox, kissed me?"

# punctuation = ",;:.!?"
# for p in punctuation:
#     sentence = sentence.replace(p, '')

# words = sentence.lower().split(' ')

tokens = nltk.word_tokenize(sentence.lower(), language='english', preserve_line=True)
words = [token for token in tokens if any(c.isalpha() for c in token)]

print(words)

