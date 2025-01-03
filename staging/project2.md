---
title: 'HG2051 (AY24/25) Project 2: Group assignment'
---

## Introduction

This project constitutes 30% of your final grade for HG2051. Please work on the
final program in groups of 2-3 and report together.

- The goal of this assignment is to demonstrate your programming and
problem-solving abilities through teamwork. If your team has an idea for
another project that you would like to do instead, talk to me for approval.

- This project involves training a part of speech tagger based on existing
tagged data and using it to tag unseen data. As with the individual project,
your team will be required to submit data, output, and annotated code along
with a short writeup that describes your goals, process, and results. Your
code will be assessed based on its functionality and simplicity.

## Project 2: Part of speech tagging

Part of speech tagging is a way to automatically identify the word class of a
particular lexical item in a string of text. A decent part of speech tagger can
help to facilitate other downstream tasks such as machine translation. The
initial project code in the repository will help you to get started, along
the following lines:

1. Two text files are provided for this project, corresponding to the two files
you used for Project 1 (if you chose to work on the language I  provided files
for). The first text will be used to train your POS-tagger, and the second will
be used to validate it.

2. Parse the first text into word-POS tuples and use them to train a POS-tagger.
This can be done using the NLTK library (see [NLTK Ch 5](https://www.nltk.org/book/ch05.html)),
but you may want to use a different library. Test your POS-tagger on the second
text to see how well it performs - this second text has been edited to include
only POS-tagged sentences. The metric you will use to determine performance is
`accuracy`.

3. The provided script gives a baseline accuracy using modules in the NLTK
library. Your accuracy should improve once you add more data to train your
POS-tagging model. The goal of your project is to improve on the existing
baseline, by additionally including rules or features for your POS-tagger. To
explore potential rules/features, you may want to do some research on the
language itself, or find some other methods for developing POS-taggers.

4. In order to improve your POS-tagger further, consider whether to incorporate
additional data from more sources, such as those linked in Project 1. You may
also want to train multiple POS-taggers and use them in combination to see if
you can improve your score.

5. This code is simply a starting point for exploration. What other features can
you think of and implement to improve accuracy? Are there other lexical
resources/corpora or algorithms within NLTK or from other sources that can
improve your results? What is the best accuracy you can get? How relevant are
these POS tags to other languages, i.e. would it be good to try and convert
them to something like the [Universal Tag Set](https://universaldependencies.org/u/pos/)?

6. With your group, write a roughly 5-page paper (no longer than 10 pages)
describing your goals, data, process, and results, and discussing some of the
concerns identified in point 5. This paper should include relevant linguistic
information and citations for your sources. Submit the paper as a PDF along with
your annotated/commented Python code in a Github repository. The PDF should also
be submitted via TurnItIn.
