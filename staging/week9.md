---
title: 'Week 9'
---

## Learning Objectives

*   Concepts:
    [higher-order functions]{.eng}
    [recursive functions]{.eng}
    [map()]{.py}
    [filter()]{.py}
    [n-grams]{.nlp}
    [collocations]{.nlp}
    [part-of-speech tags]{.nlp}

(color key: [Python/Programming]{.py} [NLP/CL]{.nlp} [Software Engineering]{.eng})

## In-class topics

- Quiz 1 review
- Project 1
- Project 2
- N-grams and collocations
- General questions

## Reading

### Higher-order and Recursive Functions

#### First-class Functions

By now you know how to define a function. For instance, to square a number,
you might write:

  ```python
  def square(x):
    return x ** 2
  ```

Note that this definition does two things: (1) it defines the code that, when
called, accepts the `x` argument then computes and returns the square of `x`;
and (2) it assigns this “function object” to the name `square`. When we invoke
the name `square` with parentheses and the appropriate arguments, we get a
result:

  ```python
  >>> square(4)
  16
  ```

And if you just type the function name without calling it in an interactive
interpreter, Python will tell you it’s a function:

  ```python
  >>> square
  <function square at 0x7ff9d780f790>
  ```

That is, the value of `square` is the function object. This object is a value
just like more traditional values in Python, such as integers and strings, and
we can reassign the function to another variable if we like:

  ```python
  >>> sq = square
  >>> sq(4)
  16
  ```

Python is said to have [first-class functions](https://en.wikipedia.org/wiki/First-class_function),
meaning that functions are not merely something to be called, but something
that can be assigned, passed as arguments to other functions, and used as the
return value of another function.

#### Higher-order Functions

Functions are said to be [higher-order functions](https://en.wikipedia.org/wiki/Higher-order_function)
if they can accept other functions as arguments or if they return a function
as their result.

Continuing our example from before, we may wish to generalize `square()` to a
function that, given an exponent `n`, returns a function that raises `x` to
the power of `n`:

  ```python
  def power(n):
    def raise_to(x):
      return x ** n
    return raise_to
  ```

Then we could create `square` simply as follows:

  ```python
  >>> square = power(2)
  >>> square(3)
  9
  >>> cube = power(3)
  >>> cube(3)
  27
  ```

You don’t even need to assign the created function to use it:

  ```python
  >>> power(3)(3)
  27
  ```

In Python, [map()](https://docs.python.org/3/library/functions.html#map) and [filter()](https://docs.python.org/3/library/functions.html#filter) are
built-in functions that take a function as their first argument and an iterable
as their second argument. The `map()` function applies the function argument
to each item in the iterable and yields the result:

  ```python
  >>> list(map(square, range(10)))  # apply square() to each value in range(10)
  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
  >>> [square(x) for x in range(10)]  # this does the same thing in a comprehension
  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
  ```

_Note: `list()` is necessary to get the full list; otherwise `map()` returns
an iterator that yields one value at a time._

The `filter()` function yields values from the iterable if the function
argument applied to the value evaluates as true.

  ```python
  >>> list(filter(str.isnumeric, '1 two 3 four 5'.split()))
  ['1', '3', '5']
  ```

We can see how this works by using `map()` to see the `True`/`False` values,
and noting that `str.isnumeric(x)` is the same as `x.isnumeric()` when `x`
is a string:

  ```python
  >>> '1'.isnumeric()  # the normal way to call `isnumeric()`
  True
  >>> str.isnumeric('1')  # the functional way to call it
  True
  >>> list(map(str.isnumeric, '1 two 3 four 5'.split()))
  [True, False, True, False, True]
  ```

To see how higher-order functions might help with NLP, please read this short
section from the NLTK book:

*   [NLTK 4.5 – Higher-Order Functions](http://www.nltk.org/book/ch04.html#higher-order-functions)

#### Recursive Functions

You may know of recursive linguistic structures, such as grammatical constructs
which allow sentences like _Kim knows that Sandy knows that Pat knows that the
dog barked_. Similarly, many programming languages allow [recursive functions](https://en.wikipedia.org/wiki/Recursion_(computer_science)) which
call themselves. For example, you may want to write a function that computes
the factorial of some integer `x`:

  ```python
  def factorial(x):
    # e.g., if x is 7, this would return 7 * factorial(6),
    # which returns 6 * factorial(5), etc.
    return x * factorial(x - 1)
  ```

Let’s try it out:

  ```python
  >>> factorial(7)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 2, in factorial
    File "<stdin>", line 2, in factorial
    File "<stdin>", line 2, in factorial
    [Previous line repeated 996 more times]
  RecursionError: maximum recursion depth exceeded
  ```

Oops. This did `7 * (6 * (5 * ...))` but it did not stop at 1, so it continued:
`... * (0 * (-1 * ...))`. Recursive functions must have a _base case_ which
decides when it should stop. For instance:

  ```python
  def factorial(x):
    if x == 0:
      return 1  # base case
    else:
      return x * factorial(x - 1)
  ```

And try again:

  ```python
  >>> factorial(7)
  5040
  >>> 7 * 6 * 5 * 4 * 3 * 2 * 1  # confirm
  5040
  ```

For some problems, recursive functions are the natural way to compute a result,
but they have limits (as seen by the `RecursionError` above) and can lead to
very inefficient code. Recursive algorithms are often more efficient as an
iterative loop (`for`, `while`, etc.), but the iterative code can be less
intuitive.

### N-grams

Bigrams, Trigrams, and more generally n-grams are subsequences of some sequence
with length 2, 3, or more. In computational linguistics we often use n-grams
for sequences of tokens, words, characters, etc. The NLTK has the
`nltk.ngrams()` function which takes an iterable and a number `n` and yields
subsequence tuples of length `n` from the iterable:

  ```python
  >>> import nltk
  >>> four_words = 'many dogs chase cats'.split()
  >>> list(nltk.ngrams(four_words, 1))  # unigrams
  [('many',), ('dogs',), ('chase',), ('cats',)]
  >>> list(nltk.ngrams(four_words, 2))  # bigrams
  [('many', 'dogs'), ('dogs', 'chase'), ('chase', 'cats')]
  >>> list(nltk.ngrams(four_words, 3))  # trigrams
  [('many', 'dogs', 'chase'), ('dogs', 'chase', 'cats')]
  >>> list(nltk.ngrams(four_words, 4))  # 4-grams
  [('many', 'dogs', 'chase', 'cats')]
  >>> list(nltk.ngrams(four_words, 5))  # 5-grams
  []
  ```

**See also:** [Google’s Ngram Viewer](https://books.google.com/ngrams#)

The items in the n-grams might be complex objects, such as n-grams of word-tag
pairs:

  ```python
  >>> nltk.download('brown')  # if you don't have it yet
  >>> from nltk.corpus import brown
  >>> tagged_sent = brown.tagged_sents()[0]
  >>> tagged_sent[0:3]  # inspect some items
  [('The', 'AT'), ('Fulton', 'NP-TL'), ('County', 'NN-TL')]
  >>> tagged_bigrams = list(nltk.ngrams(tagged_sent, 2))
  >>> for bigram in tagged_bigrams[:2]:  # inspect the first two bigrams
  ...     print(bigram)                  # note that each bigram is a word-tag pair
  (('The', 'AT'), ('Fulton', 'NP-TL'))
  (('Fulton', 'NP-TL'), ('County', 'NN-TL'))
  ```

### Collocations

N-grams of words that occur more often than you would expect in a random
distribution are called [collocations](https://en.wikipedia.org/wiki/Collocation).
Furthermore, these words may have some special, perhaps non-compositional
meaning that wouldn’t be obvious by the individual words. By counting the
occurrences of n-gram pairs and comparing them to the counts of the words
individually, we can find those that tend to appear together. For example:

  ```python
  def collocations(words):
    from operator import itemgetter
    # Count the words and bigrams
    wfd = nltk.FreqDist(words)
    pfd = nltk.FreqDist(nltk.bigrams(words))  # bigrams is the same as nltk.ngrams(words, 2)
    # Compute the scores for each pair
    scored = [((w1, w2), score(w1, w2, wfd, pfd)) for w1, w2 in pfd]
    ## sort according to the score
    scored.sort(key=itemgetter(1), reverse=True)
    return [p for (p, s) in scored]
  ```


  ```python
  def score(word1, word2, wfd, pfd, power=3):
    '''return the collocation score f(w1,w2)^power/(f(w1)*f(w2))'''
    freq1 = wfd[word1]
    freq2 = wfd[word2]
    freq12 = pfd[(word1, word2)]
    return freq12 ** power / float(freq1 * freq2)
  ```

And in use:

  ```python
  >>> from nltk.corpus import gutenberg
  >>> words = [w for w in gutenberg.words('melville-moby_dick.txt') if len(w) > 2]
  >>> print(collocations(words)[:10])
  [('Moby', 'Dick'), ('Sperm', 'Whale'), ('White', 'Whale'), ('Dough', 'Boy'),
  ('Mrs', 'Hussey'), ('Sag', 'Harbor'), ('Father', 'Mapple'), ('New', 'Bedford'),
  ('Fast', 'Fish'), ('have', 'been')]
  ```

For further information (not required reading), see:

*   [http://mlwiki.org/index.php/Collocation\_Extraction](http://mlwiki.org/index.php/Collocation_Extraction)
*   [http://www.collocations.de/](http://www.collocations.de/)

### Parts-of-Speech

I assume you are familiar with word categories, namely “parts of speech”. If
not, please read or skim the [Wikipedia article](https://en.wikipedia.org/wiki/Part_of_speech).
Then please read the following sections of the NLTK book about part-of-speech
tagging:

*   [NLTK 5 – Categorizing and Tagging Words](http://www.nltk.org/book/ch05.html)
    *   [NLTK 5.1 – Using a Tagger](http://www.nltk.org/book/ch05.html#using-a-tagger)
    *   [NLTK 5.2 – Tagged Corpora](http://www.nltk.org/book/ch05.html#tagged-corpora)

## Testing Your Knowledge

### Questions

*   **Q:** If you have a list of length `m`, how many bigrams will it have?
Trigrams? n-grams in general?

*   **Q:** How might you deal with the problem of getting an n-gram from a
sequence where the length of the sequence is less than `n`?

*   **Q:** Do all languages use the same parts of speech? Does a single
language have a clear and complete set of parts-of-speech?

*   **Q:** What is a _tagset_? What are examples of tagsets?


### Practical Work

*   Write a recursive function `fib(x)` to compute the [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number) of `x`. Calling
`fib(1)` should return 1, `fib(5)` returns 5, `fib(8)` returns 21, and so on. What happens if you
call `fib(20)`, `fib(30)`, or `fib(40)`? (use Ctrl-C to kill a stuck process).
Now try rewriting the recursive function as an iterative function. Can you go
higher than `fib(40)`?

*   Write a function `bigrams(xs)` that takes a list `xs` and returns a list of
bigrams from `xs`.

*   Write a function that takes a string of `word/TAG` formatted pairs and
returns the list of (word, tag) tuples (hint: use `nltk.str2tuple()`)

*   Write a function that uses `nltk.map_tag()` to map a list of (word, tag)
pairs to the universal tagset.
