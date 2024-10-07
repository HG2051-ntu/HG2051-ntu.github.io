---
title: 'Week 8'
---

## Learning Objectives

*   Concepts:
    [regular expressions]{.eng}
    [re]{.py}
    [stemming]{.nlp}
    [lemmatization]{.nlp}
    [segmentation]{.nlp}

(color key: [Python/Programming]{.py} [NLP/CL]{.nlp} [Software Engineering]{.eng})

## Algorithmic Thinking

1. What is the task? What is the minimum I need to do to complete the task?

> *Read the instructions! Laziness is a virtue!*

2. What are the tools and components I have at my disposal? What format or
structure are they in? How can I access the information I need?

> *Know your basics well! `list`, `dict`, `for`, `in`, etc..*

3. What is the first step? How can I make sure it is working?

> *Start simply! Introduce complexity slowly!*

- Develop using a clear feedback system.
- Address errors as they arise. Google errors if you don't understand them.

## Reading

Please see the slides from M. W. Goodman's 2019 workshop on regular expressions
for a quick introduction:

*   [Searching for Patterns with Regular Expressions](static/regex-workshop-slides.pdf)

For applications of regular expressions to NLP, please read these sections from the NLTK book:

*   [NLTK 3.4 – Regular Expressions for Detecting Word Patterns](http://www.nltk.org/book/ch03.html#regular-expressions-for-detecting-word-patterns)
*   [NLTK 3.5 – Useful Applications of Regular Expressions](http://www.nltk.org/book/ch03.html#useful-applications-of-regular-expressions)

Also, we’ve discussed _tokenization_ and basic _normalization_ already, but now
see the following to better understand _stemming_, _lemmatization_, and _segmentation_.

*   [NLTK 3.6 – Normalizing Text](http://www.nltk.org/book/ch03.html#normalizing-text)
*   [NLTK 3.7 – Regular Expressions for Tokenizing Text](http://www.nltk.org/book/ch03.html#regular-expressions-for-tokenizing-text)
*   [NLTK 3.8 – Segmentation](http://www.nltk.org/book/ch03.html#segmentation)

## Additional Reading

These links may be helpful, but are not assigned reading:

*   [Regular Expression HOWTO](https://docs.python.org/3.8/howto/regex.html) (Python documentation, by A.M. Kuchling)
*   [Python Regular Expressions](https://developers.google.com/edu/python/regular-expressions) (Google for Education)
*   [regex101](https://regex101.com/) (Useful web-app for constructing and inspecting regular expressions)

## Testing Your Knowledge

### Questions

*   **Q:** What are regex metacharacters?
*   **Q:** How is stemming different from lemmatization?
*   **Q:** What is a kind of segmentation that is not tokenization/word-segmentation?

### Practical Work

*   Write regular expressions to match the following classes of strings:
    *   A single determiner (assume that _a_, _an_, and _the_ are the only
      determiners)
    *   An arithmetic expression using integers, addition, and multiplication,
    such as `2*3+8`
    *   Phone numbers (e.g., `+65 8012 3456`)
*   Create a function `plural()` that takes an English word and returns its
plural form. Test it on _dog_, _apple_, _fly_, _boy_, _woman_.
*   Find all verb particles (things like _give up_, _look out_) in wordnet.
*   Try to expand them to different inflectional forms: _give up_, _giving up_, _gave up_, _given up_
