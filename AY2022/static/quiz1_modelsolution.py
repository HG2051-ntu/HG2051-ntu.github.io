## This is a model solution for quiz1, and as such represents only a single
## possible way of solving the challenge.
## Please enter your name and matric number as a comment below
## Name: Good Student
## Matric number: somenumber
## For this quiz you need to construct a dictionary from Swadesh wordlists and
## write it as a human-readable file (tsv/xlsx). Below is some basic code to get
## you started.
import nltk
from nltk.corpus import swadesh, wordnet
## uncomment the following line of code if you intend to work with Pandas - this
## may require installing the library using pip
import pandas as pd

# some basics of working with the Swadesh corpus
print(swadesh.fileids()) # view the languages in the Swadesh corpus
en = [x[0] for x in swadesh.entries(['en'])] # store the entries for English as a list
fr = [x[0] for x in swadesh.entries(['fr'])] # store the entries for French as a list
print(en[:5]) # print the first 5 entries in the English list
print(fr[:5]) # print the first 5 entries in the French list

df = pd.DataFrame() # instantiate a dataframe

df['French'] = fr # populate a column with the header 'French' using the `fr` wordlist
df['English'] = en # populate a column with the header 'English' using the `en` wordlist

print(df.head()) # view the first 5 rows of the dataframe

# create blank lists for the pos, def, exs
poslist = []
deflist = []
exslist = []

# loop through each word in the `en` list (remember, wordnet is an ENGLISH lexical resource)
for word in en:
    word = word.split()[0] # make sure we're dealing with just one word, not multi-word-expressions
    print(word)
    synsets = wordnet.synsets(word) # get the synsets for each word
    print(synsets)
    # using try/except blocks below, in case the synsets variable is a blank list (the word doesn't exist in wordnet)
    try:
        print(synsets[0])
        pos = synsets[0].pos() # get the part of speech for the first synset
        print(pos)
        poslist.append(pos) # append it to the list
    except:
        poslist.append("no_pos") # otherwise append a dummy string to the list
    try:
        defs = synsets[0].definition() # definition
        print(defs)
        deflist.append(defs) # append
    except:
        deflist.append("no_definition") # or not
    try:
        exs = synsets[0].examples() # examples
        print(exs)
        exslist.append(exs[0]) # append the first one
    except:
        exslist.append("no_examples") # or not

# use print statements to check the output
print(poslist)
print(len(en), len(poslist), len(deflist), len(exslist))

# create new columns based on the lists just created
df['POS'] = poslist
df['Definition'] = deflist
df['Example'] = exslist

print(df.head())

df = df.sort_values('French') # sort the dataframe based on the 'French' column
print(df.head())

df.to_excel("dictionary.xlsx", index=False) # write it to a file

df = df.sort_values('POS') # sort the dataframe based on the 'POS' column
df.to_excel("dictionary_pos.xlsx", index=False) # write it to a file
