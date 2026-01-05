# # Week 4 Practice
# ## Comprehensions, revisited

# See this for loop that computes the squares of the numbers in the list `x`:

# x = [1, 2, 3, 4]

# squares = []
# for i in x:
#     squares.append(i * i)
# print(squares)

# Rewrite the for-loop into a list comprehension:

# squares = [ ]
# print(squares)

# Now do it again, but with a condition. For instance, only numbers greater than 1:

# squares = [ ]
# print(squares)

# When iterating over strings, each element of the string is a character, not a word:

# print([c.upper() for c in 'cats and dogs'])

# We can make more complicated comprehensions with multiple loops, multiple conditions, etc.:

# words = 'cats and dogs'.split()
# print([c.upper() for word in words for c in word])

# But generally this is a bad idea. Large comprehensions get confusing.


# ## Dictionaries
# Python's dictionaries (`dict` objects) can be created in many ways:

# {'a': 1, 'b': 2}             # dictionary literal
# dict([('a', 1), ('b', 2)])   # dict() call with list of pairs
# dict(a=1, b=2)               # dict() call with keyword keys (only for simple keys)
# {c: i for i, c in enumerate('ab', 1)}  # in a dict comprehension

# #### Challenge
# Create a function that takes a string and maps the downcased first letter of
# each word to the list of words starting with that letter (upper or lowercase).

# If I don't have a good idea where to begin, I'd first start out writing what
# I do know. I want a function that takes a string and returns a dictionary:

# def lettermap(string):
#     d = {}
#     return d

# Now I'd start filling in the details. I know I need to go over each word,
# get the first character of each word, and map it to a list of words, so maybe:

# def lettermap(string):
#     d = {}
#     for word in string.split():
#         c = word[0]
#         d[c] = [word]
#     return d

# print(lettermap('dogs CHASE cats'))

# That looks better, but we haven't case-normalized the first letters.

# def lettermap(string):
#     d = {}
#     for word in string.split():
#         c = word[0].lower()
#         d[c] = [word]
#     return d

# print(lettermap('dogs CHASE cats'))

# Ok, now we've lost 'CHASE'. We need to create one list and append to it,
# rather than creating a new list for each word.

# def lettermap(string):
#     d = {}
#     for word in string.split():
#         c = word[0].lower()
#         if c not in d:
#             d[c] = []
#         # at this point we know that d[c] has a list, so append to it
#         d[c].append(word)
#     return d

# print(lettermap('dogs CHASE cats'))

# All done!


# ## Text Corpora
# import nltk
# stopwords = nltk.corpus.stopwords.words('english')
# fileids = nltk.corpus.inaugural.fileids()[-5:]
# pairs = []
# for fileid in fileids:
#     name = fileid[5:-4]
#     for word in nltk.corpus.inaugural.words(fileid):
#         word = word.lower()
#         if word not in stopwords:
#             pairs.append((name, word))
# cfd = nltk.ConditionalFreqDist(pairs)
# print(cfd)
# print(cfd.conditions())
# cfd['Bush'].plot(20)
# cfd['Obama'].plot(20)
# cfd['Trump'].plot(20)
# cfd.plot(samples=('i', 'me', 'my', 'myself'))
# cfd.plot(samples=('country', 'nation', 'people'))

# for word in ('country', 'nation', 'people'):
#     for pres in cfd.conditions():
#         print(pres, word, cfd[pres].freq(word))
